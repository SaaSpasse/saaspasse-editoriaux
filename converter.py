#!/usr/bin/env python3
"""
Convertit un HTML beehiiv en Markdown avec front matter et snippet édito.
"""

from bs4 import BeautifulSoup
import re
import json
import yaml
from pathlib import Path
from analyzer import extract_metadata, extract_editorial
import html as html_lib

def process_inline_formatting(elem):
    """Traite le formatage inline (gras, italique, liens) dans un élément."""
    result = []

    for child in elem.children:
        if isinstance(child, str):
            result.append(child)
        elif child.name == 'br':
            result.append('\n')
        elif child.name == 'strong' or child.name == 'b':
            result.append(f"**{child.get_text()}**")
        elif child.name == 'em' or child.name == 'i':
            result.append(f"*{child.get_text()}*")
        elif child.name == 'code':
            result.append(f"`{child.get_text()}`")
        elif child.name == 'a':
            href = child.get('href', '')
            text = child.get_text()
            if href:
                result.append(f"[{text}]({href})")
            else:
                result.append(text)
        elif child.name == 'span':
            # Span peut contenir du formatage imbriqué
            result.append(process_inline_formatting(child))
        else:
            # Autres éléments, récupérer le texte
            result.append(child.get_text())

    return ''.join(result)

def html_to_markdown(soup):
    """Convertit le contenu HTML en Markdown propre."""

    # Extraire le contenu principal (content-blocks)
    content_blocks = soup.find(id='content-blocks')
    if not content_blocks:
        content_blocks = soup.find('body')

    if not content_blocks:
        return ""

    markdown_lines = []
    processed_elements = set()

    # Parcourir tous les éléments de contenu dans l'ordre
    for elem in content_blocks.descendants:
        # Éviter de traiter plusieurs fois le même élément
        if elem in processed_elements:
            continue

        if not hasattr(elem, 'name') or elem.name is None:
            continue

        tag_name = elem.name

        # Titres
        if tag_name in ['h1', 'h2', 'h3', 'h4', 'h5', 'h6']:
            # Vérifier si pas déjà traité via un parent
            if elem.parent in processed_elements:
                continue
            level = int(tag_name[1])
            text = process_inline_formatting(elem)
            if text.strip():
                markdown_lines.append(f"{'#' * level} {text.strip()}")
                markdown_lines.append("")
            processed_elements.add(elem)

        # Paragraphes
        elif tag_name == 'p':
            if elem.parent in processed_elements:
                continue
            text = process_inline_formatting(elem)
            if text.strip():
                markdown_lines.append(text.strip())
                markdown_lines.append("")
            processed_elements.add(elem)

        # Listes non ordonnées
        elif tag_name == 'ul':
            if elem.parent in processed_elements:
                continue
            for li in elem.find_all('li', recursive=False):
                text = process_inline_formatting(li)
                if text.strip():
                    markdown_lines.append(f"- {text.strip()}")
            markdown_lines.append("")
            processed_elements.add(elem)
            for li in elem.find_all('li'):
                processed_elements.add(li)

        # Listes ordonnées
        elif tag_name == 'ol':
            if elem.parent in processed_elements:
                continue
            for idx, li in enumerate(elem.find_all('li', recursive=False), 1):
                text = process_inline_formatting(li)
                if text.strip():
                    markdown_lines.append(f"{idx}. {text.strip()}")
            markdown_lines.append("")
            processed_elements.add(elem)
            for li in elem.find_all('li'):
                processed_elements.add(li)

        # Citations
        elif tag_name == 'blockquote':
            if elem.parent in processed_elements:
                continue
            text = process_inline_formatting(elem)
            if text.strip():
                # Gérer les citations multi-lignes
                for line in text.strip().split('\n'):
                    if line.strip():
                        markdown_lines.append(f"> {line.strip()}")
                markdown_lines.append("")
            processed_elements.add(elem)

        # Images
        elif tag_name == 'img':
            if elem.parent in processed_elements:
                continue
            src = elem.get('src', '')
            alt = elem.get('alt', '')
            if src:
                markdown_lines.append(f"![{alt}]({src})")
                markdown_lines.append("")
            processed_elements.add(elem)

    # Nettoyer les lignes vides multiples
    cleaned = []
    prev_empty = False
    for line in markdown_lines:
        is_empty = line.strip() == ""
        if not (is_empty and prev_empty):
            cleaned.append(line)
        prev_empty = is_empty

    return '\n'.join(cleaned).strip()

