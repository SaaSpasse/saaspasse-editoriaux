What's up folks,

Merci d'être là. L’édito d’abord—les nouvelles après.

2023. Pic d'adoption ChatGPT… pic d'anxiété face au futur.

À l'époque, [mon psy](https://saaspasse.beehiiv.com/p/le-jour-o-ton-cerveau-l-che?utm_source=saaspasse.beehiiv.com&utm_medium=newsletter&utm_campaign=agents-doubles) m’a partagé une métaphore qui a collé :

Quand ta compagnie est en pleine tempête, t'as besoin d'un capitaine avec les deux pieds plantés sur le deck.

Même si ça tangue, il reste en équilibre. Il regarde l'horizon, *call* des *shots*. Il lit la météo du marché pour comprendre ce qui se passe et ce qui s'en vient.

C'est exactement cette posture que je veux adopter pour [ma conversation live avec Philippe Beaudoin](https://www.eventbrite.ca/e/billets-saaspasse-a-montreal-edition-16-1761428141989?utm_source=saaspasse.beehiiv.com&utm_medium=newsletter&utm_campaign=agents-doubles) semaine prochaine.

On va parler de comment l'AI brasse les cartes, de sécurité des systèmes agentiques, de bonnes pratiques produit pour les *builders*, de gouvernance... et plus encore.

**Mais avant d'y arriver, j'avais besoin de démêler ce que je pense comprendre de ce qui me confond.**

Au milieu de la tempête, les réponses sont souvent floues. Les certitudes, rares.

Alors voici mes notes de préparation. Ce que j'ai pigé jusqu'ici + les endroits où j'ai encore besoin d'être éduqué 👇

### Intelligence vs agency

**Ce que je pense comprendre**

L'inquiétude vis-à-vis l'AI vient pas juste de la montée en intelligence de systèmes difficiles à disséquer*. Elle vient surtout de l'explosion de leur autonomie.

*Même en 2024–2025, les leaders (OpenAI, Anthropic, DeepMind) reconnaissent qu'on ne peut pas reconstruire une causalité interne complète et déterministe des LLMs : les représentations sont distribuées/superposées, des phénomènes comme l'over-squashing brouillent les traces, et les techniques actuelles d'interprétabilité n'offrent qu'une vue partielle. En d’autres mots, c’est compliqué en h***stie, les neural networks.* [1](https://openai.com/index/extracting-concepts-from-gpt-4/?utm_source=saaspasse.beehiiv.com&utm_medium=newsletter&utm_campaign=agents-doubles), [2](https://www.anthropic.com/research/engineering-challenges-interpretability?utm_source=saaspasse.beehiiv.com&utm_medium=newsletter&utm_campaign=agents-doubles), [3](https://proceedings.neurips.cc/paper_files/paper/2024/file/b1d35561c4a4a0e0b6012b2af531e149-Paper-Conference.pdf?utm_source=saaspasse.beehiiv.com&utm_medium=newsletter&utm_campaign=agents-doubles)

Comprendre ≠ accomplir.

À la base, un LLM peut analyser, résumer, expliquer, prédire. Mais il reste statique. Il attend qu'on lui demande quelque chose.

Un agent fixe des objectifs, puis planifie, agit, corrige. Il persiste.

Ça complique la patente.

Parce qu'un système qui comprend mal peut quand même être utile. Mais un système qui comprend mal ET qui agit de façon autonome? On entre dans le territoire des conséquences réelles™️

Les modèles sont probabilistes. Les humains aussi. On raisonne en distributions, pas en certitudes.

Et quand on donne à un système probabiliste la capacité d'agir en boucle—de prendre des décisions, d'exécuter des actions, d'observer les résultats, puis de réajuster—une mauvaise spécification peut rapidement déraper.

*Input* pas clair = *output* (p-ê) nucléaire?

