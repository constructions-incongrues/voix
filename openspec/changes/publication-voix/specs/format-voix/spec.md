## ADDED Requirements

### Requirement: Voix lisible hors de la machine de son auteur

Tout fichier de voix MUST être utilisable par quelqu'un qui ne dispose pas de l'outillage privé de son auteur. Le format garantit aujourd'hui qu'une voix est routable et vérifiable ; il ne garantit pas qu'elle soit lisible ailleurs. Une voix qui vise une skill nommée que le lecteur n'a pas installée désigne un adversaire invisible : elle est alors à regarder, pas à utiliser.

#### Scenario: Voix écrite pour publication
- **QUAND** une voix est ajoutée au registre
- **ALORS** ses sections `Signaux` et de sparring visent un cadrage énoncé en clair, et tout outil tiers n'y figure qu'à titre d'exemple facultatif

#### Scenario: Voix héritée d'un usage privé
- **QUAND** une voix existante référence de l'outillage absent chez le lecteur
- **ALORS** elle est réécrite pour viser le cadrage avant d'être publiée, sans que le contenu de ses inversions ne change
