What's up folks,

Merci d'être là. Je commence par mon édito—les nouvelles après. 🪶

> *ARRivederci, s*cker*

> 
> *ARRivederci, s*cker*

Je renouvelle mon hypothèque *live*.

(*Stay with me*)

Y’a deux ans, la banque donnait 1000$ pour ouvrir un compte chez eux. Classique tactique d’acquisition.

Et ça a marché!

Aujourd’hui, on a cartes, comptes, transferts auto, etc. Quelques irritants, mais on est “dans leur *building*” mettons.

Reste des **dizaines d’années et de milliers de dollars** à payer en intérêts sur l’hypothèque. On pense même prendre une marge pour rénos.

Au renouvellement, on reçoit :

→ appel d’un dude découragé + courriels corpo mal formatés + taux peu compétitifs

**…**

On a changé de banque et ils sauront jamais pourquoi.

**Cette information-là vaut ***f*cking*** cher**.

S’ils m’avaient offert un crédit de quelques piastres, un nanane… j’aurais pris le temps. Juste pour comprendre pourquoi on quittait. Ou même un *Hail Mary* pour nous ravoir.

En SaaS, on met aussi souvent plein de cash à acquérir des clients... puis zéro piastre à comprendre pourquoi ils quittent.

Voici donc comment comprendre (et réduire) ton churn avec *this one simple trick* 🤡

version VHS de l’édito dispo pour les SaaSpal supporters

## *Exit survey* chez Snipcart

