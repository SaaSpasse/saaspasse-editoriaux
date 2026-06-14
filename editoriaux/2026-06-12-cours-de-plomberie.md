Mettons que tu veux un agent qui lit tes courriels le dimanche soir pis t'envoie un brief sur Slack : tes 5 priorités de la semaine, 3 réponses suggérées, 2 affaires à déléguer. 

Pas besoin d'être dev pour ça en 2026. Codex, Claude Cowork, Claude Code—tu configures ça assez _quick_. 

(Si t'as lu [SensAI](https://infolettre.saaspasse.com/p/sensai) ou [Outiller tes agents](https://infolettre.saaspasse.com/p/outiller-tes-agents), c'est le genre de _scheduled task_ que je roule chez nous.)

Tant que ça passe sur tes crédits d'usage—ton abonnement Claude ou Codex—la facture te fait pas trop sourciller. 

Ça, c'est un agent à l'échelle d'une personne. 

Toi. Ton laptop. Ta _job_. 

Mais prends ce pouvoir agentique-là, multiplie-le par tes utilisateurs, branche-le sur leurs vraies données, leurs permissions, leurs intégrations brisées, leurs comptes incomplets, leurs demandes formulées tout croche. 

Pis essaie de mettre ça dans TON app. 

Là c'est une autre _game_. 

Une _feature_ ou un _workflow_ agentique dans un SaaS, c'est un morceau de produit qui doit tenir dans ton infra. Ça peut impressionner en démo pis choker en prod. 

Toute cette plomberie-là, je la comprenais mal. 

Fait que j'ai fait ce que je fais quand je veux éviter de dire n'importe quoi : j'ai parlé à quelqu'un qui a les deux mains dedans. 

J'ai _booké_ une convo avec [Philippe Trépanier](https://www.linkedin.com/in/phil-tr%C3%A9panier-6308b51b7/?utm_source=infolettre.saaspasse.com&utm_medium=referral&utm_campaign=cours-de-plomberie) de chez [Unicorne](https://www.saaspasse.com/partenaires/unicorne?utm_source=infolettre.saaspasse.com&utm_medium=referral&utm_campaign=cours-de-plomberie), des nerds certifiés AWS qui _build_ pis déploient ce genre de systèmes pour des SaaS et autres compagnies. 

Je suis arrivé avec mes analogies croches. Phil les a redressées. Pis j'ai fini par mieux catcher le stock pas sexy qui décide si ton agent passe ou casse devant de vrais users. 

### Comme moi, le mot agent a pris du poids

Avant de rentrer dans les tuyaux, faut quand même s'entendre sur ce qu'on appelle un agent. 

Parce que le mot est rendu pas mal élastique. 

Dans sa version la plus simple, un agent AI, c'est un **gros modèle de langage** branché sur des outils, capable de décider quoi faire ensuite pour accomplir une tâche. 

(Je prends goût à écrire LLM en français, _no joke_)

Techniquement, l'agent dépasse le modèle. C'est le système autour. 

À la base, le modèle raisonne sur ta demande. Pis les outils lui donnent des mains pour agir. 

Par agir, je veux dire : Lire une page web. Fouiller une base de données. Appeler une API. Lancer une commande. Ouvrir un _browser_. Envoyer un message Slack. Ajouter une tâche dans Linear. Aller chercher un fichier dans Google Drive. 

À la limite, un MCP, c'est ça aussi : une manière standardisée de brancher un tiroir d'outils à ton modèle. Au lieu de lui expliquer chaque tournevis un par un, tu lui donnes accès au coffre. 

_It's tools all the way down in AI land_ 🙃 

Donc le bout agentique commence quand le système dépasse la réponse en texte. Il regarde la demande, décide de la prochaine action, appelle un outil, lit le résultat, ajuste son plan, appelle peut-être un autre outil, puis revient avec quelque chose qui ressemble à une job accomplie. 

À petite échelle, c'est presque banal. Ton agent lit tes courriels, fouille ton calendrier, te prépare un brief. 

À l'échelle d'un SaaS, le même pattern devient une _feature_ de produit. (Ou carrément un produit!) 