Le fameux scénario des [trombones de Bostrom](https://nickbostrom.com/ethics/ai.pdf?utm_source=saaspasse.beehiiv.com&utm_medium=newsletter&utm_campaign=agents-doubles) illustre bien ça : un système qui optimise aveuglément pour produire des trombones, au point de convertir toute la matière disponible—incluant les humains—en trombones. *Freaky Clippy shit, right*. Caricatural? Absolument. Mais le principe reste valide.

**Ce qui se passe en 2025**

Les agents deviennent accessibles au grand public. Aux PME. Aux *scaleups*.

À ta grand-mère ben *smath*... mais aussi au petit Timmy qui torturait des grenouilles à huit ans en écoutant du métal néo-nazi.

[OpenAI a ](https://openai.com/index/introducing-agentkit/?utm_source=saaspasse.beehiiv.com&utm_medium=newsletter&utm_campaign=agents-doubles)*droppé*[ AgentKit](https://openai.com/index/introducing-agentkit/?utm_source=saaspasse.beehiiv.com&utm_medium=newsletter&utm_campaign=agents-doubles) au DevDay 2025 — un *builder* visuel avec ChatKit, des *evals* pour agents, un *Connector Registry*. [Manus](https://www.manus.app/?utm_source=saaspasse.beehiiv.com&utm_medium=newsletter&utm_campaign=agents-doubles) exécute des projets GTM complets. [Clay](https://saaspasse.beehiiv.com/p/une-bouchee-argile?utm_source=saaspasse.beehiiv.com&utm_medium=newsletter&utm_campaign=agents-doubles), too. [GenSpark](https://www.genspark.ai/?utm_source=saaspasse.beehiiv.com&utm_medium=newsletter&utm_campaign=agents-doubles) se positionne comme un "super agent" *workspace*. [Claude Code](https://www.anthropic.com/claude-code/?utm_source=saaspasse.beehiiv.com&utm_medium=newsletter&utm_campaign=agents-doubles) permet aux devs de déléguer des tâches directement depuis leur terminal. [Codex](https://openai.com/index/codex-now-generally-available/?utm_source=saaspasse.beehiiv.com&utm_medium=newsletter&utm_campaign=agents-doubles) peut travailler 7 heures+ sur des PRs ou des tests.

[Sur Reddit](https://www.reddit.com/r/ClaudeAI/comments/1nph8ka/whats_the_longest_youve_had_claude_run_on_its_own/?utm_source=saaspasse.beehiiv.com&utm_medium=newsletter&utm_campaign=agents-doubles), y'a des threads de gens qui laissent rouler des agents pendant des heures sans supervision.

Oui, les limites existent encore. Fenêtre de contexte. Tokens. Garde-fous. Mais la capacité agentique augmente vite.

Et c'est là que les *evals* et les contrôles deviennent critiques.

Parce qu'un agent qui [tourne en rond pour maximiser une récompense mal définie](https://openai.com/research/faulty-reward-functions?utm_source=saaspasse.beehiiv.com&utm_medium=newsletter&utm_campaign=agents-doubles) (comme dans l'exemple CoastRunners d'OpenAI), c'est drôle dans un jeu vidéo.

Mais quand c'est appliqué à des systèmes qui ont accès à tes données, à tes outils, à tes clients? Moins drôle.

ET À TES BOMBES NUCL—**non** on avait dit pas de *doomer stuff* Frank replante tes pieds sul deck

**Les vraies questions**

> **Comment on balise l'autonomie sans tuer l'utilité?**

Est-ce qu'on peut vraiment remettre le dentifrice dans le tube maintenant que ces capacités sont accessibles à tous?

Comment on pense le risque quand le système ET l'humain sont [stochastiques](https://fr.wikipedia.org/wiki/Stochastique?utm_source=saaspasse.beehiiv.com&utm_medium=newsletter&utm_campaign=agents-doubles) — c'est-à-dire aléatoires, probabilistes, jamais prédictibles au cas par cas?

### Agents x SaaS : pratico-pratique

**Ce que je commence à saisir (sans encore maîtriser)**

Quand je relis mes notes de préparation, y'a des trucs qui commencent à faire du sens. Mais je serais malhonnête de prétendre tout piger.

**La sécurité produit de base**, j'en ai une idée générale : distinguer ta sécurité interne (tes données, ton infra) de celle de tes *users*. Sinon *I guess* principe du moindre privilège, i.e. un agent devrait avoir accès seulement à ce dont il a besoin, pas plus. RBAC (*Role-Based Access Control* — contrôle d'accès basé sur les rôles), périmètres, *sandbox*, *kill-switch* opérateur, etc.

**Nouvelles opportunités de distribution, nouveaux **[risques plateforme](https://saaspasse.beehiiv.com/p/danser-avec-des-geants?utm_source=saaspasse.beehiiv.com&utm_medium=newsletter&utm_campaign=agents-doubles)**…**

Si le [Apps SDK](https://openai.com/index/introducing-apps-in-chatgpt/?utm_source=saaspasse.beehiiv.com&utm_medium=newsletter&utm_campaign=agents-doubles) explose, ChatGPT devient un *workflow control point*. Comme Google ou Facebook sont devenus des *homepages* pour plein de monde, ChatGPT (et compagnie) deviennent des points de passage obligés. [Ça change la donne](https://saaspasse.beehiiv.com/p/vertical-ai?utm_source=saaspasse.beehiiv.com&utm_medium=newsletter&utm_campaign=agents-doubles).

**Les risques agentiques?** Ils montent en flèche. Une *prompt injection* en mode chat, c'est gossant. En mode agent, où les *outputs* pilotent des actions réelles? C'est **x10** plus dangereux. Faut valider, sanitiser, mettre des humains dans la boucle aux endroits critiques.

Y’a des risques économiques aussi. Si [ton pricing](https://www.youtube.com/watch?v=vAw4prSQxDw&utm_source=saaspasse.beehiiv.com&utm_medium=newsletter&utm_campaign=agents-doubles) et tes *unit economics* sont pas bien cadrés en fonction du *usage*… ça peut coûter *mucho dinero*.

**MCP — exposer ton SaaS aux agents**

Là ça devient intéressant. [MCP (](https://docs.anthropic.com/en/docs/mcp?utm_source=saaspasse.beehiiv.com&utm_medium=newsletter&utm_campaign=agents-doubles)*Model Context Protocol*[)](https://docs.anthropic.com/en/docs/mcp?utm_source=saaspasse.beehiiv.com&utm_medium=newsletter&utm_campaign=agents-doubles) c'est pas juste pour *consommer* des agents dans ton produit. C'est aussi pour *exposer* ton SaaS aux agents.

Pense-y : tes futurs "clients" pourraient être des agents AI, pas des humains.

Un agent pourrait appeler ton API pour accomplir une tâche. ChatGPT pourrait utiliser ton SaaS via MCP pour aider un utilisateur. Un agent autonome pourrait s'abonner à ton service.

Ça soulève des questions que j'ai pas encore toutes démêlées :

- Qu'est-ce que t'exposes exactement? Toutes les fonctions de ton UI? Juste des fonctions clés adaptées au mode agent?

- Comment tu *scopes* ça finement? Par ressource? Par rôle?

- Comment tu gères l'authentification quand c'est un agent qui appelle, pas un humain?

- *Dry-run* par défaut? Consentement explicite pour actions critiques?

- Logs complets? Quotas? Tests d'exécution?

**Ce qui me confond encore**

Les évaluations (*evals*).** **J'ai une liste de benchmarks pour évaluer les *modèles* : [HELM](https://crfm.stanford.edu/2022/11/17/helm.html?utm_source=saaspasse.beehiiv.com&utm_medium=newsletter&utm_campaign=agents-doubles), [AgentBench](https://github.com/THUDM/AgentBench?utm_source=saaspasse.beehiiv.com&utm_medium=newsletter&utm_campaign=agents-doubles), [WebArena](https://webarena.dev/?utm_source=saaspasse.beehiiv.com&utm_medium=newsletter&utm_campaign=agents-doubles), [SWE-bench Verified](https://openai.com/index/introducing-swe-bench-verified/?utm_source=saaspasse.beehiiv.com&utm_medium=newsletter&utm_campaign=agents-doubles).

Mais comment penser les *evals* spécifiquement pour des *agents* dans ton produit? C'est différent d'évaluer un modèle en isolation. Un agent interagit avec tes systèmes, prend des décisions, exécute des actions.

Quels outils? Quelles bonnes pratiques? Comment organiser un cycle avant-pendant-après le déploiement sans paralyser la livraison de valeur?

Parce que dans le fond, c'est ça le *tradeoff* : tu veux être prudent, mais pas *paralysé*. Tu veux *shipper*, mais pas *shipper* n'importe quoi.

J'ai pas encore la recette. J'espère que Philippe a quelques ingrédients!

### Gouvernance et grandes questions

Au-delà du pratico-pratique, y'a des questions plus larges qui me trottent dans la tête.

**Qui contrôle quoi?**

On balise l'agency humaine avec des lois, des normes, des sanctions. Ça marche plus ou moins bien, mais au moins y'a un cadre. Pis la civilisation a pas encore explosée.

Pour l'AI agentique? C'est le Far West, I guess.

Qui devrait décider des protocoles? L'industrie qui se *self-régule*? L'État? Un consortium multi-acteurs? Et surtout : est-ce qu'on peut vraiment remettre le dentifrice dans le tube maintenant que ces capacités sont accessibles à tous?

Petit détail pas si mineur : les LLM du paradigme actuel essaient de prédire le prochain *token*, d'imiter ce qu'un humain aurait dit. Ils construisent un modèle du monde basé sur du langage existant. Un modèle peut-être... imparfait? Ça complique pas mal la question de la confiance.

J'ai pas de réponse. Mais j'aimerais entendre Philippe là-dessus!

**Les frameworks de sécurité — consensus ou cacophonie?**

J'ai vu passer des noms : [OWASP Top 10 LLM](https://owasp.org/www-project-top-10-for-large-language-model-applications/?utm_source=saaspasse.beehiiv.com&utm_medium=newsletter&utm_campaign=agents-doubles), [NIST GenAI Profile](https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-generative-artificial-intelligence?utm_source=saaspasse.beehiiv.com&utm_medium=newsletter&utm_campaign=agents-doubles), [Google SAIF](https://www.saif.google/secure-ai-framework?utm_source=saaspasse.beehiiv.com&utm_medium=newsletter&utm_campaign=agents-doubles), [UK Code of Practice](https://www.gov.uk/government/publications/ai-cyber-security-code-of-practice/code-of-practice-for-the-cyber-security-of-ai?utm_source=saaspasse.beehiiv.com&utm_medium=newsletter&utm_campaign=agents-doubles).

Est-ce qu'il y a consensus sur certaines pratiques? Ou chacun tire la couverture de son bord? Lesquels sont vraiment actionnables versus aspirationnels?

**Faut-il de l'agency pour contrôler l'agency?**

Le concept de "[Scientist AI](https://arxiv.org/abs/2502.15657?utm_source=saaspasse.beehiiv.com&utm_medium=newsletter&utm_campaign=agents-doubles)" de LawZero m'intrigue : un shaman scientifique dans sa boîte hermétique. Là pour nous guider mais pas le faire à notre place, genre? Ou bien un garde-fou qui observe, évalue, et peut bloquer des actions risquées. Une sorte de police sur l'autoroute des agents?

Le [Preparedness Framework v2 d'OpenAI](https://openai.com/index/updating-our-preparedness-framework/?utm_source=saaspasse.beehiiv.com&utm_medium=newsletter&utm_campaign=agents-doubles) va un peu dans ce sens — *reasoning monitors*, classifieurs *always-on*, pipelines d'enforcement.

Mais ça soulève une question vertigineuse : si on a besoin d'agents pour surveiller des agents, qui surveille les surveillants? Et quels nouveaux risques ça introduit?

[WHO WATCHES THE WATCHMEN?](https://mir-s3-cdn-cf.behance.net/project_modules/max_1200_webp/fa618531625767.56597451752fb.jpg?utm_source=saaspasse.beehiiv.com&utm_medium=newsletter&utm_campaign=agents-doubles)

### Conclusion

Voilà où j'en suis. Certaines choses claires, d'autres confuses. Certaines réponses, beaucoup de questions.

C'est exactement pour ça qu'on fait cette conversation live avec Philippe la semaine prochaine. Pour démêler tout ça pis garder les pieds plantés sur le *deck* pendant que ça tangue.

Et c'est probablement une conversation que je vais continuer avec d'autres personnes par la suite. Si tu as des noms à me suggérer—des gens qui vivent ces enjeux-là au quotidien—fais-moi signe.

Si tu es dans le même bateau que moi avec des questions, et qu'il y en a que tu aimerais que je pose pendant la conversation live, réponds à ce courriel.

Si tu as des réponses à certaines de ces questions? Même affaire. Réponds au courriel. J'aimerais ça apprendre de toi!

**23 octobre, 18h–21h, chez EY à Montréal.** Premier arrivé, premier servi. Bouffe et *drinks* fournis (merci EY!).

[Viens te planter les pieds sur le ](https://www.eventbrite.ca/e/billets-saaspasse-a-montreal-edition-16-1761428141989?utm_source=saaspasse.beehiiv.com&utm_medium=newsletter&utm_campaign=agents-doubles)*deck*[ avec nous.](https://www.eventbrite.ca/e/billets-saaspasse-a-montreal-edition-16-1761428141989?utm_source=saaspasse.beehiiv.com&utm_medium=newsletter&utm_campaign=agents-doubles)

—

Quelque chose à ajouter? *Good*. Laisse un commentaire ou réponds à ce courriel direct.

Cheers,

[Frank](https://www.linkedin.com/in/frankln/?utm_source=saaspasse.beehiiv.com&utm_medium=newsletter&utm_campaign=agents-doubles) 💜