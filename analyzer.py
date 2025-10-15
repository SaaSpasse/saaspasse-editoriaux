#!/usr/bin/env python3
"""
Analyseur prototype pour extraire métadonnées et édito des HTML beehiiv.
"""

from bs4 import BeautifulSoup
import re
import json
from pathlib import Path
from urllib.parse import urlparse, parse_qs
from collections import Counter
import html as html_lib

def clean_text(text):
    """Nettoie le texte HTML."""
    if not text:
        return ""
    # Décoder les entités HTML
    text = html_lib.unescape(text)
    # Nettoyer les espaces
    text = re.sub(r'\s+', ' ', text)
    return text.strip()

def extract_canonical_url(soup, raw_html):
    """Extrait l'URL canonique selon les règles de priorité."""
    # 1. <link rel="canonical">
    canonical = soup.find('link', rel='canonical')
    if canonical and canonical.get('href'):
        return canonical['href']

    # 2. og:url
    og_url = soup.find('meta', property='og:url')
    if og_url and og_url.get('content'):
        return og_url['content']

    # 3. Lien "Read Online"
    read_online = soup.find('a', string=lambda t: t and 'Read Online' in t)
    if not read_online:
        # Chercher dans le HTML brut
        match = re.search(r'href="(https://saaspasse\.beehiiv\.com/p/[^"?]+)', raw_html)
        if match:
            return match.group(1)
    else:
        url = read_online.get('href', '')
        # Nettoyer les params UTM pour avoir l'URL canonique
        if '?' in url:
            url = url.split('?')[0]
        return url

    return None

def extract_date(soup, raw_html):
    """Extrait la date de publication."""
    # Chercher datetime
    datetime_elem = soup.find(attrs={'datetime': re.compile(r'\d{4}-\d{2}-\d{2}')})
    if datetime_elem:
        return datetime_elem['datetime'][:10]

    # Chercher pattern YYYY-MM-DD dans le HTML
    match = re.search(r'\b(\d{4}-\d{2}-\d{2})\b', raw_html)
    if match:
        return match.group(1)

    # Chercher format "3rd octobre 2025"
    french_months = {
        'janvier': '01', 'février': '02', 'mars': '03', 'avril': '04',
        'mai': '05', 'juin': '06', 'juillet': '07', 'août': '08',
        'septembre': '09', 'octobre': '10', 'novembre': '11', 'décembre': '12'
    }
    match = re.search(r'\b(\d+)(?:st|nd|rd|th)?\s+(\w+)\s+(\d{4})\b', raw_html, re.IGNORECASE)
    if match:
        day, month, year = match.groups()
        month_lower = month.lower()
        if month_lower in french_months:
            return f"{year}-{french_months[month_lower]}-{int(day):02d}"

    return None

