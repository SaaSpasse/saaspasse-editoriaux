#!/usr/bin/env python3
"""
Script pour convertir les fichiers HTML d'infolettre en Markdown.
Crée deux versions : editoriaux (texte pur) et posts-complets (avec metadata).
"""

import re
import sys
from pathlib import Path
from bs4 import BeautifulSoup
import html2text

def extract_content(html_path):
    """Extrait le contenu principal du HTML."""
    with open(html_path, 'r', encoding='utf-8') as f:
        html = f.read()

    soup = BeautifulSoup(html, 'html.parser')

    # Extraire le titre
    title = soup.find('title')
    title_text = title.get_text().strip() if title else "Sans titre"

    # Extraire la date (format YYYY-MM-DD)
    date_match = re.search(r'(\d{4}-\d{2}-\d{2})', html)
    date = date_match.group(1) if date_match else "0000-00-00"

    # Extraire le slug depuis l'URL
    slug_match = re.search(r'saaspasse\.beehiiv\.com/p/([^"?\s]+)', html)
    slug = slug_match.group(1) if slug_match else title_text.lower().replace(' ', '-')

    # Configurer html2text
    h = html2text.HTML2Text()
    h.ignore_links = False
    h.ignore_images = False
    h.body_width = 0  # Pas de wrapping
    h.unicode_snob = True

    # Trouver le contenu principal (dans les tables de contenu)
    content_divs = soup.find_all('td', class_='e')

    markdown_content = ""
    for div in content_divs:
        markdown_content += h.handle(str(div)) + "\n"

    return {
        'title': title_text,
        'date': date,
        'slug': slug,
        'content': markdown_content,
        'full_html': html
    }

def find_editorial_section(content):
    """Trouve et extrait la section éditorial du contenu."""
    # L'éditorial commence généralement après "What's up folks" et se termine avant les sections promos

    lines = content.split('\n')
    editorial_lines = []
    in_editorial = False

    for line in lines:
        # Début de l'éditorial
        if "What's up folks" in line or "What's up folks" in line.lower():
            in_editorial = True

        # Fin de l'éditorial (sections à exclure)
        end_markers = [
            "Rejoins les SaaSpals",
            "Partenaires certifiés",
            "Sans oublier nos partenaires",
            "Pas encore abonné au pod",
            "Okay bobye",
            "Ahem, ahem",
            "### Podcast",
            "Ton follow de la semaine",
            "HUGE merci"
        ]

        if any(marker in line for marker in end_markers):
            break

        if in_editorial:
            editorial_lines.append(line)

    return '\n'.join(editorial_lines).strip()

def count_words(text):
    """Compte le nombre de mots dans le texte."""
    # Enlever les URLs et markdown
    clean = re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', text)
    clean = re.sub(r'[#*_`]', '', clean)
    words = clean.split()
    return len(words)

def extract_links(content, html):
    """Extrait les liens du contenu."""
    # Liens internes (saaspasse)
    internal = re.findall(r'https?://[^"\s]*saaspasse[^"\s]*', html)
    # Liens externes
    external = re.findall(r'https?://[^"\s]+', html)
    external = [l for l in external if 'saaspasse' not in l and 'beehiiv' not in l.replace('saaspasse.beehiiv', '')]

    return len(set(internal)), len(set(external))

def extract_people(html):
    """Extrait les personnes mentionnées (liens LinkedIn)."""
    people = []
    soup = BeautifulSoup(html, 'html.parser')

    for link in soup.find_all('a', href=re.compile(r'linkedin\.com/in/')):
        name = link.get_text().strip()
        url = link.get('href', '')
        if name and len(name) > 1:
            people.append({'nom': name, 'linkedin': url})

    return people

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python convert_html.py <fichier.html>")
        sys.exit(1)

    html_path = sys.argv[1]
    data = extract_content(html_path)

    print(f"Titre: {data['title']}")
    print(f"Date: {data['date']}")
    print(f"Slug: {data['slug']}")
    print(f"Contenu extrait: {len(data['content'])} caractères")
