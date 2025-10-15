What's up folks,

Merci d'être là. L’édito d’abord—les nouvelles après.

Déjà manuellement nettoyé une liste de prospects?

Pas le genre de tâche qui te fait tomber en amour avec la tech.

Titres de job pas standardisés, noms de domaine qui matchent pas, profils LinkedIn introuvables. Le genre de *grind* plate qui te fait questionner si t'aurais pas dû étudier en philo finalement.

Dans cet édito, je te raconte la fois où Bruno Marchand (GoodBytes Studio) m'a montré comment automatiser ce genre de tâche GTM.

Tout ça en quelques minutes avec Manus AI et Clay. De la collecte jusqu'à l'outreach, scoring ICP inclus.

**Y'a un enregistrement et ***screen-sharing*** de notre session dispo pour les SaaSpals plus bas!**

Allons-y.

**GTM en 2025, c'est quoi au juste?**

Le go-to-market couvre tout ce qui entoure la mise en marché : ciblage client, messaging, canaux d'acquisition, parfois prix et packaging. Mais aujourd'hui, y'a une grosse portion qui devient de l'ingénierie de systèmes. Des playbooks éprouvés, des étapes à pas sauter — sinon tu accumules de la dette GTM.

Bruno cite[ Winning by Design](https://winningbydesign.com/?utm_source=saaspasse.beehiiv.com&utm_medium=newsletter&utm_campaign=une-bouchee-d-argile) pour la science de la vente et l'alignement sales-marketing.[ Vasco](https://vasco.app/?utm_source=saaspasse.beehiiv.com&utm_medium=newsletter&utm_campaign=une-bouchee-d-argile) aussi pour leur approche scientifique aux opérations de revenus. Le GTM, c’est pas juste de la créativité… c'est des processus répétables.

[Clay](https://www.clay.com/?utm_source=saaspasse.beehiiv.com&utm_medium=newsletter&utm_campaign=une-bouchee-d-argile), c'est devenu son outil d'ingénierie GTM par excellence.

**Avant l'AI : comment on se crinquait ça?**

Pour te donner un exemple concret : disons qu’on cherche à identifier des compagnies pertinentes pour publier des offres sur le job board SaaSpasse. Donc des boîtes tech/SaaS en croissance, qui embauchent activement.

Mettons que t'avais une liste de 200 noms. Fallait :

- Standardiser les titres de job manuellement

- Trouver les noms de domaine un par un

- Scraper les profils LinkedIn

- Valider les infos de taille d'entreprise

- Cross-référencer entre différents outils de prospection

- Chercher les signaux de *hiring* (offres d'emploi actives sur leur site, LinkedIn Jobs, etc.)

Tu confiais ça à un stagiaire ou un junior qui passait des jours là-dessus. Armé de magie Excel douteuse et de formules qui pétaient à la moindre secousse. Pis y'avait toujours des erreurs pareil.

Aujourd'hui? Des agents AI font ça en minutes. L'humain garde la pondération et les décisions stratégiques — l'AI fait le *grunt work*.

C'est exactement pour ça que Clay est devenu incontournable.

**Clay = l'outil d'ingénierie GTM**

Bruno le décrit comme un *blank canvas* pour GTM. C'est des tables style spreadsheet, mais avec des enrichissements, des agents, un séquenceur intégré pour email et LinkedIn... et plus encore. *Basically*, Excel pluggé sur l’Internet et l’AI.

Tu peux créer des audiences, valider des listes, générer des signaux de qualification, agréger plusieurs *data providers*, scorer selon ton ICP. Tout ça dans une seule plateforme. Et "gestion des leads” = juste UN cas d’utilisation parmi une foule d’autres.

Mais c'est intimidant* *en sacrifice si tu débarques sans plan. D'où l'importance d'arriver avec ton cadre ICP bien défini avant d'ouvrir Clay pour travailler des leads.

Disclaimer : Clay peut halluciner des fois. L'AI derrière est pas 100% déterministe, c'est un outil probabiliste. Traite-le comme un employé. Donne-lui du contexte, montre-lui des exemples, sois patient. LLM-based AI 101.

**Le workflow complet — use case SaaSpasse**

Donc, on part avec notre objectif : identifier des compagnies susceptibles de publier/booster des offres sur le [job board](https://www.saaspasse.com/emplois?utm_source=saaspasse.beehiiv.com&utm_medium=newsletter&utm_campaign=une-bouchee-d-argile) SaaSpasse.

**Étape 1 : cadrer l'ICP (Ideal Customer Profile)**

Avant d'ouvrir[ Clay](https://www.clay.com/?utm_source=saaspasse.beehiiv.com&utm_medium=newsletter&utm_campaign=une-bouchee-d-argile), on définit notre [ICP](https://www.saaspasse.com/glossaire/icp-ideal-customer-profile?utm_source=saaspasse.beehiiv.com&utm_medium=newsletter&utm_campaign=une-bouchee-d-argile) sur un[ FigJam](https://www.figma.com/figjam/?utm_source=saaspasse.beehiiv.com&utm_medium=newsletter&utm_campaign=une-bouchee-d-argile) :

- Firmographique : industrie (SaaS/tech), taille (10-200 employés), siège (Québec/Canada), langue (fr/en), stade (croissance, embauche active)

- Technographique : rien de spécifique pour ce cas-ci, mais parfois l’info est un must-have (utilisation d’un CRM, ERP, d’une stack XYZ, etc.)

- *Buyer personas* : founders/CEO pour petites boîtes, Head of People/Talent/HR pour plus grosses

- Signaux : *hiring* actif (page carrière, LinkedIn Jobs, Indeed), levées de fonds (Crunchbase), traction visible

**Étape 2 : collecte avec Manus AI**

On part de la page publique des[ SaaSpals](https://saaspasse.beehiiv.com/c/saaspals?utm_source=saaspasse.beehiiv.com&utm_medium=newsletter&utm_campaign=une-bouchee-d-argile) (supporters payants de SaaSpasse donc bon signal d’affinité).[ Manus AI](https://manus.im/?utm_source=saaspasse.beehiiv.com&utm_medium=newsletter&utm_campaign=une-bouchee-d-argile), un agent généraliste, standardise la liste : nom complet, titre, entreprise, domaine, profil LinkedIn, site web. On exporte en CSV. Ça devient notre source de données initiale.

**Étape 3 : enrichissement et scoring dans Clay**

Dans [Sculptor](https://www.clay.com/sculptor?utm_source=saaspasse.beehiiv.com&utm_medium=newsletter&utm_campaign=une-bouchee-d-argile)—le copilote AI dans le UI de Clay—on décrit notre scoring d’ICP. Ça peut aider de formater ça en JSON à l’aide d’un ChatGPT ou autre.

Sculptor génère la logique de scoring (0-100), le feature mapping (quels outils utiliser dans Clay), et les agents à configurer.

On privilégie un agent recherche web : [Claygent](https://www.clay.com/claygent?utm_source=saaspasse.beehiiv.com&utm_medium=newsletter&utm_campaign=une-bouchee-d-argile) ou clé d’API perso Claude/Gemini pour réduire les coûts. C’est lui qui va chercher les *data points* manquants : taille, points de contact clé, financement récent, embauche active, etc.

Bonne pratique de Bruno : tester sur 10 lignes avant de scaler. Les agents coûtent des crédits, donc on valide l'approche avant de faire rouler 500 lignes.

**Étape 4 : ***gut check*** des résultats**

Les scores élevés (80-95) matchent souvent l'intuition terrain. Bruno me montre[ Kimoby](https://www.kimoby.com/?utm_source=saaspasse.beehiiv.com&utm_medium=newsletter&utm_campaign=une-bouchee-d-argile) en exemple, qui score 95 — ça fait du sens, c'est clairement un fit. Ils ont déjà acheté une job du mois dans le passé. On peut aussi inspecter le raisonnement de Clay : sources consultées (LinkedIn, Crunchbase, ZoomInfo, sites officiels), hypothèses sur taille et hiring.

Si tu veux plus de rigueur, tu peux fixer les sources attendues dans ton prompt (ex : LinkedIn Jobs, Indeed, page carrière officielle).

**Étape 5 : étendre le volume**

On prend les prospects > 80 et on lance [find company lookalike](https://www.clay.com/university/lesson/find-your-next-customer-with-company-lookalikes?utm_source=saaspasse.beehiiv.com&utm_medium=newsletter&utm_campaign=une-bouchee-d-argile) (database interne de Clay). Ça génère rapidement un groupe de compagnies similaires à nos leads initiaux.

**Étape 6 : préparer l'outreach**

On exécute [find email](https://www.clay.com/tools/email-finder?utm_source=saaspasse.beehiiv.com&utm_medium=newsletter&utm_campaign=une-bouchee-d-argile) pour compléter les points de contacts. Mais ici pour SaaSpasse, Bruno recommande de privilégier des  LinkedIn DM personnalisés. Inventaire limité, clients à proximité, ticket moyen plus élevé — mieux vaut un outreach léger et ciblé.

Le outreach [sequencer](https://www.clay.com/sequencer?utm_source=saaspasse.beehiiv.com&utm_medium=newsletter&utm_campaign=une-bouchee-d-argile) (email/LinkedIn) est intégré dans Clay. Utile pour les campagnes ciblées, mais faut pas spammer.

Boom, une liste de leads qualifiée, enrichie, priorisée, et même prête à être contactée. Je sais pas combien ça vaut en salaire de BDR/SDR tout ça, mais c’est une couple de bidous certains.

**Quelques pro-tips de Bruno**

Avant d'ouvrir Clay, schématise ton ICP comme du monde. Mets une pondération sur les traits les plus importants. Définis quelques exclusions—caractéristiques que tu ne veux pas chez un lead. Ça va te sauver des heures.

Utilise Sculptor pour sauver du temps et manipuler Clay plus rapidement.

Test tes actions et agents avant de scaler. Privilégie tes API keys perso (Claude, Gemini) pour réduire les coûts.

Commence niche. Personas clairs, 50-100 comptes de ta BD / ton CRM ou d’une source sûre. Vise la qualité avant le volume. Ensuite, étends par *lookalikes*.

Utilise des JSON *mappings* dans tes prompts pour donner au modèle une structure claire. Moins d'inférence, plus de constance dans les résultats.

**Ressources pour creuser**

- [GoodBytes Studio](http://goodbytes.ca?utm_source=saaspasse.beehiiv.com&utm_medium=newsletter&utm_campaign=une-bouchee-d-argile)

- [Clay](https://www.clay.com/?utm_source=saaspasse.beehiiv.com&utm_medium=newsletter&utm_campaign=une-bouchee-d-argile)

- [Manus AI](https://manus.im/app?utm_source=saaspasse.beehiiv.com&utm_medium=newsletter&utm_campaign=une-bouchee-d-argile)

- SaaSpasse [Job board](https://www.saaspasse.com/emplois?utm_source=saaspasse.beehiiv.com&utm_medium=newsletter&utm_campaign=une-bouchee-d-argile) (encore gratuit pour l’instant!)

- Bruno Marchand [sur LinkedIn](https://www.linkedin.com/in/bruno-marchand-63524728/?utm_source=saaspasse.beehiiv.com&utm_medium=newsletter&utm_campaign=une-bouchee-d-argile)

### 🎥 Gérer ses leads avec Clay (GTM ft. Bruno, GoodBytes)

Section réservée à [nos SaaSpals](https://saaspasse.beehiiv.com/c/saaspals?utm_source=saaspasse.beehiiv.com&utm_medium=newsletter&utm_campaign=une-bouchee-d-argile)! Contient vidéo complète de ma session avec [Bruno](https://www.linkedin.com/in/bruno-marchand-63524728/?utm_source=saaspasse.beehiiv.com&utm_medium=newsletter&utm_campaign=une-bouchee-d-argile), incluant partage d’écran du *workflow* Clay.

On offre notre contenu premium—sessions pratiques non-dispo sur le pod—en primeur aux SaaSpals. Le reste de l’audience aura accès plus tard.

Si tu vois ce qui suit, **merci pour le support** 🫶
Si tu veux voir ce qui suit, [supporte directement SaaSpasse](https://saaspasse.beehiiv.com/upgrade?utm_source=saaspasse.beehiiv.com&utm_medium=newsletter&utm_campaign=une-bouchee-d-argile). La vidéo sera dispo en rappel semaine prochaine pour les SaaSpals.

### *So what now?*

Complètement débile les possibilités avec un outil comme Clay.

Si tu veux te mouiller, teste donc le *workflow* cette semaine. Prends une petite liste de 20-30 prospects, passe-la dans Manus pour l’enrichir au besoin, score-la + agrandit-la dans Clay. Chronomètre combien de temps ça te prend versus ton approche actuelle.

Pis envoie-nous tes résultats en *reply*. Sérieux. Je veux savoir si t'as réussi à sauver du temps, ou si t'as juste brûlé des crédits Clay pour rien. Si tu veux un coup de main, poke Bruno!

Sinon ben partage ça à un.e founder ou marketer qui *grind* encore sa prospection à la mitaine. Ils vont te remercier!

—

Quelque chose à ajouter? *Good*. Laisse un commentaire ou réponds à ce courriel direct.

Cheers,

[Frank](https://www.linkedin.com/in/frankln/?utm_source=saaspasse.beehiiv.com&utm_medium=newsletter&utm_campaign=une-bouchee-d-argile) 💜