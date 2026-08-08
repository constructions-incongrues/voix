---
status: "accepted, supersedes ADR-0001"
date: 2026-08-08
decision-makers: Tristan Rivoallan
consulted: —
informed: —
supersedes: ADR-0001
---

# Les types de commit font autorité sur le niveau de version, et release-please publie

## Context and Problem Statement

`adr/0001` a fait entrer Conventional Commits au dépôt. Une heure plus tard, rien ne s'en sert : le numéro de version est toujours posé à la main dans `.claude-plugin/plugin.json`, il n'existe ni `CHANGELOG.md`, ni balise, ni CI. Deux commits conformes sont sur `main`, que le tableau du README classe *corrective*, et `0.4.1` n'a pas bougé. La convention a coûté sans rendre.

Automatiser la publication suppose de trancher une question que `adr/0001` avait tranchée dans l'autre sens. Son garde-fou n°2 posait que **le tableau du README est souverain** : les types servent à *dériver* le niveau, pas à le décider — au motif que l'axe de version de ce dépôt est le registre des voix, non le code. release-please calcule la version depuis les types, mécaniquement. Les deux positions sont incompatibles.

Un ADR accepté ne se modifie pas. Trancher impose donc d'en écrire un nouveau qui supersède le précédent.

## Decision Drivers

- Tirer de la convention le bénéfice pour lequel elle a été adoptée.
- Ne pas laisser coexister une règle écrite et un outil qui disent deux choses différentes.
- Garder la publication sous un acte humain explicite.
- Ne pas ajouter de dépendance runtime.
- Ne pas dissimuler ce que l'automatisation rend invisible.

## Considered Options

1. **release-please, les types faisant autorité** — la version est calculée, le README devient descriptif
2. **release-please en rédacteur de brouillon** — il propose un numéro, l'auteur le corrige quand le registre le contredit ; `adr/0001` survit intact
3. **Automatiser sans release-please** — un script maison lisant `REGISTRE.md` en plus des types
4. **Statu quo** — publication à la main, `adr/0001` inchangé

## Decision Outcome

Chosen option: **« release-please, les types faisant autorité »**, parce que c'est la seule option qui supprime la divergence entre la règle et l'outil au lieu de la déplacer — et parce qu'un numéro calculé puis corrigé à la main (option 2) rétablit l'autorité humaine par la porte de service, ce qui aurait rendu la décision illisible six semaines plus tard.

**Cet ADR supersède `adr/0001` en entier**, la supersession portant sur le fichier. Trois de ses quatre garde-fous restent en force et sont **repris ici sans changement** :

1. **La description reste une phrase qui porte un constat.** `fix(sentinelle): correction de bug` reste conforme à la spécification et refusé au dépôt.
2. ~~Le tableau du README est souverain~~ → **remplacé.** Les types font autorité ; le tableau du README devient la description de la configuration de l'outil, et doit être corrigé si la configuration change.
3. **Les jeux de types et de scopes restent fermés**, élargis par modification de la spécification et jamais par usage de fait.
4. **L'historique antérieur n'est pas réécrit.** Un sujet sans type est *antérieur*, pas *invalide* — et il est donc invisible à l'outil, qui l'ignore.

La décision D5 de `adr/0001` — aucun outil de vérification des messages — n'est pas touchée et reste en force sous son déclencheur d'origine.

### Consequences

