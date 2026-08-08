## ADDED Requirements

### Requirement: Le niveau de version est dérivé de l'historique

Le niveau d'une publication MUST être calculé à partir des types de commit accumulés depuis la publication précédente, et non posé à la main. Les types font **autorité** : c'est ce qui distingue cette capacité de la règle antérieure, où le tableau du README tranchait et les types ne faisaient qu'indiquer.

La correspondance MUST être : `feat!` ou pied de page `BREAKING CHANGE:` → majeure · `feat` → mineure · `fix`, `docs`, `refactor`, `test`, `chore` → corrective.

#### Scenario: Accumulation de correctifs
- **QUAND** trois commits `docs(specs):` sont fusionnés depuis la dernière publication
- **ALORS** le niveau calculé est corrective, et la version passe de `0.4.1` à `0.4.2`

#### Scenario: Admission d'une voix au registre
- **QUAND** un commit `feat!(registre):` fusionne l'entrée de Federici
- **ALORS** le niveau calculé est majeure

#### Scenario: Type hors du jeu configuré
- **QUAND** un commit porte un type qui n'est pas dans le jeu fermé de `convention-commits`
- **ALORS** la publication échoue de façon visible plutôt que de l'ignorer silencieusement

### Requirement: Les types correctifs du dépôt déclenchent une publication

`docs`, `refactor`, `test` et `chore` MUST être configurés comme déclencheurs de niveau corrective. Le défaut de l'outil ne publie que sur `feat`, `fix` et `BREAKING`, ce qui laisserait sans publication des commits que le tableau du README classe corrective.

#### Scenario: Commit de documentation seul
- **QUAND** la seule chose fusionnée depuis la dernière publication est un `docs(registre):`
- **ALORS** une publication corrective est proposée, et non aucune

### Requirement: La publication reste soumise à une décision humaine

Aucune version MUST être publiée sans un acte explicite. L'outil ouvre une demande de publication portant le numéro calculé et les notes ; la publication n'a lieu qu'à sa fusion. Le calcul est automatique, l'acte ne l'est pas.

#### Scenario: Demande ouverte, non fusionnée
- **QUAND** une demande de publication est ouverte et laissée telle quelle
- **ALORS** aucune balise n'est posée, `plugin.json` n'est pas modifié sur la branche par défaut, et rien n'est publié

#### Scenario: Version calculée jugée fausse
- **QUAND** l'auteur estime que le niveau calculé ne correspond pas à ce que le changement fait au registre
- **ALORS** il corrige le commit fautif ou ferme la demande — et **ne modifie pas** le numéro à la main dans la demande, sans quoi l'autorité des types serait vidée de son sens

### Requirement: Ce que la dérivation ne sait pas voir

La dérivation MUST être documentée comme aveugle au registre. Un type mal choisi produit une version fausse sans que rien ne le signale : l'outil lit `feat` là où l'auteur voulait `feat!`, et l'entrée d'une voix passe en mineure. Le dépôt MUST porter cette limite par écrit, faute de contrôle qui la rattrape.

#### Scenario: Type sous-évalué sur une admission
- **QUAND** une voix entre au registre par un commit `feat(registre):` au lieu de `feat!(registre):`
- **ALORS** la version calculée est mineure alors que la règle du dépôt appelle une majeure
- **ET** aucun contrôle ne le détecte — c'est le coût accepté du passage à l'autorité des types

### Requirement: Le journal publié ne remplace pas le dossier de raisonnement

Le `CHANGELOG.md` produit MUST être décrit comme un index des publications, et non comme le journal de bord du dépôt. Le raisonnement complet reste dans `openspec/changes/archive/`, et le `CHANGELOG.md` MUST y renvoyer plutôt que de prétendre s'y substituer.

#### Scenario: Lecteur cherchant le motif d'un changement
- **QUAND** un lecteur veut savoir pourquoi une décision a été prise
- **ALORS** le `CHANGELOG.md` le renvoie vers `openspec/changes/archive/`, où le raisonnement est entier
