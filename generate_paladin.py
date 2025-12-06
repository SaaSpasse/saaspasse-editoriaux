#!/usr/bin/env python3
"""
Génère 3 variations d'images SaaSpaladin pour le dernier éditorial.
Utilise directement l'API Google Gemini (sans passer par l'UI).

Usage:
    python generate_paladin.py                    # Dernier éditorial local
    python generate_paladin.py --fetch            # Fetch dernier éditorial beehiiv d'abord
    python generate_paladin.py --file FILE.md    # Éditorial spécifique
    python generate_paladin.py --prompt "..."    # Prompt personnalisé direct
"""

import os
import sys
import json
import argparse
import base64
import subprocess
from pathlib import Path
from datetime import datetime

try:
    import requests
except ImportError:
    print("Installation de requests...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "requests", "-q"])
    import requests

# ============================================================================
# CONFIGURATION
# ============================================================================

BASE_DIR = Path(__file__).parent
CONFIG_FILE = BASE_DIR / ".gemini_config.json"
REF_IMAGE_FILE = Path.home() / "Claude Code/saaspasse-paladin/netlify/functions/ref-image.ts"
DOWNLOADS_DIR = Path.home() / "Downloads"

# Modèles Gemini (même que l'app La Forge)
MODELS = [
    {"name": "gemini-3-pro-image-preview", "label": "Gemini 3 Pro (Haute Qualité)"},
    {"name": "gemini-2.5-flash-preview-05-20", "label": "Gemini 2.5 Flash (Fallback)"},
]

# ============================================================================
# PROMPTS (identiques à l'app saaspasse-paladin)
# ============================================================================

SAASPALADIN_MASTER_PROMPT = """FORMAT: Image HORIZONTALE/PAYSAGE obligatoire, ratio 1.9:1, dimensions 1200x630 pixels (format header newsletter beehiiv).

Petit chevalier SaaSpaladin, 1 m 20.

TÊTE: Casque TRAPU et COMPACT couleur crème #F6F3EC, forme gélule/œuf HORIZONTAL (plus large que haut), proportions presque carrées. Sommet ARRONDI EN DÔME, jamais pointu ni allongé verticalement. Le casque ressemble à un œuf couché sur le côté.

YEUX: Deux fentes verticales noires #000000 parallèles, centrées sur le casque. Pas d'autre ouverture.

CORPS: Cape violette usée #7E4874, armure patinée ivoire #D5D0C6 sur mailles sombres, gants et bottes cuir brun #6B4B30.

STYLE: Illustration ligne claire franco-belge, hachures fines, style Moebius x Mike Mignola. Couleurs saturées mais terreuses, pas de dégradés numériques. Éclairage dramatique unique."""

NEGATIVE_PROMPT = """portrait orientation, vertical image, square image, 1:1 ratio,
visière horizontale, T-shaped visor, Mandalorian,
tête de boule, sphere head, ball head, bubble head,
casque pointu, sharp angles, spiky helmet, square helmet,
casque allongé, elongated helmet, tall helmet, vertical helmet, oblong helmet, stretched helmet,
casque haut, narrow helmet, slim helmet, thin helmet,
peau visible, skin visible, human chin, human nose, human neck, mouth,
glossy 3D, cartoon kawaii, Pixar, vector art, smooth gradients, photo realistic, futuristic sci-fi, low poly, blur."""

ANALYSIS_SYSTEM_INSTRUCTION = """Tu es le Directeur Artistique de "SaaSpaladin". Ton rôle est de traduire des concepts SaaS/Tech en métaphores Médiévales Fantastiques pour des illustrations.

Règles de traduction:
- Bug/Dette technique → Gobelins, boue, rouille, créatures des marais.
- Serveur/Cloud → Bibliothèque infinie, tours de pierre, cristaux flottants.
- Lancement/Deploy → Expédition, départ en quête, navire volant.
- Marketing/Sales → Crieurs publics, bannières, marché animé, pièces d'or.
- CEO/Manager → Le Paladin consultant des cartes ou des parchemins.
- Code → Runes magiques, parchemins complexes, forge.

Tâche:
1. Lis le texte fourni (newsletter).
2. Extrais le thème central.
3. Crée une description visuelle d'une scène unique mettant en scène le SaaSpaladin (le petit chevalier).
4. La description doit être une phrase descriptive concise, prête à être intégrée dans un prompt de génération d'image.

Format de réponse JSON attendu:
{
  "theme": "Le thème principal du texte",
  "fantasyConcept": "La métaphore fantastique choisie",
  "visualPrompt": "Description de la scène (ex: Le SaaSpaladin examine un parchemin runique brillant dans une bibliothèque sombre...)"
}"""


# ============================================================================
# FONCTIONS UTILITAIRES
# ============================================================================

def load_config():
    """Charge la clé API Gemini."""
    if CONFIG_FILE.exists():
        with open(CONFIG_FILE) as f:
            return json.load(f)

    # Chercher dans les variables d'environnement
    api_key = os.environ.get("GEMINI_API_KEY")
    if api_key:
        return {"api_key": api_key}

    print("Configuration Gemini manquante!")
    print(f"\nOption 1: Créez le fichier {CONFIG_FILE} avec:")
    print(json.dumps({"api_key": "VOTRE_CLE_API_GEMINI"}, indent=2))
    print("\nOption 2: Exportez la variable d'environnement:")
    print("  export GEMINI_API_KEY='votre_clé'")
    print("\nPour obtenir une clé: https://aistudio.google.com/app/apikey")
    sys.exit(1)


def load_ref_image():
    """Charge l'image de référence du SaaSpaladin depuis le fichier TypeScript."""
    if not REF_IMAGE_FILE.exists():
        print(f"Image de référence non trouvée: {REF_IMAGE_FILE}")
        sys.exit(1)

    with open(REF_IMAGE_FILE, 'r') as f:
        content = f.read()

    # Extraire le base64 entre les quotes ou backticks
    # Format: export const REF_IMAGE = `iVBORw0KGgo...`;
    import re
    match = re.search(r"export const REF_IMAGE\s*=\s*[`'\"]([\s\S]+?)[`'\"];?", content)
    if not match:
        print("Impossible d'extraire l'image de référence du fichier TypeScript")
        sys.exit(1)

    return match.group(1).strip()


def get_latest_editorial():
    """Récupère le dernier éditorial depuis le dossier local."""
    editoriaux_dir = BASE_DIR / "editoriaux"
    if not editoriaux_dir.exists():
        print(f"Dossier editoriaux non trouvé: {editoriaux_dir}")
        return None

    # Lister et trier par date (format YYYY-MM-DD-slug.md)
    files = sorted(editoriaux_dir.glob("*.md"), reverse=True)
    if not files:
        print("Aucun éditorial trouvé dans le dossier")
        return None

    latest = files[0]
    with open(latest, 'r', encoding='utf-8') as f:
        content = f.read()

    return {
        "filename": latest.name,
        "content": content
    }


# ============================================================================
# API GEMINI
# ============================================================================

def analyze_newsletter(api_key: str, text: str) -> dict:
    """Analyse le texte de la newsletter et génère le concept visuel."""
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent?key={api_key}"

    payload = {
        "systemInstruction": {
            "parts": [{"text": ANALYSIS_SYSTEM_INSTRUCTION}]
        },
        "contents": [{
            "parts": [{"text": f"Voici le contenu de la newsletter:\n\n{text}"}]
        }],
        "generationConfig": {
            "responseMimeType": "application/json",
            "responseSchema": {
                "type": "OBJECT",
                "properties": {
                    "theme": {"type": "STRING"},
                    "fantasyConcept": {"type": "STRING"},
                    "visualPrompt": {"type": "STRING"}
                },
                "required": ["theme", "fantasyConcept", "visualPrompt"]
            }
        }
    }

    print("  Analyse du texte via Gemini 2.5 Flash...")
    response = requests.post(url, json=payload, headers={"Content-Type": "application/json"})

    if response.status_code != 200:
        print(f"  Erreur API: {response.status_code}")
        print(f"  {response.text[:500]}")
        return None

    data = response.json()
    result_text = data.get("candidates", [{}])[0].get("content", {}).get("parts", [{}])[0].get("text", "{}")

    try:
        return json.loads(result_text)
    except json.JSONDecodeError:
        print(f"  Erreur parsing JSON: {result_text[:200]}")
        return None


def generate_image(api_key: str, scene_prompt: str, ref_image_base64: str, variation_num: int) -> str:
    """Génère une image via l'API Gemini."""

    full_prompt = f"""{SAASPALADIN_MASTER_PROMPT}
SCÈNE: {scene_prompt}

--no {NEGATIVE_PROMPT}"""

    # Essayer chaque modèle
    for model in MODELS:
        model_name = model["name"]
        model_label = model["label"]

        url = f"https://generativelanguage.googleapis.com/v1beta/models/{model_name}:generateContent?key={api_key}"

        payload = {
            "contents": [{
                "parts": [
                    {"text": "Voici une image de référence du personnage SaaSpaladin. Génère une nouvelle image en respectant EXACTEMENT ce style de casque (trapu, compact, arrondi):"},
                    {"inlineData": {"mimeType": "image/png", "data": ref_image_base64}},
                    {"text": full_prompt}
                ]
            }],
            "generationConfig": {
                "responseModalities": ["image", "text"],
                "imageConfig": {
                    "aspectRatio": "16:9"  # Closest to 1.9:1 for beehiiv header (1200x630)
                }
            }
        }

        print(f"  Génération #{variation_num} via {model_label}...")

        try:
            response = requests.post(
                url,
                json=payload,
                headers={"Content-Type": "application/json"},
                timeout=120
            )

            if response.status_code == 200:
                data = response.json()
                parts = data.get("candidates", [{}])[0].get("content", {}).get("parts", [])

                for part in parts:
                    if "inlineData" in part:
                        return part["inlineData"]["data"], model_label

                print(f"    Pas d'image dans la réponse de {model_label}")
            else:
                error_msg = response.text[:200] if response.text else "No error message"
                print(f"    {model_label} a échoué ({response.status_code}): {error_msg}")

        except requests.exceptions.Timeout:
            print(f"    Timeout avec {model_label}")
        except Exception as e:
            print(f"    Erreur avec {model_label}: {e}")

    return None, None


def save_image(image_base64: str, editorial_name: str, variation_num: int, output_dir: Path) -> Path:
    """Sauvegarde l'image en PNG."""
    import re
    # Nettoyer le nom de l'éditorial pour le filename
    # Enlever l'extension .md
    clean_name = editorial_name.replace(".md", "")
    # Enlever la date au début (format YYYY-MM-DD-)
    clean_name = re.sub(r"^\d{4}-\d{2}-\d{2}-", "", clean_name)
    # Garder seulement les 50 premiers caractères
    clean_name = clean_name[:50]

    filename = f"SaaSpaladin-{clean_name}-v{variation_num}.png"

    filepath = output_dir / filename

    image_bytes = base64.b64decode(image_base64)
    with open(filepath, "wb") as f:
        f.write(image_bytes)

    return filepath


# ============================================================================
# MAIN
# ============================================================================

def main():
    parser = argparse.ArgumentParser(description="Génère 3 images SaaSpaladin pour un éditorial")
    parser.add_argument("--fetch", action="store_true", help="Fetch le dernier éditorial beehiiv d'abord")
    parser.add_argument("--file", help="Fichier éditorial spécifique (.md)")
    parser.add_argument("--prompt", help="Prompt visuel personnalisé (skip analyse)")
    parser.add_argument("--count", type=int, default=3, help="Nombre d'images à générer (défaut: 3)")
    parser.add_argument("--output", help="Dossier de sortie (défaut: ~/Downloads)")
    args = parser.parse_args()

    print("=" * 60)
    print("SaaSpaladin Image Generator")
    print("=" * 60)

    # Charger la configuration
    config = load_config()
    api_key = config["api_key"]

    # Charger l'image de référence
    print("\n[1/4] Chargement de l'image de référence...")
    ref_image = load_ref_image()
    print(f"  Image de référence chargée ({len(ref_image) // 1024} KB)")

    # Déterminer le contenu à utiliser
    editorial_name = "custom-prompt"

    if args.prompt:
        # Prompt direct fourni
        visual_prompt = args.prompt
        print(f"\n[2/4] Utilisation du prompt personnalisé")
        print(f"  Prompt: {visual_prompt[:100]}...")
    else:
        # Récupérer l'éditorial
        if args.fetch:
            print("\n[2/4] Fetch du dernier éditorial beehiiv...")
            fetch_script = BASE_DIR / "fetch_beehiiv.py"
            if fetch_script.exists():
                subprocess.run([sys.executable, str(fetch_script)], check=True)
            else:
                print(f"  Script fetch non trouvé: {fetch_script}")
                sys.exit(1)

        if args.file:
            filepath = Path(args.file)
            if not filepath.exists():
                filepath = BASE_DIR / "editoriaux" / args.file
            if not filepath.exists():
                print(f"Fichier non trouvé: {args.file}")
                sys.exit(1)
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            editorial = {"filename": filepath.name, "content": content}
        else:
            print("\n[2/4] Récupération du dernier éditorial local...")
            editorial = get_latest_editorial()

        if not editorial:
            print("Aucun éditorial trouvé!")
            sys.exit(1)

        editorial_name = editorial["filename"]
        print(f"  Éditorial: {editorial_name}")

        # Analyser le contenu
        print("\n[3/4] Analyse du contenu...")
        analysis = analyze_newsletter(api_key, editorial["content"])

        if not analysis:
            print("Erreur lors de l'analyse!")
            sys.exit(1)

        print(f"  Thème: {analysis.get('theme', 'N/A')}")
        print(f"  Concept: {analysis.get('fantasyConcept', 'N/A')}")
        visual_prompt = analysis.get("visualPrompt", "")
        print(f"  Prompt visuel: {visual_prompt[:100]}...")

    # Générer les images
    output_dir = Path(args.output) if args.output else DOWNLOADS_DIR
    output_dir.mkdir(exist_ok=True)

    print(f"\n[4/4] Génération de {args.count} images...")
    print(f"  Dossier de sortie: {output_dir}")

    generated = []
    for i in range(1, args.count + 1):
        image_data, model_used = generate_image(api_key, visual_prompt, ref_image, i)

        if image_data:
            filepath = save_image(image_data, editorial_name, i, output_dir)
            generated.append((filepath, model_used))
            print(f"    ✓ Image {i} sauvegardée: {filepath.name}")
        else:
            print(f"    ✗ Échec génération image {i}")

    # Résumé
    print("\n" + "=" * 60)
    print("RÉSUMÉ")
    print("=" * 60)

    if generated:
        print(f"\n{len(generated)}/{args.count} images générées avec succès:\n")
        for filepath, model in generated:
            print(f"  • {filepath}")
            print(f"    (via {model})")

        # Ouvrir le dossier Downloads
        print(f"\nOuverture du dossier {output_dir}...")
        subprocess.run(["open", str(output_dir)])
    else:
        print("\nAucune image n'a pu être générée.")
        sys.exit(1)


if __name__ == "__main__":
    main()
