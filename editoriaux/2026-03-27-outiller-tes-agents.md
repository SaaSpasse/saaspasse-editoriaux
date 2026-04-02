Imagine t'engages une directrice marketing demain matin. Premier jour, tu lui donnes un laptop flambant neuf... _that's it_. Pas de compte Google. Pas de Slack. Pas d'accès au CRM. Pas de contexte sur la brand, les clients, rien. 

Tiens, débrouille-toi.

Personne fait ça. Ça serait absurde. 

Mais la majorité du monde font drette ça avec leurs agents AI. 

Tu ouvres Claude, ChatGPT, ou n'importe quel modèle. Tape un prompt. Doigts croisés pour de la magie. Pis quand le résultat est moyen, tu blâmes le modèle. 

❝ 

L'AI est pas encore assez bon. Il comprend pas ce que je veux. [Trop vanille](https://saaspasse.beehiiv.com/p/tout-go-te-la-vanille); du vrai slop!

J'ai passé les derniers mois à bâtir plusieurs agents AI chez SaaSpasse. Aujourd'hui, je t'en présente trois. Un pour le contenu, un pour les opérations, un pour le design. Ce que j'ai appris: le modèle, c'est 20% du résultat. L'outillage, c'est le 80% qui fait la différence. 

Quand je dis outillage, je parle de trois choses: 

  * **Des compétences** —ce que l'agent sait faire. Des skills spécialisés, des workflows, des pipelines. 

  * **Des accès** —ce à quoi l'agent peut se connecter. Des plateformes, des données, des APIs. 

  * **Des SOPs** —comment l'agent doit travailler. Des instructions, du contexte, des méthodes documentées. 

Sans plus tarder, procédons 🕺 

### 1\. L'agent Contenu

Lui, il co-écrit l'infolettre que tu lis en ce moment. On brainstorm ensemble, on rédige section par section, il génère les images, pis il me donne un _preview_ live du résultat formaté comme un vrai email. 

**Ses compétences.** L'agent a deux _skills_ —des commandes spécialisées que tu codes ou installes toi-même pour lui donner des pouvoirs précis. 

`/paladin` génère des illustrations on-brand pour l'infolettre. Il a un _system prompt_ avec nos références visuelles, nos couleurs, nos contraintes de taille. Le résultat: des images SaaSpasse reconnaissables. Pas du _stock art_ générique que n'importe quel autre agent produirait. 

`/edito` récupère, classifie et archive chaque éditorial publié sur beehiiv dans notre _repo_ GitHub. 68+ éditos indexés. Ça me donne un corpus complet comme référence de ton et de style, pis ça rend le _linking_ vers des éditions passées _easy-peasy_. 

**Ses accès.** L'agent se connecte à l'API beehiiv pour aller chercher les posts publiés. À l'API Gemini de Google pour la génération d'images via `/paladin`. Pis au _repo_ GitHub via le CLI `gh`—notre mémoire long-terme de tout ce qu'on a écrit. 

