#!/usr/bin/env python3
"""
Convertit un fichier HTML unique en Markdown.
"""

from pathlib import Path
from converter import convert_to_markdown
import subprocess

def main():
    # Chemins
    html_file = Path("/Users/francoislanthiernadeau/Downloads/post-html-d5f16695-e7c7-47cd-b510-941bc1a6cd4a (1).html")
    base_dir = Path.home() / "Claude Code/posts-infolettre"
    editoriaux_dir = base_dir / "editoriaux"
    posts_complets_dir = base_dir / "posts-complets"

    # Créer les dossiers s'ils n'existent pas
    editoriaux_dir.mkdir(exist_ok=True)
    posts_complets_dir.mkdir(exist_ok=True)

    print(f"Converting: {html_file.name}")

    # Lire le fichier HTML
    with open(html_file, 'r', encoding='utf-8') as f:
        html_content = f.read()

    # Convertir
    filename, metadata = convert_to_markdown(html_content, editoriaux_dir, posts_complets_dir)

    print(f"\n✓ Conversion terminée!")
    print(f"  Title: {metadata.get('title', 'N/A')}")
    print(f"  Date: {metadata.get('date', 'N/A')}")
    print(f"  Type: {'Éditorial + post complet' if metadata.get('editorial_confidence') == 'high' else 'Post complet seulement'}")

    # Ouvrir les fichiers créés
    date = metadata.get('date', 'unknown')
    slug = metadata.get('slug', 'unknown')

    post_complet_path = posts_complets_dir / f"{date}-{slug}.md"
    subprocess.run(['open', str(post_complet_path)])

    if metadata.get('editorial_confidence') == 'high':
        edito_path = editoriaux_dir / f"{date}-{slug}.md"
        subprocess.run(['open', str(edito_path)])

    print(f"\n✓ Fichiers ouverts dans votre éditeur!")

if __name__ == '__main__':
    main()
