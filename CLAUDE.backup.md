# Index d'éditoriaux d'infolettre SaaSpasse

## Mission principale

Quand Frank me demande d'aller chercher le dernier éditorial sur beehiiv, voici le workflow complet.

---

## Credentials beehiiv

- **URL**: https://app.beehiiv.com
- **Email**: francois@saaspasse.com
- **Password**: Angus00emokid1

---

## Workflow complet: Récupérer et publier un éditorial

### Étape 1: Télécharger le HTML depuis beehiiv (Playwright MCP)

1. Naviguer vers https://app.beehiiv.com
2. Se connecter avec les credentials ci-dessus
3. Aller dans **Posts**
4. Cliquer sur le post le plus récent (ou celui demandé)
5. Cliquer sur la **flèche vers le bas** à côté du bouton principal
6. Cliquer sur **Download HTML**
7. Le fichier sera téléchargé dans `~/.playwright-mcp/`

### Étape 2: Convertir le HTML

```bash
python3 "/Users/francoislanthiernadeau/Claude Code/posts-infolettre/convert_newsletter.py" "/Users/francoislanthiernadeau/.playwright-mcp/post-html-XXXXX.html" "/Users/francoislanthiernadeau/Claude Code/posts-infolettre"
```

Le script crée automatiquement:
- `editoriaux/YYYY-MM-DD-slug.md` (texte pur du copywriting)
- `posts-complets/YYYY-MM-DD-slug.md` (version complète avec metadata YAML)

### Étape 3: Vérifier les fichiers créés

```bash
ls -la "/Users/francoislanthiernadeau/Claude Code/posts-infolettre/editoriaux" | tail -5
ls -la "/Users/francoislanthiernadeau/Claude Code/posts-infolettre/posts-complets" | tail -5
```

### Étape 4: Push sur GitHub

```bash
cd "/Users/francoislanthiernadeau/Claude Code/posts-infolettre"
git add editoriaux/ posts-complets/
git commit -m "Ajout éditorial: [TITRE DE L'ÉDITORIAL]"
git push origin main
```

### Étape 5: Vérifier le déploiement

Le repo GitHub (SaaSpasse/saaspasse-editoriaux) est connecté à Netlify. Le déploiement est automatique après le push.

### Étape 6: Générer les images sur La Forge (Playwright MCP)

1. Naviguer vers https://paladin.saaspasse.com
2. Dans le dropdown "Charger un éditorial existant", sélectionner le nouvel éditorial
3. Cliquer sur **"Extraire l'essence visuelle →"**
4. Attendre que l'essence visuelle soit générée
5. Sélectionner le modèle **Gemini 3 Pro (Haute Qualité)**
6. Cliquer sur **"✨ Générer l'Illustration"**
7. Attendre la génération (~10-15 secondes)
8. Cliquer sur **"Télécharger"** (image sauvée dans `~/.playwright-mcp/`)
9. Cliquer sur **"🔄 Régénérer"**
10. Répéter téléchargement + régénération pour avoir **3 images au total**

**Note importante**: Google (Gemini) a tendance à générer les casques du paladin trop larges. C'est pourquoi on génère 3 versions pour avoir des options.

Les images sont sauvegardées avec le format: `SaaSpaladin-header-[slug].png`

---

## State of Success (Vérification finale)

Tout est bon si:

1. **HTML téléchargé** - Le fichier `post-html-*.html` existe dans `~/.playwright-mcp/`
2. **Fichiers créés** - Les deux versions existent dans `editoriaux/` et `posts-complets/`
3. **GitHub updaté** - `git status` montre "nothing to commit, working tree clean"
4. **Netlify déployé** - Attendre ~30 secondes après le push
5. **Visible sur La Forge** - L'éditorial apparaît dans le dropdown "Charger un éditorial existant"
6. **Images générées** - 3 fichiers `SaaSpaladin-header-*.png` existent dans `~/.playwright-mcp/`

---

## Dossiers

- `editoriaux/` : Texte pur du copywriting (essence de l'article)
- `posts-complets/` : Version complète avec metadata YAML

## Dépôt GitHub

- **Repo**: https://github.com/SaaSpasse/saaspasse-editoriaux
- **Branche principale**: main
- **Connecté à**: Netlify (auto-deploy)

## Format du frontmatter YAML (posts-complets)

```yaml
date: 'YYYY-MM-DD'
title: Titre de l'éditorial
url: https://saaspasse.beehiiv.com/p/slug
slug: slug
source: beehiiv
word_count: X
reading_time_min: X
editorial_confidence: high
liens_internes: X
liens_externes: X
top_domains: [...]
personnes: [...]
```

## Scripts disponibles

- `convert_newsletter.py` - Conversion principale HTML → MD (recommandé)
- `convert_html.py` - Conversion alternative
- `convert_single.py` - Pour un seul fichier
- `analyzer.py` - Analyse de contenu
