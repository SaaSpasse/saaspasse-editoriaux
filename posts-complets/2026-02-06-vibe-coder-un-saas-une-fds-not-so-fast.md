---
date: '2026-02-06'
title: Vibe-coder un SaaS une FDS? Not so fast!
url: https://saaspasse.beehiiv.com/p/vibe-coder-un-saas-une-fds-not-so-fast
slug: vibe-coder-un-saas-une-fds-not-so-fast
source: beehiiv
word_count: 1993
reading_time_min: 9
editorial_confidence: high
liens_internes: 27
liens_externes: 0
top_domains:
utm_detectes:
- url: https://www.twitter.com/frankhellend?utm_source=saaspasse.beehiiv.com&utm_medium=referral&utm_campaign=vibe-coder-un-saas-une-fds-not-so-fast
- url: https://daybits.app?utm_source=saaspasse.beehiiv.com&utm_medium=referral&utm_campaign=vibe-coder-un-saas-une-fds-not-so-fast
- url: https://localhost?utm_source=saaspasse.beehiiv.com&utm_medium=referral&utm_campaign=vibe-coder-un-saas-une-fds-not-so-fast
- url: https://CLAUDE.md?utm_source=saaspasse.beehiiv.com&utm_medium=referral&utm_campaign=vibe-coder-un-saas-une-fds-not-so-fast
- url: https://daybits.app?utm_source=saaspasse.beehiiv.com&utm_medium=referral&utm_campaign=vibe-coder-un-saas-une-fds-not-so-fast
- url: https://www.linkedin.com/in/frankln/?utm_source=saaspasse.beehiiv.com&utm_medium=referral&utm_campaign=vibe-coder-un-saas-une-fds-not-so-fast
- url: https://www.linkedin.com/in/cyndie-feltz/?utm_source=saaspasse.beehiiv.com&utm_medium=referral&utm_campaign=vibe-coder-un-saas-une-fds-not-so-fast
- url: https://www.linkedin.com/in/nicholas-m-99739390/?utm_source=saaspasse.beehiiv.com&utm_medium=referral&utm_campaign=vibe-coder-un-saas-une-fds-not-so-fast
- url: https://www.saaspasse.com/partenaires/yack?utm_source=saaspasse.beehiiv.com&utm_medium=referral&utm_campaign=vibe-coder-un-saas-une-fds-not-so-fast
- url: https://youtu.be/e39IRUjMFUg?utm_source=saaspasse.beehiiv.com&utm_medium=referral&utm_campaign=vibe-coder-un-saas-une-fds-not-so-fast
personnes:
- nom: Cyndie Feltz
  linkedin: https://www.linkedin.com/in/cyndie-feltz/?utm_source=saaspasse.beehiiv.com
- nom: Nicholas Milot
  linkedin: https://www.linkedin.com/in/nicholas-m-99739390/?utm_source=saaspasse.beehiiv.com
- nom: Guillaume Falardeau
  linkedin: https://www.linkedin.com/in/guillaume-falardeau-b213768b/?utm_source=saaspasse.beehiiv.com
---


# Éditorial (copywriting)

<!-- editorial:start -->
Tu peux _vibe-coder_ une app en un _week-end_.

On l'entend partout. X, LinkedIn, _podcasts_. Des gens qui prétendent avoir buildé un SaaS complet en 48 heures avec Claude ou Cursor. _Screenshots_ de _dashboards_ fancy, revenus Stripe en montant, etc. 

Ça m'intriguait autant que ça m'énervait. 

Fait que j'ai décidé de tester pour vrai! 

Pas un _proof of concept_ genre prototype qui marche juste sur mon laptop. Une vraie app—web ET mobile—avec du vrai _auth_ , une vraie base de données, déployée sur l'App Store. 

