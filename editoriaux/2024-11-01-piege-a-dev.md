What's up folks,

Merci d'être là. Je commence par mon édito—les nouvelles après. 🪶

> Où zèle tue vélocité, SaaS touche mortalité.

Vendredi matin d’été. Chez Boub, Lac-Beauport.

*Hot spot* pour closer des deals.

Entre mes bouchées d’omelette, je jase recrutement avec [Olivier Falardeau](https://www.linkedin.com/in/olivier-falardeau-5513139b/?utm_source=saaspasse.beehiiv.com&utm_medium=newsletter&utm_campaign=le-piege-a-dev-en-entrevue) @gaiia.

(Je plisse des yeux de temps en temps, pour voir si c’est pas Guillaume de Leviat déguisé en CTO)

La startup est en pleine croissance, et comme toutes les compagnies qui scale, ils doivent embaucher les bonnes personnes.

Ma classique : "C'est *tough* embaucher des devs ces temps-ci?"

Sa réponse me fait sourciller. Apparemment, son équipe a développé une **technique spéciale** en entrevue…

**→ Un piège à développeurs**

Une façon de détecter tôt dans le processus un trait particulièrement toxique. Le genre de réflexe qui nuit aux équipes R&D, et même à la croissance.

Mais avant de dévoiler leur sauce secrète...

Une histoire de cafétéria 🥡

### Le *pain* quand on casse la croute

Midi pile, startup cafétéria. Toute l'équipe mange ensemble. Ambiance détendue. Les conversations vont bon train à travers le *munching* de pad thaï. Tout le monde s’en sacre que Frank soit allergique.

Et là, ça commence.

Un dev (relativement nouveau) se met à critiquer une vieille partie du codebase :

"Vraiment pas optimal comme logique backend..."

"On devrait refactor tout ça en micro-services..."

"Je comprends pas pourquoi on garde ce vieux code-là, tellement 2016..."

"Si on migrait vers [nouveau framework sexy], le frontend pourrait..."

Les yeux roulent. Les épaules s'affaissent. L'énergie du dîner s’essouffle.

Un moment de *team building* informel devient une session improvisée de critique technique. Ça arrive souvent. Trop souvent.

*Don't get me wrong*—ce dev-là a probablement de bonnes intentions. C'est peut-être un vrai artisan du code qui veut pousser pour l'excellence technique. Le genre de personne qui passe ses weekends à explorer les dernières tendances en architecture logicielle, contribuer à l'open source, et rêver de *clean code* la nuit.

En soi, admirable.

En de rares occasions, nécessaire (l’app va littéralement casser si on *fuel* la croissance avec du hot VC money sans refactorer).

En général : *red herring*. Si on laissait l’équipe R&D focuser son énergie sur des détails sans réel impact sur la BUSINESSS—revenus, croissance, expérience client, maintenabilité—on n’aurait pas de compagnie. Et un produit sans compagnie c’est… communiste.

(s’t’une joke, relaxez)

## P’tit *rant* sur la dette technique

La dette technique, parlons-en.

Un peu comme la dette financière, i.e. un levier pour créer plus de valeur. Ça me rappelle une conversation avec Georges à l'époque de Snipcart. Il disait toujours que repayer sa dette technique, c'est un luxe qui se mérite. Tu le mérites quand tu génères assez de capital—en revenu ou idéalement en profit—pour investir une partie de cet excédent dans le paiement de la dette.

Chez Snipcart justement, on avait souvent des devs (souvent plus juniors) qui riaient du code "broche à foin" de Charles Ouellet, notre co-fondateur technique.

"Du spaghetti!"

"Cette partie-là; impossible à maintenir."

"Ça me prend une heure ajouter une fonction..."

“Ton code est aussi laite que toi, Carl!”

D’abord, je riais abondamment avec eux, parce que rire de Charles, ça faisait partie de notre culture d’entreprise.

Mais une partie de moi se sentait toujours mal pour lui. Parce que ce code-là dont ils riaient? C'est grâce à ça qu’ils avaient une job. C'est ce qui nous avait permis de croître, d'attirer des clients, de construire quelque chose de valeur.

La dette en finances = levier pour construire plus de richesse, aller chercher plus de retours.

La dette en éducation = investissement pour aller chercher un diplôme qui va générer plus de valeur sur le marché (DÉPEND DES DIPLÔMES HEIN DR. TIMMY EN PHILO)

La dette technique, principe semblable.

*Check*, c’est hyper facile d'arriver dans une compagnie et de blaster le codebase.

Mais considère l'historique. Faut valoriser tout l'argent et la croissance que ce code-là, aussi vieux ou laid soit-il aujourd'hui, nous a permis d'obtenir comme compagnie.

Non, je n’excuse pas tout le vieux code sale. Évidemment qu'il y a des moments où faut investir dans la stack :

- Quand ça affecte négativement la vélocité de l'équipe

- Quand tu perds des devs talentueux à cause de ça

- Quand les coûts de maintenance deviennent prohibitifs

- Quand tu passes plus de temps à éteindre des feux qu'à construire

*Rant over*. Passons au plat principal 🪤

## Le piège en action

**Minute**, *pinging* Oli pour savoir si j’ai le droit d’utiliser leur exemple spécifique…

**Étape un**

T'as un dev en entrevue. Tu lui présentes une mise en situation simple :

Ajoute trois fonctions à ce fichier existant. Pas besoin d’écrire de code—juste identifier où tu placerais ces fonctions dans le fichier.

Là, la sauce épaissit :

- Certains partent un TED talk sur l’importance de mettre les fonctions les plus utilisées au top.

- D’autres argumentent pour la séparation entre fonctions privées vs publiques.

- D’autres suggèrent de les ajouter au bas du fichier pour pas bouger le reste.

- Et d’autres… hausse des épaules et proposent de suivre les standards déjà en place pour garder la navigation dans le codebase efficace 💫

💫 DING DING DING, **BIG WINNER**

La façon d'ordonner des fonctions dans un fichier est le genre de détail dont on devrait collectivement se câli**r. Pas là-dessus qu'on veut que le jus de cerveau de nos devs brûle.

**Étape deux**

*All right*, on a un *gauge* du niveau de zèle arbitraire du candidat.

Mais on continue. Et là, la sauce… pogne au fond de la casserole.

Peu importe ce que le candidat répond, l'interviewer **joue le rôle** du zélé technique. Exemple :

Okay mais écoute, chez nous, on ordonne *toujours* les fonctions alphabétiquement. C'est *crucial* pour retrouver rapidement son chemin dans le code. J'ai lu une étude ; ça réduit le temps de recherche de 11.29%.

Argumentaire bidon AKA l’appât. Piège tendu.

Là, certains candidats doublent la mise : "Non mais c'est complètement stupide comme approche, laisse-moi t'expliquer pourquoi ma méthode est objectivement supérieure..."

👇

D'autres virent diplomatiques : "Hmm, c'est une approche intéressante. Je ne suis pas convaincu que ce soit optimal, mais si c'est le standard de l'équipe, je vais m'aligner."

Sinon t'as les *people pleasers* : "OMG vous avez tellement raison! J'adore cette approche!"

(Un peu *weird*, mais on peut comprendre, pression de l'entrevue, etc.)

Ce test révèle deux trucs super importants :

1. Comment la personne gère la confrontation technique

2. Sa capacité à relativiser l'importance des détails vs le *big picture*

Vélocité > zèle. Y’a de ces collines qui ne méritent pas notre mort.

BTW, ce concept se transpose dans n'importe quel département. Product managers, marketeurs, etc.—tout le monde peut créer une mise en situation basée sur un détail trivial et voir comment le candidat réagit quand on en fait tout un plat.

Reste que c’est souvent en R&D que ça fait le plus mal, un zélé.

C’est plus ratoureux que machiavélique IMO. Ultimement, tout le monde gagne :

- La personne évite de se retrouver dans une culture qui la frustre

- L'entreprise évite des coûts d'embauche/formation pour quelqu'un qui sera un net négatif

- L'équipe garde son énergie et sa vélocité

Si on a un guerrier évangéliste d'une méthodologie ou d'une approche au code qui va trop prendre de bande-passante dans les discussions et ralentir l'équipe, cette personne-là sera malheureuse chez nous. Mieux d’aller dans un autre type de compagnie.

On rend service à tout le monde en déployant ce petit subterfuge.

Quelque chose à ajouter? *Good*. Laisse un commentaire ou réponds à ce courriel direct.

Cheers,

[Frank](https://www.linkedin.com/in/frankln/?utm_source=saaspasse.beehiiv.com&utm_medium=newsletter&utm_campaign=le-piege-a-dev-en-entrevue) 💜