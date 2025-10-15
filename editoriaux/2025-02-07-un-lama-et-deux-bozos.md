What's up folks,

Merci d'être là. L’édito d’abord—les nouvelles après.

C’est la première fois de ma vie qu’une démo fonctionne du premier coup!

On venait de faire rouler Llama 3.2. Rendu à tester DeepSeek-R1, quand mi-*prompt…*

**___full laptop crash___**

Coincidence? JE NE CROIS PAS, CCP!

Bref, Douville d’[Apollo13](https://www.saaspasse.com/partenaires/apollo13?utm_source=saaspasse.beehiiv.com&utm_medium=newsletter&utm_campaign=un-lama-et-deux-bozos) m’a appris à rouler des modèles d’AI aux milliards de paramètres direct sur ma machine. Dans un UI très utilisateur-amical. **Pour 0 piastre**.

Bonus : ta data reste sur ton ordi. Même pas besoin d’être connecté sur le Ternet.

Tsé, les abonnements à ChatGPT, Claude, Perplexity, etc., s’accumulent. Et ils t’imposent souvent des limites d’utilisation. Ce qui aggrave **immédiatement** la situation déjà **super éprouvante** d’être un *tech worker* en Occident sur son laptop (avec latté).

Peut-être es-tu dans la position du founder avec exit récent qui m’a dit :

Le truc pour les limites d'utilisation, c'est **trois** comptes Claude pro payants.

Mais si t’es comme moi, tu comptes tes cents sans dépenser sur des folies comme un abonnement annuel à Midjourney pour faire trois images par année (je mens, je l’ai fait).

Sans coder ni dépenser un dollar, tu peux* *rouler un “ChatGPT” sur ton laptop. Voici comment, vidéo en bonus 👇

### Pourquoi rouler un LLM sur ta machine direct?

Il fait f**king frette ces temps-ci, donc je commencerai par citer [Vincent Bernard](https://www.saaspasse.com/episode/episode-66-vincent-bernard-balade-genai-a-dos-de-licorne?utm_source=saaspasse.beehiiv.com&utm_medium=newsletter&utm_campaign=un-lama-et-deux-bozos), directeur R&D chez Coveo :

Blague à part, ça peut te manger de la RAM pas mal ça de l’air. Donc si t’es encore en train d’user ton vieux Macbook à l’os, *well*… lis une des autres éditions de l’infolettre—sont toutes bonnes.

OU procure-toi un nouveau Macbook via [notre partenariat SaaSpasse x Apple](https://www.youtube.com/watch?v=dQw4w9WgXcQ&utm_source=saaspasse.beehiiv.com&utm_medium=newsletter&utm_campaign=un-lama-et-deux-bozos)*.
*dis-moi que t’as pas cliqué pour vrai?

Y’a quand même de cool avantages IMO :

- Confidentialité VIP : ta data reste chez vous, zéro leak possible
sauf si t’es du genre à pas verrouiller ton écran

- Mode avion-*friendly* : pas besoin d'Internet pour que ça roule

- Coût nul : une petite victoire dans l’éternelle guerre contre les abonnements $

- Rapidité : pas de latence réseau ni de files d'attente

- Full contrôle : possibilité de customiser selon tes besoins

### C’est quoi Ollama?

[Ollama](https://ollama.com/?utm_source=saaspasse.beehiiv.com&utm_medium=newsletter&utm_campaign=un-lama-et-deux-bozos) c'est comme ton gestionnaire de modèles AI local. Un peu comme Spotify pour des LLMs (Large Language Models). Tu télécharges l'app, puis t'as accès à un catalogue de modèles open source prêts à rouler sur ta machine.

#### Quels modèles sont dispo?

Une sélection pas piquée des vers :

- Llama 3.2 (notre fidèle compagnon de test)

- DeepSeek-R1 (spécialisé en raisonnement—quand il crash pas ton laptop)

- Mistral

- Phi-4

- *30+ autres modèles*

**Pro tip** : check le nombre de [paramètres](https://fr.wikipedia.org/wiki/Param%C3%A8tre_d%27un_mod%C3%A8le_de_langage?utm_source=saaspasse.beehiiv.com&utm_medium=newsletter&utm_campaign=un-lama-et-deux-bozos#:~:text=Dans%20le%20contexte%20des%20mod%C3%A8les,r%C3%A9seau%20de%20neurones%20du%20mod%C3%A8le.) avant d'installer. Mettons avec 8GB de RAM, tu peux en théorie rouler des modèles jusqu'à ~7 milliards de paramètres. Plus le nombre de paramètres est élevé, plus [l'inférence](https://www.youtube.com/watch?v=XtT5i0ZeHHE&t=19s&utm_source=saaspasse.beehiiv.com&utm_medium=newsletter&utm_campaign=un-lama-et-deux-bozos) sera lente et la consommation de mémoire importante.

### Comment faire ça?

Si j’ai pu le faire en trente minutes, c’est sûr que tu peux aussi. L’heure de gloire des n00bs est arrivée, je crois en toi.

Full vidéo coming soon. Je l’ai échappé côté délégation. Mais un bon leader prend la responsabilité, *you know*. Vu que je suis 80% un bon leader, vous pouvez donc blâmer Meto à 20%.

**Étape 1 : Installe Ollama**

1. Rends-toi sur [Ollama](https://ollama.com/?utm_source=saaspasse.beehiiv.com&utm_medium=newsletter&utm_campaign=un-lama-et-deux-bozos) et télécharge la version pour Mac (si t’es sur Mac, *of course*).

2. Ouvre le fichier téléchargé et déplace Ollama dans le dossier **Applications**.

3. Lance Ollama. L’icône devrait apparaître en haut à droite de ton écran.

4. Suis les instructions pour installer la ligne de commande via ton **Terminal** si demandé.

si t’as jamais ouvert ton Terminal sur Mac, ça ressemble à ça!

**Étape 2 : Installe pinokio**

1. Va sur [pinokio](https://pinokio.computer?utm_source=saaspasse.beehiiv.com&utm_medium=newsletter&utm_campaign=un-lama-et-deux-bozos) et télécharge la version pour Mac.

2. Ouvre le fichier .dmg et déplace pinokio dans le dossier **Applications**.

3. Ouvre pinokio. Si tu reçois un message de sécurité, va dans **Préférences Système > Sécurité et Confidentialité** et autorise l’application.

4. Dans pinokio, utilise l’outil **Sentinel** pour retirer pinokio de la “quarantaine” macOS si nécessaire.

**Étape 3 : Installe Open WebUI via pinokio**

1. Dans pinokio, cherche **Open WebUI** dans le *marketplace* de scripts.

2. Clique sur **Download**, puis sur **Install**. pinokio gérera automatiquement l’installation des dépendances.

3. Une fois l'installation terminée, ouvre **Open WebUI** via pinokio. Ça lancera une interface similaire à ChatGPT dans ton navigateur, accessible via un lien **localhost**.

**Étape 4 : Télécharge et utilise un LLM open source**

1. Ouvre Ollama et télécharge un modèle compatible avec ta RAM.

2. Exemple de commande dans le terminal pour télécharger un modèle :

1. Une fois le modèle téléchargé, il apparaîtra dans **Open WebUI**. Tu pourras choisir le modèle dans l’interface et commencer à interagir avec.

**Étape 5 : Change de modèle dans Open WebUI**

1. Pour ajouter un autre modèle, retourne sur le site d’Ollama et trouve un modèle qui t'intéresse (comme [DeepSeek-R1](https://api-docs.deepseek.com/news/news250120?utm_source=saaspasse.beehiiv.com&utm_medium=newsletter&utm_campaign=un-lama-et-deux-bozos) pour le raisonnement).

2. Utilise la commande suivante pour télécharger un nouveau modèle :

1. Le nouveau modèle sera disponible dans **Open WebUI**, où tu pourras alterner entre différents modèles dans une même conversation.

#### Conseils et idées :

- Les modèles plus lourds (plus de 7B paramètres) peuvent être lents ou causer des crashs si tu n'as pas assez de RAM.

- Open WebUI permet certaines fonctions comme la recherche web, mais tu devras configurer des clés API pour des services comme Google ou DuckDuckGo.

- Teste différents modèles selon tes besoins (raisonnement, code, créativité).

- Explore l'app [Apollo AI](https://apps.apple.com/ca/app/apollo-ai-private-local-ai/id6448019325?utm_source=saaspasse.beehiiv.com&utm_medium=newsletter&utm_campaign=un-lama-et-deux-bozos) sur iOS pour une expérience similaire mobile.

**Félicitations !** Tu peux maintenant utiliser des LLM open source localement sur ton ordinateur sans dépendre de services cloud payants qui espionnent tes recettes de cuisine.

Ta machine roule dans le tapis? *Good news*! Jumelle ça à un minimum de coton ouatés et bas de laine et tu peux maintenant réduire ton bill d’Hydro de 20%.

*Thank me later* 🔥

—

Quelque chose à ajouter? *Good*. Laisse un commentaire ou réponds à ce courriel direct.

Cheers,

[Frank](https://www.linkedin.com/in/frankln/?utm_source=saaspasse.beehiiv.com&utm_medium=newsletter&utm_campaign=un-lama-et-deux-bozos) 💜