## ADDED Requirements

### Requirement: Description sous la limite de la spécification

La `description` de toute voix MUST tenir en 1024 caractères ou moins. Au-delà, un chargeur conforme rejette ou tronque la voix, et l'affirmation de portabilité du dépôt devient fausse.

#### Scenario: Voix admise au registre
- **QUAND** une voix est ajoutée ou modifiée
- **ALORS** sa `description` compte au plus 1024 caractères

#### Scenario: Voix héritée hors limite
- **QUAND** une voix existante dépasse la limite
- **ALORS** elle est réduite selon l'ordre de priorité du budget, puis re-mesurée avant d'être considérée conforme

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
