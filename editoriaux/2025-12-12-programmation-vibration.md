Ma blonde dessine. Mon chien dort sur mes jambes. Lofi beats, samedi tranquille. 

Je suis canté dans le sofa, laptop sur les cuisses, écran mirroré sur la TV. 

Pis je parle tout seul (à [Monologue](https://www.monologue.to/?utm_source=saaspasse.beehiiv.com&utm_medium=referral&utm_campaign=programmation-vibration)). 

Je décris une app. Il transcrit. Google AI Studio génère le code, le preview. 

Peut-être le _side project_ le plus relax de ma vie? 

Mais c'est parti d'une frustration pas mal moins zen : j'étais tanné de juste… m'enregistrer tout le temps. De documenter. De parler de _builder_ sans rien _builder_. 

Faisait trop longtemps que j'avais pas créé quelque chose de tangible. 

Ce PM-là, j'ai décidé que ça changeait! 

Aujourd’hui, je te raconte comment j'ai pris 2 heures pour transformer un irritant de 20 minutes en app de 2 minutes. La stack, les galères, le "_prompt sandwich_ " pour garder un style visuel consistant. 

Pis surtout : des idées concrètes pour que tu fasses pareil dans ta shop. Que ce soit en marketing, sales, HR ou ops — si t'as un workflow répétitif qui te gosse, t'as peut-être une app qui dort là. 

### Le problème de base

L'édito a besoin d'illustrations chaque semaine. J’essayais d’incorporer mon personnage _custom_ le plus souvent possible : le SaaSpaladin, notre petite mascotte chevalier. Mais ça prenait trop de temps vs l’impact généré. 

![](https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/c2839a4f-53e6-47c5-98f1-3b1b732d7e95/saaspaladinmoney.gif?t=1765231252)

Meh

Le _workflow_ , c'était quelque chose comme ça : 

J’ouvre ChatGPT. J’écris un prompt de 200 mots pour décrire la scène. 

Ok là le SaaSpaladin est dans un laboratoire d'alchimie, avec des fioles qui bouillonnent, style dark fantasy, mais pas trop sombre, pis son casque doit être trapu, genre forme de gélule, couleur crème, pas pointu… surtout pas pointu.

Première image générée : le @#$%&! casque est pointu. 

Je régénère. Deuxième essai : maintenant ça ressemble à un ballon de football. 

Je _tweak_ le prompt. Troisième essai : correct, mais l'éclairage est _weird_. 

Quinze à vingt minutes plus tard, j'avais **peut-être** une image utilisable. 

C'était pas juste long. C'était incohérent d'une semaine à l'autre. Le personnage variait trop. Et impossible de partager ce _workflow_ -là avec mon équipe sans leur donner un manuel d'instructions de trois pages. 

Résultat : je créais rarement des images du SaaSpaladin. J'étais toujours _rushé_ , toujours en retard, toujours en train de sacrifier la qualité visuelle parce que j'avais pas le temps de me battre avec des prompts. 

Ça prenait une meilleure solution… genre, une APP peut-être? Ben oui c’est _overkill_ … _sue me_.

### Quand ça parle de Gemini partout

Partout… sur X, YT, LI. Exemple, sur son _channel,_ Greg Isenberg parlait de[ Gemini 3 Pro](https://deepmind.google/models/gemini/pro/?utm_source=saaspasse.beehiiv.com&utm_medium=referral&utm_campaign=programmation-vibration) et de Google AI Studio : 

Leur nouveau modèle + UI de vibe coding avait l’air _sick_! [Nano Banana Pro](https://gemini.google/overview/image-generation/?utm_source=saaspasse.beehiiv.com&utm_medium=referral&utm_campaign=programmation-vibration) avait l’air _sick_! 

Au cas où t’étais en-dessous d’une roche dans l’année dernière, le vibe coding c’est : 

Tu décris ce que tu veux au AI. Le AI écrit le code. Tu regardes ce qu’il a fait. Tu lui dis ce qui marche pas. Ça ajuste. Tu itères. Éventuellement, t'as une app qui fonctionne. 

Pas de magie. C'est du vrai code — React, TypeScript, toute la patente. Mais t'as un copilote expert assis à côté de toi qui connaît toute la syntaxe, toutes les librairies, tous les _design patterns_. 

La différence avec le **_no-code_**? Tu gardes le contrôle. Le code est là, devant toi. Tu peux l'ouvrir, le lire, le modifier. T'es pas enfermé dans une plateforme propriétaire avec des blocs _drag-and-drop_. Si un jour t'as besoin d'un.e dev pour aller plus loin, le code existe déjà. 

Google AI Studio en mode _build_ , c'est l'outil que j'ai utilisé. En gros, c’est un éditeur de code avec un AI intégré qui comprend ce que tu veux builder. Tu lui parles en français, il te répond en JavaScript. 

J'avais mon irritant, mon outil. Restait juste à essayer! 

### Le _build_

**Partie A - Prototypage dans AI Studio**

J'ouvre Google AI Studio. Je lui explique mon problème : 

❝ 

J'ai besoin d'une app qui prend le texte de mon éditorial, comprend le thème, et génère une illustration du SaaSpaladin dans une scène _fantasy_ qui _fit_ avec le sujet.

L’AI me propose une structure. Un formulaire pour coller le texte. Un bouton pour analyser. Un autre pour générer l'image. Ça écrit le code. Je vois l'app apparaître. 

Mais y'a un problème : comment garantir que le style visuel reste cohérent? Comment m'assurer que le casque du Paladin soit toujours trapu, jamais pointu, et toujours la bonne couleur? 

C'est là qu’on a ajouté une forme de "_p_ _rompt sandwich_ ". 

Imagine une recette en trois couches : 

**Couche 1 — L'analyse** : Gemini 2.5 Flash lit ton éditorial. Disons que tu parles de bugs en production. L'AI traduit ça en métaphore _fantasy_ : "Gobelins qui envahissent la salle des coffres du château." 

**Couche 2 — Le secret invisible** : L'utilisateur voit jamais cette partie. Le code injecte automatiquement une description anatomique stricte du personnage (casque ovale, couleur crème `#F6F3EC`, forme gélule), une image de référence en base64, pis des mots-clés négatifs (No tall helmet, no pointed helmet). 

**Couche 3 — La génération** : Gemini 3 Pro reçoit le package complet : la scène fantasy + les contraintes visuelles + l'image de référence. Il génère l'illustration finale. 

L'utilisateur décrit jamais le style. 

**Partie B -**_**Switch**_**vers Claude Code**

L'app fonctionnait mais j'itérais lentement. 

Google AI Studio, c'est _clean_ visuellement. T'as ton _chat_ à gauche, ton _preview_ à droite, style [Lovable](https://lovable.dev/?utm_source=saaspasse.beehiiv.com&utm_medium=referral&utm_campaign=programmation-vibration) ou [Bolt](https://bolt.new/?gad_source=1&utm_source=saaspasse.beehiiv.com&utm_medium=referral&utm_campaign=programmation-vibration). Sauf que chaque modification prend du temps à se rafraîchir. Le _feedback loop_ est pas assez rapide. 

Alors j'ai migré vers Claude Code. Rien de _fancy_. Juste toi, un terminal, pis Claude qui code avec toi en temps réel. 

Mais c’est _blazing fast_. Itérations 2-3x plus rapides. Je demande un changement, Claude l'applique, je teste immédiatement dans mon navigateur local. 

En quelques chats, j'ai : 

  * Fixé un bug d'affichage (balise script manquante) 

  * Sécurisé la clé API Gemini côté serveur (Netlify Functions) 

  * Ajouté un mot de passe pour protéger l'app 

  * Affiné le _prompt sandwich_ pour régler le problème du casque rebelle 

  * Intégré l'autocomplete des éditoriaux existants depuis notre archive (repo GitHub) 

Pour déployer, j'avais déjà un setup qui roulait bien :[ GitHub](https://github.com/?utm_source=saaspasse.beehiiv.com&utm_medium=referral&utm_campaign=programmation-vibration) +[ Netlify (tout gratis). ](https://www.netlify.com/?utm_source=saaspasse.beehiiv.com&utm_medium=referral&utm_campaign=programmation-vibration)Chaque fois que je _push_ du code, Netlify déploie automatiquement. Pas besoin de configuration compliquée, aka le cauchemar UI qu’est l’admin de Google Cloud Console. 

**Partie C - L'app finale**

Résultat : [paladin.saaspasse.com](https://paladin.saaspasse.com?utm_source=saaspasse.beehiiv.com&utm_medium=referral&utm_campaign=programmation-vibration)

_Je l’ai protégée avec mot de passe quand j’ai réalisé les insanités que vous pourriez faire en brûlant mes tokens LOL_

![](https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/5d3f23f6-21be-44ce-935a-8498d23fa6bc/CleanShot_2025-12-11_at_16.47.29_2x.png?t=1765489669)

Le flow est simple : 

  1. Tu te connectes avec le mot de passe 

  2. Tu colles ton texte OU tu sélectionnes un éditorial existant 

  3. Tu cliques "Extraire l'essence visuelle" — l'AI analyse et propose un concept 

  4. Tu cliques "Générer l'illustration" — l'image apparaît (1200×630 pixels, format parfait pour beehiiv) 

  5. Si t'aimes pas, tu régénères ou _tweak_ le prompt 

  6. Si t’aimes, tu télécharges 

Temps total : 2 minutes. Avant : 15-20 minutes. 

_**10X GAINS AM I RIGHT?**_

![](https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/7c83edd2-a15c-4eb0-91a2-3b22f18fb5bd/Flow_-_La_forge_du_SaaSpaladin.gif?t=1765501035)

_Disclaimer_ : j’avais déjà un flow Claude Code + beehiiv API qui télécharge, nettoie, classifie, et archive tous mes éditoriaux dans un repo GitHub. On a connecté ce repo-là à l’app de la forge. Par **on** , je veux dire Claude Code, moi je ne suis pas capable de faire ça.

Toute mon équipe peut l'utiliser, LA FORGE. Le style est cohérent. Plus besoin d'être un expert en _prompt engineering_. 

### Les galères

Là, ça sonne tout beau tout parfait mais, je tiens à vous rappeler que même avec le AI, rien est jamais smooth du premier coup. J’ai eu quelques défis dans le processus comme : 

**La tête de ballon**

En voulant adoucir les traits du personnage, j'ai ajouté "forme ronde" dans le meta prompt qui roule dans le “ _backend_ ”. 

Erreur. 

L'AI, très littérale, a transformé le casque en sphère parfaite. Un ballon de football posé sur une armure. Mon SaaSpaladin ressemblait à une mascotte de NFL Fantasy. 

J'ai appris que le vocabulaire sémantique compte. "Forme ronde" ≠ "Forme gélule". Les mots ont du poids. Le AI comprend exactement ce que tu dis, pas TOUJOURS ce que tu **veux** dire. 

**Le gaslighting du terminal**

Pendant un bon bout, Google AI Studio m'a convaincu qu'il y avait un terminal caché quelque part dans l'interface—quel enfer. Le modèle me guidait : "Clique ici, ouvre ce menu, tu vas voir la console." 

J'ai cherché pendant vingt minutes. 

Ça existait pas. 

Le modèle pensait que j'étais dans un **autre** environnement Google, plus complet, avec un vrai IDE. Il me donnait des instructions pour un produit que j'utilisais pas. 

Même les meilleurs modèles hallucinent parfois. Pas sur des faits, mais sur leur propre contexte. _Tip: when in doubt, share screenshots._

### Ce que ça change pour les fondateurs

T’as plus besoin d'être dev pour construire des outils internes. 

On parle pas juste de _landing pages_ ou de jouer avec Zapier et des _triggers_. On parle de vraies apps custom avec des AI features qui règlent tes irritants spécifiques. 

Pense à ton quotidien de fondateur. Les petites frictions qui te grugent du temps : 

**Marketing** — Tu génères des ads pour Facebook. Chaque semaine, tu copies-colles le même template, tu changes trois mots, tu exportes dans le bon format. 

Tu pourrais avoir une micro-app qui prend ta campagne en _input_ , génère 5 variantes _on-brand_ , pis te les sort aux bonnes dimensions. 

Note : [Jacomo](https://www.linkedin.com/in/jacomodeschatelets/?utm_source=saaspasse.beehiiv.com&utm_medium=referral&utm_campaign=programmation-vibration) de Emma a vibe-code une app pour streamline ta gestion Meta Ads, check it out: [INSTRUMNT](https://www.instrumnt.com/?utm_source=saaspasse.beehiiv.com&utm_medium=referral&utm_campaign=programmation-vibration). SaaSpasse a fait un deal avec Jacomo pour offrir 30% OFF lifetime, juste mentionner 👇

![](https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/21fcff44-8324-43fb-b8c6-811194ebc01d/CleanShot_2025-12-11_at_10.02.02_2x.png?t=1765465349)

**Sales** — Tu envoies des _one-pagers_ personnalisés à chaque prospect. Tu ouvres ton deck PowerPoint, tu changes le logo du client, tu ajustes les _use cases_. 

Tu pourrais avoir une app qui pull les infos du prospect depuis ton CRM, les notes d’appel via Granola ou autre _note-taker,_ pis te génère le _one-pager custom_ automatiquement. Et ensuite qui pré-popule un email dans ton email client ou CRM avec lien vers le _one-pager._

**HR** — Tu postes des offres d'emploi. Chaque fois, tu réécris la même structure, tu _tweakes_ le ton pour LinkedIn vs ton site. 

Tu pourrais avoir une app qui prend la description de poste pis te sort trois versions : corporate, startup vibe, pis technique. Ou carrément qui se connecte à tes comptes de job boards/HR tools et qui fait le posting pour toi. 

Meh, je dis “une app”, mais ça pourrait __ être juste un Claude Skill, un projet ChatGPT avec instructions custom, un sub-agent dans Claude Code… _whatever works_. Dépend de ton cas d’utilisation et de qui doit avoir accès au output et où.

Toujours le même _pattern_ :   
  
Un irritant répétitif + un _output_ prévisible = une opportunité de _vibe coding._

L'_anti-overengineering_ compte ici. Commence simple. Une seule _feature_. Un seul _workflow_. Itère vite. Si ça marche, tu pousses plus loin. Si ça marche pas, t'as perdu une journée, pas trois mois de développement. 

Le vrai avantage du vibe coding, c'est ça : passer de "j'ai une idée" à "j'ai un prototype fonctionnel" en une journée. 

Pis hésite pas à demander au AI : 

Doit ben avoir une manière plus simple de faire ça?  
Comment on pourrait réduire le nombre de tokens que ça coûte?  
Comment je devrais penser à la collaboration avec mes collègues?  
Quelles étapes on pourrait skipper ou abstraire là-dedans?

### Tout le monde est forgeron maintenant

Avant, y'avait une friction énorme entre l'idée et l'exécution. Tu voyais le problème. Tu savais la solution. Mais entre les deux, y'avait six mois de code, un budget de 50k, et des compromis sur ta vision parce que le dev comprenait pas exactement ce que tu voulais. Ou un VC qui te disait que c’était pas finançable. 

Cette friction-là vient de disparaître. 

Maintenant, tu peux décrire ce que tu veux. L'AI traduit. Tu valides. Tu itères. Tu déploies. 

C'est pas une question de remplacer les devs. C'est une question d'augmenter les _builders_. 

Pis _OF COURSE_ faut que tu fasses attention si tu veux commercialiser, gérer de la donnée utilisateurs, _process_ des paiements, etc. Dans cette optique-là, tu dois t’instruire un minimum sur comment prompter et équiper ton AI avec des bonnes pratiques ou tooling de sécurité. Mais tu peux _legit_ trouver ça sur YouTube, Google et… ChatGPT / Claude. Des tutoriels là-dessus, y’en pleut sur Internet. 

Je vais te laisser avec la question qui m'obsède depuis que j'ai fini cette app : 

Quels irritants mériteraient une app? Un _workflow_ d’automation?

Peut-être que c'est moins compliqué que tu penses? Peut-être qu'il te reste juste à ouvrir un terminal et décrire ton problème? 

Si t’as peur du terminal et de Claude Code, arrête de niaiser pis lis ça : 

→ [Claude Code: The Most Common Questions Beginners Ask](https://every.to/source-code/claude-code-the-most-common-questions-beginners-ask?utm_source=saaspasse.beehiiv.com&utm_medium=referral&utm_campaign=programmation-vibration)

La barrière entre toi pis ton prochain _build_ vient de rapetisser en maudit. 

— 

Quelque chose à ajouter? _Good_. Laisse un commentaire ou réponds à ce courriel direct. 

Cheers, 

[Frank](https://www.linkedin.com/in/frankln/?utm_source=saaspasse.beehiiv.com&utm_medium=referral&utm_campaign=programmation-vibration) 💜 

### 🎙️ De retour dans la Vieille Capitale

[![](https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/faeb25e1-9232-4f0e-b98b-88a82b9111f9/SaaSpasse_x_Nexapp_2.0.png?t=1765466408)](https://www.eventbrite.ca/e/billets-saaspasse-a-quebec-edition-18-1976883070480?aff=oddtdtcreator&utm_source=saaspasse.beehiiv.com&utm_medium=referral&utm_campaign=programmation-vibration)

QUÉBEC! Ça fait un bail. 

**29 janvier: On débarque chez Nexapp pour enregistrer un pod live avec Jonathan Lessard (président & cofondateur @ Nexapp/Axify).**  
  
On va jaser de : 

  * Vendre du service tech dans un marché saturé 

  * Transformer une douleur à l'interne en SaaS (Axify) 

  * Culture et modèle de leadership comme avantages compétitifs pour le talent 

  * Comment le AI transforme les pratiques et attentes des clients 

On a déjà vendu 60% des billets. Dépêche! 

[ Réserve ta place ](https://www.eventbrite.ca/e/billets-saaspasse-a-quebec-edition-18-1976883070480?aff=oddtdtcreator&utm_source=saaspasse.beehiiv.com&utm_medium=referral&utm_campaign=programmation-vibration)

### Poste ouvert chez Matador AI 💼

_New year, new career, folks!_  
  
La gang chez Matador cherche actuellement quelqu’un pour prendre le volant côté marketing. 

**Le gig**

  * Gérer la constellation de contracteurs marketing déjà en place 

  * Scaler vers de nouveaux revenue streams et partenariats stratégiques 

  * Optimiser la croissance organique (pas de rebranding, juste de la vraie croissance) 

  * Travailler direct avec les cofondateurs et l'équipe de direction 

  * Coordonner efforts marketing à travers 10 fuseaux horaires 

Si t’es intéressé.e ou que tu connais quelqu’un, c’est par ici : 

[ détails & application ](https://www.saaspasse.com/lajobdumois?utm_source=saaspasse.beehiiv.com&utm_medium=referral&utm_campaign=programmation-vibration)