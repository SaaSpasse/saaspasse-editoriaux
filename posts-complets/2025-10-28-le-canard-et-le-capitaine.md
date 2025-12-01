---
date: '2025-10-28'
title: Le canard et le capitaine
url: https://saaspasse.beehiiv.com/p/le-canard-et-le-capitaine
slug: le-canard-et-le-capitaine
source: beehiiv
word_count: 1947
reading_time_min: 9
editorial_confidence: high
liens_internes: 34
liens_externes: 1
top_domains:
- domain: hp.beehiiv.com
  count: 1
utm_detectes:
- url: https://saaspasse.beehiiv.com/p/le-canard-et-le-capitaine?utm_source=saaspasse.beehiiv.com&utm_medium=newsletter&utm_campaign=le-canard-et-le-capitaine
- url: https://www.linkedin.com/in/martgagnon/?utm_source=saaspasse.beehiiv.com&utm_medium=newsletter&utm_campaign=le-canard-et-le-capitaine
- url: https://every.to/chain-of-thought/the-knowledge-economy-is-over-welcome-to-the-allocation-economy?utm_source=saaspasse.beehiiv.com&utm_medium=newsletter&utm_campaign=le-canard-et-le-capitaine
- url: https://www.linkedin.com/in/frankln/?utm_source=saaspasse.beehiiv.com&utm_medium=newsletter&utm_campaign=le-canard-et-le-capitaine
- url: https://saaspasse.beehiiv.com/c/saaspals?utm_source=saaspasse.beehiiv.com&utm_medium=newsletter&utm_campaign=le-canard-et-le-capitaine
- url: https://www.linkedin.com/in/remiprev/?utm_source=saaspasse.beehiiv.com&utm_medium=newsletter&utm_campaign=le-canard-et-le-capitaine
- url: https://saaspasse.beehiiv.com/upgrade?utm_source=saaspasse.beehiiv.com&utm_medium=newsletter&utm_campaign=le-canard-et-le-capitaine
- url: https://www.linkedin.com/in/jd-saint-martin-57b31022/?utm_source=saaspasse.beehiiv.com&utm_medium=newsletter&utm_campaign=le-canard-et-le-capitaine
- url: https://revstarsummit.com/?utm_source=saaspasse.beehiiv.com&utm_medium=newsletter&utm_campaign=le-canard-et-le-capitaine
- url: https://www.saaspasse.com/partenaires/vasco?utm_source=saaspasse.beehiiv.com&utm_medium=newsletter&utm_campaign=le-canard-et-le-capitaine
personnes:
- nom: Martin Gagnon
  linkedin: https://www.linkedin.com/in/martgagnon/?utm_source=saaspasse.beehiiv.com
- nom: Rémi
  linkedin: https://www.linkedin.com/in/remiprev/?utm_source=saaspasse.beehiiv.com
- nom: JD Saint-Martin
  linkedin: https://www.linkedin.com/in/jd-saint-martin-57b31022/?utm_source=saaspasse.beehiiv.com
- nom: David Beauchemin
  linkedin: https://www.linkedin.com/in/david-beauchemin/?utm_source=saaspasse.beehiiv.com
---


# Éditorial (copywriting)

<!-- editorial:start -->
What's up folks,  
Merci d'être là. L’édito d’abord—les nouvelles après.  

Ton cerveau mouillé de codeur à la mitaine va-t-il encore payer le loyer dans 5 ans?   
Pis dans 10?   
Y'a 15 ans, Rémi Prévost entrait chez Mirego comme dev.   
Aujourd'hui, il manage toutes les pratiques tech de la boîte. Applications web, mobiles, des plateformes numériques… pour des gros clients.   
J’ai pris le temps d’enregistrer une convo vidéo 1:1 avec lui sur **comment son équipe utilise Claude Code au quotidien**.   
Pas pour remplacer les devs, mais pour les aider à shipper mieux, plus vite.   
La nuance est critique.   
Parce qu'entre "générer du code magiquement" et "déléguer stratégiquement à un agent autonome", y'a tout un monde.  
Un monde qui ressemble étrangement à... du management humain?   
Parlons-en.   
(conversation vidéo en intégralité incluant _screen-sharing_ dispo plus bas)  
  
### De zero-shot à rubber duck avec des bras  
  
Avant, les outils d'AI pour devs, c'était binaire.   
Tu commences à écrire une ligne de code → ça la finit → fin.   
Ou ben :   
Tu écris un prompt → ça te génère du code → tu copies-colles → fin.   
One-shot. Statique. Le modèle attendait tes ordres avant de bouger.   
Maintenant? C'est une conversation. Une _loop_ de _feedback_ continue.   
Claude Code inspecte ton _code base_ de façon autonome. Il pose des questions. Il cherche de l'information, observe les résultats et corrige.   
Rémi compare ça au _rubber duck debugging_ — cette pratique de parler à un petit canard en plastique sur ton bureau pour démêler un problème en l'expliquant à voix haute.   
Sauf que là, le canard répond. Pis il peut écrire du code pendant 7 heures si tu lui demandes.   
![](https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/fac6082d-35fb-4213-8079-280e274b0408/CleanShot_2025-10-28_at_17.40.25_2x.png?t=1761687650)  
Joëlle se pratique encore avec les images AI-gen 😅  
  
