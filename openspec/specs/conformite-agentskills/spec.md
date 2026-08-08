# conformite-agentskills

## Purpose

Ce que le dépôt doit satisfaire pour être lisible par un chargeur conforme à la spécification publique des Agent Skills, et non seulement par celui sur lequel les voix ont été écrites. Le dépôt affirmait que ses voix fonctionnaient avec tout agent chargeant des skills ; mesuré contre la norme, trois d'entre elles n'étaient pas même du YAML valide.

## Requirements

### Requirement: Description sous la limite de la spécification

La `description` de toute voix MUST tenir en 1024 caractères ou moins. Au-delà, un chargeur conforme rejette ou tronque la voix, et l'affirmation de portabilité du dépôt devient fausse.

#### Scenario: Voix admise au registre
- **QUAND** une voix est ajoutée ou modifiée
- **ALORS** sa `description` compte au plus 1024 caractères

#### Scenario: Voix héritée hors limite
- **QUAND** une voix existante dépasse la limite
- **ALORS** elle est réduite selon l'ordre de priorité du budget, puis re-mesurée avant d'être considérée conforme

### Requirement: Frontmatter analysable en YAML strict

Le frontmatter de toute voix MUST être du YAML valide pour un analyseur strict. Un scalaire non quoté MUST NOT contenir la séquence deux-points suivie d'une espace : l'analyseur y lit un séparateur clé/valeur et rejette le fichier entier.

Le piège est proprement francophone. La typographie française impose une espace insécable avant le deux-points — *« les tiers qui n'ont rien signé : un défaut imposé »* — et produit donc mécaniquement la séquence interdite. Le défaut est invisible à la lecture, indépendant de la longueur du champ, et il rend la voix illisible pour tout chargeur conforme même si tout le reste est correct.

#### Scenario: Deux-points à la française dans une description
- **QUAND** une `description` non quotée contient un deux-points précédé d'une espace
- **ALORS** la validation échoue, et la description est reformulée ou mise entre guillemets

#### Scenario: Voix écrite en français
- **QUAND** une voix est rédigée en français
- **ALORS** sa conformité est établie par l'outil de référence et non par la lecture, la ponctuation courante de la langue produisant un défaut invisible à l'œil

### Requirement: Nom conforme et aligné sur le répertoire

Le champ `name` de toute voix MUST être composé de minuscules, de chiffres et de tirets, sans tiret initial, final ni double, faire au plus 64 caractères, et MUST être identique au nom de son répertoire parent.

#### Scenario: Répertoire renommé
- **QUAND** le répertoire d'une voix change de nom
- **ALORS** le champ `name` de son `SKILL.md` est modifié en conséquence dans le même changement

### Requirement: Licence embarquée dans chaque voix

Tout `SKILL.md` MUST porter un champ `license`. Un fichier markdown circule seul : copié hors du dépôt, il quitte le `LICENSE` de la racine et perd toute trace de sa provenance. Savoir à qui appartient une chose qui circule est la question que le registre pose aux autres ; le dépôt se l'applique.

#### Scenario: Voix copiée hors du dépôt
- **QUAND** un `SKILL.md` est copié seul ailleurs
- **ALORS** sa licence reste lisible dans son propre frontmatter

### Requirement: Conformité établie par l'outil de référence

La conformité MUST être établie par la bibliothèque de validation de la spécification, et NON par un contrôle écrit dans ce dépôt. Un contrôle écrit par l'auteur teste ce qu'il a pensé, pas ce que la norme dit — un `grep` maison a déjà déclaré cet arbre propre alors qu'il ne l'était pas.

#### Scenario: Vérification de conformité
- **QUAND** la conformité d'une voix doit être établie
- **ALORS** l'outil de référence est exécuté sur son répertoire et son verdict fait foi

### Requirement: Affirmation de portabilité vérifiable

Toute affirmation de portabilité dans la documentation MUST être accompagnée de la commande qui la vérifie, ou MUST être retirée. Le dépôt affirmait que les voix fonctionnaient avec tout agent chargeant des skills ; mesuré contre la norme, les quatre étaient non conformes.

#### Scenario: Lecteur vérifiant l'affirmation
- **QUAND** le README affirme que les voix sont utilisables par un autre agent
- **ALORS** il indique la commande permettant de le vérifier soi-même