- Bon, parce que la convention rend enfin ce pour quoi elle a été adoptée : un niveau dérivé, un journal de publications, une balise, sans geste manuel sur le numéro.
- Bon, parce qu'il ne reste qu'une seule autorité. La règle et l'outil ne peuvent plus diverger, puisque la règle *est* la configuration.
- Bon, parce qu'aucune dépendance runtime n'est ajoutée : release-please est une Action de CI, et l'usager n'installe rien de plus.
- Neutre, parce que la publication reste un acte — une demande de publication ouverte n'a aucun effet tant qu'elle n'est pas fusionnée.
- **Mauvais, parce qu'un type mal choisi produit désormais une version fausse que rien ne signale.** `feat(registre):` là où il fallait `feat!(registre):` fait passer l'entrée d'une voix au registre en mineure. Sous `adr/0001`, le tableau du README rattrapait l'erreur au moment de publier à la main. Ce filet disparaît, et aucune mitigation n'est proposée : le contrôle qui le remplacerait devrait lire `REGISTRE.md` et comparer son état avant et après, ce qui est un projet en soi.
- Mauvais, parce que le dépôt accepte pour la première fois du code tiers exécuté sur lui — une Action GitHub. Ce n'est pas une dépendance runtime, mais c'est une dépendance de processus.
- Mauvais, parce que le tableau du README change de statut sans changer de forme : il ressemblera toujours à une règle en étant devenu une description.

### Confirmation

- **Cohérence règle/outil** — la table du README et la configuration `release-type` listent les mêmes types pour les mêmes niveaux ; relecture croisée à chaque modification de l'une des deux.
- **Publication non automatique** — une demande de publication ouverte et laissée telle quelle ne produit ni balise, ni modification de `plugin.json` sur la branche par défaut.
- **Numéro jamais corrigé à la main** — `git log -p -- .claude-plugin/plugin.json` ne montre que des commits de publication touchant le champ `version`.

## Pros and Cons of the Options

### release-please, les types faisant autorité

- Bon, parce qu'il supprime la divergence entre règle et outil au lieu de la gérer.
- Bon, parce que l'outil est éprouvé, maintenu ailleurs, et que le dépôt n'a rien à écrire ni à entretenir.
- Neutre, parce qu'il impose de configurer `docs` `refactor` `test` `chore` comme correctifs, contre son défaut.
- Mauvais, parce qu'il est aveugle au registre, qui est l'axe de version réel du dépôt.
- Mauvais, parce qu'il supersède un ADR d'une heure — ce qui est honnête mais signale que `adr/0001` avait tranché sans regarder la suite.

### release-please en rédacteur de brouillon

- Bon, parce que `adr/0001` survivait intact et que l'axe registre restait décisif.
- Bon, parce que l'erreur de type restait rattrapable à la relecture de la demande.
- Mauvais, parce que « corriger le numéro à la main quand il paraît faux » est une règle qu'on applique tant qu'on s'en souvient, puis plus.
- Mauvais, parce qu'il laisse deux autorités en place sans dire laquelle gagne — c'est-à-dire le problème que ce changement corrige.

### Automatiser sans release-please

- Bon, parce qu'un script lisant `REGISTRE.md` verrait ce que les types ne voient pas, et rattraperait l'erreur de D6.
- Mauvais, parce qu'il faut l'écrire, l'entretenir, et le déboguer un jour où l'on voulait publier.
- Mauvais, parce que le dépôt compte déjà un instrument maison non testé automatiquement ; un second aggraverait le facteur de bus.

### Statu quo

- Bon, parce qu'il ne coûte rien et ne casse rien.
- Mauvais, parce qu'il laisse la convention payée et non rendue — l'état constaté au moment d'écrire cet ADR.

## More Information

Mesure à l'appui : au 2026-08-08, deux commits conformes sont sur `main` depuis la fusion de la PR #2, classés *corrective* par le tableau du README, et `plugin.json` porte toujours `0.4.1`.

La première publication ramassera ces deux commits et proposera `0.4.2`. Le correctif du journal de la sentinelle, fusionné juste avant l'adoption avec un sujet sans type, sera invisible à l'outil — conséquence directe du garde-fou n°4, et acceptée comme telle.

La politique de branches reste non tranchée. release-please suppose une branche par défaut et des demandes de publication ; le dépôt a poussé 40 commits en direct. Non bloquant tant que l'auteur est seul, bloquant à la première contribution externe. ADR distinct à ouvrir.

Réexamen prévu : à la première version calculée fausse, s'il s'en produit une.
