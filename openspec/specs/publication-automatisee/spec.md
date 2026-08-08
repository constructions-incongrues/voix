# publication-automatisee

## Purpose

Comment une version est calculée et publiée, et ce que le calcul ne sait pas voir. Le dépôt versionnait à la main selon des règles écrites, appliquées de mémoire à chaque publication ; les types de commit font désormais autorité et l'outil dérive le niveau, la balise et le journal. Ce que la dérivation rate est écrit ici plutôt que découvert : un type mal posé produit une version fausse que rien ne signale, et un sujet antérieur à la convention lui est invisible.

## Requirements

### Requirement: Le niveau de version est dérivé de l'historique

Le niveau d'une publication MUST être calculé à partir des types de commit accumulés depuis la publication précédente, et non posé à la main. Les types font **autorité** : c'est ce qui distingue cette capacité de la règle antérieure, où le tableau du README tranchait et les types ne faisaient qu'indiquer.

La correspondance MUST être : `feat!` ou pied de page `BREAKING CHANGE:` → majeure · `feat` → mineure · `fix`, `docs`, `refactor`, `test`, `chore` → corrective.

**Tant que la version est inférieure à `1.0.0`**, l'option `bump-minor-pre-major` MUST être active : une rupture produit alors un **mineur** et non un majeur. Le dépôt ne passera pas en `1.0.0` par accumulation mécanique — le README pose qu'annoncer une 1.0 sur un registre à moitié écrit est exactement ce dont il se méfie. Le passage à `1.0.0` MUST rester un acte délibéré.

#### Scenario: Accumulation de correctifs
- **QUAND** trois commits `docs(specs):` sont fusionnés depuis la dernière publication
- **ALORS** le niveau calculé est corrective, et la version passe de `0.4.1` à `0.4.2`

#### Scenario: Admission d'une voix au registre, avant 1.0.0
- **QUAND** un commit `feat!(registre):` fusionne l'entrée de Federici, la version courante étant `0.4.x`
- **ALORS** le niveau calculé est **mineur** — `0.5.0` — parce que `bump-minor-pre-major` est actif
- **ET** la règle du dépôt qui appelle une majeure n'est pas contredite : elle le sera à partir de `1.0.0`

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

#### Scenario: Type sous-évalué sur une admission, avant 1.0.0
- **QUAND** une voix entre au registre par un commit `feat(registre):` au lieu de `feat!(registre):`, la version courante étant `0.4.x`
- **ALORS** la version calculée est la même dans les deux cas — `bump-minor-pre-major` fait converger `feat` et `feat!` sur un mineur
- **ET** l'erreur est donc **sans conséquence tant que le dépôt est sous `1.0.0`**

#### Scenario: Type sous-évalué sur une admission, à partir de 1.0.0
- **QUAND** le même commit est posé alors que la version courante est `1.x`
- **ALORS** la version calculée est mineure là où la règle du dépôt appelle une majeure
- **ET** aucun contrôle ne le détecte — c'est le coût accepté du passage à l'autorité des types, seulement différé

### Requirement: Le journal publié ne remplace pas le dossier de raisonnement

Le `CHANGELOG.md` produit MUST être décrit comme un index des publications, et non comme le journal de bord du dépôt. Le raisonnement complet reste dans `openspec/changes/archive/`, et le `CHANGELOG.md` MUST y renvoyer plutôt que de prétendre s'y substituer.

#### Scenario: Lecteur cherchant le motif d'un changement
- **QUAND** un lecteur veut savoir pourquoi une décision a été prise
- **ALORS** le `CHANGELOG.md` le renvoie vers `openspec/changes/archive/`, où le raisonnement est entier
