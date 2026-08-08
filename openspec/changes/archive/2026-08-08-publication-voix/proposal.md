## Why

La skillothèque fonctionne : quatre voix installées, un format contractualisé, une règle d'admission exécutable, deux tests qui se rejouent. Elle n'existe que sur une machine.

La publication était délibérément différée par le change précédent, et pour une raison écrite noir sur blanc : `voix/guy-debord/SKILL.md` définit la récupération comme *« la manière dont le spectacle absorbe toute révolte, toute avant-garde, tout geste authentique, et le revend comme style — le destin qui attend tout ce qui réussit »*. Publier une skillothèque anticapitaliste sur une place de marché de plugins, à côté de `marketing:seo-audit`, en est l'illustration littérale.

La décision de publier est prise. Ce change ne rouvre pas ce débat : il choisit **la forme de publication qui résiste le mieux à ce qu'elle expose**. Concrètement, cela veut dire une licence qui refuse l'extraction plutôt qu'un `LICENSE` par défaut, un README qui porte la thèse et sa propre critique plutôt qu'une plaquette, et des voix qui fonctionnent chez quelqu'un qui n'a pas l'outillage privé de l'auteur.

Il y a en outre un blocage technique dur : **les quatre voix référencent 26 fois de l'outillage qui n'existe pas chez le lecteur** — `office-hours`, `plan-ceo-review`, `plan-eng-review`, `cso`, `gstack`. Publiées telles quelles, elles désignent un adversaire invisible. C'est le vrai travail de ce change, et il n'est pas cosmétique : c'est la différence entre un dépôt utilisable et un dépôt à regarder.

## What Changes

- **Portabilité des voix.** Les tables d'inversion visent aujourd'hui des skills nommées. Elles doivent viser **le cadrage** — « le conseil startup qui dit *fais quelque chose que les gens veulent* » — et ne citer l'outillage qu'en exemple facultatif. La compétence est conservée intégralement ; seule la cible est généralisée.
- **Une licence non-permissive, choisie et argumentée.** Un dépôt dont Albini est la conscience financière ne peut pas être publié sous une licence qui autorise l'extraction sans réciprocité. Le choix est un acte politique et il est motivé dans le dépôt, pas seulement déclaré dans un fichier.
- **Un README qui porte la thèse.** Ce que le dépôt conteste, la règle d'admission, le registre, et une section qui nomme sa propre récupération. Pas de badges, pas de promesse, pas de « features ».
- **La publication de l'appareil de validation** — `REGISTRE.md`, `DISJONCTION.md`, `SILENCE.md` et les jeux d'evals. Ce sont les pièces qui rendent le dépôt reproductible par un tiers plutôt que consommable.
- **La publication du raisonnement** — `openspec/`, y compris le change archivé. Montrer le travail au lieu de montrer le produit est cohérent avec ce que le dépôt soutient ; c'est aussi ce qui permet à quelqu'un d'admettre une huitième voix sans deviner les règles.
- **Création du dépôt distant** `constructions-incongrues/voix` et premier envoi.

## Capabilities

### New Capabilities

- `portabilite-voix` : une voix publiée doit fonctionner sans l'outillage privé de son auteur. Vise un cadrage et non une skill nommée ; toute référence à un outil tiers est un exemple, jamais une dépendance.
- `publication-depot` : ce qui est publié et sous quelles conditions — périmètre des fichiers, licence non-permissive motivée, README portant la thèse et sa propre critique, et l'appareil de reproduction (registre, tests, evals).

### Modified Capabilities

- `format-voix` : ajout d'une exigence de portabilité au contrat d'écriture d'une voix. Aujourd'hui le format garantit qu'une voix est routable et vérifiable ; il ne garantit pas qu'elle soit lisible hors de la machine de son auteur.

## Impact

- **`voix/*/SKILL.md`** — réécriture des sections de sparring des quatre voix. Risque de régression sur des déclencheurs éprouvés : `DISJONCTION.md` et `SILENCE.md` doivent être rejoués après.
- **Nouveaux fichiers** — `README.md`, `LICENSE`, et la note qui motive le choix de licence.
- **`openspec/specs/format-voix/spec.md`** — une exigence ajoutée.
- **Dépôt distant** — création de `constructions-incongrues/voix` (inexistant à ce jour ; l'orga compte 145 dépôts, dont 5 déjà en AGPL-3.0), ajout du remote, premier push.
- **Aucun code applicatif.**

## Hors périmètre

- **La sentinelle.** Toujours le change suivant, et donc la cible « me contredire sans que je l'aie demandé » reste non servie.
- **Le lot 2** — Federici, Ostrom, Polanyi. Publier quatre voix éprouvées vaut mieux que sept dont trois non testées.
- **La distribution en plugin installable** (`.claude-plugin/marketplace.json`). Un dépôt clonable avec `install.sh` suffit à qui veut s'en servir ; l'installation en une commande depuis une place de marché est exactement le geste qui transforme la critique en produit. À rouvrir sciemment, pas par confort.
