## REMOVED Requirements

### Requirement: Plafond de sept voix

**Reason** : un plafond unique comptait des voix inscrites, c'est-à-dire des intentions, alors que son motif écrit — la dilution du routage — ne porte que sur les voix qui se convoquent seules. Le registre compte quinze noms et trois voix routables : le plafond rationnait la partie qui ne se déclenche jamais.

**Migration** : remplacée par « Deux plafonds — dix inscrites, sept routables ». Le plafond de routage reprend le nombre et le motif d'origine sans changement ; le plafond d'inscription est le seul qui monte.

## ADDED Requirements

### Requirement: Deux plafonds — dix inscrites, sept routables

Le registre MUST NOT dépasser **dix voix inscrites**, et MUST NOT dépasser **sept voix routables**. Ce sont deux plafonds distincts parce qu'ils protègent deux choses différentes, et l'un ne remplace pas l'autre.

Le plafond d'**inscription** borne ce que le registre déclare : une question, un motif, une place tenue. Il est à dix.

Le plafond de **routage** borne ce qui se convoque tout seul, et c'est lui qui porte le motif d'origine : au-delà, le routage se dilue et le coût d'entretien — un jeu d'evals de déclenchement par voix — dépasse ce qui est tenable. Il reste à sept, inchangé, parce qu'aucune mesure n'a montré qu'il pouvait monter.

La mesure du 2026-08-08 établit que la dilution **n'attend pas le plafond** : à trois voix routables et 37 termes, 12 convocations sur 16 ont été emportées par des fichiers hors du travail, la voix retenue étant celle qui touche le plus de termes. Toute admission au routage MUST donc être accompagnée de la mesure de son effet sur la sélection, et non seulement du test d'apport.

Une inscription qui n'est pas routable MUST être signalée comme telle dans le registre. **Une voix inscrite sans skill écrite n'est pas une voix disponible**, et tout compte présenté au lecteur — README compris — MUST distinguer les inscrites des routables plutôt que d'annoncer les premières.

#### Scenario: Onzième candidate sur un registre plein
- **QUAND** une candidate satisfait les trois conditions alors que dix voix sont inscrites
- **ALORS** son admission exige le retrait explicite d'une voix inscrite

#### Scenario: Huitième voix routable
- **QUAND** une huitième voix satisfait le test d'apport et demande le routage automatique
- **ALORS** son routage exige qu'une routable en sorte, l'inscription restant possible sans routage

#### Scenario: Inscription sans skill écrite
- **QUAND** une voix est inscrite au registre et qu'aucun `SKILL.md` ne lui correspond
- **ALORS** le registre la signale comme non disponible
- **ET** aucun compte public ne l'annonce comme une voix du dépôt

#### Scenario: Compte annoncé au lecteur
- **QUAND** le `README` annonce le nombre de voix
- **ALORS** il donne les deux nombres — inscrites et routables — et non le seul premier

#### Scenario: Admission au routage sans mesure de sélection
- **QUAND** une voix passe le test d'apport et entre au routage sans qu'on ait mesuré son effet sur la sélection des convocations
- **ALORS** cette exigence n'est pas satisfaite
