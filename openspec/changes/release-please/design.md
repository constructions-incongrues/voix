## Context

Le dépôt a adopté Conventional Commits il y a une heure (`adr/0001`, accepté) et n'en tire rien : version posée à la main dans `.claude-plugin/plugin.json`, aucun `CHANGELOG.md`, aucune balise, aucun répertoire `.github/`. Deux commits conformes sont sur `main`, classés *corrective* par le tableau du README, et `0.4.1` n'a pas bougé.

**La contrainte dominante est un ADR en force.** Le garde-fou n°2 de `adr/0001` — décision D3 de son design — pose que *le tableau du README est souverain : les types servent à dériver le niveau, pas à le décider*, au motif que l'axe de version du dépôt est le registre et non le code. release-please calcule la version depuis les types. Les deux ne tiennent pas ensemble.

L'auteur a tranché : **les types deviennent souverains**. Un ADR étant immuable une fois accepté, cela impose un `adr/0002` qui supersède le `0001` — et non une retouche de celui-ci.

Autres contraintes : aucune dépendance runtime (release-please est de la CI, la contrainte tient) ; aucune politique de branches tranchée ; 40 commits poussés en direct sur `main` ; un seul décideur.

## Goals / Non-Goals

**Goals :**
- Dériver le niveau de version de l'historique, sans intervention manuelle sur le numéro.
- Faire coïncider la configuration avec le tableau des trois niveaux du README.
- Garder la publication sous un acte humain explicite.
- Écrire ce que la dérivation ne sait pas voir, faute de pouvoir le rattraper.

**Non-Goals :**
- Vérifier la conformité des messages. C'est la décision D5 de `adr/0001`, inchangée : pas d'outil tant que trois commits non conformes n'ont pas atteint `main`.
- Publier sur un index tiers. Le refus tient, et il est indépendant.
- Trancher la politique de branches. Elle devient un préalable pratique, mais reste une décision distincte — prise depuis, par `adr/0003`.
- Remplacer `openspec/changes/archive/` par un `CHANGELOG.md`.

## Decisions

### D1 — Les types font autorité, et `adr/0002` supersède `adr/0001`

Un ADR accepté ne se modifie pas. `adr/0002` supersède donc `adr/0001` **en entier**, parce que la supersession porte sur le fichier et non sur une ligne — et il **reprend explicitement les trois garde-fous qui restent en force** (description portant un constat, jeux fermés, historique non réécrit). Seul le second, la souveraineté du README, est remplacé.

*Alternative écartée :* modifier le garde-fou n°2 dans `adr/0001`. Interdit par la règle d'immuabilité, et ce serait précisément le geste que le dépôt refuse ailleurs — réécrire un dossier pour qu'il ait l'air à jour.

### D2 — `docs` `refactor` `test` `chore` déclenchent un correctif

Contre le défaut de l'outil, qui ne publie que sur `feat`, `fix` et `BREAKING`. Le tableau du README classe ces types en corrective ; laisser le défaut ferait diverger la configuration et la règle dès le premier commit de documentation — c'est-à-dire immédiatement, les deux commits en attente étant des `docs`.

*Alternative écartée :* laisser le défaut et documenter la divergence. Produit un dépôt dont la règle écrite et l'outil disent deux choses différentes, ce qui est le défaut que ce changement corrige.

### D3 — La publication reste un acte, jamais un effet

release-please ouvre une demande de publication ; rien n'est publié avant sa fusion. Le calcul est automatique, l'acte ne l'est pas.

*Corollaire non trivial :* si le numéro calculé paraît faux, **on corrige le commit fautif, pas le numéro dans la demande**. Éditer le numéro à la main rétablirait l'autorité humaine par la porte de service, et viderait D1 de son sens un mois après l'avoir écrite.

### D4 — `CHANGELOG.md` est un index, pas le journal de bord

Il liste les publications et renvoie à `openspec/changes/archive/`, qui porte le raisonnement entier. Une ligne le dit en tête du fichier.

