#!/usr/bin/env python3
"""
Convertit tous les posts du CSV beehiiv en markdown.
"""

import csv
from pathlib import Path
from converter import convert_to_markdown

def main():
    """Convertit tous les posts publiés du CSV."""
    base_dir = Path.home() / "Claude Code/posts-infolettre"
    csv_file = base_dir / "posts-2025-10-0920251009-2-8kx8td.csv"
    editoriaux_dir = base_dir / "editoriaux"
    posts_complets_dir = base_dir / "posts-complets"

    # Créer les dossiers s'ils n'existent pas
    editoriaux_dir.mkdir(exist_ok=True)
    posts_complets_dir.mkdir(exist_ok=True)

    # Lire le CSV
    with open(csv_file, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        posts = list(reader)

    # Filtrer les posts publiés
    published_posts = [p for p in posts if p['status'] == 'confirmed']

    print(f"Found {len(published_posts)} published posts to convert\n")
    print("="*60)

    success_count = 0
    error_count = 0
    errors = []

    for idx, post in enumerate(published_posts, 1):
        try:
            html_content = post['content_html']

            if not html_content or html_content.strip() == '':
                print(f"\n[{idx}/{len(published_posts)}] Skipping - No HTML content")
                error_count += 1
                errors.append((idx, "No HTML content"))
                continue

            print(f"\n[{idx}/{len(published_posts)}] Converting...")

            filename, metadata = convert_to_markdown(html_content, editoriaux_dir, posts_complets_dir)

            print(f"  Title: {metadata.get('title', 'Unknown')}")
            print(f"  Date: {metadata.get('date', 'Unknown')}")

            success_count += 1

        except Exception as e:
            error_count += 1
            title = post.get('web_title', 'Unknown')
            print(f"\n[{idx}/{len(published_posts)}] ERROR converting: {title}")
            print(f"  Error: {str(e)}")
            errors.append((idx, title, str(e)))

    # Résumé
    print("\n" + "="*60)
    print("CONVERSION COMPLETE")
    print("="*60)
    print(f"✓ Successfully converted: {success_count}")
    print(f"✗ Errors: {error_count}")

    if errors:
        print("\nErrors details:")
        for error in errors:
            if len(error) == 3:
                idx, title, msg = error
                print(f"  [{idx}] {title}: {msg}")
            else:
                idx, msg = error
                print(f"  [{idx}] {msg}")

if __name__ == '__main__':
    main()
