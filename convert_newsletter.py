#!/usr/bin/env python3
"""
Script pour convertir les fichiers HTML d'infolettre beehiiv en Markdown.
Crée deux versions : editoriaux (texte pur) et posts-complets (avec metadata).
"""

import re
import sys
from pathlib import Path
from bs4 import BeautifulSoup
import html2text


def extract_metadata(html):
    """Extrait les métadonnées du HTML."""
    soup = BeautifulSoup(html, 'html.parser')

    # Titre
    title_tag = soup.find('title')
    title = title_tag.get_text().strip() if title_tag else "Sans titre"

    # Date (format YYYY-MM-DD)
    date_match = re.search(r'(\d{4}-\d{2}-\d{2})', html)
    date = date_match.group(1) if date_match else "0000-00-00"

    # Slug depuis l'URL
    slug_match = re.search(r'saaspasse\.beehiiv\.com/p/([^"?\s&]+)', html)
    slug = slug_match.group(1) if slug_match else title.lower().replace(' ', '-')

    # URL complète
    url = f"https://saaspasse.beehiiv.com/p/{slug}"

    return {
        'title': title,
        'date': date,
        'slug': slug,
        'url': url
    }


def html_to_markdown(html):
    """Convertit le HTML en Markdown."""
    soup = BeautifulSoup(html, 'html.parser')

    h = html2text.HTML2Text()
    h.ignore_links = False
    h.ignore_images = False
    h.body_width = 0
    h.unicode_snob = True

    body = soup.find('body')
    if body:
        content = h.handle(str(body))
    else:
        content = h.handle(html)

    # Nettoyer les lignes de séparation excessives
    content = re.sub(r'\n---\s*\n', '\n', content)
    content = re.sub(r'\| *\n', '\n', content)
    content = re.sub(r'\n{3,}', '\n\n', content)

    return content


def extract_editorial(content):
    """Extrait uniquement la section éditoriale du contenu."""
    lines = content.split('\n')
    editorial_lines = []
    in_editorial = False
    found_start = False

    end_markers = [
        "Rejoins les SaaSpals",
        "Partenaires certifiés",
        "Sans oublier nos partenaires",
        "Pas encore abonné au pod",
        "Okay bobye",
        "Ahem, ahem",
        "### Podcast",
        "Voici le dernier épisode",
        "Ton follow de la semaine",
        "HUGE merci",
        "## Podcast",
        "partenaires produits",
        "### Rejoins",
        "Merci tellement à tous"
    ]

    for line in lines:
        # Chercher le début (What's up folks ou le titre principal)
        if not found_start:
            if "What's up folks" in line:
                in_editorial = True
                found_start = True
                editorial_lines.append(line)
                continue

        # Vérifier si on atteint une section à exclure
        if any(marker.lower() in line.lower() for marker in end_markers):
            break

        if in_editorial:
            editorial_lines.append(line)

    result = '\n'.join(editorial_lines).strip()

    # Nettoyer les artefacts de table
    result = re.sub(r'\| *', '', result)
    result = re.sub(r' *\|', '', result)
    result = re.sub(r'---+', '', result)
    result = re.sub(r'\n{3,}', '\n\n', result)

    return result


def extract_links_and_people(html):
    """Extrait les liens et personnes mentionnées."""
    soup = BeautifulSoup(html, 'html.parser')

    # Liens
    all_links = soup.find_all('a', href=True)
    internal_links = []
    external_links = []
    utm_links = []

    for link in all_links:
        href = link.get('href', '')
        if 'saaspasse' in href:
            internal_links.append(href)
        elif href.startswith('http'):
            external_links.append(href)
        if 'utm_' in href:
            utm_links.append(href)

    # Personnes (LinkedIn)
    people = []
    for link in soup.find_all('a', href=re.compile(r'linkedin\.com/in/')):
        name = link.get_text().strip()
        url = link.get('href', '')
        if name and len(name) > 1 and name not in ['Frank', 'LinkedIn']:
            people.append({'nom': name, 'linkedin': url.split('?')[0] + '?utm_source=saaspasse.beehiiv.com'})

    # Domaines top
    domains = {}
    for href in external_links:
        match = re.search(r'https?://([^/]+)', href)
        if match:
            domain = match.group(1)
            domains[domain] = domains.get(domain, 0) + 1

    top_domains = sorted(domains.items(), key=lambda x: x[1], reverse=True)[:5]

    return {
        'liens_internes': len(set(internal_links)),
        'liens_externes': len(set(external_links)),
        'utm_detectes': utm_links[:20],
        'top_domains': [{'domain': d, 'count': c} for d, c in top_domains],
        'personnes': people[:10]
    }


