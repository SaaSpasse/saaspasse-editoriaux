---
date: '2026-04-24'
title: Brouillard sur la ligne
url: https://saaspasse.beehiiv.com/p/brouillard-sur-la-ligne
slug: brouillard-sur-la-ligne
source: beehiiv
word_count: 3443
reading_time_min: 17
editorial_confidence: high
liens_internes: 50
liens_externes: 1
top_domains:
- domain: www.linkedin.com
  count: 1
utm_detectes:
- url: https://www.twitter.com/frankhellend?utm_source=saaspasse.beehiiv.com&utm_medium=referral&utm_campaign=brouillard-sur-la-ligne
- url: https://www.stableapp.cloud/?utm_source=saaspasse.beehiiv.com&utm_medium=referral&utm_campaign=brouillard-sur-la-ligne
- url: https://www.youtube.com/watch?v=e2R0NSKtVA0&utm_source=saaspasse.beehiiv.com&utm_medium=referral&utm_campaign=brouillard-sur-la-ligne
- url: https://superwhisper.com/?utm_source=saaspasse.beehiiv.com&utm_medium=referral&utm_campaign=brouillard-sur-la-ligne
- url: https://www.monologue.to/?utm_source=saaspasse.beehiiv.com&utm_medium=referral&utm_campaign=brouillard-sur-la-ligne
- url: https://langfuse.com/docs/evaluation/evaluation-methods/llm-as-a-judge?utm_source=saaspasse.beehiiv.com&utm_medium=referral&utm_campaign=brouillard-sur-la-ligne
- url: https://www.coval.ai/?utm_source=saaspasse.beehiiv.com&utm_medium=referral&utm_campaign=brouillard-sur-la-ligne
- url: https://www.cekura.ai/?utm_source=saaspasse.beehiiv.com&utm_medium=referral&utm_campaign=brouillard-sur-la-ligne
- url: https://roark.ai/?utm_source=saaspasse.beehiiv.com&utm_medium=referral&utm_campaign=brouillard-sur-la-ligne
- url: https://hamming.ai/?utm_source=saaspasse.beehiiv.com&utm_medium=referral&utm_campaign=brouillard-sur-la-ligne
personnes:
- nom: Thomas Ferland
  linkedin: https://www.linkedin.com/in/thomas-ferland-80851615a/?utm_source=saaspasse.beehiiv.com
- nom: Vincent Lamanna
  linkedin: https://www.linkedin.com/in/vincentlamanna/?utm_source=saaspasse.beehiiv.com
- nom: Sylvain Boily
  linkedin: https://www.linkedin.com/in/sylvainboily/?utm_source=saaspasse.beehiiv.com
- nom: Alexis Boucher
  linkedin: https://www.linkedin.com/in/alexis-boucher-27a956a4/?utm_source=saaspasse.beehiiv.com
- nom: Benjamin Philion
  linkedin: https://www.linkedin.com/in/benjamin-philion-9594aa6/?utm_source=saaspasse.beehiiv.com
- nom: Felix Simard
  linkedin: https://www.linkedin.com/in/felixsimard/?utm_source=saaspasse.beehiiv.com
- nom: Sasha Denouvilliez-Pech
  linkedin: https://www.linkedin.com/in/sasha-denouvilliez-pech/?utm_source=saaspasse.beehiiv.com
- nom: Marc Obeid
  linkedin: https://www.linkedin.com/in/marcobeid/?utm_source=saaspasse.beehiiv.com
- nom: William Garneau
  linkedin: https://www.linkedin.com/in/william-garneau/?utm_source=saaspasse.beehiiv.com
- nom: Guillaume Falardeau
  linkedin: https://www.linkedin.com/in/guillaume-falardeau-b213768b/?utm_source=saaspasse.beehiiv.com
---


# Éditorial (copywriting)

<!-- editorial:start -->
Y'a ~deux mois, appel vidéo avec quelqu'un que je respecte. 

Le pitch: une startup dans le _voice ops_. MVP déjà full avancé. 

L'invitation: m'impliquer, voire en prendre la tête. 

J'ai raccroché, un peu flatté, un peu stressé. 

Une invitation comme ça, d'une personne que t'estimes, dans un _space_ en pleine ébullition—tu dis pas non _on-the-spot_. 

_Spoiler alert_ , mais je me pense pas en position de dire oui. SaaSpasse m'occupe full-time, j'ai l'agenda rempli pas mal plus que la batterie. Pis pour être honnête, je comprenais pas assez le voice AI pour _commit_ à quoi que ce soit. 

Fait que j'ai fait la seule affaire que je sais faire quand j'ai un angle mort: booker des appels avec du monde plus brillant que moi là-dessus. 

J'ai parlé à huit fondateurs en voice AI au Québec. 

Aujourd'hui, je te partage ce que j'ai appris—les outils, les _patterns_ , les vrais pains, pis le spectre de monde qui bâtit dans cette industrie-là. 

L'édito veut faire deux affaires en même temps: te donner un _primer_ solide sur les bases du voice AI (architectures, terminologie, _trade-offs_), pis t'exposer aux enjeux réels quand tu _build_ dans ce _space_. 

Un p'tit _caveat_ avant de plonger: le voice AI bouge vite en tabarouette. Des affirmations ici pourraient être incomplètes. Si t'as de l'info qui nuance ou contredit, commente sous le post LinkedIn de cet édito ou _reply_ direct—je peux mettre à jour la version web.

On part. 

### C'est quoi un voice agent en 2026

Okay, mettons un **bot** , c'est le vieux "faites le 1 pour français"—arbre de décision rigide, cul-de-sac garantis. Un **agent** , c'est un système dynamique propulsé par des modèles AI. Ça raisonne, appelle des _tools_ , gère le flow d'une vraie conversation. 

Sous le capot, deux grandes familles d'architectures. 

**Le** _**pipeline**_**en cascade** enchaîne trois modèles séparés, souvent chez trois fournisseurs différents.

STT (_speech-to-text_) = les oreilles. LLM = le cerveau. TTS (_text-to-speech_) = la bouche. Exemple: Deepgram pour entendre, OpenAI pour penser, ElevenLabs pour parler. Chaque bloc se _swap_ indépendamment—c'est là que vient la flexibilité. 

![](https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/7cebec69-2267-45bf-8430-baa81f156338/STT-LLM-TTS.png?t=1776910259)

Ça a l'air lent dit de même, trois étapes en série. Mais grâce au _streaming_ , chaque bloc commence à travailler avant que le précédent ait fini. La transcription sort mot par mot, le LLM commence à générer avant la fin de la phrase, le TTS parle avant que le LLM finisse sa réponse. Comme Netflix—tu regardes un _chunk_ de KPop Demon Hunters pendant que le prochain _download_. Pas besoin d'attendre la vidéo complète. 

J'écoute pas KPop Demon Hunters pour vrai, je trouvais juste ça drôle. Écris-moi pas pour qu'on _bond_ sur notre amour du KPop, ça marchera pas.

**Le** _**realtime**_ (aussi _speech-to-speech_)—un seul modèle _multimodal_ qui prend de l'audio et émet de l'audio. Pas de texte entre les deux, pas de traduction interne. Le modèle "pense" directement en tokens audio. OpenAI Realtime, Gemini Live, ElevenLabs Conversational—les gros _providers_. 

Note: au début, je pensais que streaming et realtime c'était la même affaire. Pas pantoute. Le streaming, c'est une optimisation du pipeline en cascade. Le realtime, c'est une architecture complètement différente.

### Et le voice ops dans tout ça?