(Un _CLI_ , c'est un outil en ligne de commande. Genre au lieu de cliquer dans une interface, l'agent tape une commande dans le terminal. `gh` c'est le CLI officiel de GitHub.) 

**Ses SOPs.** Le fichier `CLAUDE.md` du projet contient toutes les conventions de rédaction: tutoiement, _sentence case_ , italiques pour les termes anglais seulement, em-dash collé, pas de fluff. L'agent le lit au début de chaque session. _Basically_ manuel d'employé. 

Y'a aussi un processus itératif documenté: braindump → structure → intro → section par section, avec mon _feedback_ entre CHAQUE étape. L'agent sait qu'il doit jamais essayer de tout écrire d'un coup. 

Pis le _unlock_ le plus concret: `preview.py`. Un script Python qui génère un _preview_ HTML live dans un _mockup_ de client email, éditable en temps réel. 

Avant, le _flow_ c'était: prompter → lire → annoter ou reprompter → relire → répéter. Maintenant je peux me mettre les mains directement dans le _copy_ pour aller _fine-tuner_ les passages trop froids ou génériques. Ajouter de l'humour, de la chaleur... un peu d'âme du POPE u kno. Pis quand c'est des changements plus de fond ou qui impliquent des recherches, je peux juste parler dans le terminal via [Monologue](https://www.monologue.to/?utm_source=saaspasse.beehiiv.com&utm_medium=referral&utm_campaign=outiller-tes-agents). 

### 2\. L'agent Ops

Mon EA virtuel. Il trie mes emails, gère mon calendrier, fait le suivi de facturation, pis m'envoie des rapports automatiques sur Telegram. Si l'agent Contenu est mon co-auteur, celui-ci est mon _chief of staff, kinda_. 

**Ses compétences.** `/triage` fait le tour de mes listes de cossins—emails, Slack, Gcal, TODOs—et me sort les urgences du bruit. Genre de commande que je lance quand je suis en mode gestion. 

**Ses accès.** Y'est plus connecté qu'un _dope dealer_ : branché sur sept plateformes via des MCPs. 

(Un MCP, c'est un connecteur standardisé qui permet à un agent AI de parler à une app externe. Genre de  _plugin_ universel. Au lieu de coder une intégration _custom_ pour chaque service, tu _plug_ un MCP et l'agent voit automatiquement les actions disponibles—lire des emails, créer une facture, poster dans Slack.) 

La liste: 

  * **Notion** — base de données projets, calendrier podcast, contacts 

  * **Xero** — comptabilité, factures, contacts fournisseurs 

  * **Missive** — collaboration emails, recherche, brouillons (un MCP custom qu'on a bâti. On comme dans Claude Code pis moi.) 

  * **Slack x2** — un pour le _workspace_ interne de l'équipe, un pour la communauté de membres 

  * **Google Calendar** — événements, TODOs, disponibilités 

  * **Stripe** — abonnements de la communauté privée + SaaSpals 

  * **Telegram** — canal portable (mobile) via lequel l'agent peut  _report_

Deux _scheduled tasks_ roulent automatiquement. Le dimanche à 14h, l'agent se réveille, scanne mon calendrier, mes emails non lus, mes Slacks, mes TODOs, et m'envoie un résumé sur Telegram. Le lundi à 9h, il fait un _deep dive_ dans Xero—factures ouvertes, paiements en retard, factures à créer. 

Résultat: je pogne ma semaine par surprise avant même qu'elle commence pis j'y montre c'est qui le boss, LOL. 

**Ses SOPs.** Le `CLAUDE.md` de ce projet est une bête. Tous les numéros de comptes Xero, les codes de taxes, les _patterns_ de facturation par client, les conventions de drafts Missive. Des dizaines de _gotchas_ documentés au fil du temps—les trucs qui plantent si tu fais pas attention. 

C'est ça le _compounding_. Chaque erreur corrigée, chaque _edge case_ découvert, ça finit dans le `CLAUDE.md`. L'agent devient meilleur à chaque session sans que j'aie besoin de le recontextualiser. 

### 3\. L'agent Designer

Celui-là est né d'une frustration. Demande à n'importe quel modèle AI de te faire une landing page. Tu vas avoir: gradient violet, police Inter, _card grid_ identique, _hero section_ avec des gros chiffres. Dix agents différents, même résultat. Zéro personnalité, zéro mémorabilité. Du [slop visuel](https://saaspasse.beehiiv.com/p/tout-go-te-la-vanille). 

Ça fait que j'ai investi sérieusement dans son outillage. Plus que les deux autres combinés. 

**Ses compétences.** Un _pipeline_ de review en 8 étapes, gracieuseté d'Impeccable—un _toolkit_ open source d'Anthropic pour le design. `/critique` fait une analyse UX en 10 dimensions avec détection de slop AI. `/audit` vérifie l'accessibilité, la performance, le _responsive_. `/polish` pour les détails d'alignement. `/harden` pour le contraste WCAG et le _reduced-motion_. Chaque commande est un filet de sécurité. Sur le projet [MIAM](https://miam-three.vercel.app/?utm_source=saaspasse.beehiiv.com&utm_medium=referral&utm_campaign=outiller-tes-agents) **[une idée brouillon de soirées formations AI + cocktails, réponds à ce courriel si ça t'allume]** le _pipeline_ a attrapé 18 issues. Des vrais problèmes de contraste et de _responsive_ qu'un humain aurait ratés. 

Il a aussi des _skills_ pour générer des interfaces web, des visuels statiques, et de l'art génératif. Mais les _skills_ de review d'Impeccable, c'est eux qui font la vraie différence. 

**Ses accès.** Une douzaine de MCPs spécialisés: Gemini pour la génération d'images, Coolors pour les palettes, un convertisseur de couleurs avec calcul de contraste WCAG, Remotion pour les vidéos programmatiques, un conseiller typographique, 60 000+ icônes SVG. Pis le Chrome MCP pour vérifier visuellement le rendu sur desktop et mobile—comme un QA qui ouvre le site dans un vrai _browser_. 

**Ses SOPs.** Le document fondateur, c'est un [manifeste de ](https://taste-preview.vercel.app/?utm_source=saaspasse.beehiiv.com&utm_medium=referral&utm_campaign=outiller-tes-agents)_[TASTE](https://taste-preview.vercel.app/?utm_source=saaspasse.beehiiv.com&utm_medium=referral&utm_campaign=outiller-tes-agents)_ en trois couches. La première: des lois non-négociables. Jamais de polices génériques. Hiérarchie de taille dramatique. Pas de noir pur ni de blanc pur. Des anti-patterns nommés explicitement—"si ça ressemble à un template Tailwind UI, recommence." 

La deuxième couche: mes tendances naturelles. Serif _display_ \+ mono pour les données. Micro-détails au deuxième regard. Texture _retro computing_ comme accent. 

La troisième: la direction artistique, décidée AVANT chaque projet. Palette, typo, _mood_ , densité, niveau de motion, _layout_. Six axes à définir avec moi avant d'écrire une seule ligne de code. 

Le test ultime: 

❝ 

_Est-ce que 10 autres agents auraient produit la même chose? Si oui, on recommence._

### Le pattern

Aucun de ces trois agents n'a été stratégiquement planifié. J'ai pas fait un Miro board avec des _user stories_ pis des diagrammes d'architecture. Zéro _grand plan_. Juste des jams avec Claude Code à droite à gauche quand j'avais du temps ou quand j'étais écoeuré de quelque chose. 

L'agent Contenu est né parce que j'étais tanné de copier-coller du markdown entre Claude et beehiiv. Ops est né parce que j'oubliais des factures. Designer est né parce que tout ce que l'AI me générait avait l'air pareil. Pis parce que je peux enfin dire à un designer quoi faire sans avoir à argumenter deux heures avec sur l'art ou les bonnes pratiques ou les tendances. BURN

Chaque frustration → un outil. Chaque erreur → un _gotcha_ documenté. Chaque session → un `CLAUDE.md` un peu plus épais, qu'on épure à la longue. 

Y’a sûrement plein de manières de mieux faire ce que je fais _right now_. Si t’en as, shoot!

C'est du _learning-by-doing_ appliqué à l'outillage AI. Tu commences avec un prompt nu. Tu frappes un mur. Tu fixes. Tu documentes. Tu recommences. Au bout de 50 sessions, t'as un agent qui connaît tes numéros de taxes, tes préférences typographiques, pis ta façon d'écrire une intro. 

Pis l'agent lui-même peut t'aider à s'équiper. Tu lui dis: 

Cherche sur GitHub, X, le web, dans des répertoires de _skills_ et de _plugins_. Trouve-moi des outils qui font XYZ. Évalue leur crédibilité, leur sécurité, pis leur pertinence pour notre _use case_.

Il revient avec des options, tu choisis, tu installes, tu testes. Ton agent devient son propre département de R&D. 

Le _unlock_ , c'est que ça _compound_. Chaque ajout est petit—une ligne dans le `CLAUDE.md`, un nouveau _skill_ , un MCP de plus. Mais l'effet cumulatif est massif. L'agent d'aujourd'hui est méconnaissable comparé à celui d'il y a trois mois. Ma productivité et mon excitation à travailler, même chose. 

### Le visual mapping

Pour donner une idée de ce que ça donne visuellement, j'ai demandé à l'agent Designer de me mapper l'outillage des trois agents. Le résultat: 

[![](https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/9190469f-ae2d-4d4d-bebc-63f5fae7b559/CleanShot_2026-03-20_at_21.59.36_2x.png?t=1774058442)](https://circuit-board-alpha.vercel.app/?utm_source=saaspasse.beehiiv.com&utm_medium=referral&utm_campaign=outiller-tes-agents)

[Voir le site ↗](https://circuit-board-alpha.vercel.app/?utm_source=saaspasse.beehiiv.com&utm_medium=referral&utm_campaign=outiller-tes-agents)

C'est un diagramme cute pis un portrait fidèle de comment les pièces s'emboîtent. Chaque _skill_ , chaque MCP, chaque SOP—placé dans son contexte. 

Si t'es curieux de bâtir le tien, c'est un bon point de départ pour voir ce qu'il te manque! 

Pas eu le temps de _fine-tune_ à mon goût mais ça fait la job si tu zoom dans le site. M’en vais au Mexique une semaine, adios!

— 

Quelque chose à ajouter? _Good_. Laisse un commentaire ou réponds à ce courriel direct. 

Cheers, 

[Frank](https://www.linkedin.com/in/frankln/?utm_source=saaspasse.beehiiv.com&utm_medium=referral&utm_campaign=outiller-tes-agents) 💜 

### Il reste même pas 10 billets….

[![](https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/2667f967-3926-4b10-bca4-5f313cc98bcc/SaaSpasse_Event.png?t=1774544635)](https://www.eventbrite.ca/e/billets-saaspasse-a-quebec-edition-19-1984566480767?aff=oddtdtcreator&utm_source=saaspasse.beehiiv.com&utm_medium=referral&utm_campaign=outiller-tes-agents)

_Last call_ pas mal, la gang. Il reste seulement quelques billets pour notre événement du 9 avril prochain. Si t’as repoussé ça dans ta _todo,_ il est temps de passer à l’action.  
  
Podcast _live,_ bouffe, boisson et _networking._ Ça promet! 

[ réserve ta place ici ](https://www.eventbrite.ca/e/billets-saaspasse-a-quebec-edition-19-1984566480767?aff=oddtdtcreator&utm_source=saaspasse.beehiiv.com&utm_medium=referral&utm_campaign=outiller-tes-agents)

### Un banquier qui comprend la tech?!

Ça existe → [Desjardins — Caisse des Technologies.](https://saaspasse.com/partenaires/desjardins-caisse-des-technologies-5c3d3/?utm_source=saaspasse.beehiiv.com&utm_medium=referral&utm_campaign=outiller-tes-agents)  
  
Si t’es pas convaincu.e, tu peux aller voir notre capsule avec leur gang. On y couvre plusieurs sujets comme :   
  
• Pourquoi une caisse spécialisée en tech existe  
• Comment naviguer les transitions entre salarié → consultant → fondateur  
• L'accompagnement financier quand ton revenu fait du yo-yo dans ta business bootstrapped  
• Pourquoi ta santé mentale de fondateur est ton meilleur avantage compétitif  
  
J’ai eu un _blast_ à enregistrer ça avec eux. Vraiment une belle discussion.  
  
Si tu veux en savoir plus sur la Caisse en général, c’est ici : 

[ tous les détails ](https://saaspasse.com/partenaires/desjardins-caisse-des-technologies-5c3d3/?utm_source=saaspasse.beehiiv.com&utm_medium=referral&utm_campaign=outiller-tes-agents)

### On t’aide à trouver ton prochain défi

[![](https://qhmbbgerejsxibphinnu.supabase.co/storage/v1/object/public/images/0f1ab83b-6f2e-44ad-b7d8-6215bff1e6fb/social_image.png)Y’a de la job en masse!](https://saaspasse.com/startups/poka/?utm_source=saaspasse.beehiiv.com&utm_medium=referral&utm_campaign=outiller-tes-agents)

On l’entend pas mal ces temps-ci; le marché de l’emploi en tech est un peu _rough_. C’est pourquoi on est _stoked_ de t’annoncer que y’a des postes en or chez Poka en ce moment : 

  * **[Gestionnaire Développement Logiciel (Équipe Produit)](https://saaspasse.com/emploi/poka-gestionnaire-developpement-logiciel-equipe-produit/?utm_source=saaspasse.beehiiv.com&utm_medium=newsletter&utm_campaign=petites-douceurs)**

  * **[Développeuse / Développeur Backend](https://saaspasse.com/emploi/poka-developpeuse-developpeur-backend/?utm_source=saaspasse.beehiiv.com&utm_medium=newsletter&utm_campaign=petites-douceurs)**

  * **[Gestionnaire Développement Logiciel (Équipe Core)](https://saaspasse.com/emploi/poka-gestionnaire-developpement-logiciel-equipe-core/?utm_source=saaspasse.beehiiv.com&utm_medium=newsletter&utm_campaign=petites-douceurs)**

Si t'as envie d’évoluer dans une compagnie qui opère à l'échelle mondiale, c'est le temps de cogner à la porte. 

[ Tous les détails sur Poka ](https://saaspasse.com/startups/poka/?utm_source=saaspasse.beehiiv.com&utm_medium=referral&utm_campaign=outiller-tes-agents)