def create_front_matter(metadata):
    """Crée le front matter YAML."""
    # Nettoyer les None et listes vides
    clean_meta = {}
    for key, value in metadata.items():
        if value is not None and value != [] and value != {}:
            clean_meta[key] = value

    # Utiliser yaml.dump avec options pour un formatage propre
    yaml_str = yaml.dump(clean_meta,
                         allow_unicode=True,
                         default_flow_style=False,
                         sort_keys=False,
                         width=120)

    return f"---\n{yaml_str}---"

def is_beehiiv_quote(elem):
    """Détecte si un élément fait partie d'une citation beehiiv (avec ❝)."""
    # Chercher le symbole ❝ dans les éléments parents/voisins
    if elem.name == 'td':
        text = elem.get_text()
        if '❝' in text:
            return True
        # Vérifier les éléments frères
        for sibling in elem.find_previous_siblings():
            if '❝' in sibling.get_text():
                return True
        # Vérifier aussi dans la table parente
        parent_table = elem.find_parent('table')
        if parent_table:
            for td in parent_table.find_all('td'):
                if '❝' in td.get_text() and '❝' == td.get_text().strip():
                    return True
    return False

def extract_editorial_clean(editorial_html):
    """Extrait l'édito et le convertit en markdown propre."""
    if not editorial_html:
        return None

    # Parser le HTML de l'édito
    soup = BeautifulSoup(editorial_html, 'html.parser')

    lines = []
    processed = set()
    in_quote_block = False
    quote_lines = []

    # Parcourir dans l'ordre pour préserver la structure
    for elem in soup.descendants:
        if elem in processed:
            continue

        if not hasattr(elem, 'name') or elem.name is None:
            continue

        tag_name = elem.name

        # Titres
        if tag_name in ['h1', 'h2', 'h3', 'h4', 'h5', 'h6']:
            if elem.parent in processed:
                continue
            level = int(tag_name[1])
            text = process_inline_formatting(elem)
            if text.strip():
                lines.append(f"{'#' * level} {text.strip()}\n")
            processed.add(elem)

        # Paragraphes
        elif tag_name == 'p':
            if elem.parent in processed:
                continue
            text = process_inline_formatting(elem)
            if text.strip():
                # Vérifier si c'est une citation beehiiv
                if is_beehiiv_quote(elem.parent):
                    # C'est une citation
                    quote_lines.append(f"> {text.strip()}\n")
                    processed.add(elem)
                    # Chercher s'il y a un texte en italique qui suit (attribution)
                    parent_table = elem.find_parent('table')
                    if parent_table:
                        for next_elem in parent_table.find_all(['i', 'em']):
                            if next_elem not in processed:
                                attr_text = process_inline_formatting(next_elem)
                                if attr_text.strip():
                                    quote_lines.append(f"> \n> *{attr_text.strip()}*\n")
                                processed.add(next_elem)
                                processed.add(next_elem.parent)
                    # Ajouter la citation complète
                    lines.extend(quote_lines)
                    quote_lines = []
                else:
                    # Paragraphe normal
                    lines.append(f"{text.strip()}\n")
                processed.add(elem)

        # Listes non ordonnées
        elif tag_name == 'ul':
            if elem.parent in processed:
                continue
            # Traiter chaque item de liste
            for li in elem.find_all('li', recursive=False):
                # Extraire seulement le texte direct du <li>, pas des sous-listes
                li_text_parts = []
                for child in li.children:
                    if isinstance(child, str):
                        li_text_parts.append(child)
                    elif child.name in ['p', 'span', 'b', 'strong', 'i', 'em', 'a', 'code']:
                        li_text_parts.append(process_inline_formatting(child))
                    elif child.name in ['ul', 'ol']:
                        # Sous-liste - on la traite séparément après
                        continue

                li_text = ''.join(li_text_parts).strip()
                if li_text:
                    lines.append(f"- {li_text}\n")

                # Traiter les sous-listes
                for sub_list in li.find_all(['ul', 'ol'], recursive=False):
                    for sub_li in sub_list.find_all('li', recursive=False):
                        sub_text = process_inline_formatting(sub_li)
                        if sub_text.strip():
                            lines.append(f"  - {sub_text.strip()}\n")
                    processed.add(sub_list)
                    for sub_li_elem in sub_list.find_all('li'):
                        processed.add(sub_li_elem)

            processed.add(elem)
            for li in elem.find_all('li', recursive=False):
                processed.add(li)

        # Listes ordonnées
        elif tag_name == 'ol':
            if elem.parent in processed:
                continue
            # Traiter chaque item de liste ordonnée
            for idx, li in enumerate(elem.find_all('li', recursive=False), 1):
                # Extraire seulement le texte direct du <li>, pas des sous-listes
                li_text_parts = []
                for child in li.children:
                    if isinstance(child, str):
                        li_text_parts.append(child)
                    elif child.name in ['p', 'span', 'b', 'strong', 'i', 'em', 'a', 'code']:
                        li_text_parts.append(process_inline_formatting(child))
                    elif child.name in ['ul', 'ol']:
                        # Sous-liste - on la traite séparément après
                        continue

                li_text = ''.join(li_text_parts).strip()
                if li_text:
                    lines.append(f"{idx}. {li_text}\n")

                # Traiter les sous-listes
                for sub_list in li.find_all(['ul', 'ol'], recursive=False):
                    for sub_li in sub_list.find_all('li', recursive=False):
                        sub_text = process_inline_formatting(sub_li)
                        if sub_text.strip():
                            lines.append(f"   - {sub_text.strip()}\n")
                    processed.add(sub_list)
                    for sub_li_elem in sub_list.find_all('li'):
                        processed.add(sub_li_elem)

            processed.add(elem)
            for li in elem.find_all('li', recursive=False):
                processed.add(li)

        # Citations
        elif tag_name == 'blockquote':
            if elem.parent in processed:
                continue
            text = process_inline_formatting(elem)
            if text.strip():
                for line in text.strip().split('\n'):
                    if line.strip():
                        lines.append(f"> {line.strip()}\n")
            processed.add(elem)

    return '\n'.join(lines).strip()

