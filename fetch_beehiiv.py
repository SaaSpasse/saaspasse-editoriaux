#!/usr/bin/env python3
"""
Script pour récupérer les posts beehiiv via API au lieu de Playwright.
Économise ~20,000 tokens par exécution.

Usage:
    python fetch_beehiiv.py                    # Récupère le dernier post
    python fetch_beehiiv.py --post-id POST_ID  # Récupère un post spécifique
    python fetch_beehiiv.py --list             # Liste les 10 derniers posts
"""

import os
import sys
import json
import argparse
import subprocess
from pathlib import Path
from datetime import datetime

try:
    import requests
except ImportError:
    print("Installation de requests...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "requests", "-q"])
    import requests

# Configuration
CONFIG_FILE = Path(__file__).parent / ".beehiiv_config.json"
BASE_DIR = Path(__file__).parent
CONVERT_SCRIPT = BASE_DIR / "convert_newsletter.py"


def load_config():
    """Charge la configuration API."""
    if not CONFIG_FILE.exists():
        print("Configuration manquante!")
        print(f"Créez le fichier {CONFIG_FILE} avec:")
        print(json.dumps({
            "api_key": "VOTRE_CLE_API",
            "publication_id": "pub_XXXXXXXX"
        }, indent=2))
        print("\nPour obtenir ces valeurs:")
        print("1. Allez sur https://app.beehiiv.com")
        print("2. Settings > API (sous Workspace Settings)")
        print("3. Créez une nouvelle clé API")
        print("4. Copiez aussi le Publication ID (en bas de la page)")
        sys.exit(1)

    with open(CONFIG_FILE) as f:
        return json.load(f)


def get_headers(api_key):
    """Retourne les headers pour l'API."""
    return {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }


def list_posts(config, limit=10):
    """Liste les derniers posts."""
    url = f"https://api.beehiiv.com/v2/publications/{config['publication_id']}/posts"
    params = {
        "limit": limit,
        "status": "confirmed",  # Posts publiés seulement
        "order_by": "publish_date",
        "direction": "desc"
    }

    response = requests.get(url, headers=get_headers(config['api_key']), params=params)
    response.raise_for_status()

    data = response.json()
    return data.get('data', [])


def post_exists_in_repo(slug, publish_date):
    """Vérifie si un post existe déjà dans le repo."""
    if isinstance(publish_date, int):
        date_str = datetime.fromtimestamp(publish_date).strftime('%Y-%m-%d')
    else:
        date_str = str(publish_date)[:10]

    # Vérifier dans editoriaux/
    pattern = f"{date_str}-{slug}*.md"
    existing = list(BASE_DIR.glob(f"editoriaux/{pattern}"))
    return len(existing) > 0


def get_post(config, post_id=None, check_exists=False):
    """
    Récupère un post avec son contenu HTML.
    Si post_id est None, récupère le dernier éditorial (audience=both).
    Si check_exists=True, retourne None si le post existe déjà dans le repo.
    """
    if post_id is None:
        # Récupérer les derniers posts et trouver le premier éditorial (audience=both)
        posts = list_posts(config, limit=10)
        if not posts:
            print("Aucun post trouvé!")
            return None

        # Filtrer pour ne garder que les vrais éditoriaux (audience=both)
        # Les annonces aux SaasPals sont audience=premium ou audience=free
        editorials = [p for p in posts if p.get('audience') == 'both']
        if not editorials:
            print("Aucun éditorial trouvé (que des annonces audience=premium/free)")
            return None

        latest = editorials[0]
        post_id = latest['id']
        title = latest.get('title', 'Sans titre')
        slug = latest.get('slug', '')
        publish_date = latest.get('publish_date')

        # Vérifier si déjà dans le repo
        if check_exists and slug and post_exists_in_repo(slug, publish_date):
            print(f"Le dernier éditorial est déjà dans le repo: {title}")
            return None

        print(f"Dernier post trouvé: {title}")

    url = f"https://api.beehiiv.com/v2/publications/{config['publication_id']}/posts/{post_id}"
    params = {
        "expand[]": ["free_web_content", "free_email_content"]
    }

    response = requests.get(url, headers=get_headers(config['api_key']), params=params)
    response.raise_for_status()

    return response.json().get('data')


def save_html(post, output_dir=None):
    """Sauvegarde le HTML du post."""
    if output_dir is None:
        output_dir = Path.home() / ".playwright-mcp"
    output_dir = Path(output_dir)
    output_dir.mkdir(exist_ok=True)

    # Utiliser le contenu web (plus complet que email)
    html_content = post.get('content', {}).get('free', {}).get('web', '')

    if not html_content:
        # Fallback sur le contenu email
        html_content = post.get('content', {}).get('free', {}).get('email', '')

    if not html_content:
        print("Aucun contenu HTML trouvé dans le post!")
        return None

    # Générer un nom de fichier
    slug = post.get('slug', 'post')
    timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    filename = f"post-html-{slug}-{timestamp}.html"
    filepath = output_dir / filename

    # Ajouter les métadonnées dans le HTML pour que le convertisseur les trouve
    title = post.get('title', 'Sans titre')
    publish_date = post.get('publish_date')
    if isinstance(publish_date, int):
        # Timestamp Unix
        date_str = datetime.fromtimestamp(publish_date).strftime('%Y-%m-%d')
    elif publish_date:
        # String ISO
        try:
            dt = datetime.fromisoformat(str(publish_date).replace('Z', '+00:00'))
            date_str = dt.strftime('%Y-%m-%d')
        except:
            date_str = str(publish_date)[:10]
    else:
        date_str = datetime.now().strftime('%Y-%m-%d')

    web_url = post.get('web_url', f"https://saaspasse.beehiiv.com/p/{slug}")

    # Wrapper le HTML avec les métadonnées
    full_html = f"""<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>{title}</title>
    <meta name="publish-date" content="{date_str}">
    <meta name="url" content="{web_url}">
    <meta name="slug" content="{slug}">
</head>
<body>
{html_content}
</body>
</html>"""

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(full_html)

    print(f"HTML sauvegardé: {filepath}")
    return filepath


def convert_html(html_path):
    """Convertit le HTML en Markdown via le script existant."""
    if not CONVERT_SCRIPT.exists():
        print(f"Script de conversion non trouvé: {CONVERT_SCRIPT}")
        return False

    result = subprocess.run(
        [sys.executable, str(CONVERT_SCRIPT), str(html_path), str(BASE_DIR)],
        capture_output=True,
        text=True
    )

    print(result.stdout)
    if result.returncode != 0:
        print(f"Erreur de conversion: {result.stderr}")
        return False

    return True


def git_commit(title):
    """Commit et push les changements."""
    os.chdir(BASE_DIR)

    # Add
    subprocess.run(["git", "add", "editoriaux/", "posts-complets/"], check=True)

    # Commit
    commit_msg = f"Ajout éditorial: {title}"
    result = subprocess.run(
        ["git", "commit", "-m", commit_msg],
        capture_output=True,
        text=True
    )

    if "nothing to commit" in result.stdout or "nothing to commit" in result.stderr:
        print("Rien à committer (fichiers déjà à jour)")
        return True

    if result.returncode != 0:
        print(f"Erreur git commit: {result.stderr}")
        return False

    # Push
    result = subprocess.run(["git", "push", "origin", "main"], capture_output=True, text=True)
    if result.returncode != 0:
        print(f"Erreur git push: {result.stderr}")
        return False

    print("Changements poussés sur GitHub!")
    return True


def main():
    parser = argparse.ArgumentParser(description="Récupère les posts beehiiv via API")
    parser.add_argument("--post-id", help="ID du post à récupérer")
    parser.add_argument("--list", action="store_true", help="Liste les derniers posts")
    parser.add_argument("--no-convert", action="store_true", help="Ne pas convertir en Markdown")
    parser.add_argument("--no-git", action="store_true", help="Ne pas commit/push sur Git")
    parser.add_argument("--force", action="store_true", help="Forcer même si déjà dans le repo")
    args = parser.parse_args()

    config = load_config()

    if args.list:
        print("\n10 derniers posts:")
        print("-" * 60)
        for post in list_posts(config):
            status = post.get('status', '?')
            audience = post.get('audience', '?')
            title = post.get('title', 'Sans titre')[:35]
            post_id = post.get('id', '?')
            publish_date = post.get('publish_date')
            if isinstance(publish_date, int):
                date = datetime.fromtimestamp(publish_date).strftime('%Y-%m-%d')
            elif publish_date:
                date = str(publish_date)[:10]
            else:
                date = '????-??-??'
            # Marquer les vrais éditoriaux vs annonces
            marker = "📝" if audience == "both" else "📢"
            print(f"{marker} [{audience:7}] {date} | {title}")
            print(f"           ID: {post_id}")
        print("\n📝 = éditorial (audience=both)  📢 = annonce (premium/free)")
        return

    # Récupérer le post
    print("Récupération du post via API beehiiv...")
    # Vérifier si existe déjà (sauf si --force ou --post-id spécifique)
    check_exists = not args.force and not args.post_id
    post = get_post(config, args.post_id, check_exists=check_exists)

    if not post:
        # Si check_exists était True, c'est peut-être juste que le post existe déjà (pas une erreur)
        if check_exists:
            sys.exit(0)  # Succès, rien à faire
        sys.exit(1)

    title = post.get('title', 'Sans titre')
    print(f"\nPost: {title}")
    print(f"Slug: {post.get('slug', '?')}")
    print(f"Status: {post.get('status', '?')}")

    # Sauvegarder le HTML
    html_path = save_html(post)
    if not html_path:
        sys.exit(1)

    # Convertir
    if not args.no_convert:
        print("\nConversion en Markdown...")
        if not convert_html(html_path):
            sys.exit(1)

    # Git
    if not args.no_git and not args.no_convert:
        print("\nCommit et push sur GitHub...")
        git_commit(title)

    print("\nTerminé!")


if __name__ == "__main__":
    main()
