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

    # Synchroniser avec GitHub
    sync_with_github(base_dir, metadata)

def sync_with_github(base_dir, metadata):
    """Synchronise automatiquement les nouveaux fichiers avec GitHub"""
    print(f"\n🔄 Synchronisation avec GitHub...")

    try:
        # Vérifier qu'on est dans un repo Git
        result = subprocess.run(
            ['git', '-C', str(base_dir), 'status'],
            capture_output=True,
            text=True,
            check=False
        )

        if result.returncode != 0:
            print("⚠️  Pas un repo Git. Synchronisation ignorée.")
            return

        # Git add
        subprocess.run(
            ['git', '-C', str(base_dir), 'add', 'editoriaux/', 'posts-complets/'],
            check=True
        )

        # Git commit
        title = metadata.get('title', 'Nouveau post')
        commit_msg = f"""Ajout éditorial: {title}

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>"""

        result = subprocess.run(
            ['git', '-C', str(base_dir), 'commit', '-m', commit_msg],
            capture_output=True,
            text=True,
            check=False
        )

        if "nothing to commit" in result.stdout:
            print("✓ Aucun changement à synchroniser")
            return

        # Git push
        subprocess.run(
            ['git', '-C', str(base_dir), 'push'],
            check=True
        )

        print("✓ Synchronisé avec GitHub!")
        print("  → https://github.com/SaaSpasse/saaspasse-editoriaux")

    except subprocess.CalledProcessError as e:
        print(f"⚠️  Erreur de synchronisation Git: {e}")
        print("   Vous pouvez synchroniser manuellement avec:")
        print("   cd ~/Claude\\ Code/posts-infolettre && git add . && git commit -m 'update' && git push")

if __name__ == '__main__':
    main()