def convert_to_markdown(html_content, editoriaux_dir, posts_complets_dir):
    """Convertit un HTML en fichier Markdown complet."""

    # Extraire métadonnées
    metadata, editorial_html = extract_metadata(html_content)

    # Parser HTML pour conversion markdown
    soup = BeautifulSoup(html_content, 'html.parser')

    # Convertir en markdown
    markdown_content = html_to_markdown(soup)

    # Créer le nom de fichier
    date = metadata.get('date', 'unknown')
    slug = metadata.get('slug', 'unknown')
    filename = f"{date}-{slug}.md"

    # Créer le front matter
    front_matter = create_front_matter(metadata)

    # Créer le contenu complet
    full_markdown = f"{front_matter}\n\n{markdown_content}"

    # Isoler l'édito si trouvé
    if editorial_html and metadata.get('editorial_confidence') == 'high':
        editorial_clean = extract_editorial_clean(editorial_html)

        # Ajouter la section éditoriale dans le markdown principal
        editorial_section = f"\n\n# Éditorial (copywriting)\n\n<!-- editorial:start -->\n{editorial_clean}\n<!-- editorial:end -->\n"

        # Insérer après le front matter, avant le reste
        full_markdown = f"{front_matter}\n{editorial_section}\n{markdown_content}"

        # Créer fichier édito séparé dans le dossier editoriaux
        edito_filename = f"{date}-{slug}.md"
        edito_path = editoriaux_dir / edito_filename
        with open(edito_path, 'w', encoding='utf-8') as f:
            f.write(editorial_clean)
        print(f"  ✓ Editorial: editoriaux/{edito_filename}")

    # Sauvegarder le markdown complet dans le dossier posts-complets
    output_path = posts_complets_dir / filename
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(full_markdown)

    print(f"  ✓ Complete post: posts-complets/{filename}")

    return filename, metadata

def main():
    """Test sur les 3 samples."""
    base_dir = Path.home() / "Claude Code/posts-infolettre"
    samples_dir = base_dir / "samples"
    editoriaux_dir = base_dir / "editoriaux"
    posts_complets_dir = base_dir / "posts-complets"

    # Créer les dossiers s'ils n'existent pas
    editoriaux_dir.mkdir(exist_ok=True)
    posts_complets_dir.mkdir(exist_ok=True)

    for i in range(1, 4):
        html_file = samples_dir / f"sample_{i}.html"

        print(f"\nConverting sample {i}...")

        with open(html_file, 'r', encoding='utf-8') as f:
            html_content = f.read()

        filename, metadata = convert_to_markdown(html_content, editoriaux_dir, posts_complets_dir)
        print(f"  Title: {metadata['title']}")

if __name__ == '__main__':
    main()
