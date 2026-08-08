# ADR Review Manifest

## ADR Review Completed

- Date: 2026-08-08
- Reviewer: Tristan Rivoallan
- Change: release-please

## In-Force ADR Context Reviewed

- adr/0001-conventional-commits.md - En force au moment de la revue. Son garde-fou n°2 (« le tableau du README est souverain sur le niveau de version ») est **directement incompatible** avec une publication dérivée des types. Les trois autres garde-fous et sa décision D5 restent pertinents et sont repris tels quels par le nouvel ADR.

## Repository-Level ADRs Created

- adr/0002-release-please.md - Les types de commit font autorité sur le niveau de version et release-please publie. **Supersède ADR-0001**, la supersession portant sur le fichier entier ; les trois garde-fous encore en force y sont repris explicitement, seul celui de la souveraineté du README est remplacé.

## Notes

Style `madr-full`, conforme à `preferences.md`.

Le graphe de supersession compte désormais une arête : `0002 → 0001`. Un consommateur qui dérive l'état courant en suivant les `supersedes` doit lire `0002` seul ; `0001` reste au dépôt comme trace historique et n'a **pas** été modifié, conformément à la règle d'immuabilité.

Quatre options ont été comparées. L'option 2 (release-please en rédacteur de brouillon) préservait `adr/0001` intact et avait été recommandée à l'ouverture ; l'auteur a tranché pour l'option 1. Le motif du rejet est consigné dans l'ADR : une règle du type « corriger le numéro à la main quand il paraît faux » s'applique tant qu'on s'en souvient, puis plus.

Le coût est nommé sans mitigation : sous l'autorité des types, un `feat` écrit là où il fallait `feat!` produit une version fausse qu'aucun contrôle ne rattrape.
