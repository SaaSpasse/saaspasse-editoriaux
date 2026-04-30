Wrap de fin de session — sauvegarde le contexte aux bons endroits pour reprendre facilement la prochaine fois.

> **Note pour la première utilisation:** ce skill assume que ton projet a un fichier `MEMORY.md` (système de mémoire auto de Claude Code). Si tu ne l'as pas, Claude va le créer automatiquement dans le dossier memory du projet courant. Tu peux aussi adapter le path en bas pour pointer vers ton propre système de notes (Obsidian, Notion, fichier markdown perso, etc.).

Analyse la conversation actuelle et fais les étapes suivantes:

## 1. Analyser la session

Identifie:
- **Accompli** — Ce qu'on a fait (actions concrètes, pas du fluff)
- **En cours / pending** — Ce qui reste à faire, prochaines étapes
- **Chaîne d'outils** — Quels MCPs/outils ont été utilisés et dans quel ordre (seulement si c'est un pattern non-trivial worth remembering)
- **Gotchas** — Problèmes rencontrés, tokens expirés, bugs MCP, workarounds utilisés
- **Décisions** — Choix techniques ou stratégiques faits pendant la session

## 2. Mettre à jour la memory du projet

Écris un résumé concis dans le fichier `MEMORY.md` du projet actuel (auto memory directory).

Format:
```markdown
### Wrap [date YYYY-MM-DD]

**Accompli:**
- Point 1
- Point 2

**Pending:**
- Point 1

**Gotchas/notes:**
- Seulement si pertinent
```

Règles:
- Ajouter la section au début du fichier (après le titre H1), pas à la fin
- Si un wrap du même jour existe déjà, le mettre à jour au lieu d'en créer un nouveau
- Garder le fichier `MEMORY.md` sous 200 lignes (c'est chargé dans le system prompt)
- Si le fichier déborde, condenser les vieilles sections ou déplacer le détail dans un fichier séparé dans le même dossier memory
- Ne pas répéter des infos déjà présentes dans `MEMORY.md` ou `CLAUDE.md`

## 3. Proposer des apprentissages `CLAUDE.md` (si pertinent)

Si la session a révélé:
- Un gotcha reproductible (bug MCP, token qui expire, etc.)
- Un pattern/recette réutilisable
- Une décision structurante

Alors proposer de l'ajouter au `CLAUDE.md` ou `learnings.md`. Demander confirmation avant d'écrire.

Si rien de notable, ne rien proposer — pas besoin de forcer un apprentissage à chaque session.

## 4. Afficher le résumé

Affiche un résumé court de ce qui a été sauvegardé:
- Fichier(s) modifié(s) avec chemin
- Nombre de points capturés
- Apprentissages proposés (ou "aucun")

Garder l'output minimal — l'utilisateur est sur le point de quitter.
