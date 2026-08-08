# ADR Review Manifest

## ADR Review Completed

- Date: 2026-08-08
- Reviewer: Tristan Rivoallan
- Change: outillage-nanopm

## In-Force ADR Context Reviewed

- `adr/0002-release-please.md` — **en force.** Les types de commit font autorité sur le niveau de version, release-please publie. Ne parle pas d'outillage ; sa seule adhérence au présent changement est qu'il a fait entrer la première Action de CI du dépôt, c'est-à-dire la première dépendance de processus assumée.
- `adr/0003-politique-de-branche.md` — **en force.** Ne parle pas d'outillage non plus. Deux points l'y relient : il a réaffirmé la règle de `REGISTRE.md` selon laquelle une prescription de méthode entre par décision, et il a introduit la sentinelle de contributeurs dans le même workflow que celui dont ce changement retire une ligne morte.
- `adr/0001-conventional-commits.md` — **superséd par `adr/0002`** (`supersedes: ADR-0001`). Contexte historique ; ne contraint plus par lui-même.

## Repository-Level ADRs Created

- `adr/0004-outillage-nanopm.md` — `.nanopm/` est classé méthode prescrite et n'entre pas au dépôt : `.gitignore` sous la catégorie *outillage régénérable* déjà tenue, plus une ligne au tableau d'outillage avec ce qu'il prescrivait et le déclencheur de réouverture. L'exclusion de routage de la sentinelle passe par `.gitignore` plutôt que par une liste, et la ligne `.serena/` en dur du hook — devenue morte — est supprimée. La règle d'admission de l'outillage devient la capacité `admission-outillage` et cesse de nommer un répertoire.

## Notes

**Pas de supersession.** Aucun ADR en force ne traite de l'outillage : `adr/0004` comble un espace plutôt qu'il n'en corrige un. Statut `accepted` sans `Supersedes:`.

**Correction de portée consignée, non effacée.** La première rédaction attribuait à ce dépôt les 12 convocations déclenchées par `.nanopm/`. Vérification faite, le journal de la sentinelle est global à la machine : **11 de ces 12 viennent d'un autre dépôt**, et une seule est d'ici. L'ADR porte la correction et sa conséquence — la décision est un précédent, pas un remède, et le `.gitignore` d'un dépôt ne corrige que ce dépôt.

**Une exigence de spec a servi immédiatement.** « Le coût de routage d'un outil est mesuré avant sa décision » a produit la mesure qui a produit la correction ci-dessus. Sans elle, l'ADR aurait affirmé une portée fausse.

**Contrainte d'immuabilité respectée.** Aucun fichier existant sous `adr/` n'a été modifié. `0001`, `0002` et `0003` sont inchangés ; seul `0004` est ajouté.

**Un défaut voisin est nommé et non traité :** un silence de la sentinelle ne laisse pas de marqueur, donc se rejoue au tour suivant — d'où six convocations quasi identiques de `guy-debord`. Il relève d'un changement distinct.
