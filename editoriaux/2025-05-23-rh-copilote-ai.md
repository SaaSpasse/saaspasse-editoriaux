What's up folks,

Merci d'être là. L’édito d’abord—les nouvelles après.

Inscris-moi au championnat de contorsionnisme…

Je viens de m’extirper d’un Catch-22 classique de startup!

→ **T'as besoin d'embaucher parce que t'as trop de job, mais t'as pas le temps d'embaucher... parce que t'as trop de job** 🤸‍♂️

(*That’s right*, on a trouvé notre [Pieuvre](https://www.notion.so/saaspasse/SaaSpasse-sur-ton-CV-1cd5c10632bb80b4b868eac3ade07dfe?utm_source=saaspasse.beehiiv.com&utm_medium=newsletter&utm_campaign=rh-co-pilote-ai)!)

Énergie plus limitée ces temps-ci—j’avais deux options :

1. Remettre l'embauche à plus tard (drainer ma pile déjà orange foncée)

2. Trouver une façon de faire qui ne me grille pas le cerveau ou l’horaire

J'ai opté pour l'option 2. *No joke*, sans l'AI, j'aurais probablement craqué.

Cette semaine, je te raconte comment l'AI est devenue ma co-pilote lors de la dernière embauche chez SaaSpasse, de la création du test technique jusqu'à l*'onboarding* interactif.

Outils utilisés = ChatGPT o3, Superwhisper, Notion AI, Manus

Je te partage le plus de prompts et exemples possibles. En bonus, le site web interactif d’*onboarding* construit avec Manus.

**À la fin de l’édito, je partage des nananes réservées aux ****SaaSpals**** **🍬

→ **Notion** : Le test de la pieuvre

→ **Manus** : *full replay & prompts*

→ **Manus** : codes d’invitation

### Conception du test technique

Chaque fois que j’entre en recrutement, je me dis :

Ai-je **vraiment** besoin d’un test technique pour cette embauche? J’ai embauché 30+ personnes dans ma vie, j’ai 35 ans, je suis quand même un bon juge de caractère…

Et chaque fois que je *close* une embauche :

**Une foutue chance** que j’ai fait passer un test technique à tout le monde.

Ne jamais prendre une décision **juste** sur la *vibe* de la personne. **Inclure** ton *feeling*, ton intuition, *sure*. Mais pas juste ça. C’est encore plus crève-coeur renvoyer quelqu’un de super smath qui n’avait finalement pas les compétences pour le rôle.

Voici donc comment j’ai développé un test technique simple pour notre rôle de Pieuvre.

J’ai utilisé un export Notion de [l’offre d’emploi](https://www.notion.so/saaspasse/SaaSpasse-sur-ton-CV-1cd5c10632bb80b4b868eac3ade07dfe?utm_source=saaspasse.beehiiv.com&utm_medium=newsletter&utm_campaign=rh-co-pilote-ai) comme point de départ.

Ensuite, le prompt que j'ai utilisé dans ChatGPT o3 :

J'ai dicté ça via [Superwhisper](https://saaspasse.beehiiv.com/p/super-murmure?utm_source=saaspasse.beehiiv.com&utm_medium=newsletter&utm_campaign=rh-co-pilote-ai&last_resource_guid=Post%3Abeefaa2a-0287-4496-8018-022f760493d5) au lieu de taper. Dépendant du cas, je *switch* entre ‘Voice mode’ ou ‘Superwhisper + minimum clavier’. Économie d'énergie massive quand t’as le cerveau déjà fragile. Et accélération des interactions.

Tu ne **vois** pas ce que ChatGPT *output* **pendant** une convo Voice (URLs, tableaux, images, etc.). Mais tout est transcrit et dispo *in-chat* quand tu quittes Voice. Facile d’ensuite copier-coller et reformatter dans un autre *thread*.

Y’a sûrement un truc plus cool ou efficace, mais j’utilise [cette extension Chrome](https://chromewebstore.google.com/detail/ChatGPT%20to%20PDF%20by%20PDFCrowd/ccjfggejcoobknjolglgmfhoeneafhhm?utm_source=saaspasse.beehiiv.com&utm_medium=newsletter&utm_campaign=rh-co-pilote-ai) pour de beaux exports PDF de mes convos. Je les *reupload* souvent dans d’autres *threads* pour bootstrapper du contexte.

ChatGPT m'a suggéré quelques tests. On a *jam* dix minutes, et décidé d’y aller avec une mise en situation réelle : plonger les candidats dans des scénarios courriels typiques de SaaSpasse. Prioriser, déléguer, répondre sans fautes avec le bon ton, identifier les urgences, taguer.

### Création d'un environnement de test réaliste

J’aime tester dans l'outil exact où la personne va travailler quotidiennement.

Missive est puissant mais des fois complexe à configurer. J'ai passé [leur doc](https://learn.missiveapp.com/?utm_source=saaspasse.beehiiv.com&utm_medium=newsletter&utm_campaign=rh-co-pilote-ai) à ChatGPT + utilisé la fonction recherche pour m'aider à **configurer l'environnement de test** :

- Créer des équipes isolées dans Missive (*sandbox* hermétiques)

- Configurer des alias emails dans Google Admin

  - pieuvre-rouge@saaspasse.com

  - pieuvre-jaune@saaspasse.com

  - et ainsi de suite!

- S'assurer que les candidats n'aient accès à rien d'autre que l’équipe et l’alias

### Génération des scénarios

J’ai dépoussiéré mon vieux [wazabimonster@gmail.com](mailto:wazabimonster@gmail.com), histoire d’envoyer les courriels fictifs aux boîtes partagées Missive.

J’ai ensuite *upload* la [base de données Notion des tâches chez SaaSpasse](https://saaspasse.beehiiv.com/p/cartographier-le-chaos?utm_source=saaspasse.beehiiv.com&utm_medium=newsletter&utm_campaign=rh-co-pilote-ai&last_resource_guid=Post%3Abeefaa2a-0287-4496-8018-022f760493d5) dans ChatGPT. *Overkill* mais plus détaillé que la description de tâches dans l’offre. On a discuté brièvement pour s’entendre sur les cas à traiter dans ce test.

Prompt utilisé après coup pour générer les faux emails :

**Résultat** : cinq emails tellement crédibles que même Joëlle a cru qu'ils étaient réels quand elle les a vus. En même temps, elle a aussi cru au Père Noël jusqu’à genre quinze ans à ce qui paraît. Les *spoilers* arrivaient moins vite en Gaspésie faut croire.

Ensuite, l’AI et moi on a structuré le **format du test** :

- 2 heures dédiées

- Candidat invité dans l'équipe Missive

- Page Notion remplie d’instructions et de ressources

- Joëlle et moi dispo dans Missive (comme dans la vraie vie)

- Rémunération du temps passé (important pour moi)

Après avoir designé le test avec ChatGPT, ça a été un jeu d’enfant de lui faire générer le contenu pour le Notion :

Assez fier du réalisme du test. Fidèle à mes habitudes, j’ai caché quelques oeufs de Pâques et pièges dans certains courriels :

### Optimisation du plan d'onboarding

Une fois La Pieuvre choisie, direction l'*onboarding*. Mais repartir d'une page blanche? *Hell no*.

*Workflow* :

1. **Upload du plan existant** : j'ai pris le plan d'onboarding de Joëlle (rédigé il y a un an) et l'ai uploadé dans ChatGPT.

2. **Prompt d'adaptation** :

1. **Export et personnalisation** : ChatGPT m'a pondu une structure solide que j'ai ensuite affinée manuellement dans Notion.

**Dans ma réalité actuelle***,*** **l'AI excelle pour dissiper le brouillard cognitif ou émotif avant un projet : “ouf, je sais même pas par où commencer” ou “ouf, j’ai peur du résultat de telle décision”.

Il me donne souvent un doux coup de pied au cul initial. L'humain prend le relais pour les nuances, détails, priorités. Ici, j'ai gardé 80% de ce que ChatGPT a proposé, mais les 20% que j'ai modifiés étaient cruciaux.

J’ai hâte d’expérimenter pour vrai avec des automations de *workflows* plus complètes. À date, j’utilise plus l’AI comme un employé que je gère à quelques reprises dans la journée, i.e. *check-in* et *feedbacks* fréquents.

### Création d'un onboarding ‘interactif’

Tu sais le monde qui rénove pis se ramasse avec un château à force de dire “tant qu’à y’être…”?

Crime, je suis un peu de même quand je joue avec ces outils-là :

*What if* on rendait l'onboarding plus engageant qu'un document Notion statique?

**→ Enter **[Manus](https://manus.im/?utm_source=saaspasse.beehiiv.com&utm_medium=newsletter&utm_campaign=rh-co-pilote-ai) : agent IA généraliste capable de générer des sites web, apps, visualisations.

**Ma démarche** :

1. **Préparation du prompt** avec ChatGPT :

1. **Génération avec Manus** : le prompt optimisé a produit un microsite avec :

   - Checklist d'onboarding interactive

   - Fichier .ics auto-généré (importe événements direct dans ton cal)

   - Design aux couleurs SaaSpasse

   - Sections dépliables par semaine

2. **Boucle feedback vocale** (mon moment préféré) :

   - Je regarde le site généré par Manus

   - Je dicte mes commentaires à SuperWhisper

   - SuperWhisper formate et colle dans le chat Manus

   - Manus itère automatiquement

   - Rince et répète

**Résultat** : cycles d'amélioration ultra-rapides sans toucher au clavier.

Pas parfait mais gênant comme site *custom* d’accueil :

[ Onboarding La Pieuvre | SaaSpasse pxzgirjd.manus.space](https://pxzgirjd.manus.space/?utm_source=saaspasse.beehiiv.com&utm_medium=newsletter&utm_campaign=rh-co-pilote-ai)

pxzgirjd.manus.space

### Enseignements et limites

**Ce qui marche** :

1. **L'AI comme catalyseur** : elle défriche, l'humain tranche. Parfait pour contourner la page blanche ou la paralysie décisionnelle.

2. **Voice-to-text = game changer** : quand tu as des limitations cognitives temporaires, dicter plutôt que taper change tout. Même sans ça… tu vas juste plus vite.

3. **Tester dans l'environnement réel** : évaluer dans l'outil quotidien (Missive) révèle les vraies compétences, pas les théoriques.

**Ce qui marche moins** :

1. **Automatisations prématurées** : j'aurais pu automatiser les invitations calendrier et l'envoi d'emails avec Lindy/Gumloop, mais pour 5 candidats... *overkill*.

2. **L'AI ne remplace pas le jugement** : elle accélère la logistique, mais les décisions importantes restent humaines.

3. **La personnalisation a ses limites** : le site Manus était cool, mais j'ai quand même dû peaufiner manuellement plusieurs éléments.

### Pistes futures

L'AI n'a pas révolutionné notre processus d'embauche. Elle l'a rendu soutenable dans un contexte où mon énergie était limitée.

**Le vrai ***unlock* : utiliser l'AI pour préserver ton énergie mentale pour les décisions qui comptent vraiment. Déléguer la poutine, garder la stratégie.

Avec un volume d'embauche plus grand, j'automatiserais :

- **Scoring initial automatique** : faire analyser les réponses Missive par l'AI pour un premier tri

- **Workflow n8n/Gumloop/Lindy complet** : setup test en un clic (création comptes, envoi scenarios, invitations)

- **Mesure du ROI temps** : quantifier précisément le temps économisé vs processus 100% manuel

**Pour l'instant**, on profite d'avoir trouvé La Pieuvre et on pousse en avant.

👋

*si tu vois la prochaine section ***Bonus pour les SaaSpals **🍬*, c’est parce que t’es un.e *[SaaSpal supporter](https://saaspasse.beehiiv.com/c/saaspals?utm_source=saaspasse.beehiiv.com&utm_medium=newsletter&utm_campaign=rh-co-pilote-ai&last_resource_guid=Post%3Abeefaa2a-0287-4496-8018-022f760493d5)* — ***MERCI***. j’espère que les extra goodies te plairont!*

*si tu la vois pas et que tu veux la voir, *[check out l’abonnement](https://saaspasse.beehiiv.com/upgrade?utm_source=saaspasse.beehiiv.com&utm_medium=newsletter&utm_campaign=rh-co-pilote-ai&last_resource_guid=Post%3Abeefaa2a-0287-4496-8018-022f760493d5)*.*

bobye!

### Bonus pour les SaaSpals 🍬

- **Notion** : [Le test de la pieuvre](https://saaspasse.notion.site/Le-test-de-la-pieuvre-1eb5c10632bb80e3bdeaf39cde698524?utm_source=saaspasse.beehiiv.com&utm_medium=newsletter&utm_campaign=rh-co-pilote-ai)

- **Manus** : *full replay & prompts* — pas toujours chic, mais peut être utile

- **Manus** : codes d’invitation — ça nous donne plus de crédits aux deux

  - Réponds avec ‘Manus SaaSpal’ à ce courriel. J’envoie mes 4 aux premiers.

—

Quelque chose à ajouter? *Good*. Laisse un commentaire ou réponds à ce courriel direct.

Cheers,

[Frank](https://www.linkedin.com/in/frankln/?utm_source=saaspasse.beehiiv.com&utm_medium=newsletter&utm_campaign=rh-co-pilote-ai) 💜