def extract_editorial(raw_html):
    """
    Extrait l'édito entre les marqueurs de début et fin.

    Début: "What's up folks," puis "Merci d'être là. L'édito d'abord—les nouvelles après."
    Fin: "Quelque chose à ajouter? Good. Laisse un commentaire..." puis "Cheers," puis "Frank"
    """
    # Travailler directement sur le HTML décodé pour trouver ET extraire
    text = html_lib.unescape(raw_html)

    # Pattern de début (très flexible)
    # Chercher "What's up folks" (peu importe la typo)
    start_what = re.search(r"What.{0,5}s.{0,5}up.{0,5}folks", text, re.IGNORECASE | re.DOTALL)
    if not start_what:
        return None, "low"

    # Chercher "Merci d'être là" après
    start_merci = re.search(r"Merci.{0,5}d.{0,5}être.{0,5}là", text[start_what.start():], re.IGNORECASE | re.DOTALL)
    if not start_merci:
        return None, "low"

    # Trouver le début du tag <p> qui contient "What's up folks"
    # Chercher en arrière depuis start_what pour trouver l'ouverture de <p>
    search_back = text[:start_what.start()]
    # Trouver le dernier <p avant "What's up folks"
    last_p_open = search_back.rfind('<p')
    if last_p_open == -1:
        # Fallback: commencer à "What's up folks" si pas de <p> trouvé
        start_pos = start_what.start()
    else:
        start_pos = last_p_open

    # Pattern de fin - chercher "Quelque chose à ajouter"
    end_quelque = re.search(r"Quelque.{0,5}chose.{0,5}à.{0,5}ajouter", text[start_pos:], re.IGNORECASE | re.DOTALL)
    if not end_quelque:
        return None, "low"

    # Chercher "Frank" puis capturer jusqu'au emoji coeur (💜)
    # Le pattern doit capturer tout le lien HTML complet + emoji
    end_frank = re.search(r"Frank</span></a>\s*💜", text[start_pos + end_quelque.start():], re.IGNORECASE | re.DOTALL)
    if not end_frank:
        # Fallback: chercher Frank suivi éventuellement d'un lien et emoji
        end_frank = re.search(r"Frank.{0,200}(?:💜|♥)", text[start_pos + end_quelque.start():], re.IGNORECASE | re.DOTALL)
        if not end_frank:
            # Dernier fallback
            end_frank = re.search(r"Frank.{0,100}", text[start_pos + end_quelque.start():], re.IGNORECASE | re.DOTALL)
            if not end_frank:
                return None, "low"

    end_pos = start_pos + end_quelque.start() + end_frank.end()

    # Extraire le segment (déjà décodé)
    editorial_text = text[start_pos:end_pos]

    return editorial_text, "high"

def extract_links(soup):
    """Extrait tous les liens avec métadonnées."""
    links = []
    for a in soup.find_all('a', href=True):
        url = a['href']
        text = clean_text(a.get_text())
        links.append({
            'url': url,
            'text': text
        })
    return links

def analyze_links(links):
    """Analyse les liens et extrait entités."""
    internal_domains = {'www.saaspasse.com', 'saaspasse.beehiiv.com'}

    internal_count = 0
    external_count = 0
    domain_counter = Counter()
    utm_links = []
    newsletters = []
    podcasts = []
    people = []
    companies = []
    products = []
    jobs = []

    for link in links:
        url = link['url']
        text = link['text']

        # Parse URL
        parsed = urlparse(url)
        domain = parsed.netloc.lower()

        # Interne vs externe
        if domain in internal_domains:
            internal_count += 1
        else:
            external_count += 1
            if domain:
                domain_counter[domain] += 1

        # UTM
        if 'utm_' in url:
            utm_links.append({'url': url})

        # Infolettres
        if 'saaspasse.beehiiv.com/p/' in url:
            newsletters.append({'titre': text or None, 'url': url})

        # Podcasts (heuristique)
        if 'saaspasse.com/episode/' in url or 'youtube.com' in url or 'spotify.com' in url:
            # Regrouper par titre si possible
            podcast_entry = {'titre': text or None}
            if 'saaspasse.com/episode/' in url:
                podcast_entry['Site web URL'] = url
            elif 'youtube.com' in url or 'youtu.be' in url:
                podcast_entry['YouTube URL'] = url
            elif 'spotify.com' in url:
                podcast_entry['Spotify URL'] = url
            podcasts.append(podcast_entry)

        # LinkedIn personnes
        if '/in/' in url and 'linkedin.com' in domain:
            people.append({'nom': text or None, 'linkedin': url})

        # LinkedIn compagnies
        if '/company/' in url and 'linkedin.com' in domain:
            companies.append({'nom': text or None, 'linkedin': url})

        # Produits (heuristique basique)
        known_products = ['clay.com', 'notion.so', 'apollo.io']
        if any(p in domain for p in known_products):
            products.append({'nom': text or None, 'domaine': domain})

        # Jobs
        if 'saaspasse.com/emplois' in url:
            jobs.append({'titre': text or None, 'url': url})

    # Top 5 domaines externes
    top_domains = [{'domain': d, 'count': c} for d, c in domain_counter.most_common(5)]

    return {
        'liens_internes': internal_count,
        'liens_externes': external_count,
        'top_domains': top_domains,
        'utm_detectes': utm_links if utm_links else [],
        'infolettres_mentionnees': newsletters if newsletters else [],
        'podcasts_mentionnes': podcasts if podcasts else [],
        'personnes': people if people else [],
        'compagnies': companies if companies else [],
        'produits': products if products else [],
        'jobs': jobs if jobs else []
    }