Un utilisateur clique sur un bouton dans ton app. En arrière, un agent analyse ses données, appelle trois services, écrit dans ta base de données, génère une recommandation, déclenche une action, puis affiche un résultat dans ton interface. 

L'expérience a l'air simple. 

La mécanique en dessous, elle, reste très logiciel. _ENGINEEEEERING_.

À ton échelle perso, un agent _basic_ qui se trompe te fait perdre dix minutes pis dix piastres. 

À l'échelle produit, la même erreur devient une action faite dans le compte d'un client. _Hit_ sur le churn, la réputation, ou les deux. Ou ben un massacre silencieux de tes marges. Quelqu'un doit pouvoir comprendre ce qui s'est passé, reprendre le contrôle, corriger le tir, puis empêcher que ça revienne. 

Mets ta salopette, ta calotte, pis lisse ta moustache, parce qu'on _drop_ dans les tuyaux live, _buddy_. 

(C'est une référence à Mario Bros.) 

((J'ai des problèmes d'insécurité donc j'ai expliqué ma référence au cas où quelqu'un me trouve juste _weird_))

(((Jesus Christ c'est encore pire avec toutes les parenthèses... au moins je sais de quoi parler au prochain [RDV avec mon psy](https://saaspasse.beehiiv.com/p/le-jour-o-ton-cerveau-l-che?utm_source=infolettre.saaspasse.com&utm_medium=referral&utm_campaign=cours-de-plomberie))))

### Où ça vit, un agent?

Question niaiseuse en apparence, mais elle m'a vraiment aidé. 

Quand tu utilises Claude Code ou Codex sur ton laptop, la réponse semble simple. L'agent vit dans ton app desktop, dans ton terminal, dans ta session, avec tes fichiers. 

Mais dans un SaaS, l'agent devient un morceau de ton produit. 

L'utilisateur voit un bouton, un champ de texte, une recommandation, une action magique dans l'interface. 

En arrière, c'est une chaîne d'approvisionnement. 

Phil m'a ramené aux bases : l'infra d'un agent a rien d'une brume mystique. Un serveur pour hoster ton code, du _load balancing_ , du DNS, de l'observabilité, de la sécurité. Des affaires _boring_ jusqu'au moment où elles manquent. 

Okay, bougeons ensemble à travers cette chaîne. 

**Première étape** : ton app reçoit la demande. Elle sait quel utilisateur est connecté, dans quel compte, avec quelles permissions. 

**Deuxième étape** : ton _backend_ prépare la job. Il va chercher les bonnes données, enlève ce que l'agent ne devrait pas voir, ajoute le contexte utile, choisit quels outils sont disponibles. 

**Troisième étape** : la job est envoyée à la partie agentique de ton produit. Elle roule quelque part, dans un _runtime_. 

Un _runtime_ , c'est grosso modo l'environnement où ton code s'exécute. Le petit appartement où ton agent habite le temps de faire sa job.

**Quatrième étape** : l'agent appelle un modèle. Gemini, Claude, GPT, un modèle open source, peu importe. Il lui envoie un paquet : la demande du _user_ , les instructions, le contexte, les outils disponibles, les contraintes. 

C'est là que **l'inférence** entre en jeu : le moment où le modèle prend ce paquet-là et fait son calcul.

**Cinquième étape** : quelque part, dans un _data center_ , des GPU utilisent de l'électricité et font ce calcul-là. Le modèle génère une réponse, un plan, ou une demande d'action. 

**Sixième étape** : la réponse revient à l'agent. L'agent peut décider d'appeler un outil, lire le résultat, continuer, arrêter, demander plus d'info, ou produire la réponse finale. 

**Septième étape** : ton app reprend le contrôle. Elle sauvegarde ce qui doit être sauvegardé, affiche le résultat, déclenche l'action, ou bloque quelque chose si ça pète tes _guardrails_. 

Tout ça peut se passer en quelques secondes. 

Vu du user : un bouton. 

Vu de l'ingénierie : une vraie petite chaîne industrielle avec des entrées, des sorties, des fournisseurs, des machines, des contrats implicites entre chaque morceau. 

Tu pars de ce qui est proche de toi : ton interface, ton compte, tes crédits, ton usage. 

Tu recules d'un cran : ton app, ton _backend_ , tes données, tes outils. 

Tu recules encore : le _runtime_ de l'agent, les appels API, les modèles. 

Encore : les _data centers_ , les racks, les GPU, l'électricité, le réseau. 

Pis après toute cette poutine-là, ça revient jusqu'à ton user en forme de petite réponse propre dans ton interface. 

Magique en surface. 

Très matériel en dessous. Comme [l'Internet](https://www.flanthiernadeau.com/internet/?utm_source=infolettre.saaspasse.com&utm_medium=referral&utm_campaign=cours-de-plomberie). 

_SO_ —les tuyaux décident si l'eau est potable, pis si elle se rend au robinet. 

### La démo qui jette à terre

Les démos d'agents AI sont rendues absurdes. 

Tu vois un système qui regarde à travers tes lunettes, comprend ton salon, te sort une version 3D de ta maison, appelle un designer d'intérieur, commande trois plantes, booke quelqu'un pour peinturer, pis t'envoie un résumé dans Slack. 

Je dis n'importe quoi, _of course_. Mais je suis pas loin!

Les démos sont faites pour montrer le moment magique : le _use case_ propre, la route dorée, le scénario où tout répond comme prévu. _Happy happy path_. 

En prod, ce beau petit chemin _clean_ se transforme en centre-ville un jeudi de slush. 

Même _feature_ , mille chemins : un client qui n'a pas donné le bon accès, une donnée héritée d'un import croche, une intégration qui répond lentement, un user qui demande l'inverse de ce que ton _flow_ attendait. 

Pis ton agent doit quand même livrer. 

**Le premier**** _reality-check_****de prod de Phil, c'est le**** _context bloat_****.**

Le contexte, c'est tout ce qu'on met devant le modèle au moment d'un appel d'inférence : la demande du user, les instructions, l'historique, les données récupérées, les outils disponibles, les résultats d'outils précédents. 

La fenêtre de contexte, c'est l'espace de travail où tout ça doit rentrer. Même énorme, elle peut se remplir de bruit. 

Phil me disait : quand tu arrives en prod, tu découvres souvent que tes outils retournent beaucoup trop de données. Ils donnent tout au modèle au lieu de lui donner juste ce dont il a besoin pour faire la prochaine étape. 

Son analogie : c'est comme les humains. Trop de contexte, trop de _context switching_ , trop de signaux à gérer en même temps, pis tu fais moins bien ta job. 

Même affaire pour un modèle. Plus de place n'est pas une excuse pour lui pitcher tous tes bagages. 

Un bon exemple : la navigation dans un _browser_. 

Mettons qu'un agent doit inspecter une page web pour comprendre ce qui s'y passe. Une approche sub-optimale, c'est de lui envoyer le DOM complet. 

Le DOM, pour les non-devs, c'est grosso modo la structure interne d'une page web : les titres, les boutons, les liens, les menus, mais aussi une tonne de conteneurs, d'attributs, de bouts invisibles, de scrap technique qui existe pour que la page fonctionne.

Des fois, toi, tout ce que tu voulais, c'était le texte visible pis le nom du bouton. 

Mais ton outil pitche au modèle l'équivalent du plan électrique complet du bâtiment. 

Résultat : ça coûte plus cher en tokens, ça remplit le contexte avec du bruit, pis ça augmente les chances que l'agent perde le fil. 

Le coût devient vite plus qu'un détail comptable. 

C'est le bout [FinOps](https://youtu.be/nlPdA-1JIEY?utm_source=infolettre.saaspasse.com&utm_medium=referral&utm_campaign=cours-de-plomberie) de l'affaire. 

Phil me disait que les _founders_ savent que les LLM vont coûter cher, mais sous-estiment presque toujours à quel point. À mon échelle perso, ça mange un peu plus de ma _sub_. À l'échelle d'un produit, ça devient une ligne dans ton coût PAR utilisateur. 

Si tu n'as pas de quotas, pas de limites par compte, pas de choix intelligent de modèles, pas d'outils qui retournent juste assez de données, ta belle _feature_ agentique peut gruger tes marges pendant que tout le monde applaudit la démo. 

**Deuxième affaire qui pète souvent : le code**** _custom_****.**

Quand tu _build_ un agent pour ton SaaS, tu assembles du logiciel : fonctions, appels API, lectures en base de données, intégrations client, garde-fous, _jobs async_ , _retries_ , erreurs 500 à 23h42 un mardi soir. 

Tout le code autour de ton agent AI peut encore péter. 

Mais l'agent ajoute un genre de bug plus _weird_ : il peut se tromper sans crasher. 

Il appelle le mauvais outil, oublie une contrainte, lit un résultat de travers, puis continue comme si tout allait bien. 

Pas d'erreur rouge. Pas de page qui plante. Juste une mauvaise décision emballée dans une réponse crédible. 

Donc le _gap_ entre démo et prod est pas philosophique. Il est très concret. 

À ce stade-là, regarder l'interface ne suffit pas. 

Faut ouvrir l'armoire pis se pencher en dessous de l'évier. 

### Quand ça pète, tu regardes où?

Dans un SaaS normal, quand une page plante ou qu'une API retourne une erreur, tu vas voir tes _logs_ : telle requête est arrivée, tel service a répondu, telle erreur est sortie. 

Avec un agent, tu as encore besoin de ça, mais faut aussi voir son parcours : appel au modèle, appel à un outil, réponse de l'outil, changement de plan, deuxième outil, résultat final. 

Phil m'a réexpliqué la notion d'observabilité : comprendre ce qui se passe dans ton système à partir des traces qu'il laisse derrière lui. 

Une trace, c'est le fil d'Ariane d'une requête. Tu pars du clic du user, puis tu suis ton _workflow_ en étapes à travers ton _backend_ , ton modèle, tes outils, tes APIs. 

Chaque bout du trajet peut devenir un _span_ : une étape mesurable avec un début, une fin, une durée, parfois des métadonnées. Combien de temps le _call_ a pris? Quel outil a été appelé? Quelle réponse est revenue? Où est-ce que ça a ralenti? Où est-ce que ça a pété? 

[OpenTelemetry](https://opentelemetry.io/?utm_source=infolettre.saaspasse.com&utm_medium=referral&utm_campaign=cours-de-plomberie) sert à standardiser cette collecte-là. 

Ce standard dépasse l'AI. Il sert à instrumenter des apps cloud : générer des traces, des métriques, des logs, puis les envoyer dans tes outils d'observabilité. 

Dans un système agentique, ça compte encore plus parce que la job peut être distribuée entre ton app, ton _backend_ , ton _runtime_ d'agent, ton modèle, tes outils, tes APIs, tes bases de données. 

Sans traces, tu regardes le résultat final comme un piment en te demandant : pourquoi il a fait ça? 

Pour le monde plus produit/marketing, l'analogie qui m'a aidé : c'est du _behavior analytics_ , mais pour ton système au lieu de ton utilisateur. La valeur, c'est de comprendre le chemin, pas juste de constater que ça a mal fini.

Pour diagnostiquer et _debugger_ , Phil ne fait plus cette enquête à la main dans une console. 

Il branche [Kiro](https://kiro.dev/?utm_source=infolettre.saaspasse.com&utm_medium=referral&utm_campaign=cours-de-plomberie), ou un outil comme Claude Code, à des MCP qui donnent accès aux données AWS : logs, métriques, traces, services. 

Puis il demande en langage naturel : 

_J'ai beaucoup d'erreurs 500 en prod. Va voir les logs autour de tel call, trouve-moi l'hypothèse la plus probable, propose un plan de remediation._

L'agent ne remplace pas le jugement du dev. 

Mais au lieu de passer huit heures à fouiller dans les logs, filtrer, cliquer, corréler des métriques, il peut parfois obtenir un rapport d'enquête en trente minutes. 

Tu utilises des agents pour bâtir et opérer des agents. 

Méta-plomberie récursive. 

### Les trois étages AI d'AWS

Là, si tu es comme moi, tu te dis : 

OK, mais AWS là-dedans, ça sert à quoi exactement? 

Parce que dire « AWS pour les agents », c'est aussi précis que dire « Internet pour les entreprises ». 

Techniquement vrai. 

Pas exactement éclairant. 

Phil m'a aidé à séparer ça en trois étages. 

**Premier étage :****[Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-bedrock.html?utm_source=infolettre.saaspasse.com&utm_medium=referral&utm_campaign=cours-de-plomberie)****.**

Bedrock, c'est le morceau le plus proche du modèle. Tu veux appeler Claude, Llama, Mistral, un modèle que tu importes toi-même, ou un autre modèle disponible dans l'écosystème AWS? Ça passe par là. 

Dans mon cerveau de non-dev, c'est le comptoir d'inférence. 

Tu arrives avec une demande, du contexte, des instructions. Tu appelles un modèle. Le modèle fait son calcul sur les GPU d'AWS, puis il te retourne une sortie. 

Pour transformer un transcript en résumé, générer un _template_ , classifier des tickets de support ou extraire des champs d'un document, un appel direct au modèle peut suffire. 

**Deuxième étage :****[Bedrock Agents](https://docs.aws.amazon.com/bedrock/latest/userguide/agents.html?utm_source=infolettre.saaspasse.com&utm_medium=referral&utm_campaign=cours-de-plomberie)****.**

Là, tu configures un agent managé qui peut orchestrer des étapes : utiliser des données, appeler des APIs, déclencher des actions, répondre dans un _workflow_. 

Phil parlait de _click ops_ : aller dans la console AWS, cliquer, configurer, provisionner la ressource. 

Bedrock Agents vient encadrer ce taponnage-là. Tu lui donnes des instructions, tu branches des actions, des bases de connaissance, des morceaux de ton système, puis AWS s'occupe de faire vivre l'agent dans son environnement. 

Tu ne pars pas d'un _framework_ comme LangChain ou CrewAI pour coder toute l'orchestration toi-même. Tu restes dans le cadre managé de Bedrock. 

Si tu as l'image d'un [agent managé côté Claude](https://platform.claude.com/docs/en/managed-agents/overview?utm_source=infolettre.saaspasse.com&utm_medium=referral&utm_campaign=cours-de-plomberie), c'est la même famille d'idée : tu configures un cadre agentique déjà assemblé au lieu de coder toute l'orchestration toi-même. Sauf qu'ici, c'est branché dans le monde AWS.

Une analogie de Phil m'a débloqué : 

Bedrock Agents, c'est un peu comme le WordPress de la patente. 

Dans le sens : tu peux aller assez loin avec de la configuration, des blocs existants, des connexions prévues, une structure déjà pensée pour toi. 

Pour un _workflow_ assez standard, genre générer un rapport mensuel, répondre à des questions sur des documents internes, ou automatiser une suite d'actions bien cadrées, ça peut être exactement ce que tu veux. 

**Troisième étage :****[Amazon Bedrock AgentCore](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/what-is-bedrock-agentcore.html?utm_source=infolettre.saaspasse.com&utm_medium=referral&utm_campaign=cours-de-plomberie)****.**

Là, on tombe dans le _custom_. 

AgentCore, c'est la couche pour bâtir, déployer et opérer ton propre agent à l'échelle. Ton code. Ton _framework_ agentique. Ton comportement sur mesure. 

Phil me disait : pense à React. 

Avec WordPress, tu configures beaucoup dans un cadre déjà très structuré. 

Avec React, tu construis ton interface comme tu veux, mais tu prends aussi plus de décisions d'architecture. 

AgentCore, c'est ça pour un système agentique. Tu écris ton agent avec un _framework_ comme Strands, LangChain, LangGraph, CrewAI ou _whatever_ , puis tu le fais rouler dans une couche AWS faite pour le déployer, le _scaler_ , le sécuriser, l'observer. 

C'est là que la « poutine _serverless_ » de Phil rentre en jeu. 

Le _runtime_. L'identité. Les outils. La mémoire. L'observabilité. Le _scaling_. La sécurité. Toute la plomberie plate qui sort ton agent du projet de fin de semaine sur ton laptop. 

**Le** _**what's the point**_**de cette plomberie-là, c'est le contrôle et la puissance.**

Pour automatiser une tâche personnelle, l'outil clé en main, une _feature_ de Claude ou _whatever_ , peut très bien faire la job. 

Si tu veux une _feature_ agentique collée à ton SaaS et déployée à l'échelle, tu vas probablement avoir besoin de plus que ça. 

Tu vas vouloir le niveau de contrôle que le cadre managé ne te donne pas toujours. 

Ça, c'est plus proche du logiciel que de la magie. 

Et c'est exactement pour ça que toute cette plomberie existe! 

### Le vrai test

Un agent dans ton SaaS, c'est du logiciel avec **plus d'autonomie que d'habitude**. 

Il peut créer beaucoup de valeur, mais aussi se tromper d'une manière qui ne ressemble pas toujours à un bon vieux bug rouge dans ta console. 

Le test de padawan : 

Est-ce que ça marche? 

Le test de _master_ : 

Est-ce qu'on peut le faire rouler dans notre produit avec assez de garde-fous pour miser dessus? 

La démo montre que c'est possible. 

La plomberie décide si ça _scale_! 

— 

Quelque chose à ajouter? _Good_. Laisse un commentaire ou réponds à ce courriel direct. 

Cheers, 

[Frank](https://www.linkedin.com/in/frankln/?utm_source=infolettre.saaspasse.com&utm_medium=referral&utm_campaign=cours-de-plomberie) 💜 

### SaaSpasse Conf ‘26 : Nouveau branding 🎨

[![](https://conf.saaspasse.com/img/og-image.webp)](https://conf.saaspasse.com/?utm_source=infolettre.saaspasse.com&utm_medium=referral&utm_campaign=cours-de-plomberie)

10 septembre 2026. Une journée avec 250 founders & builders. Keynotes, pitch party, podcast en direct, after-party avec bar ouvert et beaucoup de fun.  
  
Mise en garde avant que tu cliques :  
  
L'an passé, on a manqué de billets. Cette année, y'a encore juste 250 places. Les _early bird_ sont déjà tous vendus (merci 💜).   
  
Quand c'est plein, c'est plein. Manque pas le bateau.

[ réserve ta place ](https://conf.saaspasse.com/?utm_source=infolettre.saaspasse.com&utm_medium=referral&utm_campaign=cours-de-plomberie)

### SaaS global, bâti depuis Québec 🏭

Yannick Haeck, CPO, appelle [Poka](https://saaspasse.com/startups/poka/?utm_source=infolettre.saaspasse.com&utm_medium=referral&utm_campaign=cours-de-plomberie) "une startup avec des privilèges."   
  
~200 employés, Nestlé, Bosch, Danone comme clients, portée internationale et encore assez d'agilité pour que le monde prenne des risques.  
  
Clique ici si tu veux te joindre à leur aventure. Y’a plusieurs postes disponibles : 

[ tous les détails ](https://?utm_source=infolettre.saaspasse.com&utm_medium=referral&utm_campaign=cours-de-plomberie)

### Section partenaires deux

[![](https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/f3842929-4774-4515-ab87-e6ec01b49abc/CleanShot_2026-06-11_at_15.15.32_2x.png?t=1781205378)](https://www.linkedin.com/feed/update/urn:li:activity:7470093802934968321/?utm_source=infolettre.saaspasse.com&utm_medium=referral&utm_campaign=cours-de-plomberie)

Y’a rien que je pourrais dire ici qui va battre ce _hook_ de [Guillaume Falardeau](https://www.linkedin.com/in/guillaume-falardeau-b213768b?utm_source=infolettre.saaspasse.com&utm_medium=referral&utm_campaign=cours-de-plomberie) dans son dernier post LinkedIn.  
  
Si t’es pas déjà sur sa page en train de lire [le post complet](https://www.linkedin.com/feed/update/urn:li:activity:7470093802934968321/?utm_source=infolettre.saaspasse.com&utm_medium=referral&utm_campaign=cours-de-plomberie), sache qu’il publie régulièrement des bijoux du genre et qu’un _follow_ vaut grandement la peine.  
  
Sinon, tu peux aller en apprendre plus sur sa compagnie 👇 

[ c’est quoi Leviat Legal? ](https://saaspasse.com/partenaires/leviat-legal?utm_source=infolettre.saaspasse.com&utm_medium=referral&utm_campaign=cours-de-plomberie)