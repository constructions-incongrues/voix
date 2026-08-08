## MODIFIED Requirements

### Requirement: Extension additive des déclencheurs

Une réécriture MUST étendre la `description` d'une voix sans en retirer d'amorce de déclenchement, **sauf si la suppression est suivie d'une mesure établissant l'absence de régression**. Les déclencheurs sont des artefacts réglés par itérations successives : une suppression détruit un travail coûteux à retrouver, alors qu'un ajout ne peut pas faire cesser un déclenchement qui fonctionnait.

L'interdiction pure était tenable tant qu'aucune contrainte externe n'imposait de réduire. Une limite de taille imposée par la spécification publique la rend inapplicable. La protection change donc de nature : elle ne repose plus sur l'interdiction, mais sur la preuve — ce qui est plus exigeant, puisqu'une suppression non mesurée reste interdite.

#### Scenario: Réécriture qui n'ajoute que
- **QUAND** la `description` d'une voix est étendue sans suppression
- **ALORS** toutes les amorces présentes avant la modification y figurent encore, et aucune mesure supplémentaire n'est exigée

#### Scenario: Suppression imposée par une contrainte externe
- **QUAND** une amorce doit être retirée pour satisfaire une limite de la spécification
- **ALORS** la suppression est permise, et le test de routage et le test de silence sont rejoués avant que la voix ne soit considérée valide

#### Scenario: Suppression non mesurée
- **QUAND** une amorce est retirée sans rejeu des tests
- **ALORS** la modification est refusée
