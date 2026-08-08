# ADR Review Manifest

## ADR Review Completed

- Date: 2026-08-08
- Reviewer: Tristan Rivoallan
- Change: conventional-commits

## In-Force ADR Context Reviewed

- None: no existing repository-level ADRs were present. Le répertoire `adr/` n'existait pas avant ce changement ; le graphe de supersession est donc vide et aucune décision antérieure ne contraint celle-ci.

## Repository-Level ADRs Created

- adr/0001-conventional-commits.md - Adopte Conventional Commits 1.0.0 tel quel, assorti de quatre garde-fous : la description reste une phrase portant un constat, le README reste souverain sur les niveaux de version, les jeux de types et de scopes sont fermés, et l'historique antérieur n'est pas réécrit.

## Notes

Style `madr-full`, choisi par l'auteur ; `.agents/skills/architectural-decision-records/preferences.md` est passé de `unset` à `madr-full` dans ce changement.

Quatre options ont été comparées. L'analyse recommandait l'option 3 (pied de page machine) ; l'auteur a tranché pour l'option 1. Le désaccord et son motif sont consignés dans l'ADR plutôt qu'effacés — l'option 3 reste disponible en complément.

Le coût principal est nommé sans mitigation dans les conséquences : la correction d'une croyance antérieure, 15 % de l'historique, n'a pas de type propre dans la spécification.
