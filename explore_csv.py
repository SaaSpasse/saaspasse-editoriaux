#!/usr/bin/env python3
"""
Exploration du CSV beehiiv pour extraire quelques échantillons d'éditions publiées.
"""

import csv
import json
from pathlib import Path

csv_path = Path.home() / "claude-code/posts-infolettre/posts-2025-10-0920251009-2-8kx8td.csv"
output_dir = Path.home() / "claude-code/posts-infolettre/samples"
output_dir.mkdir(exist_ok=True)

# Lire le CSV et extraire les 3 éditions publiées les plus récentes
published_posts = []

with open(csv_path, 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        if row['status'] == 'confirmed' and row['url']:
            published_posts.append(row)

# Trier par date de création (plus récent en premier)
published_posts.sort(key=lambda x: x['created_at'], reverse=True)

# Prendre les 3 plus récents
samples = published_posts[:3]

print(f"Total published posts: {len(published_posts)}")
print(f"\nExtracting {len(samples)} most recent samples:\n")

for i, post in enumerate(samples, 1):
    print(f"{i}. {post['web_title']}")
    print(f"   URL: {post['url']}")
    print(f"   Created: {post['created_at']}")

    # Sauvegarder le HTML dans un fichier
    html_file = output_dir / f"sample_{i}.html"
    with open(html_file, 'w', encoding='utf-8') as f:
        f.write(post['content_html'])

    # Sauvegarder aussi les métadonnées
    meta_file = output_dir / f"sample_{i}_meta.json"
    meta = {
        'id': post['id'],
        'web_title': post['web_title'],
        'url': post['url'],
        'email_subject_line': post['email_subject_line'],
        'created_at': post['created_at'],
        'content_tags': post['content_tags']
    }
    with open(meta_file, 'w', encoding='utf-8') as f:
        json.dump(meta, f, indent=2, ensure_ascii=False)

    print(f"   Saved to: {html_file.name}")
    print()

print(f"\nSamples saved to: {output_dir}")
