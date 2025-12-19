# SaaSpasse - Archive des Éditoriaux

Archive des éditoriaux d'infolettres SaaSpasse pour référence et rédaction avec Claude Web et ChatGPT.

## 📁 Structure

```
posts-infolettre/
├── posts-complets/          # 83 posts avec metadata YAML complète (RECOMMANDÉ pour Claude Web)
│   ├── 2023-06-15-elfe-troll-wu-tang.md
│   ├── 2024-09-06-ta-job-cest-de-vendre-ta-job.md
│   └── ...
├── editoriaux/              # 53 éditoriaux (texte pur, sans metadata)
│   ├── 2024-09-06-ta-job-cest-de-vendre-ta-job.md
│   └── ...
├── samples/                 # Échantillons HTML et analyses
└── README.md               # Ce fichier
```

## 🎯 Utilisation avec Claude Web

### Pour uploader dans Claude Projects

1. **Télécharger le dossier** `posts-complets/` de ce repo GitHub
2. **Créer un Claude Project** sur https://claude.ai
3. **Ajouter les fichiers** comme "Project Knowledge"

### Metadata disponible dans `posts-complets/`

Chaque fichier contient un frontmatter YAML avec:
- `url`: Lien vers la version publiée (IMPORTANT pour références)
- `date`: Date de publication
- `title`: Titre de l'éditorial
- `word_count`: Nombre de mots
- `liens_internes`: Liens vers d'autres contenus SaaSpasse
- `personnes`: Personnes mentionnées (avec LinkedIn)
- `compagnies`: Compagnies mentionnées

### Exemple d'utilisation avec Claude

**Prompt type:**
> "Trouve-moi des références sur le storytelling ou la vente dans mes éditoriaux précédents. Donne-moi le titre et l'URL pour que je puisse les intégrer dans mon nouveau brouillon."

Claude pourra:
1. Chercher dans le contenu textuel
2. Identifier les éditoriaux pertinents
3. Vous donner l'URL exacte à insérer

## 🔄 Workflow automatisé (recommandé)

### Ajouter un nouvel éditorial

**Le workflow est maintenant entièrement automatisé!**

1. **Télécharger la version HTML** de votre éditorial publié
2. **Donner le fichier à Claude Code** et dire:
   > "Convertis-moi ça dans les deux versions de Markdown qu'on a besoin, puis mets-le dans le dossier posts-infolettre"
3. Claude Code va automatiquement:
   - ✅ Convertir en Markdown (éditorial + post complet)
   - ✅ Sauvegarder dans les bons dossiers
   - ✅ `git add` + `commit` + `push` vers GitHub
   - ✅ Claude Web verra la mise à jour automatiquement!

**C'est tout!** Plus besoin de toucher à Git manuellement.

---

## 🔧 Workflow manuel (si nécessaire)

### Si vous ajoutez des fichiers manuellement

```bash
# 1. Naviguer vers le dossier
cd "/Users/francoislanthiernadeau/Claude Code/posts-infolettre"

# 2. Ajouter les nouveaux fichiers
git add posts-complets/
git add editoriaux/

# 3. Vérifier ce qui va être committé
git status

# 4. Créer le commit
git commit -m "Ajout éditorial: [TITRE]"

# 5. Synchroniser avec GitHub
git push
```

### Commandes Git utiles

```bash
# Voir l'état actuel
git status

# Voir les derniers commits
git log --oneline -5

# Voir les changements avant de committer
git diff

# Pull les derniers changements (si modifié ailleurs)
git pull
```

## 📊 Statistiques

- **83 posts complets** avec metadata
- **53 éditoriaux** (texte pur)
- Date du plus ancien: 2023-06-15
- Date du plus récent: 2025-10-24

## 📝 Notes

- Le fichier CSV n'est **pas** synchronisé (`.gitignore`)
- La source de vérité reste le dossier local
- GitHub sert de miroir et de source pour Claude Web/ChatGPT