_Ops_ , c'est le _tooling_ qui t'aide à **opérer** une techno complexe en production—pas juste à la _build_. Pense DevOps (apps + infra), FinOps (coûts cloud e.g. [Stable](https://www.stableapp.cloud/?utm_source=saaspasse.beehiiv.com&utm_medium=referral&utm_campaign=brouillard-sur-la-ligne)), MLOps (modèles ML). Voice ops suit le même pattern: outils pour opérer des voice agents en prod. _Testing_ , _monitoring_ , _evals_ , compliance, permissioning, versioning, observabilité par couche. 

La boîte à outils pour pas gérer tes agents dans le noir. 

### Le LLM, c'est le nerf de la guerre

Première chose que plusieurs fondateurs m'ont clarifiée, chiffres en main: dans un pipeline en cascade qui fonctionne bien, le STT et le TTS prennent à peine 100-150 millisecondes combinés. Le reste de la latence vient du LLM. 

**85% à 90% de la latence totale = le cerveau qui pense.**

Deepgram, Whisper, ElevenLabs, Google TTS—les oreilles et la bouche sont devenues des commodités. La plupart des fondateurs choisissent leur STT/TTS selon la latence publiée ou les coûts, _swap_ quand un meilleur modèle sort, pis passent à autre chose. 

Ce qui occupe plusieurs builders, c'est le **LLM**. Quel modèle? Quel _provider_? Quand switcher? Comment abstraire les providers pour pouvoir pivoter rapidement? Comment l'équiper avec les bons _tools_? Comment le contrôler avec des _guardrails_? 

Des outils comme OpenRouter permettent d'abstraire plusieurs LLMs derrière une interface unifiée. Un fondateur à qui j'ai parlé s'en sert pour tester différents _providers_ pis identifier les outliers de latence dans ses logs—pas pour faire du swap automatique mid-call, mais pour garder la flexibilité de pivoter quand un _provider_ devient moins bon. 

### OK mais pourquoi pas juste du realtime dans ce cas-là?

Bonne question, que je me suis posée aussi. 

Les modèles _speech-to-speech_ (OpenAI Realtime, Gemini Live) promettent du _sub_ -500ms, intonation préservée, interruptions naturelles. Sur papier, la solution élégante au problème de latence. 

Dans la vraie vie? 

Les modèles _realtime_ ont été bâtis pour de la conversation naturelle—moins de _guardrails_ , moins de _tool calls_ précis, moins de logique business entre l'écoute pis la réponse. Un design optimisé pour la fluidité d'échange, moins pour les _workflows_ business sérieux (B2B ou B2C). Ce qui est magnifique en démo devient problématique quand ton agent doit: vérifier une identité avant de donner accès à un dossier, rejeter une question hors-scope avec un message compliance-approved, appeler ton CRM au bon moment dans la conversation, ou se brancher sur un état précis d'un _workflow_ pré-défini. 

Les _founders_ à qui j'ai parlé qui ont essayé du _realtime_ en prod sont revenus au pipeline en cascade. La raison qui revient: **le contrôle**. 

Dans un pipeline, chaque étape (STT → LLM → TTS) est une fenêtre où tu peux injecter de la logique. Valider le transcript avant de l'envoyer au LLM. Vérifier la réponse avant le TTS. _Trigger_ un _tool call_ précis à un moment précis. Logger pour compliance. En _realtime_ , tout se passe dans la boîte noire du modèle multimodal—t'as pas de fenêtre de contrôle. 

Le _realtime_ a été designé pour un autre _job-to-be-done_ : des interactions naturelles ouvertes. Les _workflows_ business avec _guardrails_ , compliance et _tool calling_ chirurgical appartiennent à un terrain différent. 

Résultat: en 2026, le pipeline en cascade gagne dans la vraie vie. Le _realtime_ impressionne en démo mais attend son _fit_ production. 

### "Siri nous a traumatisés"

C'est pas ma phrase—c'est un fondateur qui me l'a lâchée pendant un appel, pis elle m'est restée. 

Il m'a raconté une anecdote pour l'illustrer: ses enfants de 9-10 ans, quand ils ont une question, ils ouvrent Gemini en mode voix direct. Pas de _screen first_ , pas de _typing_. Juste "Gemini, peux-tu m'expliquer..." Ils trouvent ça normal, fluide, efficace. 

Nous autres les adultes... 

On a eu Siri 2011, Alexa 2014, [Okay GooGoo](https://www.youtube.com/watch?v=e2R0NSKtVA0&utm_source=saaspasse.beehiiv.com&utm_medium=referral&utm_campaign=brouillard-sur-la-ligne) je sais pu trop quand. Un paquet d'assistants vocaux qui comprenaient pas notre accent, qui répondaient mal, ou qui nous balançaient des résultats Google en mode "voici ce que j'ai trouvé sur le web". Conditionnement classique: tu te brûles assez souvent, tu arrêtes d'essayer. 

Résultat: on est plus lents à adopter les interfaces vocales nouvelle génération—même quand elles sont rendues vraiment bonnes. 

J'ai vécu une version de ce biais moi aussi. Circa 2018, je jouais avec les modèles _speech-to-text_ pour des besoins perso. L'expérience était… _meh_. Transcription croche, latence éternelle, frustration quotidienne. _Fast-forward_ à 2024-2025: des outils comme [Super Whisper](https://superwhisper.com/?utm_source=saaspasse.beehiiv.com&utm_medium=referral&utm_campaign=brouillard-sur-la-ligne) pis [Monologue](https://www.monologue.to/?utm_source=saaspasse.beehiiv.com&utm_medium=referral&utm_campaign=brouillard-sur-la-ligne) sortent, pis ils sont _sharp_. Mais moi j'ai pris du temps avant de les essayer—mon cerveau était encore en mode "ça va pas marcher". J'ai manqué plusieurs mois d'usage à cause de mes vieux réflexes. 

Le _twist_ dans l'autre sens, que j'ai aussi entendu: certaines entreprises demandent explicitement des voix **moins** naturelles pour leurs agents. Genre des répondeurs automatiques à menus style "faites le 1 pour français" (ce qu'on appelle dans le jargon un **IVR** , pour _Interactive Voice Response_). Pourquoi? Parce que leurs clients se méfient du trop-vrai. Se faire duper par un agent qui sonne humain = pire que savoir d'avance que c'est un robot. 

Donc t'as deux dynamiques qui jouent en parallèle: 

  * Les jeunes qui adoptent la voice AI naturellement, parce qu'ils ont pas le bagage Siri 

  * Les adultes qui se méfient, pis certains clients enterprises qui veulent qu'on leur dise clairement "c'est un bot" 

La techno évolue vite. Nos habitudes, moins. 

## Qu'est-ce qui fait le plus mal aux builders?

J'ai demandé à chaque fondateur c'est quoi qui leur fait le plus mal au quotidien. 

Quatre patterns reviennent. 

### 1\. Le QA se fait encore à la mitaine

Comment tu testes un voice agent avant de le _ship_ en prod? Comment tu monitores la qualité des appels en live? 

T'appelles l'agent toi-même, t'écoutes, t'ajustes à l'oreille. 

J'exagère à peine. Plusieurs fondateurs à qui j'ai parlé—même ceux qui pèsent des milliers d'appels par mois—font encore du QA en appelant leurs propres agents pis en jugeant manuellement. Ça QA au feeling pas mal (_for now_). 

Des outils voice ops émergent depuis 12-18 mois pour régler ça: simulation de scénarios, **monitoring par couche** (latence et qualité mesurées séparément pour le STT, le LLM et le TTS), évaluation automatisée via _[LLM-as-judge](https://langfuse.com/docs/evaluation/evaluation-methods/llm-as-a-judge?utm_source=saaspasse.beehiiv.com&utm_medium=referral&utm_campaign=brouillard-sur-la-ligne)_. Plusieurs joueurs sérieux sont dans le _space_. 

Mais l'adoption chez les builders à qui j'ai parlé? Faible. 

Certains ont ça sur leur _roadmap_ à faire éventuellement. D'autres _build_ leur propre _tooling_ maison parce que les outils existants matchent pas leur _stack_. Je l'ai senti comme super important mais pas **urgent** mettons. 

La catégorie "voice ops" est émergente, avec une vraie proposition de valeur, mais le _reach_ vers ces outils semble pas fort en date d'aujourd'hui. Y'a un gap entre "ça existe, c'est cool" pis "on l'utilise en prod". 

Pourquoi? Peut-être que le _pain_ est pas encore assez aigu. Peut-être que les builders sont trop occupés à bâtir leur produit pour investir dans les outils autour. Peut-être les deux. 

### 2\. Un voice agent n'a pas de budget de tolérance

Of course les humains _mess up_ au téléphone—tout le monde a sa collection d'appels frustrants. Mais avec un humain comme toi ("the devil you know"), y'a un minimum de bonne foi préchargée. Il a mal compris? Stressé? Fatigué? Tu lui donnes une chance. 

Le voice AI part à zéro sur ce plan-là. Aucune banque de bonne foi préchargée. 

Pis quand il fait des erreurs, elles sont qualitativement différentes: 

  * Figer 5-10 secondes _mid-phrase_

  * Rire tout seul à un endroit random 

  * Inventer des infos qui existent pas dans ton dossier 

  * Sortir un artefact audio weird (voix qui craque, _pitch_ qui change) 

  * Perdre le contexte après 3-4 échanges 

  * Répéter une réponse qu'il t'a déjà donnée 

Ces failures sentent le **système cassé**. Chaque glitch ajoute à une méfiance qui monte vite. 

Le voice AI n'a aucun budget de tolérance. L'accumulation de hiccups coûte disproportionnellement cher en _trust_. 

Pis c'est un pain transversal—il amplifie tous les autres. 

### 3\. L'autre mur: le change management interne

Disons que t'as réglé la fiabilité techno. _Dope_! 

Y'a un autre mur devant toi. 

Un fondateur l'a flaggé directement comme une friction terrain: 

Tes 200, 500, 1000 appels par jour roulent en prod sans que personne puisse les écouter tous en temps réel. Le monitoring back-end est pas toujours _fine-tuned_ , le _tracing_ capture pas toujours ce qu'il faudrait pour comprendre les hiccups après coup. Ton agent parle au nom de ta brand pendant que tu dors. 

Tu vas me dire: 

_Même affaire si ce sont des humains?_

Mmm, "noui". Le volume d'appels peut exploser avec des agents vs des humains. Plus de surface où foutre la merde dans ta compagnie, vu que ça _scale_ , justement. Sinon, un humain a quand même l'incitatif de faire une bonne job, ou juste... garder sa job. Pis l'humain sait que ses appels peuvent être enregistrés et écoutés par sa boss. 

Ça demande un acte de foi opérationnel de la part du client. 

Pis la tolérance varie selon l'industrie. Un cabinet de thérapeutes pis un garage, c'est pas le même niveau d'enjeu si l'agent répond mal une fois. 

Le frein est autant humain que technique. Pis c'est une friction que les startups en voice AI traverse client par client. 

### 4\. L'argent, pas juste le temps

_Full disclosure_ : j'ai commencé mes appels en pensant que la latence était LE pain #1 des voice agents. Ça me semblait évident—tout le monde en parle, c'est le KPI central dans les démos, c'est ce qui distingue "ça feel humain" de "ça feel cassé". 

Mais un CEO m'a nuancé ça dès le début de notre appel. 

Pour lui, la latence reste un concern réel. Mais la vraie douleur quotidienne, c'est **la prévisibilité des coûts**. 

Pourquoi? Parce que les outils et les modèles que tu utilises dans ta _stack_ voice AI bougent leur pricing. Des changements de tarification qui peuvent rendre ton _operation_ pas sustainable du jour au lendemain. 

Exemple concret qu'il m'a donné: facturer via la couche agentique d'un _vendor_ populaire (la version _turnkey_ où le vendor gère tout le _pipeline_ pour toi) peut coûter plusieurs fois plus cher que d'appeler directement l'API des mêmes LLM, STT et TTS sous-jacents—dans son cas, il parlait de 4-5x. Pis la variabilité est _wild_ selon lui—dupliquer deux agents identiques (mêmes instructions, mêmes LLM) peut générer des prix qui oscillent entre 20¢ et 80¢ d'un appel à l'autre. Bonne chance pour pricer tes clients en aval. 

Plusieurs fondateurs à qui j'ai parlé ont fini par sortir du _stack_  _vendor_ populaire quand ils ont scalé. Ils rebuildent des morceaux à partir des APIs plus basiques, abstractent leurs LLMs pour pouvoir _swap_ vite, cherchent de la prévisibilité à tout prix. 

Le _stack_ standard, c'est un point de départ. 

### 5\. Compréhension vs exécution

Cette citation [légérement modifiée] d'un fondateur pendant notre appel me trotte dans la tête: 

_"Le vibe-code de features prend 30 secondes. L'intelligence opérationnelle derrière, ça m'a pris 4 mois."_

Contexte: il _build_ un voice agent vertical dans une industrie spécifique. Le _vibe-code_ facile, c'est typer un prompt, générer un CRUD, setup les APIs, déployer. Claude Code, Cursor, Codex, peu importe. Builder une app c'est facile. 

Les 4 mois, c'est autre chose. 

C'est mapper le domaine métier de ses clients de façon structurée: 

  * Les services offerts par ses clients 

  * Les variantes de prix selon le plan, la localisation, le _tier_

  * Les professionnels qui peuvent livrer quel service 

  * Les horaires, les contraintes, les exceptions 

  * Les règles qui peuvent pas être déduites logiquement (exceptions historiques, deals particuliers avec certains clients, politiques maison qui vivent dans la tête du patron) 

Cette couche-là se gagne seulement en passant du temps avec le client, dans son métier, à débusquer les _edge cases_ qui n'apparaissent nulle part dans la documentation officielle. 

Pour un fondateur voice AI, c'est un moat potentiellement intéressant—qui ressemble d'ailleurs au moat classique du [Vertical SaaS](https://saaspasse.beehiiv.com/p/vertical-ai). Le code qui entoure l'agent, des dizaines d'autres peuvent le rebuild en un _week-end_. La carte détaillée du domaine opérationnel, c'est des mois de terrain qui se copient mal. 

Les fondateurs qui scalent l'ont compris. Ils _trackent_ leurs apprentissages. Ils _buildent_ leur _playbook_ domaine comme un asset à part entière, distinct de leur _codebase_. 

### Le brouillard sur la ligne

Un truc m'a frappé en compilant mes notes: les huit fondateurs à qui j'ai parlé construisent des business fondamentalement différentes les unes des autres. 

T'as un fondateur non-technique qui vise une verticale spécifique, qui déverrouille tout par la connaissance métier. T'as des jeunes fondateurs avec le couteau entre les dents, qui attaquent un angle d'abord horizontal pis _ship_ vite. T'as un fondateur hyper focused, avec une équipe super technique, qui maximise la souveraineté des données et de la _stack_. 

_Fun fact_ : je m’attendais à ce que la souveraineté des données et de l’infra soit un enjeu plus _top-of-mind_ dans mes discussions, mais pas tant. Dépend de plein trucs, et sujet pour un autre édito, hehe.

Pis y'a un autre axe qui traverse ça: t'en as qui n'hésitent pas à payer pour des applications ou des plateformes _turnkey_ pour bouger plus vite, t'en as d'autres qui _leverage_ l'open source pis l'_agentic coding_ pour tout développer à l'interne. 

Mettons que j'ai utilisé le terme "space" très largement pour rassembler tout ce beau monde-là en voice AI. Y'ont des thèses radicalement différentes. _Stacks_ différents. Stratégies différentes. 

C'est le signe d'un _space_ qui est encore tôt—personne s'entend sur c'est quoi le bon _playbook_ , parce qu'il y en a pas encore un. 

Le titre de l'édito, il vient de cette sensation qui m'est revenue à chaque appel: ce _space_ -là est dans un pas pire _**fog of war**_. Meh, pas juste ce _space_ , _I guess_.

T'as des applications construites par-dessus des modèles, qui cherchent à se verticaliser ou s'horizontaliser le plus vite possible avant que quelqu'un d'autre _claim_ leur niche ou leur positionnement universel. T'as des gros labs (OpenAI, Google, ElevenLabs) qui _ship_ leurs propres applications pis qui mangent des parts de marché que les apps pensaient à eux. Pis t'as des outils voice ops _in-between_ (comme celui que mon ami m'a pitché, ou [Coval](https://www.coval.ai/?utm_source=saaspasse.beehiiv.com&utm_medium=referral&utm_campaign=brouillard-sur-la-ligne), [Cekura](https://www.cekura.ai/?utm_source=saaspasse.beehiiv.com&utm_medium=referral&utm_campaign=brouillard-sur-la-ligne), [Roark](https://roark.ai/?utm_source=saaspasse.beehiiv.com&utm_medium=referral&utm_campaign=brouillard-sur-la-ligne), [Hamming](https://hamming.ai/?utm_source=saaspasse.beehiiv.com&utm_medium=referral&utm_campaign=brouillard-sur-la-ligne)) qui occupent un créneau réel mais potentiellement fragile—vulnérables d'un côté si les plateformes _model_ montent dans le _ops_ , vulnérables de l'autre si les apps descendent dans le _ops_ elles-mêmes. 

Un _timing_ intéressant. Un _squeeze_ réel aussi? 

Si t’as un _take_ pour m’éduquer sur la défensibilité et longévité des startups en _voice ops_ , écris-moi stp.

Est-ce que je vais prendre la tête de cette startup? Je le sais pas encore au moment où tu lis ça. Probablement pas. Mais bâtir dans le voice AI en 2026, ça demande un certain appétit pour le chaos pis l'incertitude—le brouillard sur la ligne fait partie de la job. 

### Remerciements

Merci à tous ceux qui m'ont écrit ou DM pour m'offrir de jaser—j'ai pas eu le temps de prendre tous les _calls_ ni de répondre à tout le monde. Je vais essayer de faire une autre passe plus tard cette année. 

Pour les huit qui ont pris le temps de me parler directement, gros merci. Toutes les opinions dans ce texte sont les miennes—plusieurs insights qui se recoupent viennent d'eux: 

  * [Thomas Ferland](https://www.linkedin.com/in/thomas-ferland-80851615a/?utm_source=saaspasse.beehiiv.com&utm_medium=referral&utm_campaign=brouillard-sur-la-ligne) ([Angel Softwares](https://angelsoftwares.ca/?utm_source=saaspasse.beehiiv.com&utm_medium=referral&utm_campaign=brouillard-sur-la-ligne)) 

  * [Vincent Lamanna](https://www.linkedin.com/in/vincentlamanna/?utm_source=saaspasse.beehiiv.com&utm_medium=referral&utm_campaign=brouillard-sur-la-ligne) ([Crewdle](https://crewdle.com/?utm_source=saaspasse.beehiiv.com&utm_medium=referral&utm_campaign=brouillard-sur-la-ligne)) 

  * [Sylvain Boily](https://www.linkedin.com/in/sylvainboily/?utm_source=saaspasse.beehiiv.com&utm_medium=referral&utm_campaign=brouillard-sur-la-ligne) ([RoomKit](https://www.roomkit.live/?utm_source=saaspasse.beehiiv.com&utm_medium=referral&utm_campaign=brouillard-sur-la-ligne)) 

  * [Alexis Boucher](https://www.linkedin.com/in/alexis-boucher-27a956a4/?utm_source=saaspasse.beehiiv.com&utm_medium=referral&utm_campaign=brouillard-sur-la-ligne) et [Benjamin Philion](https://www.linkedin.com/in/benjamin-philion-9594aa6/?utm_source=saaspasse.beehiiv.com&utm_medium=referral&utm_campaign=brouillard-sur-la-ligne) ([Solving.ai](https://Solving.ai?utm_source=saaspasse.beehiiv.com&utm_medium=referral&utm_campaign=brouillard-sur-la-ligne)) 

  * [Felix Simard](https://www.linkedin.com/in/felixsimard/?utm_source=saaspasse.beehiiv.com&utm_medium=referral&utm_campaign=brouillard-sur-la-ligne) ([Dimedove](https://dimedove.com/?utm_source=saaspasse.beehiiv.com&utm_medium=referral&utm_campaign=brouillard-sur-la-ligne)) 

  * [Sasha Denouvilliez-Pech](https://www.linkedin.com/in/sasha-denouvilliez-pech/?utm_source=saaspasse.beehiiv.com&utm_medium=referral&utm_campaign=brouillard-sur-la-ligne) ([Vatel](https://www.vatel.ai/?utm_source=saaspasse.beehiiv.com&utm_medium=referral&utm_campaign=brouillard-sur-la-ligne)) 

  * [Marc Obeid](https://www.linkedin.com/in/marcobeid/?utm_source=saaspasse.beehiiv.com&utm_medium=referral&utm_campaign=brouillard-sur-la-ligne) ([Walaw](https://walaw.io/?utm_source=saaspasse.beehiiv.com&utm_medium=referral&utm_campaign=brouillard-sur-la-ligne)) 

  * [William Garneau](https://www.linkedin.com/in/william-garneau/?utm_source=saaspasse.beehiiv.com&utm_medium=referral&utm_campaign=brouillard-sur-la-ligne) ([NordAI](https://nordai.ca/?utm_source=saaspasse.beehiiv.com&utm_medium=referral&utm_campaign=brouillard-sur-la-ligne)) 

Si tu bâtis dans le voice AI au Québec pis que tu veux jaser— _reply_ à cet édito. 

— 

Cheers, 

[Frank](https://www.linkedin.com/in/frankln/?utm_source=saaspasse.beehiiv.com&utm_medium=referral&utm_campaign=brouillard-sur-la-ligne) 💜 

### Gros jalon pour Unicorne 🦄

[![](https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/7f133e8b-fcbb-49a7-a0d7-3b5e9bd2190b/stable_plateform.png?t=1776964838)](https://www.stableapp.cloud/?utm_source=saaspasse.beehiiv.com&utm_medium=referral&utm_campaign=brouillard-sur-la-ligne)

Belle réussite pour nos amis chez [Unicorne](https://saaspasse.com/partenaires/unicorne?utm_source=saaspasse.beehiiv.com&utm_medium=referral&utm_campaign=brouillard-sur-la-ligne) 🦄  
  
Leur produit [Stable](https://www.linkedin.com/company/stable-cloud/?utm_source=saaspasse.beehiiv.com&utm_medium=referral&utm_campaign=brouillard-sur-la-ligne) vient de franchir les 30M$ de dépenses AWS optimisées.  
  
L'optimisation cloud, c'est pas juste couper du gras. C'est libérer du budget pour ce qui fait vraiment avancer ta business.  
  
Stable donne aux équipes le contrôle et la visibilité qu'elles méritent : alertes plus tôt, meilleure lecture des variations de dépenses, recommandations sur lesquelles tu peux réellement te fier.  
  
Félicitations à toute l'équipe 💜  
  
D'ailleurs, on avait enregistré une capsule sur Stable l'an passé si tu veux en savoir plus : 

[ capsule sur Stable ](https://youtu.be/9uZ8WmWOMZQ?utm_source=saaspasse.beehiiv.com&utm_medium=referral&utm_campaign=brouillard-sur-la-ligne)

### 95% du web n’a pas d’API 🌐

"95% du web n'a pas d'API." 🌐  
  
Zapier, Make, les gros joueurs d'automation → ils connectent les apps qui ont des API.  
  
Mais le reste? Cliniques médicales, assureurs, sites legacy... Pour eux, construire une API pour les devs, ce n'est pas la priorité.  
  
La mission de [Deck](https://saaspasse.com/partenaires/deck/?utm_source=saaspasse.beehiiv.com&utm_medium=referral&utm_campaign=brouillard-sur-la-ligne): donner accès au 95% du web qui n'a jamais été pensé pour être accessible. 

[ plus d’info sur deck ](https://saaspasse.com/partenaires/deck/?utm_source=saaspasse.beehiiv.com&utm_medium=referral&utm_campaign=brouillard-sur-la-ligne)

### Quand ton board vote contre toi sans le dire

[![](https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/60fbfb91-7ae9-4284-9ed1-f526ca53d16a/SaaSpaladin-leviat-v1.png?t=1776966188)](https://www.linkedin.com/in/guillaume-falardeau-b213768b/?utm_source=saaspasse.beehiiv.com&utm_medium=referral&utm_campaign=brouillard-sur-la-ligne)

[Guillaume Falardeau](https://www.linkedin.com/in/guillaume-falardeau-b213768b/?utm_source=saaspasse.beehiiv.com&utm_medium=referral&utm_campaign=brouillard-sur-la-ligne) de [Leviat Legal](https://saaspasse.com/partenaires/leviat-legal?utm_source=saaspasse.beehiiv.com&utm_medium=referral&utm_campaign=brouillard-sur-la-ligne) a décortiqué un cas qui devrait faire suer pas mal de founders. 

Le scénario : une compagnie se vend. Les VCs récupèrent leur mise. Les fondateurs et employés obtiennent zéro. Et 6 des 7 membres du board avaient des conflits d'intérêts. 

CEO avec un bonus négocié en secret avec l'acheteur. CFO idem. Administrateur "indépendant" qui investissait dans les fonds du VC. Beau comité. 

C'est quoi le _dual fiduciary_ , pourquoi ta _waterfall_ de liquidation peut te coûter des millions, et comment te protéger avant que ce soit urgent — Guillaume l'explique clairement. 

Genre de post que tu lis maintenant, pas juste quand t'en as besoin. 👇 

[ Lire le post complet ](https://www.linkedin.com/posts/guillaume-falardeau-b213768b_jai-entendu-une-histoire-de-fou-une-entreprise-share-7449807822101372929-brPc?utm_source=share&utm_medium=member_desktop&rcm=ACoAAAtGvEwBMjZr6fTGqSsX7sYnLbJ1Y9DB7lA)
<!-- editorial:end -->

# Brouillard sur la ligne

## Gros primer voice AI feat. 8 builders queb 🗣️

![Author](https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/user/profile_picture/ed291c1d-2cc1-4f26-88a3-680bc46b9500/thumb_FLN_copy.jpeg)

[Francois Lanthier Nadeau](https://www.twitter.com/frankhellend?utm_source=saaspasse.beehiiv.com&utm_medium=referral&utm_campaign=brouillard-sur-la-ligne)  
24th avril 2026 

[](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fsaaspasse.beehiiv.com%2Fp%2Fbrouillard-sur-la-ligne)[](https://twitter.com/intent/tweet?text=Gros+primer+voice+AI+feat.+8+builders+queb+%F0%9F%97%A3%EF%B8%8F&url=https%3A%2F%2Fsaaspasse.beehiiv.com%2Fp%2Fbrouillard-sur-la-ligne&via=frankhellend)[](https://www.threads.net/intent/post?text=Gros+primer+voice+AI+feat.+8+builders+queb+%F0%9F%97%A3%EF%B8%8F+https%3A%2F%2Fsaaspasse.beehiiv.com%2Fp%2Fbrouillard-sur-la-ligne)[](https://www.linkedin.com/sharing/share-offsite?url=https%3A%2F%2Fsaaspasse.beehiiv.com%2Fp%2Fbrouillard-sur-la-ligne)

![](https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/4e2f6d87-4a59-42af-a925-3380e2b046c4/paladin-brouillard-sur-la-ligne.png?t=1776911329)

Y'a ~deux mois, appel vidéo avec quelqu'un que je respecte. 

Le pitch: une startup dans le _voice ops_. MVP déjà full avancé. 

L'invitation: m'impliquer, voire en prendre la tête. 

J'ai raccroché, un peu flatté, un peu stressé. 

Une invitation comme ça, d'une personne que t'estimes, dans un _space_ en pleine ébullition—tu dis pas non _on-the-spot_. 

_Spoiler alert_ , mais je me pense pas en position de dire oui. SaaSpasse m'occupe full-time, j'ai l'agenda rempli pas mal plus que la batterie. Pis pour être honnête, je comprenais pas assez le voice AI pour _commit_ à quoi que ce soit. 

Fait que j'ai fait la seule affaire que je sais faire quand j'ai un angle mort: booker des appels avec du monde plus brillant que moi là-dessus. 

J'ai parlé à huit fondateurs en voice AI au Québec. 

Aujourd'hui, je te partage ce que j'ai appris—les outils, les _patterns_ , les vrais pains, pis le spectre de monde qui bâtit dans cette industrie-là. 

L'édito veut faire deux affaires en même temps: te donner un _primer_ solide sur les bases du voice AI (architectures, terminologie, _trade-offs_), pis t'exposer aux enjeux réels quand tu _build_ dans ce _space_. 

Un p'tit _caveat_ avant de plonger: le voice AI bouge vite en tabarouette. Des affirmations ici pourraient être incomplètes. Si t'as de l'info qui nuance ou contredit, commente sous le post LinkedIn de cet édito ou _reply_ direct—je peux mettre à jour la version web.

On part. 

### C'est quoi un voice agent en 2026

Okay, mettons un **bot** , c'est le vieux "faites le 1 pour français"—arbre de décision rigide, cul-de-sac garantis. Un **agent** , c'est un système dynamique propulsé par des modèles AI. Ça raisonne, appelle des _tools_ , gère le flow d'une vraie conversation. 

Sous le capot, deux grandes familles d'architectures. 

**Le** _**pipeline**_**en cascade** enchaîne trois modèles séparés, souvent chez trois fournisseurs différents.

STT (_speech-to-text_) = les oreilles. LLM = le cerveau. TTS (_text-to-speech_) = la bouche. Exemple: Deepgram pour entendre, OpenAI pour penser, ElevenLabs pour parler. Chaque bloc se _swap_ indépendamment—c'est là que vient la flexibilité. 

![](https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/7cebec69-2267-45bf-8430-baa81f156338/STT-LLM-TTS.png?t=1776910259)

Ça a l'air lent dit de même, trois étapes en série. Mais grâce au _streaming_ , chaque bloc commence à travailler avant que le précédent ait fini. La transcription sort mot par mot, le LLM commence à générer avant la fin de la phrase, le TTS parle avant que le LLM finisse sa réponse. Comme Netflix—tu regardes un _chunk_ de KPop Demon Hunters pendant que le prochain _download_. Pas besoin d'attendre la vidéo complète. 

J'écoute pas KPop Demon Hunters pour vrai, je trouvais juste ça drôle. Écris-moi pas pour qu'on _bond_ sur notre amour du KPop, ça marchera pas.

**Le** _**realtime**_ (aussi _speech-to-speech_)—un seul modèle _multimodal_ qui prend de l'audio et émet de l'audio. Pas de texte entre les deux, pas de traduction interne. Le modèle "pense" directement en tokens audio. OpenAI Realtime, Gemini Live, ElevenLabs Conversational—les gros _providers_. 

Note: au début, je pensais que streaming et realtime c'était la même affaire. Pas pantoute. Le streaming, c'est une optimisation du pipeline en cascade. Le realtime, c'est une architecture complètement différente.

### Et le voice ops dans tout ça?

_Ops_ , c'est le _tooling_ qui t'aide à **opérer** une techno complexe en production—pas juste à la _build_. Pense DevOps (apps + infra), FinOps (coûts cloud e.g. [Stable](https://www.stableapp.cloud/?utm_source=saaspasse.beehiiv.com&utm_medium=referral&utm_campaign=brouillard-sur-la-ligne)), MLOps (modèles ML). Voice ops suit le même pattern: outils pour opérer des voice agents en prod. _Testing_ , _monitoring_ , _evals_ , compliance, permissioning, versioning, observabilité par couche. 

La boîte à outils pour pas gérer tes agents dans le noir. 

### Le LLM, c'est le nerf de la guerre

Première chose que plusieurs fondateurs m'ont clarifiée, chiffres en main: dans un pipeline en cascade qui fonctionne bien, le STT et le TTS prennent à peine 100-150 millisecondes combinés. Le reste de la latence vient du LLM. 

**85% à 90% de la latence totale = le cerveau qui pense.**

Deepgram, Whisper, ElevenLabs, Google TTS—les oreilles et la bouche sont devenues des commodités. La plupart des fondateurs choisissent leur STT/TTS selon la latence publiée ou les coûts, _swap_ quand un meilleur modèle sort, pis passent à autre chose. 

Ce qui occupe plusieurs builders, c'est le **LLM**. Quel modèle? Quel _provider_? Quand switcher? Comment abstraire les providers pour pouvoir pivoter rapidement? Comment l'équiper avec les bons _tools_? Comment le contrôler avec des _guardrails_? 

Des outils comme OpenRouter permettent d'abstraire plusieurs LLMs derrière une interface unifiée. Un fondateur à qui j'ai parlé s'en sert pour tester différents _providers_ pis identifier les outliers de latence dans ses logs—pas pour faire du swap automatique mid-call, mais pour garder la flexibilité de pivoter quand un _provider_ devient moins bon. 

### OK mais pourquoi pas juste du realtime dans ce cas-là?

Bonne question, que je me suis posée aussi. 

Les modèles _speech-to-speech_ (OpenAI Realtime, Gemini Live) promettent du _sub_ -500ms, intonation préservée, interruptions naturelles. Sur papier, la solution élégante au problème de latence. 

Dans la vraie vie? 

Les modèles _realtime_ ont été bâtis pour de la conversation naturelle—moins de _guardrails_ , moins de _tool calls_ précis, moins de logique business entre l'écoute pis la réponse. Un design optimisé pour la fluidité d'échange, moins pour les _workflows_ business sérieux (B2B ou B2C). Ce qui est magnifique en démo devient problématique quand ton agent doit: vérifier une identité avant de donner accès à un dossier, rejeter une question hors-scope avec un message compliance-approved, appeler ton CRM au bon moment dans la conversation, ou se brancher sur un état précis d'un _workflow_ pré-défini. 

Les _founders_ à qui j'ai parlé qui ont essayé du _realtime_ en prod sont revenus au pipeline en cascade. La raison qui revient: **le contrôle**. 

Dans un pipeline, chaque étape (STT → LLM → TTS) est une fenêtre où tu peux injecter de la logique. Valider le transcript avant de l'envoyer au LLM. Vérifier la réponse avant le TTS. _Trigger_ un _tool call_ précis à un moment précis. Logger pour compliance. En _realtime_ , tout se passe dans la boîte noire du modèle multimodal—t'as pas de fenêtre de contrôle. 

Le _realtime_ a été designé pour un autre _job-to-be-done_ : des interactions naturelles ouvertes. Les _workflows_ business avec _guardrails_ , compliance et _tool calling_ chirurgical appartiennent à un terrain différent. 

Résultat: en 2026, le pipeline en cascade gagne dans la vraie vie. Le _realtime_ impressionne en démo mais attend son _fit_ production. 

### "Siri nous a traumatisés"

C'est pas ma phrase—c'est un fondateur qui me l'a lâchée pendant un appel, pis elle m'est restée. 

Il m'a raconté une anecdote pour l'illustrer: ses enfants de 9-10 ans, quand ils ont une question, ils ouvrent Gemini en mode voix direct. Pas de _screen first_ , pas de _typing_. Juste "Gemini, peux-tu m'expliquer..." Ils trouvent ça normal, fluide, efficace. 

Nous autres les adultes... 

On a eu Siri 2011, Alexa 2014, [Okay GooGoo](https://www.youtube.com/watch?v=e2R0NSKtVA0&utm_source=saaspasse.beehiiv.com&utm_medium=referral&utm_campaign=brouillard-sur-la-ligne) je sais pu trop quand. Un paquet d'assistants vocaux qui comprenaient pas notre accent, qui répondaient mal, ou qui nous balançaient des résultats Google en mode "voici ce que j'ai trouvé sur le web". Conditionnement classique: tu te brûles assez souvent, tu arrêtes d'essayer. 

Résultat: on est plus lents à adopter les interfaces vocales nouvelle génération—même quand elles sont rendues vraiment bonnes. 

J'ai vécu une version de ce biais moi aussi. Circa 2018, je jouais avec les modèles _speech-to-text_ pour des besoins perso. L'expérience était… _meh_. Transcription croche, latence éternelle, frustration quotidienne. _Fast-forward_ à 2024-2025: des outils comme [Super Whisper](https://superwhisper.com/?utm_source=saaspasse.beehiiv.com&utm_medium=referral&utm_campaign=brouillard-sur-la-ligne) pis [Monologue](https://www.monologue.to/?utm_source=saaspasse.beehiiv.com&utm_medium=referral&utm_campaign=brouillard-sur-la-ligne) sortent, pis ils sont _sharp_. Mais moi j'ai pris du temps avant de les essayer—mon cerveau était encore en mode "ça va pas marcher". J'ai manqué plusieurs mois d'usage à cause de mes vieux réflexes. 

Le _twist_ dans l'autre sens, que j'ai aussi entendu: certaines entreprises demandent explicitement des voix **moins** naturelles pour leurs agents. Genre des répondeurs automatiques à menus style "faites le 1 pour français" (ce qu'on appelle dans le jargon un **IVR** , pour _Interactive Voice Response_). Pourquoi? Parce que leurs clients se méfient du trop-vrai. Se faire duper par un agent qui sonne humain = pire que savoir d'avance que c'est un robot. 

Donc t'as deux dynamiques qui jouent en parallèle: 

  * Les jeunes qui adoptent la voice AI naturellement, parce qu'ils ont pas le bagage Siri 

  * Les adultes qui se méfient, pis certains clients enterprises qui veulent qu'on leur dise clairement "c'est un bot" 

La techno évolue vite. Nos habitudes, moins. 

## Qu'est-ce qui fait le plus mal aux builders?

J'ai demandé à chaque fondateur c'est quoi qui leur fait le plus mal au quotidien. 

Quatre patterns reviennent. 

### 1\. Le QA se fait encore à la mitaine

Comment tu testes un voice agent avant de le _ship_ en prod? Comment tu monitores la qualité des appels en live? 

T'appelles l'agent toi-même, t'écoutes, t'ajustes à l'oreille. 

J'exagère à peine. Plusieurs fondateurs à qui j'ai parlé—même ceux qui pèsent des milliers d'appels par mois—font encore du QA en appelant leurs propres agents pis en jugeant manuellement. Ça QA au feeling pas mal (_for now_). 

Des outils voice ops émergent depuis 12-18 mois pour régler ça: simulation de scénarios, **monitoring par couche** (latence et qualité mesurées séparément pour le STT, le LLM et le TTS), évaluation automatisée via _[LLM-as-judge](https://langfuse.com/docs/evaluation/evaluation-methods/llm-as-a-judge?utm_source=saaspasse.beehiiv.com&utm_medium=referral&utm_campaign=brouillard-sur-la-ligne)_. Plusieurs joueurs sérieux sont dans le _space_. 

Mais l'adoption chez les builders à qui j'ai parlé? Faible. 

Certains ont ça sur leur _roadmap_ à faire éventuellement. D'autres _build_ leur propre _tooling_ maison parce que les outils existants matchent pas leur _stack_. Je l'ai senti comme super important mais pas **urgent** mettons. 

La catégorie "voice ops" est émergente, avec une vraie proposition de valeur, mais le _reach_ vers ces outils semble pas fort en date d'aujourd'hui. Y'a un gap entre "ça existe, c'est cool" pis "on l'utilise en prod". 

Pourquoi? Peut-être que le _pain_ est pas encore assez aigu. Peut-être que les builders sont trop occupés à bâtir leur produit pour investir dans les outils autour. Peut-être les deux. 

### 2\. Un voice agent n'a pas de budget de tolérance

Of course les humains _mess up_ au téléphone—tout le monde a sa collection d'appels frustrants. Mais avec un humain comme toi ("the devil you know"), y'a un minimum de bonne foi préchargée. Il a mal compris? Stressé? Fatigué? Tu lui donnes une chance. 

Le voice AI part à zéro sur ce plan-là. Aucune banque de bonne foi préchargée. 

Pis quand il fait des erreurs, elles sont qualitativement différentes: 

  * Figer 5-10 secondes _mid-phrase_

  * Rire tout seul à un endroit random 

  * Inventer des infos qui existent pas dans ton dossier 

  * Sortir un artefact audio weird (voix qui craque, _pitch_ qui change) 

  * Perdre le contexte après 3-4 échanges 

  * Répéter une réponse qu'il t'a déjà donnée 

Ces failures sentent le **système cassé**. Chaque glitch ajoute à une méfiance qui monte vite. 

Le voice AI n'a aucun budget de tolérance. L'accumulation de hiccups coûte disproportionnellement cher en _trust_. 

Pis c'est un pain transversal—il amplifie tous les autres. 

### 3\. L'autre mur: le change management interne

Disons que t'as réglé la fiabilité techno. _Dope_! 

Y'a un autre mur devant toi. 

Un fondateur l'a flaggé directement comme une friction terrain: 

Tes 200, 500, 1000 appels par jour roulent en prod sans que personne puisse les écouter tous en temps réel. Le monitoring back-end est pas toujours _fine-tuned_ , le _tracing_ capture pas toujours ce qu'il faudrait pour comprendre les hiccups après coup. Ton agent parle au nom de ta brand pendant que tu dors. 

Tu vas me dire: 

_Même affaire si ce sont des humains?_

Mmm, "noui". Le volume d'appels peut exploser avec des agents vs des humains. Plus de surface où foutre la merde dans ta compagnie, vu que ça _scale_ , justement. Sinon, un humain a quand même l'incitatif de faire une bonne job, ou juste... garder sa job. Pis l'humain sait que ses appels peuvent être enregistrés et écoutés par sa boss. 

Ça demande un acte de foi opérationnel de la part du client. 

Pis la tolérance varie selon l'industrie. Un cabinet de thérapeutes pis un garage, c'est pas le même niveau d'enjeu si l'agent répond mal une fois. 

Le frein est autant humain que technique. Pis c'est une friction que les startups en voice AI traverse client par client. 

### 4\. L'argent, pas juste le temps

_Full disclosure_ : j'ai commencé mes appels en pensant que la latence était LE pain #1 des voice agents. Ça me semblait évident—tout le monde en parle, c'est le KPI central dans les démos, c'est ce qui distingue "ça feel humain" de "ça feel cassé". 

Mais un CEO m'a nuancé ça dès le début de notre appel. 

Pour lui, la latence reste un concern réel. Mais la vraie douleur quotidienne, c'est **la prévisibilité des coûts**. 

Pourquoi? Parce que les outils et les modèles que tu utilises dans ta _stack_ voice AI bougent leur pricing. Des changements de tarification qui peuvent rendre ton _operation_ pas sustainable du jour au lendemain. 

Exemple concret qu'il m'a donné: facturer via la couche agentique d'un _vendor_ populaire (la version _turnkey_ où le vendor gère tout le _pipeline_ pour toi) peut coûter plusieurs fois plus cher que d'appeler directement l'API des mêmes LLM, STT et TTS sous-jacents—dans son cas, il parlait de 4-5x. Pis la variabilité est _wild_ selon lui—dupliquer deux agents identiques (mêmes instructions, mêmes LLM) peut générer des prix qui oscillent entre 20¢ et 80¢ d'un appel à l'autre. Bonne chance pour pricer tes clients en aval. 

Plusieurs fondateurs à qui j'ai parlé ont fini par sortir du _stack_  _vendor_ populaire quand ils ont scalé. Ils rebuildent des morceaux à partir des APIs plus basiques, abstractent leurs LLMs pour pouvoir _swap_ vite, cherchent de la prévisibilité à tout prix. 

Le _stack_ standard, c'est un point de départ. 

### 5\. Compréhension vs exécution

Cette citation [légérement modifiée] d'un fondateur pendant notre appel me trotte dans la tête: 

_"Le vibe-code de features prend 30 secondes. L'intelligence opérationnelle derrière, ça m'a pris 4 mois."_

Contexte: il _build_ un voice agent vertical dans une industrie spécifique. Le _vibe-code_ facile, c'est typer un prompt, générer un CRUD, setup les APIs, déployer. Claude Code, Cursor, Codex, peu importe. Builder une app c'est facile. 

Les 4 mois, c'est autre chose. 

C'est mapper le domaine métier de ses clients de façon structurée: 

  * Les services offerts par ses clients 

  * Les variantes de prix selon le plan, la localisation, le _tier_

  * Les professionnels qui peuvent livrer quel service 

  * Les horaires, les contraintes, les exceptions 

  * Les règles qui peuvent pas être déduites logiquement (exceptions historiques, deals particuliers avec certains clients, politiques maison qui vivent dans la tête du patron) 

Cette couche-là se gagne seulement en passant du temps avec le client, dans son métier, à débusquer les _edge cases_ qui n'apparaissent nulle part dans la documentation officielle. 

Pour un fondateur voice AI, c'est un moat potentiellement intéressant—qui ressemble d'ailleurs au moat classique du [Vertical SaaS](https://saaspasse.beehiiv.com/p/vertical-ai). Le code qui entoure l'agent, des dizaines d'autres peuvent le rebuild en un _week-end_. La carte détaillée du domaine opérationnel, c'est des mois de terrain qui se copient mal. 

Les fondateurs qui scalent l'ont compris. Ils _trackent_ leurs apprentissages. Ils _buildent_ leur _playbook_ domaine comme un asset à part entière, distinct de leur _codebase_. 

### Le brouillard sur la ligne

Un truc m'a frappé en compilant mes notes: les huit fondateurs à qui j'ai parlé construisent des business fondamentalement différentes les unes des autres. 

T'as un fondateur non-technique qui vise une verticale spécifique, qui déverrouille tout par la connaissance métier. T'as des jeunes fondateurs avec le couteau entre les dents, qui attaquent un angle d'abord horizontal pis _ship_ vite. T'as un fondateur hyper focused, avec une équipe super technique, qui maximise la souveraineté des données et de la _stack_. 

_Fun fact_ : je m’attendais à ce que la souveraineté des données et de l’infra soit un enjeu plus _top-of-mind_ dans mes discussions, mais pas tant. Dépend de plein trucs, et sujet pour un autre édito, hehe.

Pis y'a un autre axe qui traverse ça: t'en as qui n'hésitent pas à payer pour des applications ou des plateformes _turnkey_ pour bouger plus vite, t'en as d'autres qui _leverage_ l'open source pis l'_agentic coding_ pour tout développer à l'interne. 

Mettons que j'ai utilisé le terme "space" très largement pour rassembler tout ce beau monde-là en voice AI. Y'ont des thèses radicalement différentes. _Stacks_ différents. Stratégies différentes. 

C'est le signe d'un _space_ qui est encore tôt—personne s'entend sur c'est quoi le bon _playbook_ , parce qu'il y en a pas encore un. 

Le titre de l'édito, il vient de cette sensation qui m'est revenue à chaque appel: ce _space_ -là est dans un pas pire _**fog of war**_. Meh, pas juste ce _space_ , _I guess_.

T'as des applications construites par-dessus des modèles, qui cherchent à se verticaliser ou s'horizontaliser le plus vite possible avant que quelqu'un d'autre _claim_ leur niche ou leur positionnement universel. T'as des gros labs (OpenAI, Google, ElevenLabs) qui _ship_ leurs propres applications pis qui mangent des parts de marché que les apps pensaient à eux. Pis t'as des outils voice ops _in-between_ (comme celui que mon ami m'a pitché, ou [Coval](https://www.coval.ai/?utm_source=saaspasse.beehiiv.com&utm_medium=referral&utm_campaign=brouillard-sur-la-ligne), [Cekura](https://www.cekura.ai/?utm_source=saaspasse.beehiiv.com&utm_medium=referral&utm_campaign=brouillard-sur-la-ligne), [Roark](https://roark.ai/?utm_source=saaspasse.beehiiv.com&utm_medium=referral&utm_campaign=brouillard-sur-la-ligne), [Hamming](https://hamming.ai/?utm_source=saaspasse.beehiiv.com&utm_medium=referral&utm_campaign=brouillard-sur-la-ligne)) qui occupent un créneau réel mais potentiellement fragile—vulnérables d'un côté si les plateformes _model_ montent dans le _ops_ , vulnérables de l'autre si les apps descendent dans le _ops_ elles-mêmes. 

Un _timing_ intéressant. Un _squeeze_ réel aussi? 

Si t’as un _take_ pour m’éduquer sur la défensibilité et longévité des startups en _voice ops_ , écris-moi stp.

Est-ce que je vais prendre la tête de cette startup? Je le sais pas encore au moment où tu lis ça. Probablement pas. Mais bâtir dans le voice AI en 2026, ça demande un certain appétit pour le chaos pis l'incertitude—le brouillard sur la ligne fait partie de la job. 

### Remerciements

Merci à tous ceux qui m'ont écrit ou DM pour m'offrir de jaser—j'ai pas eu le temps de prendre tous les _calls_ ni de répondre à tout le monde. Je vais essayer de faire une autre passe plus tard cette année. 

Pour les huit qui ont pris le temps de me parler directement, gros merci. Toutes les opinions dans ce texte sont les miennes—plusieurs insights qui se recoupent viennent d'eux: 

  * [Thomas Ferland](https://www.linkedin.com/in/thomas-ferland-80851615a/?utm_source=saaspasse.beehiiv.com&utm_medium=referral&utm_campaign=brouillard-sur-la-ligne) ([Angel Softwares](https://angelsoftwares.ca/?utm_source=saaspasse.beehiiv.com&utm_medium=referral&utm_campaign=brouillard-sur-la-ligne)) 

  * [Vincent Lamanna](https://www.linkedin.com/in/vincentlamanna/?utm_source=saaspasse.beehiiv.com&utm_medium=referral&utm_campaign=brouillard-sur-la-ligne) ([Crewdle](https://crewdle.com/?utm_source=saaspasse.beehiiv.com&utm_medium=referral&utm_campaign=brouillard-sur-la-ligne)) 

  * [Sylvain Boily](https://www.linkedin.com/in/sylvainboily/?utm_source=saaspasse.beehiiv.com&utm_medium=referral&utm_campaign=brouillard-sur-la-ligne) ([RoomKit](https://www.roomkit.live/?utm_source=saaspasse.beehiiv.com&utm_medium=referral&utm_campaign=brouillard-sur-la-ligne)) 

  * [Alexis Boucher](https://www.linkedin.com/in/alexis-boucher-27a956a4/?utm_source=saaspasse.beehiiv.com&utm_medium=referral&utm_campaign=brouillard-sur-la-ligne) et [Benjamin Philion](https://www.linkedin.com/in/benjamin-philion-9594aa6/?utm_source=saaspasse.beehiiv.com&utm_medium=referral&utm_campaign=brouillard-sur-la-ligne) ([Solving.ai](https://Solving.ai?utm_source=saaspasse.beehiiv.com&utm_medium=referral&utm_campaign=brouillard-sur-la-ligne)) 

  * [Felix Simard](https://www.linkedin.com/in/felixsimard/?utm_source=saaspasse.beehiiv.com&utm_medium=referral&utm_campaign=brouillard-sur-la-ligne) ([Dimedove](https://dimedove.com/?utm_source=saaspasse.beehiiv.com&utm_medium=referral&utm_campaign=brouillard-sur-la-ligne)) 

  * [Sasha Denouvilliez-Pech](https://www.linkedin.com/in/sasha-denouvilliez-pech/?utm_source=saaspasse.beehiiv.com&utm_medium=referral&utm_campaign=brouillard-sur-la-ligne) ([Vatel](https://www.vatel.ai/?utm_source=saaspasse.beehiiv.com&utm_medium=referral&utm_campaign=brouillard-sur-la-ligne)) 

  * [Marc Obeid](https://www.linkedin.com/in/marcobeid/?utm_source=saaspasse.beehiiv.com&utm_medium=referral&utm_campaign=brouillard-sur-la-ligne) ([Walaw](https://walaw.io/?utm_source=saaspasse.beehiiv.com&utm_medium=referral&utm_campaign=brouillard-sur-la-ligne)) 

  * [William Garneau](https://www.linkedin.com/in/william-garneau/?utm_source=saaspasse.beehiiv.com&utm_medium=referral&utm_campaign=brouillard-sur-la-ligne) ([NordAI](https://nordai.ca/?utm_source=saaspasse.beehiiv.com&utm_medium=referral&utm_campaign=brouillard-sur-la-ligne)) 

Si tu bâtis dans le voice AI au Québec pis que tu veux jaser— _reply_ à cet édito. 

— 

Cheers, 

[Frank](https://www.linkedin.com/in/frankln/?utm_source=saaspasse.beehiiv.com&utm_medium=referral&utm_campaign=brouillard-sur-la-ligne) 💜 

### Gros jalon pour Unicorne 🦄

[![](https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/7f133e8b-fcbb-49a7-a0d7-3b5e9bd2190b/stable_plateform.png?t=1776964838)](https://www.stableapp.cloud/?utm_source=saaspasse.beehiiv.com&utm_medium=referral&utm_campaign=brouillard-sur-la-ligne)

Belle réussite pour nos amis chez [Unicorne](https://saaspasse.com/partenaires/unicorne?utm_source=saaspasse.beehiiv.com&utm_medium=referral&utm_campaign=brouillard-sur-la-ligne) 🦄  
  
Leur produit [Stable](https://www.linkedin.com/company/stable-cloud/?utm_source=saaspasse.beehiiv.com&utm_medium=referral&utm_campaign=brouillard-sur-la-ligne) vient de franchir les 30M$ de dépenses AWS optimisées.  
  
L'optimisation cloud, c'est pas juste couper du gras. C'est libérer du budget pour ce qui fait vraiment avancer ta business.  
  
Stable donne aux équipes le contrôle et la visibilité qu'elles méritent : alertes plus tôt, meilleure lecture des variations de dépenses, recommandations sur lesquelles tu peux réellement te fier.  
  
Félicitations à toute l'équipe 💜  
  
D'ailleurs, on avait enregistré une capsule sur Stable l'an passé si tu veux en savoir plus : 

[ capsule sur Stable ](https://youtu.be/9uZ8WmWOMZQ?utm_source=saaspasse.beehiiv.com&utm_medium=referral&utm_campaign=brouillard-sur-la-ligne)

### 95% du web n’a pas d’API 🌐

"95% du web n'a pas d'API." 🌐  
  
Zapier, Make, les gros joueurs d'automation → ils connectent les apps qui ont des API.  
  
Mais le reste? Cliniques médicales, assureurs, sites legacy... Pour eux, construire une API pour les devs, ce n'est pas la priorité.  
  
La mission de [Deck](https://saaspasse.com/partenaires/deck/?utm_source=saaspasse.beehiiv.com&utm_medium=referral&utm_campaign=brouillard-sur-la-ligne): donner accès au 95% du web qui n'a jamais été pensé pour être accessible. 

[ plus d’info sur deck ](https://saaspasse.com/partenaires/deck/?utm_source=saaspasse.beehiiv.com&utm_medium=referral&utm_campaign=brouillard-sur-la-ligne)

### Quand ton board vote contre toi sans le dire

[![](https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/60fbfb91-7ae9-4284-9ed1-f526ca53d16a/SaaSpaladin-leviat-v1.png?t=1776966188)](https://www.linkedin.com/in/guillaume-falardeau-b213768b/?utm_source=saaspasse.beehiiv.com&utm_medium=referral&utm_campaign=brouillard-sur-la-ligne)

[Guillaume Falardeau](https://www.linkedin.com/in/guillaume-falardeau-b213768b/?utm_source=saaspasse.beehiiv.com&utm_medium=referral&utm_campaign=brouillard-sur-la-ligne) de [Leviat Legal](https://saaspasse.com/partenaires/leviat-legal?utm_source=saaspasse.beehiiv.com&utm_medium=referral&utm_campaign=brouillard-sur-la-ligne) a décortiqué un cas qui devrait faire suer pas mal de founders. 

Le scénario : une compagnie se vend. Les VCs récupèrent leur mise. Les fondateurs et employés obtiennent zéro. Et 6 des 7 membres du board avaient des conflits d'intérêts. 

CEO avec un bonus négocié en secret avec l'acheteur. CFO idem. Administrateur "indépendant" qui investissait dans les fonds du VC. Beau comité. 

C'est quoi le _dual fiduciary_ , pourquoi ta _waterfall_ de liquidation peut te coûter des millions, et comment te protéger avant que ce soit urgent — Guillaume l'explique clairement. 

Genre de post que tu lis maintenant, pas juste quand t'en as besoin. 👇 

[ Lire le post complet ](https://www.linkedin.com/posts/guillaume-falardeau-b213768b_jai-entendu-une-histoire-de-fou-une-entreprise-share-7449807822101372929-brPc?utm_source=share&utm_medium=member_desktop&rcm=ACoAAAtGvEwBMjZr6fTGqSsX7sYnLbJ1Y9DB7lA)

### Rejoins les SaaSpals 👇 

Merci tellement à tous [nos SaaSpals](https://saaspasse.beehiiv.com/c/saaspals). Votre support nous motive _**BIG TIME**_. 

[![](https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/7acf8ce8-6a80-4794-aa1c-cc3ea311f3c4/Upgrade_CTA_-_beehiiv.jpg?t=1727976675)](https://saaspasse.beehiiv.com/upgrade)

### Partenaires certifiés SaaSpasse 💜

_HUGE_ merci à tous nos partenaires certifiés pour cette année : 

  * [Le Chiffre](https://www.saaspasse.com/partenaires/le-chiffre?utm_source=saaspasse.beehiiv.com&utm_medium=referral&utm_campaign=brouillard-sur-la-ligne) 🧾 

  * [Leviat](https://www.saaspasse.com/partenaires/leviat-legal?utm_source=saaspasse.beehiiv.com&utm_medium=referral&utm_campaign=brouillard-sur-la-ligne) 👨‍⚖️ 

  * [Baseline](https://www.saaspasse.com/partenaires/baseline?utm_source=saaspasse.beehiiv.com&utm_medium=referral&utm_campaign=brouillard-sur-la-ligne) 🤖 

  * [Unicorne](https://www.saaspasse.com/partenaires/unicorne?utm_source=saaspasse.beehiiv.com&utm_medium=referral&utm_campaign=brouillard-sur-la-ligne) 🌩️ 

  * [Finalta Capital](https://www.saaspasse.com/partenaires/finalta-capital?utm_source=saaspasse.beehiiv.com&utm_medium=referral&utm_campaign=brouillard-sur-la-ligne) 💰

### Podcast

Voici le dernier épisode du pod : 

**→**[**Ep.178 - Le gardien des héritages (40M$, death tech & AI)**](https://saaspasse.com/episode/episode-178-le-gardien-des-heritages-40m-death-tech-ai/?utm_source=saaspasse.beehiiv.com&utm_medium=referral&utm_campaign=brouillard-sur-la-ligne)

Pas encore abonné au pod? Let’s go : 

  * [Spotify](https://saaspasse.us21.list-manage.com/track/click?u=08069c7a09572a6f53206b186&id=2175264455&e=f6fe3433c4&utm_source=saaspasse.beehiiv.com&utm_medium=referral&utm_campaign=brouillard-sur-la-ligne)

  * [Apple Podcasts](https://saaspasse.us21.list-manage.com/track/click?u=08069c7a09572a6f53206b186&id=41dc209695&e=f6fe3433c4&utm_source=saaspasse.beehiiv.com&utm_medium=referral&utm_campaign=brouillard-sur-la-ligne)

  * [YouTube](https://saaspasse.us21.list-manage.com/track/click?u=08069c7a09572a6f53206b186&id=0db39a54bc&e=f6fe3433c4&utm_source=saaspasse.beehiiv.com&utm_medium=referral&utm_campaign=brouillard-sur-la-ligne)

_Okay bobye!_