def extract_metadata(html_content):
    """Extrait toutes les métadonnées d'un HTML beehiiv."""
    soup = BeautifulSoup(html_content, 'html.parser')

    # URL et slug
    url = extract_canonical_url(soup, html_content)
    slug = url.split('/p/')[-1].split('?')[0] if url and '/p/' in url else None

    # Titre
    title_tag = soup.find('title')
    title = clean_text(title_tag.get_text()) if title_tag else None
    if not title:
        h1 = soup.find('h1')
        title = clean_text(h1.get_text()) if h1 else None

    # Date
    date = extract_date(soup, html_content)

    # Édito
    editorial_html, editorial_confidence = extract_editorial(html_content)

    # Liens
    links = extract_links(soup)
    link_analysis = analyze_links(links)

    # Compter mots (approximatif depuis le texte)
    text = soup.get_text()
    word_count = len(text.split())
    reading_time_min = (word_count + 199) // 200  # Arrondi supérieur

    # Construire métadonnées
    metadata = {
        'date': date,
        'title': title,
        'url': url,
        'slug': slug,
        'source': 'beehiiv',
        'word_count': word_count,
        'reading_time_min': reading_time_min,
        'editorial_confidence': editorial_confidence,
        **link_analysis
    }

    return metadata, editorial_html

def main():
    samples_dir = Path.home() / "claude-code/posts-infolettre/samples"

    for i in range(1, 4):
        html_file = samples_dir / f"sample_{i}.html"
        meta_file = samples_dir / f"sample_{i}_meta.json"

        print(f"\n{'='*60}")
        print(f"Analyzing sample {i}: {html_file.name}")
        print('='*60)

        # Charger le HTML
        with open(html_file, 'r', encoding='utf-8') as f:
            html_content = f.read()

        # Charger meta original
        with open(meta_file, 'r', encoding='utf-8') as f:
            original_meta = json.load(f)

        # Extraire métadonnées
        metadata, editorial_html = extract_metadata(html_content)

        # Afficher résultats
        print(f"\nOriginal title: {original_meta['web_title']}")
        print(f"Extracted title: {metadata['title']}")
        print(f"\nOriginal URL: {original_meta['url']}")
        print(f"Extracted URL: {metadata['url']}")
        print(f"Slug: {metadata['slug']}")
        print(f"\nDate: {metadata['date']}")
        print(f"Word count: {metadata['word_count']}")
        print(f"Reading time: {metadata['reading_time_min']} min")
        print(f"\nEditorial confidence: {metadata['editorial_confidence']}")
        print(f"Editorial found: {'Yes' if editorial_html else 'No'}")
        if editorial_html:
            preview = editorial_html[:200].replace('\n', ' ')
            print(f"Editorial preview: {preview}...")

        print(f"\nLinks analysis:")
        print(f"  Internal: {metadata['liens_internes']}")
        print(f"  External: {metadata['liens_externes']}")
        print(f"  Top domains: {metadata['top_domains'][:3]}")
        print(f"  Newsletters mentioned: {len(metadata['infolettres_mentionnees'])}")
        print(f"  Podcasts mentioned: {len(metadata['podcasts_mentionnes'])}")
        print(f"  People: {len(metadata['personnes'])}")
        print(f"  Companies: {len(metadata['compagnies'])}")

        # Sauvegarder résultat d'analyse
        output_file = samples_dir / f"sample_{i}_analysis.json"
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(metadata, f, indent=2, ensure_ascii=False)
        print(f"\nAnalysis saved to: {output_file.name}")

if __name__ == '__main__':
    main()