Semaine passée, je jasais justement d’expérience client avec [Philippe Genois](https://www.linkedin.com/in/philippegenois/?utm_source=saaspasse.beehiiv.com&utm_medium=newsletter&utm_campaign=avant-de-partir-dis-moi) @InputKit.

Il m’expliquait sa stupéfaction en réalisant à quel point les PME n’investissaient pas en rétention vs acquisition. Je ne conterai pas son histoire ici; son épisode sort dans quelques semaines.

Mais ça m’a rappelé un truc simple qu’on faisait chez Snipcart — nos *exit surveys*.

Assez *straightforward*, i.e. un courriel envoyé automatiquement à tout le monde qui cancel.

Sujet : *Before you go! A monthly refund for your thoughts?* 💵

(hésite pas à remixer ce modèle)

Un petit remboursement mensuel en échange de quelques minutes de leur temps. Pas juste pour les retours—on voulait aussi finir sur une note positive, contrairement à ma banque.

On comprenait **pourquoi** ils partaient, mais aussi **où** ils allaient. Ça nous aidait à améliorer le produit et notre positionnement.

Mais surtout à ne pas jouer à l'autruche 𓅦

Cool bonus : à plusieurs reprises, ça a mené à de beaux échanges et témoignages positifs.

### La recette qu'on suivait

Notre *workflow* à l’époque :

1. Envoi courriel automatisé dans Sendgrid à chaque cancellation

2. *From* & *reply-to* à mon email Snipcart perso

3. [Règle](https://missiveapp.com/help/rules/overview?utm_source=saaspasse.beehiiv.com&utm_medium=newsletter&utm_campaign=avant-de-partir-dis-moi) dans Missive pour auto-label les réponses exit survey

4. Traitement par lots des remboursements via [intégration custom](https://missiveapp.com/integrations/iframe?utm_source=saaspasse.beehiiv.com&utm_medium=newsletter&utm_campaign=avant-de-partir-dis-moi) dans Missive (on avait un *side panel* UI avec liens vers derniers paiements Stripe du client)

5. Catégorisation dans Gsheet des raisons & détails du churn

6. Documentation des verbatims dans *stories* Pivotal Tracker (RIP)

Gsheet brouillon où on déposait l’info

Je copiais-collais les verbatims intéressants dans le Gsheet. J’incrémentais à la mitaine le churn des comptes / raisons du churn.

Quand j’étais PO (Product Owner) j’allais aussi copier-coller les verbatims pertinents dans les *stories* Pivotal associées.

C'était pas super sexy, mais ça marchait—les devs avaient le contexte client direct dans leur outil de travail.

Puis quand on faisait du *sprint planning* et *backlog* *grooming*, on gardait ce sheet-là pas loin pour supporter nos décisions de prioriser X > Y.

### Ce que je ferais de plus aujourd'hui

Si j’opérais encore chez Snip (avec [Mark](https://www.linkedin.com/in/markzalzal/?utm_source=saaspasse.beehiiv.com&utm_medium=newsletter&utm_campaign=avant-de-partir-dis-moi) pour m’épauler en BI), je piquerais ce Gsheet-là aux stéroïdes pour *cross-reference* tous les *churned user* IDs en fonction de :

- Taille business

- Industrie

- Stack techno

- Temps passé avec le support

- Fonctionnalités utilisées (ou pas)

But? Mieux informer l'équipe produit + marketing si on veut :

1. Moins d'une cible X

2. Mieux servir une cible Y

## Apprentissages, mais surtout actions

Un *exit survey*, c'est comme l'inverse d'une étude de cas. Au lieu de comprendre pourquoi ils restent, tu piges pourquoi ils partent. Mais tu le publies pas sur ton site marketing 😂

Pour que ça vaille la peine, faut **faire** quelque chose avec l’info collectée.

Quelques *moves* qui ont marché pour nous :

1. **Étudie ton compétiteur de A à Z**

→ Chez qui le monde s’en vont?

- Scan le web pour commentaires client sur ce compétiteur (reviews, témoignages, forums, etc.)

- Parle à des clients qui utilisent ce compétiteur

- Identifie tous les points forts+faibles que t’as pas

- Rédige des pages de comparaison et du matériel pour les ventes en conséquence

(Drette ça qu'on faisait pour positionner Duda eComm vs Shopify)

1. **Identifie tes clients "red flag"**

En partant de tes métriques SaaS + metadata utilisateurs + tes réponses de exit surveys, tu veux *reverse engineer* ton marketing pour ne plus les attirer.

(Métrique SaaS 🚩 : high churn, low ARPU, high support, low NPS, etc.)

(Metadata utilisateurs : industrie, rôle, taille d’entreprise, stack, nb. d’utilisateurs, etc.)

→ À quel canal d’acquisition sont-ils attribuables?

→ À quelle campagne, événement, pièce de contenu spécifique?

→ Est-ce que d’autres clients “green flag” viennent des mêmes sources? Non?

Arrête ces efforts marketing et mesure l'impact. Prends les dollars sauvés et *target* les clients payants.

1. **Priorise les profils à risque**

- Déploie des règles de support spéciales pour clients *high value*

- Interviens *avant* le churn

- Fais pas juste leur envoyer une template courriel — écris, appelle, déplace-toi.

1. **Construis des presque-solutions**

Les réponses à tes questionnaires de sortie (fallait bien je l’essaye en français une fois) parlent sans cesse de fonctionnalités et d’intégrations?

Considère les **presque-solutions**.

Le genre de demi-fonctionnalité pas trop chèrante à livrer, qui s’appuie souvent sur d’autres produits/solutions. Parfois sur de bonnes vieilles intégrations avec de la “colle” techno, i.e. les APIs ou Zapier de ce monde.

Chez Snip, les utilisateurs voulaient TOUT LE TEMPS de nouvelles passerelles de paiement. Dans la catégorie de churn “fonctionnalité manquante”, c’était la raison la plus populaire.

On n’avait pas la bande passante pour développer et maintenir des douzaines d’intégrations de la sorte. Donc notre presque-solution : [custom payment gateways](https://docs.snipcart.com/v3/custom-payment-gateway?utm_source=saaspasse.beehiiv.com&utm_medium=newsletter&utm_campaign=avant-de-partir-dis-moi).

Pas mal de taponnage à configurer, *sure*. Mais quand le problème fesse assez fort, le monde se tape un peu de friction pour le régler. Surtout s’ils adorent le reste du produit.

## *Flows* modernes?

Aujourd’hui, y’a un paquet de manières de suivre le **pourquoi** de ton churn.

Je regardais InputKit vite vite. Phil et son équipe ont construit quelque chose *next level* comparé à notre setup DIY chez Snip. Je sais qu’il le *dogfood* pour son propre produit, donc doit y’avoir quelque chose là. Juste valider si ça fit pour tes besoins SaaS.

mes comptables du Chiffre utilisent ça pour voir si je vais churn (I won’t)

Sinon t'as plein d’options toutes plus fancy les unes que les autres. Qui font tout ça en une seule plateforme ou *whatever*. Google ou ChatGPT ça. Sinon laisse un commentaire!

Si j’étais solo ou en démarrage, j’essaierais un p’tit setup no/low-code avec genre :

→ Stripe Automations + Zapier/Make | webhooks + Gsheet/Airtable

[minute je ping [Douville](https://www.linkedin.com/in/francoisdouville/?utm_source=saaspasse.beehiiv.com&utm_medium=newsletter&utm_campaign=avant-de-partir-dis-moi), mon no-code expert d’Apollo13 par excellence…
…il fait dire que la majorité du *use case* pourrait être géré dans un outil comme [Fillout](https://www.fillout.com/workflows?utm_source=saaspasse.beehiiv.com&utm_medium=newsletter&utm_campaign=avant-de-partir-dis-moi) 🤷‍♂️]

J'essaierais peut-être aussi d’ajouter un court Loom amical dans mon exit survey? Pas sûr.

## Carottes

Si t’es cassé raide, **peut-être** que tu peux déployer ces questionnaires sans nanane.

Mais la carotte, même si mini, prouve que tu valorises les retours. Ça aligne les incitatifs.

Si t’es pas cassé pantoute, tu peux donner le nanane dès le départ, même sans garantie de réponse. Ça augmente tes changes d’engager le [principe de réciprocité](https://www.nngroup.com/articles/reciprocity-principle/?utm_source=saaspasse.beehiiv.com&utm_medium=newsletter&utm_campaign=avant-de-partir-dis-moi).

**→ Donc quel nanane offrir pour recevoir du feedback honnête?**

Carottes testées et approuvées, en ordre de préférence personnelle :

- Remboursement

  - utilisateur n’a rien à faire + reçoit du vrai $

- Tombola ou concours

  - double-valeur, projet marketing en même temps.

- Don à une cause

  - peut être trèèès cool en fonction de ton ICP.

- Accès premium ou ressources exclusives

  - quand t’as juste du temps & de l’expertise à offrir.

- Réduction sur les plans

  - s’ils reviennent… mais dé-valorise ton produit IMO.

- Cartes-cadeaux

  - très B2C, très plate, meh, marche p-ê I guess.

- Appel avec l'équipe

  - si vous êtes game de prendre le feedback live. scale pas.

**Pro-tip**: fesse pendant que le fer est chaud. N’attends pas trois mois post-churn pour envoyer le questionnaire. Comme ma banque qui m'appelle maintenant que je suis pas client—*too little, too late* mes p’tits chums.

## La danse du produit

Tu vas en recevoir, mais capote pas avec tout le feedback négatif.

Garde ton équilibre pis continue de valser, *buddy*.

Les clients qui partent ont une raison, pis c'est correct. Des fois t'as *f*ck up*, tu planifies un fix, tu continues d’avancer. D'autres fois, t'as juste pas attiré la bonne cible.

Rappelle-toi: le monde mécontent dramatisent souvent plus que le monde content.

Faut pas rusher pour tout fixer ce qui *pop* dans les questionnaires—*be smart about what to build.*

([check ça](https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/b7e93ed3-b67c-4258-a7c8-795f20459e93/image.png?t=1726532501&utm_source=saaspasse.beehiiv.com&utm_medium=newsletter&utm_campaign=avant-de-partir-dis-moi), tiré d’[un édito précédent](https://saaspasse.beehiiv.com/p/ca-fait-pas-assez-mal?utm_source=saaspasse.beehiiv.com&utm_medium=newsletter&utm_campaign=avant-de-partir-dis-moi&last_resource_guid=Post%3A50476d14-3eb1-4096-b139-18952a024e30))

Quelque chose à ajouter? *Good*. Laisse un commentaire ou réponds à ce courriel direct.

Cheers,

[Frank](https://www.linkedin.com/in/frankln/?utm_source=saaspasse.beehiiv.com&utm_medium=newsletter&utm_campaign=avant-de-partir-dis-moi) 💜