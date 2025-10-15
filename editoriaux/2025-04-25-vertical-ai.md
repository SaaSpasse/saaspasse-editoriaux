What's up folks,

Merci d'être là. L’édito d’abord—les nouvelles après.

En février, [Guillaume](https://www.linkedin.com/in/guillaume-falardeau-b213768b/?utm_source=saaspasse.beehiiv.com&utm_medium=newsletter&utm_campaign=vertical-ai) m’a partagé un article :

*→ *[Tomorrow’s Titans: Vertical AI](https://www.nea.com/blog/tomorrows-titans-vertical-ai?utm_source=saaspasse.beehiiv.com&utm_medium=newsletter&utm_campaign=vertical-ai)

Il a passé des mois dans le goulag de mes onglets Chrome, jusqu’à sa résurrection, dimanche de Pâques.

Les auteurs sont partenaires chez [NEA](https://www.nea.com/?utm_source=saaspasse.beehiiv.com&utm_medium=newsletter&utm_campaign=vertical-ai), une petite firme VC circa 1977. Ils gèrent >$25B et ont investi tôt dans Cloudflare, Robinhood, Duolingo, MongoDB, et plus.

J’ai commencé à lire et prendre des notes. Quand je ne comprends pas quelque chose, j’écris là-dessus. Ça explique toute la poésie de mes années d’uni.

NEA ont une cool thèse :

Si tu canalises la puissance des modèles fondamentaux d’IA dans une opportunité d’affaires verticale, tu creuses une bonne vieille DOUVE (*moat*).

Armé d’expertise et d’IA, tu plonges creux dans une industrie (ex: légal, finance, santé) et tu y améliores l’ensemble de la chaîne de production.

Tu tasses les géants—*systems of record*—avec tes agents—*systems of actions*.

Dans cet édito, je te vulgarise leur thèse du mieux que je peux et j’y ajoute mon grain de sel [himalayen](https://fr.wikipedia.org/wiki/Himalayen?utm_source=saaspasse.beehiiv.com&utm_medium=newsletter&utm_campaign=vertical-ai).
Si tu as des questions, tu peux écrire à Guillaume.

### TL;DR sur le vertical

Quand on parle d’une verticale, on veut simplement dire une tranche de marché spécifique à une industrie.

**Horizontal** : le produit règle des problèmes pour un paquet de compagnies, **peu importe leur industrie**.

→ Couvre souvent une **fonction** en entreprise dans tous les secteurs.

- **Hubspot** permet à n’importe quelle PME de gérer ses leads dans leur CRM.

- [Workleap](https://workleap.com/?utm_source=saaspasse.beehiiv.com&utm_medium=newsletter&utm_campaign=vertical-ai) → gérer ses RH/TI (ShareGate).

- [Missive](https://missiveapp.com/?utm_source=saaspasse.beehiiv.com&utm_medium=newsletter&utm_campaign=vertical-ai) → collaborer en équipe autour de courriels.

**Vertical** : le produit règle un paquet de problèmes pour les compagnies d’**une industrie précise**.

→ Sert des joueurs partageant les mêmes processus métier, normes et jargon.

- [Procore](https://www.procore.com/en-ca?utm_source=saaspasse.beehiiv.com&utm_medium=newsletter&utm_campaign=vertical-ai) permet aux compagnies de construction de gérer leurs plans, projets, facturation, équipes, ressources, etc.

- [gaiia](https://www.gaiia.com/?utm_source=saaspasse.beehiiv.com&utm_medium=newsletter&utm_campaign=vertical-ai) → Internet Service Providers (ISPs)

- [Empego](https://www.empego.ca/?utm_source=saaspasse.beehiiv.com&utm_medium=newsletter&utm_campaign=vertical-ai) → pharmaciens

quick o3 prompt

Plein de startups ont misé sur une verticale pour gagner.

Tu limites ton [TAM](https://en.wikipedia.org/wiki/Total_addressable_market?utm_source=saaspasse.beehiiv.com&utm_medium=newsletter&utm_campaign=vertical-ai), mais les barrières à l’entrée sont plus élevées pour les gros joueurs généralistes. Ils parlent pas le jargon, et ont pas l’expertise/l’incitatif pour couvrir tous les cas d’utilisation spécifiques à un métier.

Souvent, tu augmentes la rétention quand tu t’intègres aussi loin dans les *workflows* d’une compagnie. **STICKY**.

Si tu veux lire un excellent article sur comment gagner en vertical SaaS spécifiquement :

→ [Control Point Patterns (Tidemark)](https://www.notion.so/Vertical-AI-1dc5c10632bb8033bfc5f8c94c661add?pvs=21&utm_source=saaspasse.beehiiv.com&utm_medium=newsletter&utm_campaign=vertical-ai)

PS: quand j’aurai un peu de temps (lol), je couvrirai la nuance avec les produits **orthogonal **😵‍💫

### Qu’est-ce qui change avec l’AI?

> *As AI capabilities mature to offer generative, agentic and multi-modal functions, we see an exciting opportunity for new verticalized applications.*

> 
> *As AI capabilities mature to offer generative, agentic and multi-modal functions, we see an exciting opportunity for new verticalized applications.*

> 
> *Tomorrow’s Titans: Vertical AI*

*All right*, on se démêle un peu, histoire de comprendre de quoi l’IA actuelle est capable 👇

Capacité IA

Définition simple

Exemple concret

**Générative**

Le modèle **génère du contenu** : texte, code, image, vidéo ou audio. Il apprend sur d’énormes *datasets*, et produit un résultat quand on lui donne une consigne (prompt).

ChatGPT résume le site de ton concurrent. Midjourney dessine un visuel pour ta campagne. Claude écrit ta fonction *serverless* à ta place.

**Agentique**

L’IA **planifie et exécute** des actions pour atteindre un objectif : lire, décider, appeler des outils, boucler jusqu’au résultat.

Lindy parcourt tes emails, détecte ceux qui exigent un rendez-vous, consulte ton agenda et répond avec tes disponibilités, sans intervention humaine.

**Multimodale**

Le système **comprend et produit plusieurs types de données** (texte, images, audio, vidéo, code) **dans le même flux** et peut raisonner en combinant ces canaux.

On prend une photo d’un tableau blanc barbouillé ; l’IA décrit le schéma, le convertit en graphique interactif et explique le tout à l’oral.

**Bienvenue dans la nouvelle ère I/O (Input/Output).**

Tu peux demander *basically* n’importe quoi de n’importe quelle manière au système et il va trouver lui-même la manière de te répondre.

Bon, des fois ça pète, hallucine, ou s’intègre moins bien avec des systèmes déterministes—le bon vieux code classique. Plus dur à tester / QA, *sure*.

Mais j’aimerais te rappeler que **ça fait seulement deux ans** qu’on a vécu le gros moment OMG de ChatGPT…

Les modèles (et produits) s’améliorent extrêmement vite. “Ouais mais on est en train de pogner un plateau on dirait!” Peut-être bien. Mais même si ça stoppe à l’état actuel, les opportunités de disruption en tech sont *insane*.

Si tu penses que l’IA agentique relève de la sphère BS, [je t’invite à regarder ça](https://www.youtube.com/watch?v=_qr7ogLpTJs&utm_source=saaspasse.beehiiv.com&utm_medium=newsletter&utm_campaign=vertical-ai).

### Le nouveau David est un agent?

Comme le mentionnent les auteurs, l’époque cloud a vu son lot de succès en vertical SaaS. Des Goliath comme Guidewire, Toast, ServiceTitan.

Je remâche leurs mots, mais ces vainqueurs suivaient une recette : devenir le *system of record* (où la data client vit), supporter les flux financiers (paiements+facturation), créer un *network effect* en amenant tous acteurs de l’industrie sur une même plateforme.

Avec l’IA, NEA suppose une disruption via les systèmes agentiques. *AKA AI agents*.

> *The nature of software is changing from a system of record to a system of actions. In the AI era, defensibility is likely to emerge from specialization and orchestration of AI agents, lending itself to verticalized solutions. Early examples include **Harvey AI** and **Abridge**.*

> 
> *The nature of software is changing from a system of record to a system of actions. In the AI era, defensibility is likely to emerge from specialization and orchestration of AI agents, lending itself to verticalized solutions. Early examples include*

> 
> *[Harvey AI](https://www.harvey.ai/?utm_source=saaspasse.beehiiv.com&utm_medium=newsletter&utm_campaign=vertical-ai)*

> 
> *and*

> 
> *[Abridge](https://www.abridge.com/?utm_source=saaspasse.beehiiv.com&utm_medium=newsletter&utm_campaign=vertical-ai)*

> 
> *.*

Comme on disait, leur thèse soutient que si tu diriges la puissance croissante des modèles fondamentaux vers une niche sectorielle, tu te bâtis une solide douve défensive.

Ton *play*?

1. Comprendre en profondeur les détails et exceptions d’une industrie. exemples : notaires, psychiatres, fiscalistes

2. Collecter une quantité phénoménale de données non-structurées dans l’industrie. exemples : contrats, factures, appels, transcripts, questionnaires, actualités, courriels, reviews

3. Automatiser et améliorer toute la chaîne d’actions / de production dans l’industrie avec l’IA. exemples : agents de *workflows*, agents vocaux, recherche sémantique, génération de contenu

La thèse repose sur quelques points importants :

1. **La majorité de la donnée dans le monde est non-structurée**.

2. Les agents IA augmentent la capacité des corporations & professionnels à fournir des services en demande.

3. Plusieurs industries critiquent manquent de main d’oeuvre (plombiers, électriciens, comptables, entre autres).

4. Les agents IA *scale* plus facilement que les humains.

Bref, il existe dans l’univers un paquet d’information qui nous permettrait de vendre plus de services pour moins cher, mais on manque de mains humaines. C’est là que les robots débarquent!

Si tu remplaces une tonne de tâches automatisables (pas nécessairement des tâches de base en passant), ton TAM est immense. Ça veut dire quoi pour les jobs de ce monde-là? À voir, *I guess*. Certaines vont être [OP](https://www.notion.so/Vertical-AI-1dc5c10632bb8033bfc5f8c94c661add?pvs=21&utm_source=saaspasse.beehiiv.com&utm_medium=newsletter&utm_campaign=vertical-ai), d’autres, [DOA](https://dictionary.cambridge.org/dictionary/english/doa?utm_source=saaspasse.beehiiv.com&utm_medium=newsletter&utm_campaign=vertical-ai).

Honnêtement, fais l’exercice de méta-cognition : mesure à quel point tu copies-*[transforme]*-colles de la donnée d’une place à l’autre dans une journée. Tu vas voir l’opportunité.

Ah, t’es un mage technophile qui a tout automatisé dans Gumloop?

Regarde 8h par-dessus l’épaule de n’importe qui dans les entreprises où t’es client. Après avoir essuyé tout le sang coulant de tes yeux, tu vas arriver à la même conclusion.

Ce que je trouve débile, c’est que la diminution des coûts d’IA ouvre la possibilité de sur-nicher un système pour une verticale ultra-précise genre :

- SANTÉ

  - SPORTIVE  OSTÉO  QUÉBEC

- FINANCE

  - FISCALITÉ  SUCCESSIONS  CANADA

Ah, pertinent dans le cadre de cet édito : [l’acquisition de CoeurWay par MEDFAR](https://infobref.com/vente-coeurway-2025-03/?utm_source=saaspasse.beehiiv.com&utm_medium=newsletter&utm_campaign=vertical-ai).

### Tasser les géants

Pour que ça marche comme *playbook*, faut quand même que tu tasses les gros *systems of record* (*incumbents*).

Pis sont pas facile à tasser.

Ils storent et structurent de la donnée critique. Les équipes font leur travail au complet là-dedans. Elles associent “*getting things done*” à “travailler dans Salesforce”. Ils ont des intégrations avec une tonne d’autres systèmes.

Un *system of record*, c’est souvent considéré comme un “*control point*” selon NEA (voir [l’article de Tidemark](https://www.tidemarkcap.com/vskp-chapter/control-points-patterns-2024?utm_source=saaspasse.beehiiv.com&utm_medium=newsletter&utm_campaign=vertical-ai)). En gros, l’outil #1 dont le client/la compagnie peut pas se passer pour réussir à opérer.

Leur thèse, c’est que le *control point* se ramasse dans la couche agentique de l’IA, qui voit, process, transmets un paquet de data clé avant même qu’elle atteigne le vieux *control point* de *system of record*.

Important à noter : NEA ne suggèrent pas nécessairement de te battre contre un *incumbent* directement. Au contraire, plusieurs des exemples qu’ils donnent s’intègrent “par-dessus” les Goliath en les augmentant :

- Avoca/Revin/Drillbit >> ServiceTitan

- Sixfold >> Guidewire

- Trunk Tools >> Procore, Sharepoint, Autodesk

- MagicSchool/SchoolAI >> SIS/LMS

- Backflip >> Solidworks

- Axon >> CAD/RMS

Mais APRÈS…

Tu collectes et stores tellement de data via ton nouveau *system of action* que tu peux “flip the script” et détrôner le *system of record*.

*Sneaky*.
*Naughty*.
*Oh well, **BUSINESS**, AM I RIGHT!?*

Reste à voir comment les *incumbents* vont réagir à tout ça, aussi.

Ces modèles et cette tech-là sont dispo pour tous. Certains pourront pas spécialiser ou verticaliser parce qu’ils ont le bras trop loin dans le tordeur horizontal. Mais peut-être qu’avec leur effet de réseau et leur *marketplace* d’apps / fournisseurs, ils vont pouvoir verticaliser des applications par-dessus leur *system of record* générique, *dunno*. En tout cas ils ont déjà l’infra et la *compliance* pour le marché enterprise!

### Mais pourquoi verticaliser si *AGI SOON*? 👽

ChatGPT ou d’autres vont devenir tellement puissants que je vais pouvoir les déployer dans n’importe quelle verticale!

Peut-être. J’ai pas de PhD ni de boule de crystal. ¯\(ツ)/¯

Mais *right now*, y’a une raison pourquoi un LLM générique devient vraiment meilleur quand tu le *prompt* [avec du role-play](https://openreview.net/pdf/b87c2afe1c2c59b81cba7f443481a4edc22052e2.pdf?utm_source=saaspasse.beehiiv.com&utm_medium=newsletter&utm_campaign=vertical-ai).

Exemple si tu lui dis de s’imaginer expert en dentisterie, avec scénario et donnée spécifique. Il cherche moins à droite à gauche, il plonge plus creux (vertical) dans son océan sémantique pour te pêcher quelque chose de plus utile. Extrapole à des centaines d’agents qui font juste ça. Ils risquent d’être 10x meilleurs que ChatGPT pour aider ces dentistes imaginaires.

Mais pour réussir à faire une meilleure job que les modèles et produits généralistes qui augmentent en capacités chaque trimestre… la quantité et qualité d’expertise à amasser va être phénoménale. Fait longtemps qu’OpenAI a arrêté d’être une compagnie juste de modèle. ChatGPT c’est un produit, pis tout qu’un produit à part de ça.

On voit déjà du monde [vibe-coder](https://x.com/karpathy/status/1886192184808149383?utm_source=saaspasse.beehiiv.com&utm_medium=newsletter&utm_campaign=vertical-ai) des outils internes au lieu de payer pour des SaaS génériques trop cher. On pourrait commencer à voir l’équivalent des *no-coders* qui te bâtissent une solution personnalisée mais pour l’IA. Des dompteurs d’IA qui t’entraînent un GPT pour un cas d’utilisation vertical en quelques semaines, sans que tu payes le gros prix. Meh, ça existe sûrement déjà dans le fond!

**BON.** C’est bien cool le VERTICAL AI mais là c’est l’heure d’aller mettre [FRANK à l’HORIZONTAL](https://share.cleanshot.com/BsLmMRgq?utm_source=saaspasse.beehiiv.com&utm_medium=newsletter&utm_campaign=vertical-ai). 😴

—

Quelque chose à ajouter? *Good*. Laisse un commentaire ou réponds à ce courriel direct.

Cheers,

[Frank](https://www.linkedin.com/in/frankln/?utm_source=saaspasse.beehiiv.com&utm_medium=newsletter&utm_campaign=vertical-ai) 💜