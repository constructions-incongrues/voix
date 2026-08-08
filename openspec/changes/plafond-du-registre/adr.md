# ADR Review Manifest

## ADR Review Completed

- Date: 2026-08-08
- Reviewer: Tristan Rivoallan
- Change: plafond-du-registre

## In-Force ADR Context Reviewed

- `adr/0002-release-please.md` — en force. Ne parle pas du registre. Seule adhérence : le registre est l'axe de version du dépôt, et une admission de voix est une majeure.
- `adr/0003-politique-de-branche.md` — en force. Ne parle pas du registre.
- `adr/0004-outillage-nanopm.md` — en force, et **directement adhérent** : son exclusion de `.nanopm/` est ce qui a retiré la cause de la dilution que ce changement invoquait. Sans elle, D2 aurait conclu l'inverse.
- `adr/0001-conventional-commits.md` — superséd par `adr/0002`. Contexte historique.

## Repository-Level ADRs Created

- `adr/0005-plafond-du-registre.md` — deux plafonds distincts : dix voix inscrites, sept routables. Le plafond de routage reprend le nombre et le motif d'origine sans changement. Le classement du hook n'est pas touché ; la réponse à la dilution est une exigence de mesure à l'admission, non un mécanisme. Le registre distingue désormais ce qu'il déclare de ce qui répond, et le critère de 1.0 cesse d'employer un plafond comme dénominateur.

## Notes

**Pas de supersession.** Aucun ADR en force ne traite du registre des voix. Statut `accepted` sans `Supersedes:`.

**Une correction consignée, non effacée.** La proposition fondait son argument sur une dilution du routage mesurée à 12 convocations sur 16. Vérification faite en excluant `.nanopm/` — retiré par `adr/0004` le même jour — la répartition sur du travail réel est `lessig` 7, `illich` 2, `guy-debord` 1. **Les huit victoires de Debord venaient toutes de l'échafaudage.** La cause était déjà traitée, et D2 en tire la conséquence : ne pas construire un correctif de classement.

**Le biais du journal, rencontré pour la deuxième fois.** Comme dans `adr/0004`, le journal de la sentinelle est global à la machine et mêle plusieurs dépôts. La répartition 7/2/1 vaut pour l'usage de l'auteur, non pour ce dépôt seul. C'est écrit en conséquence mauvaise.

**Le compte du registre vient d'une voix.** `guy-debord`, convoquée par la sentinelle sur la proposition, a produit les quinze noms pour trois voix et la table d'inversions. Le résultat est dans `proposal.md`, avec son marqueur.

**Contrainte d'immuabilité respectée.** Aucun fichier existant sous `adr/` n'a été modifié ; seul `0005` est ajouté.