L'app s'appelle [daybits](https://daybits.app?utm_source=saaspasse.beehiiv.com&utm_medium=referral&utm_campaign=vibe-coder-un-saas-une-fds-not-so-fast). Un _habit tracker_ super simple que j'ai construit d’abord pour moi-même avec Claude Code. 

~33 jours. 36 sessions. 102 _commits_. 170 tests. Une app sur TestFlight.

À temps partiel pas mal, mettons. 

Autant de "_holy shit_ " que de "_ah shit_ ". 

C'est ni le _week-end_ promis, ni les 6 mois que ça m'aurait pris avec une équipe. C'est entre les deux—et c'est là que ça devient intéressant. 

![](https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/014d37f3-f852-4554-988f-ca29fc3f4baa/daybits-screenshot-1.png?t=1769998250)

App Store asset

_Of course_ , tu pourras essayer l'app mobile ou web pis me dire ce que t'en penses! 

### Avant le code

Avant d'ouvrir Claude Code, j'ai sorti ma tablette Remarkable. Pas d'écran, pas de notifications, juste du papier digital. 

J'ai commencé par décrire le problème que j'essayais de régler. 

![](https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/8822b129-f744-4027-8992-9a8ddb3aaa49/remarkable1.png?t=1769998383)

j’écris à la main comme un enfant de sept ans

Depuis des années, je track _on and off_ mes habitudes de vie sur un calendrier papier. Des X de couleurs différentes—bleu pour gym, mauve pour marche, orange pour fast-food évité, etc. 

![](https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/102f6bb8-1ccb-402b-8b2e-dbc2cb8f300c/remarkable2.png?t=1769998403)

épouvantable

Ça marchait. Mais c'était pas portable. Des fois j'oubliais le calendrier dans mon sac quelques jours. Ou je me rappelais plus si j'avais mangé du fast-food mardi ou mercredi. J'ai essayé Notion, mais j'avais le goût de séparer mes trucs perso de pro. Pis mon setup boboche sur mobile était _janky_. 

Fait que j'ai listé quelques critères pour une bonne app, comme: 

  * **Portabilité** – accessible sur mon cell, ordi, _offline_ , partout, tout le temps. Technos populaires, bien documentées, avec une grosse communauté 

  * **Sécurité** – protection des données, bases de sécurité 

  * **Maintenabilité** – si un dev ou un AI rentre dans le code, il comprend ce qui se passe 

![](https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/5c63ddf6-d4fc-4a34-ae24-08ff07cb99a0/remarkable3.png?t=1769998481)

eh boy

Tout ça avant d'écrire une seule ligne de code. Ou plutôt, avant de demander à Claude d'en écrire une. 

C'est peut-être la partie la plus importante du processus. Le _vibe coding_ , c'est pas juste "prompter et prier". C'est savoir ce que tu veux avant de le demander. 

### Ce qui est magique

**Itérations dev+design**

La vitesse d'itération en local, c'est complètement débile. 

Avant d'ajouter une _feature_ ou une vue, je demandais à Claude de me montrer des _mockups_ en _[localhost](https://localhost?utm_source=saaspasse.beehiiv.com&utm_medium=referral&utm_campaign=vibe-coder-un-saas-une-fds-not-so-fast)_. Différents types d'icônes, différentes animations, différents _color schemes_. Quand je trouvais quelque chose qui marchait, je disais "ok, ajoute ça au _codebase_ ". C'est comme avoir un designer-dev à côté de toi qui fait des prototypes en temps réel. 

Il y a eu des moments où je me suis presque senti comme un vrai dev. Ou peut-être plus comme un vrai _product owner_ avec des vrais devs pluggés sur la matrice Neuromancer-style.

Implémenter le SSO avec Apple Sign In et Google Sign In? Quelques minutes. Créer un _repo_ GitHub, une _database_ Supabase, un projet Vercel? Claude faisait ça via le CLI directement dans le terminal. Moi je regardais ça se passer en me disant "oh my god, le monde est à moi". 

**Marketing**

La partie marketing m'a aussi impressionné. Je me rappelle le labeur qu'on mettait chez Snipcart pour créer un site web, des visuels promo, des _screenshots_ et _mockups_. Des semaines de travail. Là, j'ai généré tout ça en deux sessions. _Landing page_ , _copy_ , _assets_ —le kit complet. 

J'ai créé une _skill_ Claude Code—un fichier de directives—pour définir la voix de **daybits**. Ton, mots interdits, patterns de _copy_ pour chaque contexte. Genre: jamais dire "streak" ou "unlock your potential". Toujours écrire le nom en minuscules. Boutons en CAPS, titres en _lowercase_. 

Après ça, j'ai fait un exercice de positionnement avec la méthode April Dunford. Alternatives compétitives, attributs uniques, client idéal, _tagline_. Claude m'a guidé à travers les 6 étapes comme un vrai consultant stratégique. 

**Résultat**

  *  _Landing page_ complète 

  * Description App Store 

  * _Tagline_ : "Habit commits for busy builders." 

  * Battlecards des compétiteurs 

  * Emails transactionnels 

Tout ça en deux sessions. Le genre de travail qui prenait des semaines chez Duda avec une équipe marketing. 

![](https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/18d6a9eb-bd2b-408f-a40d-bbd7e2d41619/daybits-landing.png?t=1769998786)

Landing page — daybits.app

**Multi-tasking**

Un autre _unlock_ : les sessions parallèles. 

Je pouvais travailler sur l'app mobile dans une fenêtre, sur le marketing _copy_ dans une autre, sur la stratégie long terme dans une troisième. Chaque session avait son contexte, son _focus_. Pis à la fin de chaque session, on loguait tout dans le [CLAUDE.md](https://CLAUDE.md?utm_source=saaspasse.beehiiv.com&utm_medium=referral&utm_campaign=vibe-coder-un-saas-une-fds-not-so-fast)—ce qu'on avait fait, les erreurs rencontrées, la _roadmap_. 

Donc je pouvais reprendre n'importe quel chantier sans friction. Pas besoin de me re-contextualiser pendant 30 minutes. Claude savait exactement où on en était. 

![](https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/7bb54a7e-663d-4bc9-a877-9dd3ef561b4e/daybits-screenshot-4.png?t=1769998839)

App Store asset

### Les murs

**Mobile**

Beaucoup de ce qui touche à l'app mobile était… _painful_. 

_Setup_ Expo, React Native, simulateur sur Mac, _builds_ locaux, tester sur mon cell... J'ai sacré quelques fois avec ça. 

**Patentage**

Ça pis le _wiring_. 

Il y a un paquet de services que tu utilises pour un paquet de choses. Supabase pour la base de données. Vercel pour le déploiement web. Google Cloud Console pour l'_auth_. Apple pour l'App Store. Chaque service demande un compte, une configuration, des clés API qui doivent passer au bon endroit de façon sécure dans ton _codebase_. 

Tu peux pas tout faire par CLI. Tu dois rentrer dans des interfaces que tu connais pas. Cliquer sur des boutons stressants. Lire de la documentation. C'est là que le _vibe coding_ montre ses limites. 

**Apple**

L'enfer Apple, parlons-en. 

Créer un Apple Developer Account, ça prend des jours. Il faut un numéro DUNS lié à ta _business_. Des temps d'attente avant approbation. Pis après, App Store Connect: _uploader_ ton _build_ , décrire tout ce que ton app fait, faire tous les _screenshots_ , répondre à des questionnaires sur le contenu, la _privacy_ , les permissions... c'est pas un mur, c'est un mini labyrinthe bureaucratique. 

**Builds, CI/CD**

J'ai aussi passé des heures sur des _builds_ Vercel qui cassaient. Je copiais les messages d'erreur dans Claude Code, il proposait des _fixes_ , ça marchait pas, on recommençait. Une _loop_ frustrante. Éventuellement, en _brute force_ , on a trouvé les erreurs de config. 

_**Dangerously skipping permissions**_

Pis il y a eu l'incident _yolo_. 

Un soir, tard, j'ai demandé à Claude de supprimer mes utilisateurs test dans la base de données. J'utilisais l'extension Claude for Chrome pour cliquer à ma place dans des interfaces complexes quand j'étais trop fatigué. Cette fois-là, il a tout supprimé. Incluant mon vrai compte avec mes deux semaines de données. _WHOOPS_. Après ça, j'ai mis des règles: 

Même si je te donne carte blanche en mode _dangerously skip permissions_ partout, double-valide avec moi avant de toucher à la BD!

![](https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/b43c7dfd-8a91-4c59-8d02-6dc0e8254ce1/daybits_today_view.png?t=1769999039)

Today view — web

### La poutine vs l'emballage

Générer du code, des pixels, du texte—assembler ça dans une expérience cohésive, interactive—c'est rendu facile. Quand t'as une bonne idée et que tu sais ce que tu veux, l'AI peut te _cook_ la pout assez vite. 

Mais le contenant autour de ta poutine pour la servir à de vrais clients? Le déploiement, la sécurité, l'hébergement, le _versioning_? C'est ça qui est _tough_. 

C'est l'emballage. Pis l'emballage, c'est plate. 

Mais quand tu veux construire un produit que d'autres vont utiliser de façon sérieuse et sécuritaire, ces choses-là sont essentielles. Pas la partie _fun_ du processus _though_. 

![](https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/acc1114e-07ee-4b3d-a79f-902e929485ca/daybits_architecture.png?t=1769999711)

Il y a un monde de différence entre un _internal tool_ pour toi ou tes collègues versus un produit que tu vas commercialiser et distribuer à du monde partout sur la planète. Le premier, tu peux le _vibe-coder_ en une fin de semaine. Le deuxième? Ajoute facile quelques semaines pour l'emballage. 

### Vibe verdict

C'est pas de la magie le _vibe-coding_ , mais pas loin. Si t'es patient, un minimum instruit, pas mal curieux… tu peux faire des trucs _insane_. 

Si t'as une idée claire, des critères bien définis, et que tu sais ce que tu veux—l'AI va te permettre de _builder_ des choses que t'aurais jamais pu faire seul. Moi, je suis pas _designer_. Je suis pas dev. Mais j'ai bientôt une app sur l'App Store. ¯\\_(ツ)_/¯ 

Par contre, il reste plein de choses opaques pour moi. Je comprends à haut niveau comment les parties de mon app interagissent. Mais quelle ligne de code fait quoi exactement? Aucune idée. J'ai encadré, supervisé, testé. Mais c'est pas moi qui ai codé le produit. 

Sinon, **mon**** _take_****sur les apps mobiles** : à moins que t'aies vraiment besoin de _features_ natives (GPS, caméra, _health data_), une bonne web app _mobile-first_ fait probablement la job. Le processus App Store, c'est _heavy_. Mais si tu penses pouvoir optimiser ce canal de distribution, ça peut payer _big time_! 

Est-ce que je referais ça? _Hell yes_. Mais avec des attentes calibrées. 

Genre, au début du processus, je prenais des _learning breaks_ sur ChatGPT ou Claude web pour "apprendre" c'était quoi tout ce que je faisais: 

❝ 

_Oh tell me more about data modelling please!_

Mais après quelques sessions, j'étais comme: 

❝ 

_let it f***ing RIP CLAUDE!_

\--dangerously-skip-permissions FTW 

Je vais continuer de m'amuser avec daybits, c'est un beau terrain de jeu. J'ai _of course_ d'autres idées de quoi builder, mais faut que j'aille au gym, que je marche, que je médite, que je ferme mes écrans avant 23:00… 

**Au moins maintenant j'ai une app pour cocher tout ça** 🙃 

→ **[Essaie daybits](https://daybits.app?utm_source=saaspasse.beehiiv.com&utm_medium=referral&utm_campaign=vibe-coder-un-saas-une-fds-not-so-fast)** — web ou mobile, c'est gratuit, simple, pis ça track tes _habits_ sans te faire sentir coupable.

![](https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/da0354f7-a22d-41c0-86d3-16212c117faf/daybits_calendar_view.png?t=1769999067)

Calendar view — web

— 

Quelque chose à ajouter? _Good_. Laisse un commentaire ou réponds à ce courriel direct. 

Cheers, 

[Frank](https://www.linkedin.com/in/frankln/?utm_source=saaspasse.beehiiv.com&utm_medium=referral&utm_campaign=vibe-coder-un-saas-une-fds-not-so-fast) 💜 

### Cybersécurité pour SaaS 👾

❝ 

"Ta clé API OpenAI traîne probablement sur GitHub."

Ouch. Mais c'est le genre de vérité _cash_ que [Cyndie Feltz](https://www.linkedin.com/in/cyndie-feltz/?utm_source=saaspasse.beehiiv.com&utm_medium=referral&utm_campaign=vibe-coder-un-saas-une-fds-not-so-fast) et [Nicholas Milot](https://www.linkedin.com/in/nicholas-m-99739390/?utm_source=saaspasse.beehiiv.com&utm_medium=referral&utm_campaign=vibe-coder-un-saas-une-fds-not-so-fast) te disent quand ils font affaire avec toi. 

Dans cette capsule, on démystifie la cybersécurité pour SaaS avec les _cofounders_ de [Yack](https://www.saaspasse.com/partenaires/yack?utm_source=saaspasse.beehiiv.com&utm_medium=referral&utm_campaign=vibe-coder-un-saas-une-fds-not-so-fast): 

  * C'est quoi un pen test et quand en faire un 

  * Les 2 vulnérabilités classiques qui reviennent tout le temps 

  * Gestion des secrets 

  * Est-ce que l'AI expose de nouvelles failles? 

[ Instruis-toi ](https://youtu.be/e39IRUjMFUg?utm_source=saaspasse.beehiiv.com&utm_medium=referral&utm_campaign=vibe-coder-un-saas-une-fds-not-so-fast)

### Le temps des impôts s’en vient vite….

[![](https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/df6d8de7-97e6-41c8-9d05-6ba68306393f/SaaSpaladin-le-temps-des-impots-approche-le-saaspaladin-va-vi-v1__1_.png?t=1770310371)](https://www.linkedin.com/posts/la-saison-des-imp%C3%B4ts-approche-ugcPost-7424816079627153409-Q7F4?utm_source=saaspasse.beehiiv.com&utm_medium=referral&utm_campaign=vibe-coder-un-saas-une-fds-not-so-fast)

Tu peux soit improviser comme d'habitude ou tu peux confier ça à des pros qui le font déjà pour pleins d’entrepreneurs. 

[Le Chiffre](https://www.saaspasse.com/partenaires/le-chiffre?utm_source=saaspasse.beehiiv.com&utm_medium=referral&utm_campaign=vibe-coder-un-saas-une-fds-not-so-fast) peut t'aider à: 

  * Préparer tes documents sans stress 

  * Poser les bonnes questions fiscales 

  * Garder tes chiffres en ordre 

Stratégie > improvisation. Clarté > chaos. 

[ Check them out ](https://www.saaspasse.com/partenaires/le-chiffre?utm_source=saaspasse.beehiiv.com&utm_medium=referral&utm_campaign=vibe-coder-un-saas-une-fds-not-so-fast)

### On creuse term-sheets avec notre pro pref

[![](https://beehiiv-images-production.s3.amazonaws.com/uploads/asset/file/2e83ae63-bd38-45be-a04e-fdc03284e35f/leviatxsaaspasse.jpeg?t=1770311408)Dissection d'un term sheet — Étude de cas SaaSpassew/ Guillaume Falardeau, avocat et fondateur @ Leviat Legal](https://www.saaspasse.com/blog/dissection-dun-term-sheet-ft-leviat-legaletude-de-cas-saaspasse?utm_source=saaspasse.beehiiv.com&utm_medium=referral&utm_campaign=vibe-coder-un-saas-une-fds-not-so-fast)

**Les clauses qui vont te revenir dans face** 🪤 

T'es sur le point de signer ton _term sheet_. Excité. Stressé. Un peu perdu dans le jargon. 

"Attends, c'est quoi ça exactement?" 

On a pris un vrai _term sheet_ et on l'a décortiqué avec [Guillaume Falardeau](https://www.linkedin.com/in/guillaume-falardeau-b213768b/?utm_source=saaspasse.beehiiv.com&utm_medium=referral&utm_campaign=vibe-coder-un-saas-une-fds-not-so-fast) de [Leviat Legal](https://www.saaspasse.com/partenaires/leviat-legal?utm_source=saaspasse.beehiiv.com&utm_medium=referral&utm_campaign=vibe-coder-un-saas-une-fds-not-so-fast). Ligne par ligne. Clause par clause. 

Au menu: 

  * Les clauses au _look_ anodin qui peuvent te _bamboozle_ 3 ans plus tard 

  * Ce que les VCs négocient (et pourquoi) 

  * Les termes standards vs les _red flags_

[ Lis ça avant de signer ](https://www.saaspasse.com/blog/dissection-dun-term-sheet-ft-leviat-legaletude-de-cas-saaspasse?utm_source=saaspasse.beehiiv.com&utm_medium=referral&utm_campaign=vibe-coder-un-saas-une-fds-not-so-fast)
<!-- editorial:end -->

# Vibe-coder un SaaS une FDS? Not so fast!

## daybits : de zéro à App Store en 33 jours

![Author](https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/user/profile_picture/ed291c1d-2cc1-4f26-88a3-680bc46b9500/thumb_FLN_copy.jpeg)

[Francois Lanthier Nadeau](https://www.twitter.com/frankhellend?utm_source=saaspasse.beehiiv.com&utm_medium=referral&utm_campaign=vibe-coder-un-saas-une-fds-not-so-fast)  
6th février 2026 

[](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fsaaspasse.beehiiv.com%2Fp%2Fvibe-coder-un-saas-une-fds-not-so-fast)[](https://twitter.com/intent/tweet?text=daybits+%3A+de+ze%CC%81ro+a%CC%80+App+Store+en+33+jours&url=https%3A%2F%2Fsaaspasse.beehiiv.com%2Fp%2Fvibe-coder-un-saas-une-fds-not-so-fast&via=frankhellend)[](https://www.threads.net/intent/post?text=daybits+%3A+de+ze%CC%81ro+a%CC%80+App+Store+en+33+jours+https%3A%2F%2Fsaaspasse.beehiiv.com%2Fp%2Fvibe-coder-un-saas-une-fds-not-so-fast)[](https://www.linkedin.com/sharing/share-offsite?url=https%3A%2F%2Fsaaspasse.beehiiv.com%2Fp%2Fvibe-coder-un-saas-une-fds-not-so-fast)

![](https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/4e401eb3-24ab-429d-be72-d8f2f1f178ef/SaaSpaladin-custom-prompt-v2.png?t=1769998016)

❝ 

Tu peux _vibe-coder_ une app en un _week-end_.

On l'entend partout. X, LinkedIn, _podcasts_. Des gens qui prétendent avoir buildé un SaaS complet en 48 heures avec Claude ou Cursor. _Screenshots_ de _dashboards_ fancy, revenus Stripe en montant, etc. 

Ça m'intriguait autant que ça m'énervait. 

Fait que j'ai décidé de tester pour vrai! 

Pas un _proof of concept_ genre prototype qui marche juste sur mon laptop. Une vraie app—web ET mobile—avec du vrai _auth_ , une vraie base de données, déployée sur l'App Store. 

L'app s'appelle [daybits](https://daybits.app?utm_source=saaspasse.beehiiv.com&utm_medium=referral&utm_campaign=vibe-coder-un-saas-une-fds-not-so-fast). Un _habit tracker_ super simple que j'ai construit d’abord pour moi-même avec Claude Code. 

~33 jours. 36 sessions. 102 _commits_. 170 tests. Une app sur TestFlight.

À temps partiel pas mal, mettons. 

Autant de "_holy shit_ " que de "_ah shit_ ". 

C'est ni le _week-end_ promis, ni les 6 mois que ça m'aurait pris avec une équipe. C'est entre les deux—et c'est là que ça devient intéressant. 

![](https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/014d37f3-f852-4554-988f-ca29fc3f4baa/daybits-screenshot-1.png?t=1769998250)

App Store asset

_Of course_ , tu pourras essayer l'app mobile ou web pis me dire ce que t'en penses! 

### Avant le code

Avant d'ouvrir Claude Code, j'ai sorti ma tablette Remarkable. Pas d'écran, pas de notifications, juste du papier digital. 

J'ai commencé par décrire le problème que j'essayais de régler. 

![](https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/8822b129-f744-4027-8992-9a8ddb3aaa49/remarkable1.png?t=1769998383)

j’écris à la main comme un enfant de sept ans

Depuis des années, je track _on and off_ mes habitudes de vie sur un calendrier papier. Des X de couleurs différentes—bleu pour gym, mauve pour marche, orange pour fast-food évité, etc. 

![](https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/102f6bb8-1ccb-402b-8b2e-dbc2cb8f300c/remarkable2.png?t=1769998403)

épouvantable

Ça marchait. Mais c'était pas portable. Des fois j'oubliais le calendrier dans mon sac quelques jours. Ou je me rappelais plus si j'avais mangé du fast-food mardi ou mercredi. J'ai essayé Notion, mais j'avais le goût de séparer mes trucs perso de pro. Pis mon setup boboche sur mobile était _janky_. 

Fait que j'ai listé quelques critères pour une bonne app, comme: 

  * **Portabilité** – accessible sur mon cell, ordi, _offline_ , partout, tout le temps. Technos populaires, bien documentées, avec une grosse communauté 

  * **Sécurité** – protection des données, bases de sécurité 

  * **Maintenabilité** – si un dev ou un AI rentre dans le code, il comprend ce qui se passe 

![](https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/5c63ddf6-d4fc-4a34-ae24-08ff07cb99a0/remarkable3.png?t=1769998481)

eh boy

Tout ça avant d'écrire une seule ligne de code. Ou plutôt, avant de demander à Claude d'en écrire une. 

C'est peut-être la partie la plus importante du processus. Le _vibe coding_ , c'est pas juste "prompter et prier". C'est savoir ce que tu veux avant de le demander. 

### Ce qui est magique

**Itérations dev+design**

La vitesse d'itération en local, c'est complètement débile. 

Avant d'ajouter une _feature_ ou une vue, je demandais à Claude de me montrer des _mockups_ en _[localhost](https://localhost?utm_source=saaspasse.beehiiv.com&utm_medium=referral&utm_campaign=vibe-coder-un-saas-une-fds-not-so-fast)_. Différents types d'icônes, différentes animations, différents _color schemes_. Quand je trouvais quelque chose qui marchait, je disais "ok, ajoute ça au _codebase_ ". C'est comme avoir un designer-dev à côté de toi qui fait des prototypes en temps réel. 

Il y a eu des moments où je me suis presque senti comme un vrai dev. Ou peut-être plus comme un vrai _product owner_ avec des vrais devs pluggés sur la matrice Neuromancer-style.

Implémenter le SSO avec Apple Sign In et Google Sign In? Quelques minutes. Créer un _repo_ GitHub, une _database_ Supabase, un projet Vercel? Claude faisait ça via le CLI directement dans le terminal. Moi je regardais ça se passer en me disant "oh my god, le monde est à moi". 

**Marketing**

La partie marketing m'a aussi impressionné. Je me rappelle le labeur qu'on mettait chez Snipcart pour créer un site web, des visuels promo, des _screenshots_ et _mockups_. Des semaines de travail. Là, j'ai généré tout ça en deux sessions. _Landing page_ , _copy_ , _assets_ —le kit complet. 

J'ai créé une _skill_ Claude Code—un fichier de directives—pour définir la voix de **daybits**. Ton, mots interdits, patterns de _copy_ pour chaque contexte. Genre: jamais dire "streak" ou "unlock your potential". Toujours écrire le nom en minuscules. Boutons en CAPS, titres en _lowercase_. 

Après ça, j'ai fait un exercice de positionnement avec la méthode April Dunford. Alternatives compétitives, attributs uniques, client idéal, _tagline_. Claude m'a guidé à travers les 6 étapes comme un vrai consultant stratégique. 

**Résultat**

  *  _Landing page_ complète 

  * Description App Store 

  * _Tagline_ : "Habit commits for busy builders." 

  * Battlecards des compétiteurs 

  * Emails transactionnels 

Tout ça en deux sessions. Le genre de travail qui prenait des semaines chez Duda avec une équipe marketing. 

![](https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/18d6a9eb-bd2b-408f-a40d-bbd7e2d41619/daybits-landing.png?t=1769998786)

Landing page — daybits.app

**Multi-tasking**

Un autre _unlock_ : les sessions parallèles. 

Je pouvais travailler sur l'app mobile dans une fenêtre, sur le marketing _copy_ dans une autre, sur la stratégie long terme dans une troisième. Chaque session avait son contexte, son _focus_. Pis à la fin de chaque session, on loguait tout dans le [CLAUDE.md](https://CLAUDE.md?utm_source=saaspasse.beehiiv.com&utm_medium=referral&utm_campaign=vibe-coder-un-saas-une-fds-not-so-fast)—ce qu'on avait fait, les erreurs rencontrées, la _roadmap_. 

Donc je pouvais reprendre n'importe quel chantier sans friction. Pas besoin de me re-contextualiser pendant 30 minutes. Claude savait exactement où on en était. 

![](https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/7bb54a7e-663d-4bc9-a877-9dd3ef561b4e/daybits-screenshot-4.png?t=1769998839)

App Store asset

### Les murs

**Mobile**

Beaucoup de ce qui touche à l'app mobile était… _painful_. 

_Setup_ Expo, React Native, simulateur sur Mac, _builds_ locaux, tester sur mon cell... J'ai sacré quelques fois avec ça. 

**Patentage**

Ça pis le _wiring_. 

Il y a un paquet de services que tu utilises pour un paquet de choses. Supabase pour la base de données. Vercel pour le déploiement web. Google Cloud Console pour l'_auth_. Apple pour l'App Store. Chaque service demande un compte, une configuration, des clés API qui doivent passer au bon endroit de façon sécure dans ton _codebase_. 

Tu peux pas tout faire par CLI. Tu dois rentrer dans des interfaces que tu connais pas. Cliquer sur des boutons stressants. Lire de la documentation. C'est là que le _vibe coding_ montre ses limites. 

**Apple**

L'enfer Apple, parlons-en. 

Créer un Apple Developer Account, ça prend des jours. Il faut un numéro DUNS lié à ta _business_. Des temps d'attente avant approbation. Pis après, App Store Connect: _uploader_ ton _build_ , décrire tout ce que ton app fait, faire tous les _screenshots_ , répondre à des questionnaires sur le contenu, la _privacy_ , les permissions... c'est pas un mur, c'est un mini labyrinthe bureaucratique. 

**Builds, CI/CD**

J'ai aussi passé des heures sur des _builds_ Vercel qui cassaient. Je copiais les messages d'erreur dans Claude Code, il proposait des _fixes_ , ça marchait pas, on recommençait. Une _loop_ frustrante. Éventuellement, en _brute force_ , on a trouvé les erreurs de config. 

_**Dangerously skipping permissions**_

Pis il y a eu l'incident _yolo_. 

Un soir, tard, j'ai demandé à Claude de supprimer mes utilisateurs test dans la base de données. J'utilisais l'extension Claude for Chrome pour cliquer à ma place dans des interfaces complexes quand j'étais trop fatigué. Cette fois-là, il a tout supprimé. Incluant mon vrai compte avec mes deux semaines de données. _WHOOPS_. Après ça, j'ai mis des règles: 

Même si je te donne carte blanche en mode _dangerously skip permissions_ partout, double-valide avec moi avant de toucher à la BD!

![](https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/b43c7dfd-8a91-4c59-8d02-6dc0e8254ce1/daybits_today_view.png?t=1769999039)

Today view — web

### La poutine vs l'emballage

Générer du code, des pixels, du texte—assembler ça dans une expérience cohésive, interactive—c'est rendu facile. Quand t'as une bonne idée et que tu sais ce que tu veux, l'AI peut te _cook_ la pout assez vite. 

Mais le contenant autour de ta poutine pour la servir à de vrais clients? Le déploiement, la sécurité, l'hébergement, le _versioning_? C'est ça qui est _tough_. 

C'est l'emballage. Pis l'emballage, c'est plate. 

Mais quand tu veux construire un produit que d'autres vont utiliser de façon sérieuse et sécuritaire, ces choses-là sont essentielles. Pas la partie _fun_ du processus _though_. 

![](https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/acc1114e-07ee-4b3d-a79f-902e929485ca/daybits_architecture.png?t=1769999711)

Il y a un monde de différence entre un _internal tool_ pour toi ou tes collègues versus un produit que tu vas commercialiser et distribuer à du monde partout sur la planète. Le premier, tu peux le _vibe-coder_ en une fin de semaine. Le deuxième? Ajoute facile quelques semaines pour l'emballage. 

### Vibe verdict

C'est pas de la magie le _vibe-coding_ , mais pas loin. Si t'es patient, un minimum instruit, pas mal curieux… tu peux faire des trucs _insane_. 

Si t'as une idée claire, des critères bien définis, et que tu sais ce que tu veux—l'AI va te permettre de _builder_ des choses que t'aurais jamais pu faire seul. Moi, je suis pas _designer_. Je suis pas dev. Mais j'ai bientôt une app sur l'App Store. ¯\\_(ツ)_/¯ 

Par contre, il reste plein de choses opaques pour moi. Je comprends à haut niveau comment les parties de mon app interagissent. Mais quelle ligne de code fait quoi exactement? Aucune idée. J'ai encadré, supervisé, testé. Mais c'est pas moi qui ai codé le produit. 

Sinon, **mon**** _take_****sur les apps mobiles** : à moins que t'aies vraiment besoin de _features_ natives (GPS, caméra, _health data_), une bonne web app _mobile-first_ fait probablement la job. Le processus App Store, c'est _heavy_. Mais si tu penses pouvoir optimiser ce canal de distribution, ça peut payer _big time_! 

Est-ce que je referais ça? _Hell yes_. Mais avec des attentes calibrées. 

Genre, au début du processus, je prenais des _learning breaks_ sur ChatGPT ou Claude web pour "apprendre" c'était quoi tout ce que je faisais: 

❝ 

_Oh tell me more about data modelling please!_

Mais après quelques sessions, j'étais comme: 

❝ 

_let it f***ing RIP CLAUDE!_

\--dangerously-skip-permissions FTW 

Je vais continuer de m'amuser avec daybits, c'est un beau terrain de jeu. J'ai _of course_ d'autres idées de quoi builder, mais faut que j'aille au gym, que je marche, que je médite, que je ferme mes écrans avant 23:00… 

**Au moins maintenant j'ai une app pour cocher tout ça** 🙃 

→ **[Essaie daybits](https://daybits.app?utm_source=saaspasse.beehiiv.com&utm_medium=referral&utm_campaign=vibe-coder-un-saas-une-fds-not-so-fast)** — web ou mobile, c'est gratuit, simple, pis ça track tes _habits_ sans te faire sentir coupable.

![](https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/da0354f7-a22d-41c0-86d3-16212c117faf/daybits_calendar_view.png?t=1769999067)

Calendar view — web

— 

Quelque chose à ajouter? _Good_. Laisse un commentaire ou réponds à ce courriel direct. 

Cheers, 

[Frank](https://www.linkedin.com/in/frankln/?utm_source=saaspasse.beehiiv.com&utm_medium=referral&utm_campaign=vibe-coder-un-saas-une-fds-not-so-fast) 💜 

### Cybersécurité pour SaaS 👾

❝ 

"Ta clé API OpenAI traîne probablement sur GitHub."

Ouch. Mais c'est le genre de vérité _cash_ que [Cyndie Feltz](https://www.linkedin.com/in/cyndie-feltz/?utm_source=saaspasse.beehiiv.com&utm_medium=referral&utm_campaign=vibe-coder-un-saas-une-fds-not-so-fast) et [Nicholas Milot](https://www.linkedin.com/in/nicholas-m-99739390/?utm_source=saaspasse.beehiiv.com&utm_medium=referral&utm_campaign=vibe-coder-un-saas-une-fds-not-so-fast) te disent quand ils font affaire avec toi. 

Dans cette capsule, on démystifie la cybersécurité pour SaaS avec les _cofounders_ de [Yack](https://www.saaspasse.com/partenaires/yack?utm_source=saaspasse.beehiiv.com&utm_medium=referral&utm_campaign=vibe-coder-un-saas-une-fds-not-so-fast): 

  * C'est quoi un pen test et quand en faire un 

  * Les 2 vulnérabilités classiques qui reviennent tout le temps 

  * Gestion des secrets 

  * Est-ce que l'AI expose de nouvelles failles? 

[ Instruis-toi ](https://youtu.be/e39IRUjMFUg?utm_source=saaspasse.beehiiv.com&utm_medium=referral&utm_campaign=vibe-coder-un-saas-une-fds-not-so-fast)

### Le temps des impôts s’en vient vite….

[![](https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/df6d8de7-97e6-41c8-9d05-6ba68306393f/SaaSpaladin-le-temps-des-impots-approche-le-saaspaladin-va-vi-v1__1_.png?t=1770310371)](https://www.linkedin.com/posts/la-saison-des-imp%C3%B4ts-approche-ugcPost-7424816079627153409-Q7F4?utm_source=saaspasse.beehiiv.com&utm_medium=referral&utm_campaign=vibe-coder-un-saas-une-fds-not-so-fast)

Tu peux soit improviser comme d'habitude ou tu peux confier ça à des pros qui le font déjà pour pleins d’entrepreneurs. 

[Le Chiffre](https://www.saaspasse.com/partenaires/le-chiffre?utm_source=saaspasse.beehiiv.com&utm_medium=referral&utm_campaign=vibe-coder-un-saas-une-fds-not-so-fast) peut t'aider à: 

  * Préparer tes documents sans stress 

  * Poser les bonnes questions fiscales 

  * Garder tes chiffres en ordre 

Stratégie > improvisation. Clarté > chaos. 

[ Check them out ](https://www.saaspasse.com/partenaires/le-chiffre?utm_source=saaspasse.beehiiv.com&utm_medium=referral&utm_campaign=vibe-coder-un-saas-une-fds-not-so-fast)

### On creuse term-sheets avec notre pro pref

[![](https://beehiiv-images-production.s3.amazonaws.com/uploads/asset/file/2e83ae63-bd38-45be-a04e-fdc03284e35f/leviatxsaaspasse.jpeg?t=1770311408)Dissection d'un term sheet — Étude de cas SaaSpassew/ Guillaume Falardeau, avocat et fondateur @ Leviat Legal](https://www.saaspasse.com/blog/dissection-dun-term-sheet-ft-leviat-legal----etude-de-cas-saaspasse?utm_source=saaspasse.beehiiv.com&utm_medium=referral&utm_campaign=vibe-coder-un-saas-une-fds-not-so-fast)

**Les clauses qui vont te revenir dans face** 🪤 

T'es sur le point de signer ton _term sheet_. Excité. Stressé. Un peu perdu dans le jargon. 

"Attends, c'est quoi ça exactement?" 

On a pris un vrai _term sheet_ et on l'a décortiqué avec [Guillaume Falardeau](https://www.linkedin.com/in/guillaume-falardeau-b213768b/?utm_source=saaspasse.beehiiv.com&utm_medium=referral&utm_campaign=vibe-coder-un-saas-une-fds-not-so-fast) de [Leviat Legal](https://www.saaspasse.com/partenaires/leviat-legal?utm_source=saaspasse.beehiiv.com&utm_medium=referral&utm_campaign=vibe-coder-un-saas-une-fds-not-so-fast). Ligne par ligne. Clause par clause. 

Au menu: 

  * Les clauses au _look_ anodin qui peuvent te _bamboozle_ 3 ans plus tard 

  * Ce que les VCs négocient (et pourquoi) 

  * Les termes standards vs les _red flags_

[ Lis ça avant de signer ](https://www.saaspasse.com/blog/dissection-dun-term-sheet-ft-leviat-legal----etude-de-cas-saaspasse?utm_source=saaspasse.beehiiv.com&utm_medium=referral&utm_campaign=vibe-coder-un-saas-une-fds-not-so-fast)

### Rejoins les SaaSpals 👇 

Merci tellement à tous [nos SaaSpals](https://saaspasse.beehiiv.com/c/saaspals). Votre support nous motive _**BIG TIME**_. 

[![](https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/7acf8ce8-6a80-4794-aa1c-cc3ea311f3c4/Upgrade_CTA_-_beehiiv.jpg?t=1727976675)](https://saaspasse.beehiiv.com/upgrade)

### Partenaires certifiés SaaSpasse 💜

_HUGE_ merci à tous nos partenaires certifiés pour cette année : 

  * [Le Chiffre](https://www.saaspasse.com/partenaires/le-chiffre?utm_source=saaspasse.beehiiv.com&utm_medium=referral&utm_campaign=vibe-coder-un-saas-une-fds-not-so-fast) 🧾 

  * [Leviat](https://www.saaspasse.com/partenaires/leviat-legal?utm_source=saaspasse.beehiiv.com&utm_medium=referral&utm_campaign=vibe-coder-un-saas-une-fds-not-so-fast) 👨‍⚖️ 

  * [Baseline](https://www.saaspasse.com/partenaires/baseline?utm_source=saaspasse.beehiiv.com&utm_medium=referral&utm_campaign=vibe-coder-un-saas-une-fds-not-so-fast) 🤖 

  * [Unicorne](https://www.saaspasse.com/partenaires/unicorne?utm_source=saaspasse.beehiiv.com&utm_medium=referral&utm_campaign=vibe-coder-un-saas-une-fds-not-so-fast) 🌩️ 

  * [Finalta Capital](https://www.saaspasse.com/partenaires/finalta-capital?utm_source=saaspasse.beehiiv.com&utm_medium=referral&utm_campaign=vibe-coder-un-saas-une-fds-not-so-fast) 💰

### Podcast

Voici le dernier épisode du pod : 

**→**[**Ep.171 - Benoit Lacroix : Brûlé mais pas cramé (burn out, EV tech & résilience)**](https://www.saaspasse.com/episode/episode-171-benoit-lacroix-brule-mais-pas-crame-burn-out-ev-tech-resilience?utm_source=saaspasse.beehiiv.com&utm_medium=referral&utm_campaign=vibe-coder-un-saas-une-fds-not-so-fast)

Pas encore abonné au pod? Let’s go : 

  * [Spotify](https://saaspasse.us21.list-manage.com/track/click?u=08069c7a09572a6f53206b186&id=2175264455&e=f6fe3433c4&utm_source=saaspasse.beehiiv.com&utm_medium=referral&utm_campaign=vibe-coder-un-saas-une-fds-not-so-fast)

  * [Apple Podcasts](https://saaspasse.us21.list-manage.com/track/click?u=08069c7a09572a6f53206b186&id=41dc209695&e=f6fe3433c4&utm_source=saaspasse.beehiiv.com&utm_medium=referral&utm_campaign=vibe-coder-un-saas-une-fds-not-so-fast)

  * [YouTube](https://saaspasse.us21.list-manage.com/track/click?u=08069c7a09572a6f53206b186&id=0db39a54bc&e=f6fe3433c4&utm_source=saaspasse.beehiiv.com&utm_medium=referral&utm_campaign=vibe-coder-un-saas-une-fds-not-so-fast)

_Okay bobye!_