def count_words(text):
    """Compte les mots."""
    clean = re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', text)
    clean = re.sub(r'[#*_`]', '', clean)
    clean = re.sub(r'https?://\S+', '', clean)
    return len(clean.split())


def generate_editorial_md(metadata, editorial_content):
    """Génère le fichier éditorial (texte pur)."""
    return editorial_content


def generate_post_complet_md(metadata, full_content, editorial_content, links_data):
    """Génère le fichier post-complet avec metadata YAML."""
    word_count = count_words(full_content)
    reading_time = max(1, word_count // 200)

    yaml = f"""---
date: '{metadata['date']}'
title: {metadata['title']}
url: {metadata['url']}
slug: {metadata['slug']}
source: beehiiv
word_count: {word_count}
reading_time_min: {reading_time}
editorial_confidence: high
liens_internes: {links_data['liens_internes']}
liens_externes: {links_data['liens_externes']}
top_domains:
"""
    for d in links_data['top_domains']:
        yaml += f"- domain: {d['domain']}\n  count: {d['count']}\n"

    yaml += "utm_detectes:\n"
    for url in links_data['utm_detectes'][:10]:
        yaml += f"- url: {url}\n"

    yaml += "personnes:\n"
    for p in links_data['personnes']:
        yaml += f"- nom: {p['nom']}\n  linkedin: {p['linkedin']}\n"

    yaml += "---\n\n"

    # Contenu
    content = f"""
# Éditorial (copywriting)

<!-- editorial:start -->
{editorial_content}
<!-- editorial:end -->

{full_content}
"""
    return yaml + content


def convert_file(html_path, output_dir):
    """Convertit un fichier HTML et crée les deux versions MD."""
    with open(html_path, 'r', encoding='utf-8') as f:
        html = f.read()

    metadata = extract_metadata(html)
    full_content = html_to_markdown(html)
    editorial_content = extract_editorial(full_content)
    links_data = extract_links_and_people(html)

    # Nom de fichier
    filename = f"{metadata['date']}-{metadata['slug']}.md"

    # Créer les dossiers si nécessaire
    editoriaux_dir = Path(output_dir) / 'editoriaux'
    posts_dir = Path(output_dir) / 'posts-complets'
    editoriaux_dir.mkdir(exist_ok=True)
    posts_dir.mkdir(exist_ok=True)

    # Écrire l'éditorial
    editorial_path = editoriaux_dir / filename
    with open(editorial_path, 'w', encoding='utf-8') as f:
        f.write(generate_editorial_md(metadata, editorial_content))

    # Écrire le post complet
    post_path = posts_dir / filename
    with open(post_path, 'w', encoding='utf-8') as f:
        f.write(generate_post_complet_md(metadata, full_content, editorial_content, links_data))

    return {
        'title': metadata['title'],
        'date': metadata['date'],
        'slug': metadata['slug'],
        'editorial_path': str(editorial_path),
        'post_path': str(post_path),
        'word_count': count_words(full_content)
    }


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python convert_newsletter.py <fichier.html> [output_dir]")
        sys.exit(1)

    html_path = sys.argv[1]
    output_dir = sys.argv[2] if len(sys.argv) > 2 else "."

    result = convert_file(html_path, output_dir)

    print(f"✅ Converti: {result['title']}")
    print(f"   Date: {result['date']}")
    print(f"   Mots: {result['word_count']}")
    print(f"   → {result['editorial_path']}")
    print(f"   → {result['post_path']}")