###  _Ownership_ non-négociable  
  
Rémi pis sa gang ont une règle béton : **le ou la dev est** _**owner**_**du code final. Point.**  
Ça veut dire quoi, concrètement?   
  
  * Toute modification générée par Claude doit être approuvée manuellement par un humain 
  * Code review nécessaire avant de merge quoi que ce soit en production 
  * Phrase interdite dans l'équipe : "C'est Claude qui a généré ça 🤷‍♂️" 

  
Si t'es pas satisfait du résultat généré, c'est _**on you**_. Pas de la faute à Claude. Y’a déjà le dos assez large, pauvre Claude.   
[Martin Gagnon](https://www.linkedin.com/in/martgagnon/?utm_source=saaspasse.beehiiv.com&utm_medium=newsletter&utm_campaign=le-canard-et-le-capitaine), co-founder de Mirego, le résume bien :   
❝   
Si l'AI te génère du code qui ne te satisfait pas, c'est à toi de lui dire comment itérer jusqu'à temps que tu sois satisfait.  
Autrement dit, Claude Code, c’est une lampe à l’huile avec un génie dedans. Mais c’est ta job de gérer le génie. Tu le manages, le guides et tu délègues stratégiquement.   
  
### Tests automatiques = filet de sécurité  
  
Le principal _guardrail_ chez du _agentic coding_ → les tests automatiques.   
Ta suite de tests doit passer avant de _merge_. Non-négociable.   
Un LLM, ça peut générer une quantité infinie de code. Mais le output reste… **probabiliste**. Il prédit le prochain token le plus probable, pas le code idéal pour ton use case à 100%.   
Les tests, eux, restent une barrière **déterministe** qui protège l’intégralité de ton _code base_.   
Rémi le dit clairement :   
❝   
C'est exactement la même problématique qu'en 2015 avec Stack Overflow, mais à plus grande échelle.  
Avant, les juniors copiaient-collaient du code de Stack Overflow sans trop comprendre le pourquoi du comment.   
Maintenant, c'est pareil. Mais x100. Pis ça va beaucoup plus vite.   
D'où l'importance de garder des humains dans ta _team_ qui comprennent pourquoi le code a été écrit comme ça.   
  
### Le _workflow_ en action  
  
On rentre dans le croustillant, folks.   
Rémi m'a montré un _refactoring_ live : splitter un attribut "name" en "first_name" + "last_name" dans un projet Ruby on Rails open source.   
Le flow de Claude Code :   
  
  1. **Analyse du contexte** : Claude lit le README, les dépendances, la structure du projet 
  2. **Génération d'un plan technique détaillé** : il propose une approche step-by-step 
  3. **Demande de permissions** : avant chaque modification de fichier, il demande l'approbation 
  4. **Exécution avec feedback visuel** : tokens utilisés, commandes bash exécutées, tout est transparent 
  5. **Tests automatiques** : la suite de tests roule pour valider que rien n'a cassé 
  6. **Commit avec co-author tag** : le commit est fait avec Claude marqué comme co-auteur 

  
Temps estimé manuellement : quelques heures.  
Temps avec Claude Code : 15 minutes.   
Mais attention à la règle **80/20** de Rémi : le premier 80% va vite, mais le 20% final est critique et demande tes vraies compétences de dev.  
C'est là que t'as besoin d'expertise humaine pour le _refinement_ , les _edge cases_ , la qualité finale. Feature estimée en 5 jours? Tu peux la faire en 1-2 jours avec Claude. Mais le polissage final peut ramener ça à 4 jours total (des fois).   
**Les compétences humaines deviennent plus importantes, pas moins. Elles sont juste déployées différemment.**  
  
### Pas de _silver bullet_ dans l'écosystème  
  
Claude Code, Cursor, OpenAI Codex, OpenCode... ils sont tous "assez bons" pour un usage quotidien selon Rémi.   
La course n'est pas tant sur la qualité fondamentale du modèle. C'est sur les features, l'UX, l'intégration.   
Pis ça change littéralement chaque semaine… nouvelles capacités, nouveaux outils, nouvelle compétition.   
Attention aux benchmarks aussi. SWE-bench, par exemple, est orienté Python. Si tu travailles dans une autre stack, les scores peuvent être moins représentatifs.   
Le principe reste : c'est pas l'outil qui va transformer ton dev process. C'est comment tu l'utilises, comment tu le guides et comment tu valides ses outputs.   
  
### _Bar open_  
  
Chez Mirego, ils laissent l'équipe expérimenter. Pas de procédure rigide imposée top-down.   
Tu veux essayer Cursor? Go! Claude Code? Parfa! Un autre outil? Vas-y donc!   
Les _early adopters_ vont triper. Les réticents vont traîner de la patte.   
L'important :   
  
  * Commencer petit 
  * Aller chercher des gains incrémentaux 
  * Cultiver le bon _mindset_ dans l'équipe 
  * Mettre en place des _guardrails_ déterministes (tests, code review) 
  * Encourager l'expérimentation sans paralyser avec des règles 

  
Pas de révolution du jour au lendemain mais des améliorations quotidiennes qui s'accumulent.   
  
### Le mindset à la bonne place  
  
Il faut aborder l’utilisation de ces outils comme si tu délègues de la job à un humain.   
Tu dirais pas "mon junior a écrit du code de marde, c'est sa faute", tu dirais "j'ai mal expliqué ce que je voulais, faut que je sois plus clair dans mes instructions".  
(**ou en tk, je l’espère pour tes juniors)**  
Même principe avec les agents.   
C'est un _mindset_ de **management et**[**d'allocation**](https://every.to/chain-of-thought/the-knowledge-economy-is-over-welcome-to-the-allocation-economy?utm_source=saaspasse.beehiiv.com&utm_medium=newsletter&utm_campaign=le-canard-et-le-capitaine). Tu distribues des tâches. Tu valides les résultats. Tu guides. Tu itères.   
Si le _output_ est pas bon, c'est à toi de clarifier le _input_. Donne plus de contexte. Ajoute des exemples. Dis-lui "_what good looks like_ ".   
Rémi insiste : cultiver ce _mindset_ dans l'équipe, c'est encore plus important que choisir le bon outil.   
  
### _Back to the future_  
  
L'_agentic_ AI change pas juste ce qu'on peut faire techniquement.   
Ça change comment on travaille.   
Pour les devs, les CTOs, les fondateurs tech : c'est le temps d'expérimenter. Pas dans 6 mois. Live là.   
Parce que pendant que tu te demandes si c'est une mode passagère, y'a des équipes qui sont déjà rendues ailleurs dans le futur. 🛸   
Quelque chose à ajouter? Good. Laisse un commentaire ou réponds à ce courriel direct.   
Cheers,   
[Frank](https://www.linkedin.com/in/frankln/?utm_source=saaspasse.beehiiv.com&utm_medium=newsletter&utm_campaign=le-canard-et-le-capitaine) 💜   
  
### 🎥 Claude Code : quand les devs parlent aux agents  
  
Section réservée à [nos SaaSpals](https://saaspasse.beehiiv.com/c/saaspals?utm_source=saaspasse.beehiiv.com&utm_medium=newsletter&utm_campaign=le-canard-et-le-capitaine)! Contient vidéo complète de ma session avec [Rémi](https://www.linkedin.com/in/remiprev/?utm_source=saaspasse.beehiiv.com&utm_medium=newsletter&utm_campaign=le-canard-et-le-capitaine), incluant partage d’écran du _workflow_ avec Claude Code.  
On offre notre contenu premium—sessions pratiques non-dispo sur le pod—en primeur aux SaaSpals. Le reste de l’audience aura accès plus tard.  
Si tu vois ce qui suit, **merci pour le support** 🫶  
Si tu veux voir ce qui suit, [supporte directement SaaSpasse](https://saaspasse.beehiiv.com/upgrade?utm_source=saaspasse.beehiiv.com&utm_medium=newsletter&utm_campaign=le-canard-et-le-capitaine). La vidéo sera dispo en rappel semaine prochaine pour les SaaSpals.  

### MC professionnel, bonjour 👋  
  
![](https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/4538ee1b-ebd5-4e24-8ab7-9b6f939169ec/RevStar.jpeg?t=1761761914)  
Crédit photo : [JD Saint-Martin](https://www.linkedin.com/in/jd-saint-martin-57b31022/?utm_source=saaspasse.beehiiv.com&utm_medium=newsletter&utm_campaign=le-canard-et-le-capitaine)  
J’ai tripé à jouer le rôle de MC pour [RevStar](https://revstarsummit.com/?utm_source=saaspasse.beehiiv.com&utm_medium=newsletter&utm_campaign=le-canard-et-le-capitaine) mercredi!   
Le feedback était bon, et ça a _unlock_ quelques opportunités cool pour SaaSpasse. Hâte d’en parler plus.  
  
Merci à ceux qui étaient sur place, méchante belle _crowd_!  
  
Et bien sûr, gros shoutout à [Vasco](https://www.saaspasse.com/partenaires/vasco?utm_source=saaspasse.beehiiv.com&utm_medium=newsletter&utm_campaign=le-canard-et-le-capitaine), [Lightspeed](https://www.linkedin.com/company/lightspeedcommerce/posts/?feedView=all&utm_source=saaspasse.beehiiv.com&utm_medium=newsletter&utm_campaign=le-canard-et-le-capitaine) et [Boreal Ventures ](https://www.linkedin.com/company/borealvc/?utm_source=saaspasse.beehiiv.com&utm_medium=newsletter&utm_campaign=le-canard-et-le-capitaine)pour une première édition de feu.   

### Les agents AI — le nouveau Excel? 🤖  
  
[![](https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/static_assets/youtube_play_icon.png)[![YouTube video by SaaSpasse](https://i.ytimg.com/vi/5mkfdirataY/maxresdefault.jpg)](https://youtu.be/5mkfdirataY?utm_source=saaspasse.beehiiv.com&utm_medium=newsletter&utm_campaign=le-canard-et-le-capitaine)  
Agents = le nouveau Excel? (Ops AI ft. David, Baseline) ](https://youtu.be/5mkfdirataY?utm_source=saaspasse.beehiiv.com&utm_medium=newsletter&utm_campaign=le-canard-et-le-capitaine)  
Pas besoin d'un post-doc en ML pour automatiser tes processus.  
  
Dans cette capsule avec **[David Beauchemin](https://www.linkedin.com/in/david-beauchemin/?utm_source=saaspasse.beehiiv.com&utm_medium=newsletter&utm_campaign=le-canard-et-le-capitaine)**(@ **[Baseline](https://www.linkedin.com/company/baseline-quebec/?utm_source=saaspasse.beehiiv.com&utm_medium=newsletter&utm_campaign=le-canard-et-le-capitaine)**), on jase de trucs concrets:  
→ Générer une offre de service complète en 6 minutes post-meeting   
→ Suivi CRM automatique avec des drafts d'emails ready to go   
→ Veille concurrentielle hebdo pour ~2$/mois   
→ Quand automatiser  
  
Ah et, on parle aussi de ce qui marche pas avec les LLMs et pourquoi il faut garder un humain _in the loop_.   
[ Regarde ça! ](https://?utm_source=saaspasse.beehiiv.com&utm_medium=newsletter&utm_campaign=le-canard-et-le-capitaine)  

### Tu veux réparer ta croissance? 📈  
  
[![](https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/static_assets/youtube_play_icon.png)[![YouTube video by SaaSpasse](https://i.ytimg.com/vi/DjRfxrclh8s/maxresdefault.jpg)](https://youtu.be/DjRfxrclh8s?utm_source=saaspasse.beehiiv.com&utm_medium=newsletter&utm_campaign=le-canard-et-le-capitaine)  
''Pourquoi ton marketing SaaS brûle du cash'' avec Charbel Farah (ex-Lighspeed, ex-Google) ](https://youtu.be/DjRfxrclh8s?utm_source=saaspasse.beehiiv.com&utm_medium=newsletter&utm_campaign=le-canard-et-le-capitaine)  
Commence par regarder cette capsule, tu vas capoter.  
  
Charbel Farah (et ses 17 ans d’expérience dans le domaine) nous parle de :   
  
• Focus sur un seul channel  
• POAS > ROAS  
• Réparer l'attribution avant de brûler du cash en ads+  
• Aborder Google Ads avec des attentes réalistes  
• Et plus encore...  
  
Encore mieux, lâche un ping à Charbel et son équipe chez Digital Growth Core pour qu’ils t’aident à réparer ce qui fonctionnent pas 👇   
[ Pas game de cliquer ici ](https://www.saaspasse.com/partenaires/digital-growth-core?utm_source=saaspasse.beehiiv.com&utm_medium=newsletter&utm_campaign=le-canard-et-le-capitaine)
<!-- editorial:end -->

Comment Rémi Prévost utilise Claude Code 🦆 ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ 

| | | |  31st octobre 2025 | [Read Online](https://saaspasse.beehiiv.com/p/le-canard-et-le-capitaine?utm_source=saaspasse.beehiiv.com&utm_medium=newsletter&utm_campaign=le-canard-et-le-capitaine)  

#  Le canard et le capitaine 

Comment Rémi Prévost utilise Claude Code 🦆   
| | | What's up folks,  
| | Merci d'être là. L’édito d’abord—les nouvelles après.  
| | 
Ton cerveau mouillé de codeur à la mitaine va-t-il encore payer le loyer dans 5 ans?   
Pis dans 10?   
Y'a 15 ans, Rémi Prévost entrait chez Mirego comme dev.   
Aujourd'hui, il manage toutes les pratiques tech de la boîte. Applications web, mobiles, des plateformes numériques… pour des gros clients.   
J’ai pris le temps d’enregistrer une convo vidéo 1:1 avec lui sur **comment son équipe utilise Claude Code au quotidien**.   
Pas pour remplacer les devs, mais pour les aider à shipper mieux, plus vite.   
La nuance est critique.   
Parce qu'entre "générer du code magiquement" et "déléguer stratégiquement à un agent autonome", y'a tout un monde.  
Un monde qui ressemble étrangement à... du management humain?   
Parlons-en.   
(conversation vidéo en intégralité incluant _screen-sharing_ dispo plus bas)  
  
### De zero-shot à rubber duck avec des bras  
  
Avant, les outils d'AI pour devs, c'était binaire.   
Tu commences à écrire une ligne de code → ça la finit → fin.   
Ou ben :   
Tu écris un prompt → ça te génère du code → tu copies-colles → fin.   
One-shot. Statique. Le modèle attendait tes ordres avant de bouger.   
Maintenant? C'est une conversation. Une _loop_ de _feedback_ continue.   
Claude Code inspecte ton _code base_ de façon autonome. Il pose des questions. Il cherche de l'information, observe les résultats et corrige.   
Rémi compare ça au _rubber duck debugging_ — cette pratique de parler à un petit canard en plastique sur ton bureau pour démêler un problème en l'expliquant à voix haute.   
Sauf que là, le canard répond. Pis il peut écrire du code pendant 7 heures si tu lui demandes.   
| ![](https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/fac6082d-35fb-4213-8079-280e274b0408/CleanShot_2025-10-28_at_17.40.25_2x.png?t=1761687650)  
Joëlle se pratique encore avec les images AI-gen 😅  
  
###  _Ownership_ non-négociable  
  
Rémi pis sa gang ont une règle béton : **le ou la dev est** _**owner**_**du code final. Point.**  
Ça veut dire quoi, concrètement?   
  
  * Toute modification générée par Claude doit être approuvée manuellement par un humain 
  * Code review nécessaire avant de merge quoi que ce soit en production 
  * Phrase interdite dans l'équipe : "C'est Claude qui a généré ça 🤷‍♂️" 

  
Si t'es pas satisfait du résultat généré, c'est _**on you**_. Pas de la faute à Claude. Y’a déjà le dos assez large, pauvre Claude.   
[Martin Gagnon](https://www.linkedin.com/in/martgagnon/?utm_source=saaspasse.beehiiv.com&utm_medium=newsletter&utm_campaign=le-canard-et-le-capitaine), co-founder de Mirego, le résume bien :   
| |  ❝   
Si l'AI te génère du code qui ne te satisfait pas, c'est à toi de lui dire comment itérer jusqu'à temps que tu sois satisfait.  
Autrement dit, Claude Code, c’est une lampe à l’huile avec un génie dedans. Mais c’est ta job de gérer le génie. Tu le manages, le guides et tu délègues stratégiquement.   
  
### Tests automatiques = filet de sécurité  
  
Le principal _guardrail_ chez du _agentic coding_ → les tests automatiques.   
Ta suite de tests doit passer avant de _merge_. Non-négociable.   
Un LLM, ça peut générer une quantité infinie de code. Mais le output reste… **probabiliste**. Il prédit le prochain token le plus probable, pas le code idéal pour ton use case à 100%.   
Les tests, eux, restent une barrière **déterministe** qui protège l’intégralité de ton _code base_.   
Rémi le dit clairement :   
| |  ❝   
C'est exactement la même problématique qu'en 2015 avec Stack Overflow, mais à plus grande échelle.  
Avant, les juniors copiaient-collaient du code de Stack Overflow sans trop comprendre le pourquoi du comment.   
Maintenant, c'est pareil. Mais x100. Pis ça va beaucoup plus vite.   
D'où l'importance de garder des humains dans ta _team_ qui comprennent pourquoi le code a été écrit comme ça.   
  
### Le _workflow_ en action  
  
On rentre dans le croustillant, folks.   
Rémi m'a montré un _refactoring_ live : splitter un attribut "name" en "first_name" + "last_name" dans un projet Ruby on Rails open source.   
Le flow de Claude Code :   
  
  1. **Analyse du contexte** : Claude lit le README, les dépendances, la structure du projet 
  2. **Génération d'un plan technique détaillé** : il propose une approche step-by-step 
  3. **Demande de permissions** : avant chaque modification de fichier, il demande l'approbation 
  4. **Exécution avec feedback visuel** : tokens utilisés, commandes bash exécutées, tout est transparent 
  5. **Tests automatiques** : la suite de tests roule pour valider que rien n'a cassé 
  6. **Commit avec co-author tag** : le commit est fait avec Claude marqué comme co-auteur 

  
Temps estimé manuellement : quelques heures.  
Temps avec Claude Code : 15 minutes.   
Mais attention à la règle **80/20** de Rémi : le premier 80% va vite, mais le 20% final est critique et demande tes vraies compétences de dev.  
C'est là que t'as besoin d'expertise humaine pour le _refinement_ , les _edge cases_ , la qualité finale. Feature estimée en 5 jours? Tu peux la faire en 1-2 jours avec Claude. Mais le polissage final peut ramener ça à 4 jours total (des fois).   
**Les compétences humaines deviennent plus importantes, pas moins. Elles sont juste déployées différemment.**  
  
### Pas de _silver bullet_ dans l'écosystème  
  
Claude Code, Cursor, OpenAI Codex, OpenCode... ils sont tous "assez bons" pour un usage quotidien selon Rémi.   
La course n'est pas tant sur la qualité fondamentale du modèle. C'est sur les features, l'UX, l'intégration.   
Pis ça change littéralement chaque semaine… nouvelles capacités, nouveaux outils, nouvelle compétition.   
Attention aux benchmarks aussi. SWE-bench, par exemple, est orienté Python. Si tu travailles dans une autre stack, les scores peuvent être moins représentatifs.   
Le principe reste : c'est pas l'outil qui va transformer ton dev process. C'est comment tu l'utilises, comment tu le guides et comment tu valides ses outputs.   
  
### _Bar open_  
  
Chez Mirego, ils laissent l'équipe expérimenter. Pas de procédure rigide imposée top-down.   
Tu veux essayer Cursor? Go! Claude Code? Parfa! Un autre outil? Vas-y donc!   
Les _early adopters_ vont triper. Les réticents vont traîner de la patte.   
L'important :   
  
  * Commencer petit 
  * Aller chercher des gains incrémentaux 
  * Cultiver le bon _mindset_ dans l'équipe 
  * Mettre en place des _guardrails_ déterministes (tests, code review) 
  * Encourager l'expérimentation sans paralyser avec des règles 

  
Pas de révolution du jour au lendemain mais des améliorations quotidiennes qui s'accumulent.   
  
### Le mindset à la bonne place  
  
Il faut aborder l’utilisation de ces outils comme si tu délègues de la job à un humain.   
Tu dirais pas "mon junior a écrit du code de marde, c'est sa faute", tu dirais "j'ai mal expliqué ce que je voulais, faut que je sois plus clair dans mes instructions".  
(**ou en tk, je l’espère pour tes juniors)**  
Même principe avec les agents.   
C'est un _mindset_ de **management et**[**d'allocation**](https://every.to/chain-of-thought/the-knowledge-economy-is-over-welcome-to-the-allocation-economy?utm_source=saaspasse.beehiiv.com&utm_medium=newsletter&utm_campaign=le-canard-et-le-capitaine). Tu distribues des tâches. Tu valides les résultats. Tu guides. Tu itères.   
Si le _output_ est pas bon, c'est à toi de clarifier le _input_. Donne plus de contexte. Ajoute des exemples. Dis-lui "_what good looks like_ ".   
Rémi insiste : cultiver ce _mindset_ dans l'équipe, c'est encore plus important que choisir le bon outil.   
  
### _Back to the future_  
  
L'_agentic_ AI change pas juste ce qu'on peut faire techniquement.   
Ça change comment on travaille.   
Pour les devs, les CTOs, les fondateurs tech : c'est le temps d'expérimenter. Pas dans 6 mois. Live là.   
Parce que pendant que tu te demandes si c'est une mode passagère, y'a des équipes qui sont déjà rendues ailleurs dans le futur. 🛸   
Quelque chose à ajouter? Good. Laisse un commentaire ou réponds à ce courriel direct.   
Cheers,   
[Frank](https://www.linkedin.com/in/frankln/?utm_source=saaspasse.beehiiv.com&utm_medium=newsletter&utm_campaign=le-canard-et-le-capitaine) 💜   
  
### 🎥 Claude Code : quand les devs parlent aux agents  
  
| | Section réservée à [nos SaaSpals](https://saaspasse.beehiiv.com/c/saaspals?utm_source=saaspasse.beehiiv.com&utm_medium=newsletter&utm_campaign=le-canard-et-le-capitaine)! Contient vidéo complète de ma session avec [Rémi](https://www.linkedin.com/in/remiprev/?utm_source=saaspasse.beehiiv.com&utm_medium=newsletter&utm_campaign=le-canard-et-le-capitaine), incluant partage d’écran du _workflow_ avec Claude Code.  
On offre notre contenu premium—sessions pratiques non-dispo sur le pod—en primeur aux SaaSpals. Le reste de l’audience aura accès plus tard.  
Si tu vois ce qui suit, **merci pour le support** 🫶  
Si tu veux voir ce qui suit, [supporte directement SaaSpasse](https://saaspasse.beehiiv.com/upgrade?utm_source=saaspasse.beehiiv.com&utm_medium=newsletter&utm_campaign=le-canard-et-le-capitaine). La vidéo sera dispo en rappel semaine prochaine pour les SaaSpals.  

### MC professionnel, bonjour 👋  
  
| ![](https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/4538ee1b-ebd5-4e24-8ab7-9b6f939169ec/RevStar.jpeg?t=1761761914)  
Crédit photo : [JD Saint-Martin](https://www.linkedin.com/in/jd-saint-martin-57b31022/?utm_source=saaspasse.beehiiv.com&utm_medium=newsletter&utm_campaign=le-canard-et-le-capitaine)  
J’ai tripé à jouer le rôle de MC pour [RevStar](https://revstarsummit.com/?utm_source=saaspasse.beehiiv.com&utm_medium=newsletter&utm_campaign=le-canard-et-le-capitaine) mercredi!   
Le feedback était bon, et ça a _unlock_ quelques opportunités cool pour SaaSpasse. Hâte d’en parler plus.  
  
Merci à ceux qui étaient sur place, méchante belle _crowd_!  
  
Et bien sûr, gros shoutout à [Vasco](https://www.saaspasse.com/partenaires/vasco?utm_source=saaspasse.beehiiv.com&utm_medium=newsletter&utm_campaign=le-canard-et-le-capitaine), [Lightspeed](https://www.linkedin.com/company/lightspeedcommerce/posts/?feedView=all&utm_source=saaspasse.beehiiv.com&utm_medium=newsletter&utm_campaign=le-canard-et-le-capitaine) et [Boreal Ventures ](https://www.linkedin.com/company/borealvc/?utm_source=saaspasse.beehiiv.com&utm_medium=newsletter&utm_campaign=le-canard-et-le-capitaine)pour une première édition de feu.   

### Les agents AI — le nouveau Excel? 🤖  
  
[| | ![](https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/static_assets/youtube_play_icon.png)[![YouTube video by SaaSpasse](https://i.ytimg.com/vi/5mkfdirataY/maxresdefault.jpg)](https://youtu.be/5mkfdirataY?utm_source=saaspasse.beehiiv.com&utm_medium=newsletter&utm_campaign=le-canard-et-le-capitaine)  
Agents = le nouveau Excel? (Ops AI ft. David, Baseline) ](https://youtu.be/5mkfdirataY?utm_source=saaspasse.beehiiv.com&utm_medium=newsletter&utm_campaign=le-canard-et-le-capitaine)  
Pas besoin d'un post-doc en ML pour automatiser tes processus.  
  
Dans cette capsule avec **[David Beauchemin](https://www.linkedin.com/in/david-beauchemin/?utm_source=saaspasse.beehiiv.com&utm_medium=newsletter&utm_campaign=le-canard-et-le-capitaine)**(@ **[Baseline](https://www.linkedin.com/company/baseline-quebec/?utm_source=saaspasse.beehiiv.com&utm_medium=newsletter&utm_campaign=le-canard-et-le-capitaine)**), on jase de trucs concrets:  
→ Générer une offre de service complète en 6 minutes post-meeting   
→ Suivi CRM automatique avec des drafts d'emails ready to go   
→ Veille concurrentielle hebdo pour ~2$/mois   
→ Quand automatiser  
  
Ah et, on parle aussi de ce qui marche pas avec les LLMs et pourquoi il faut garder un humain _in the loop_.   
| | [ Regarde ça! ](https://?utm_source=saaspasse.beehiiv.com&utm_medium=newsletter&utm_campaign=le-canard-et-le-capitaine)  

### Tu veux réparer ta croissance? 📈  
  
[| | ![](https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/static_assets/youtube_play_icon.png)[![YouTube video by SaaSpasse](https://i.ytimg.com/vi/DjRfxrclh8s/maxresdefault.jpg)](https://youtu.be/DjRfxrclh8s?utm_source=saaspasse.beehiiv.com&utm_medium=newsletter&utm_campaign=le-canard-et-le-capitaine)  
''Pourquoi ton marketing SaaS brûle du cash'' avec Charbel Farah (ex-Lighspeed, ex-Google) ](https://youtu.be/DjRfxrclh8s?utm_source=saaspasse.beehiiv.com&utm_medium=newsletter&utm_campaign=le-canard-et-le-capitaine)  
Commence par regarder cette capsule, tu vas capoter.  
  
Charbel Farah (et ses 17 ans d’expérience dans le domaine) nous parle de :   
  
• Focus sur un seul channel  
• POAS > ROAS  
• Réparer l'attribution avant de brûler du cash en ads+  
• Aborder Google Ads avec des attentes réalistes  
• Et plus encore...  
  
Encore mieux, lâche un ping à Charbel et son équipe chez Digital Growth Core pour qu’ils t’aident à réparer ce qui fonctionnent pas 👇   
| | [ Pas game de cliquer ici ](https://www.saaspasse.com/partenaires/digital-growth-core?utm_source=saaspasse.beehiiv.com&utm_medium=newsletter&utm_campaign=le-canard-et-le-capitaine)  

### Rejoins les SaaSpals 👇   
  
Merci tellement à tous [nos SaaSpals](https://saaspasse.beehiiv.com/c/saaspals?utm_source=saaspasse.beehiiv.com&utm_medium=newsletter&utm_campaign=le-canard-et-le-capitaine). Votre support nous motive _**BIG TIME**_.   
| [![](https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/7acf8ce8-6a80-4794-aa1c-cc3ea311f3c4/Upgrade_CTA_-_beehiiv.jpg?t=1727976675)](https://saaspasse.beehiiv.com/upgrade?utm_source=saaspasse.beehiiv.com&utm_medium=newsletter&utm_campaign=le-canard-et-le-capitaine)  

| 

### Partenaires certifiés SaaSpasse 💜  
  
 _HUGE_ merci à tous nos partenaires certifiés pour cette année :   
  
  * [Le Chiffre](https://www.saaspasse.com/partenaires/le-chiffre?utm_source=saaspasse.beehiiv.com&utm_medium=newsletter&utm_campaign=le-canard-et-le-capitaine) 🧾 
  * [Leviat](https://www.saaspasse.com/partenaires/leviat-legal?utm_source=saaspasse.beehiiv.com&utm_medium=newsletter&utm_campaign=le-canard-et-le-capitaine) 👨‍⚖️ 
  * [Baseline](https://www.saaspasse.com/partenaires/baseline?utm_source=saaspasse.beehiiv.com&utm_medium=newsletter&utm_campaign=le-canard-et-le-capitaine) 🤖 
  * [Unicorne](https://www.saaspasse.com/partenaires/unicorne?utm_source=saaspasse.beehiiv.com&utm_medium=newsletter&utm_campaign=le-canard-et-le-capitaine) 🌩️ 

  

#### Sans oublier **nos partenaires produits** :  
  
  * [Apollo13](https://www.saaspasse.com/partenaires/apollo13?utm_source=saaspasse.beehiiv.com&utm_medium=newsletter&utm_campaign=le-canard-et-le-capitaine) 💻 
  * [Vasco](https://www.saaspasse.com/partenaires/vasco?utm_source=saaspasse.beehiiv.com&utm_medium=newsletter&utm_campaign=le-canard-et-le-capitaine) 🧭 
  * [Missive](https://www.saaspasse.com/partenaires/missive?utm_source=saaspasse.beehiiv.com&utm_medium=newsletter&utm_campaign=le-canard-et-le-capitaine) 💌 

  
_Check ‘em all out_ — on est déjà clients, et on leur envoie régulièrement des clients (maintenant) satisfaits.   
  
### Podcast  
  
Voici le dernier épisode du pod :   
**→**[**Ep.160 - Vincent Guérin : 20 ans à bâtir des ponts (32M$ série B, marketing, leadership)**](https://www.saaspasse.com/episode/episode-160-vincent-guerin-20-ans-a-batir-des-ponts-32m-serie-b-marketing-leadership?utm_source=saaspasse.beehiiv.com&utm_medium=newsletter&utm_campaign=le-canard-et-le-capitaine)  
Pas encore abonné au pod? Let’s go :   
  
  * [Spotify](https://saaspasse.us21.list-manage.com/track/click?u=08069c7a09572a6f53206b186&id=2175264455&e=f6fe3433c4&utm_source=saaspasse.beehiiv.com&utm_medium=newsletter&utm_campaign=le-canard-et-le-capitaine)
  * [Apple Podcasts](https://saaspasse.us21.list-manage.com/track/click?u=08069c7a09572a6f53206b186&id=41dc209695&e=f6fe3433c4&utm_source=saaspasse.beehiiv.com&utm_medium=newsletter&utm_campaign=le-canard-et-le-capitaine)
  * [YouTube](https://saaspasse.us21.list-manage.com/track/click?u=08069c7a09572a6f53206b186&id=0db39a54bc&e=f6fe3433c4&utm_source=saaspasse.beehiiv.com&utm_medium=newsletter&utm_campaign=le-canard-et-le-capitaine)

  
 _Okay bobye!_  
| | | | | [![tw](https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/static_assets/x_light.png)](https://x.com/SaaSpasse?utm_source=saaspasse.beehiiv.com&utm_medium=newsletter&utm_campaign=le-canard-et-le-capitaine)| [![ig](https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/static_assets/instagram_light.png)](https://www.instagram.com/saaspasse/?utm_source=saaspasse.beehiiv.com&utm_medium=newsletter&utm_campaign=le-canard-et-le-capitaine)| [![yt](https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/static_assets/youtube_light.png)](https://www.youtube.com/@SaaSpasse?utm_source=saaspasse.beehiiv.com&utm_medium=newsletter&utm_campaign=le-canard-et-le-capitaine)| [![in](https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/static_assets/linkedin_light.png)](https://www.linkedin.com/company/saaspasse?utm_source=saaspasse.beehiiv.com&utm_medium=newsletter&utm_campaign=le-canard-et-le-capitaine)
---|---|---|---|---|---  
| [![](https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/d5103c55-95d8-40af-9793-bb39a3057ead/Lettres_d_amour__.png?t=1730927524)](https://saaspasse.beehiiv.com/upgrade?utm_source=saaspasse.beehiiv.com&utm_medium=newsletter&utm_campaign=le-canard-et-le-capitaine)  
|  Mettre à jour vos préférences e-mail ou vous désabonner [ ici](https://saaspasse.beehiiv.com/subscribe/SUBSCRIBER_ID/preferences?post_id=e013e8e4-6498-4bd6-900e-0dd38938102d&last_resource_guid=Post%3Ae013e8e4-6498-4bd6-900e-0dd38938102d&utm_source=saaspasse.beehiiv.com&utm_medium=newsletter&utm_campaign=le-canard-et-le-capitaine) © 2025 SaaSpasse  226 Rue Saint-Joseph E  
Quebec, QC G1K3A9, Canada   
| [![beehiiv logo](https://media.beehiiv.com/output-onlinepngtools.png)Powered by beehiiv](https://www.beehiiv.com/?utm_campaign=e013e8e4-6498-4bd6-900e-0dd38938102d&utm_medium=post_email&utm_source=saaspasse)  
[ Terms of Service ](https://hp.beehiiv.com/SUBSCRIBER_ID)

