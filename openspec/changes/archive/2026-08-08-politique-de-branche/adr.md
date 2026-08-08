# ADR Review Manifest

## ADR Review Completed

- Date: 2026-08-08
- Reviewer: Tristan Rivoallan
- Change: politique-de-branche

## In-Force ADR Context Reviewed

- `adr/0002-release-please.md` — **seul ADR en force.** Les types de commit font autorité sur le niveau de version et release-please publie. Contraint ce changement sur trois points : le message atteignant `main` est ce dont la version est dérivée, la publication reste un acte humain, et la décision D5 (aucun outil de vérification des messages avant trois non-conformités) est maintenue « sous son déclencheur d'origine ».
- `adr/0001-conventional-commits.md` — **superséd par `adr/0002`**, qui porte `supersedes: ADR-0001`. Contexte historique seulement ; ne contraint plus par lui-même. Ce qui en reste en force est ce qu'`adr/0002` a explicitement repris : ses garde-fous 1, 3 et 4, et sa décision D5.

## Repository-Level ADRs Created

- `adr/0003-politique-de-branche.md` — `main` est la seule branche de publication ; le travail la rejoint par écrasement et se met à jour par rebasage ; la forge n'offre plus qu'une méthode ; le titre de la demande devient le message qui fait autorité ; la protection de `main` est décidée mais différée, armée par une sentinelle de contributeurs mécanique plutôt que par la mémoire ; les branches se nomment `<contributeur>/<slug>`, les branches d'outil étant exemptées nommément.

## Notes

**Pas de supersession.** `adr/0003` tranche ce que `adr/0001` et `adr/0002` ont tous deux explicitement laissé ouvert — chacun se terminant sur « ADR distinct à ouvrir ». Il ne revient sur aucune décision en force, et son statut est donc `accepted` sans `Supersedes:`.

**Question ouverte du design, résolue ici.** `design.md` demandait si corriger l'instrument désigné par D5 constituait une supersession d'`adr/0002`. Non : D5 elle-même — aucun outil avant trois non-conformités — reste intacte et son déclencheur n'est pas avancé. L'instrument, un hook `commit-msg`, n'est nommé que dans la prose d'`adr/0001`, qui est supersédée et ne contraint plus. `adr/0003` nomme le remplaçant (contrôle du titre de la demande en CI) sans toucher à ce qui est en force.

**Analyse des modalités de régulation.** Les cinq contraintes du changement ont été passées aux quatre modalités — loi, norme, prix, architecture — avec leur ligne de recours ; le tableau est dans `design.md`. Quatre sur cinq ont une voie de contestation documentée, et la licence CC BY-SA fait de la sortie un droit concédé par écrit. Le point dur est C3 : le jeu fermé de types est aujourd'hui une norme et migrera vers l'architecture au déclenchement de D5. D6 en découle et a été ajoutée à `adr/0003` avant acceptation, avec deux exigences correspondantes dans la spec.

**Contrainte d'immuabilité respectée.** Aucun fichier sous `adr/` n'a été modifié. `0001` et `0002` sont inchangés ; seul `0003` est ajouté.