*Pourquoi :* le dépôt publie ses motifs, pas ses livraisons. Un `CHANGELOG.md` généré depuis des sujets de commit ne porte que des conclusions ; laisser croire qu'il est le dossier appauvrirait ce qui existe.

### D5 — Le type de release est `simple`, avec `extra-files` sur `plugin.json`

Le dépôt n'est ni un paquet npm ni un module Go : c'est de la prose et un script. Le type `simple` suffit, et `extra-files` met à jour le champ `version` de `.claude-plugin/plugin.json`.

*Alternative écartée :* le type `node`. Suppose un `package.json`, que le dépôt n'a pas et ne veut pas.

### D6 — La limite est écrite, faute d'être rattrapable

Sous D1, un type mal choisi produit une version fausse et **rien ne le signale** : `feat(registre):` là où il fallait `feat!(registre):` fait passer l'entrée d'une voix en mineure. Sous l'ancienne règle, le tableau du README rattrapait l'erreur au moment de publier à la main.

Aucune mitigation n'est proposée : le contrôle qui la rattraperait devrait connaître le registre, donc lire `REGISTRE.md` et comparer son contenu avant/après — ce qui est un projet en soi. La limite est portée par une exigence de la spec et par les conséquences de `adr/0002`.

## Risks / Trade-offs

- **Une version fausse passe sans être vue** (D6) → Aucune mitigation. C'est le prix payé pour l'autorité des types, et il est nommé plutôt que dilué. Réexamen si le cas se produit une fois.
- **La publication devient un effet de bord de la fusion** → Mitigation : D3, la demande de publication est un acte séparé. Risque résiduel : l'habitude de fusionner sans lire.
- **Premier `.github/` du dépôt** → Une Action est du code exécuté par un tiers sur le dépôt, ce qu'il n'avait jamais accepté. Ce n'est pas une dépendance runtime, mais c'est une dépendance de processus, et il faut le dire.
- **Le tableau du README change de statut sans changer de forme** → Il devient la description d'une configuration alors qu'il ressemble toujours à une règle. Mitigation : une ligne explicite au README, dans les tâches.
- **La politique de branches non tranchée** → release-please suppose une branche par défaut et des PR. Le dépôt pousse en direct. Non bloquant tant que l'auteur est seul, mais la première contribution externe le rendra bloquant. **Risque levé depuis** par `adr/0003`, qui exempte nommément la branche que release-please se nomme et laisse `main` non protégée tant que le relecteur est l'auteur.

## Migration Plan

1. Écrire `adr/0002`, superséder `0001`, reprendre les trois garde-fous maintenus.
2. Ajouter la configuration release-please et le workflow GitHub.
3. Amender le README : le tableau devient descriptif, et la section « Convention de commit » gagne la règle « on corrige le commit, pas le numéro ».
4. Première publication : elle ramassera les commits déjà sur `main` depuis `0.4.1` — deux `docs`, donc `0.4.2`. *Constaté :* la demande a bien proposé `0.4.2`, puis recalculé `0.5.0` quand `feat(sentinelle)` a atterri avant sa fusion. Publiée le 2026-08-08 en `v0.5.0`.

## Open Questions

- ~~La politique de branches reste non tranchée.~~ **Close** par `adr/0003`, accepté le 2026-08-08 sans superséder `adr/0002`.
- ~~La première publication portera `0.4.2`.~~ Elle a porté **`0.5.0`**. ~~Reste ouverte la seule question de fond : le correctif du journal de la sentinelle est absent du `CHANGELOG` généré — décider s'il y est ajouté à la main.~~ **Tranchée : il n'y est pas ajouté.** Le `CHANGELOG` est un index des publications ; le journal de bord est `openspec/changes/archive/`, où le correctif figure. Corriger à la main un journal dérivé rétablirait l'autorité humaine par la porte de service, ce qu'`adr/0002` refuse pour le numéro de version.
