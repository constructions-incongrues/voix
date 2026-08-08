## ADDED Requirements

### Requirement: Les deux chemins d'installation documentés, et leur exclusivité

Le `README.md` MUST documenter les deux chemins d'installation — plugin, et clone avec liens symboliques — et MUST indiquer d'en choisir un seul. Les deux posent la même voix à deux endroits différents ; employés ensemble, ils peuvent en charger deux copies.

#### Scenario: Lecteur choisissant son installation
- **QUAND** quelqu'un veut installer les voix
- **ALORS** le README lui donne les deux chemins, dit lequel convient à son agent, et l'avertit de ne pas les cumuler

### Requirement: Chemins périmés des archives signalés

Le `README.md` MUST signaler que les documents archivés dans `openspec/changes/archive/` citent des chemins qui ne sont plus ceux du dépôt. Ces documents décrivent un état passé : les corriger falsifierait un compte rendu, alors que le dépôt publie son historique complet, erreurs comprises, précisément parce qu'il soutient l'inverse.

#### Scenario: Lecteur suivant un chemin cité dans une archive
- **QUAND** un document archivé désigne un fichier à un emplacement qui n'existe plus
- **ALORS** le README a prévenu que les archives ne sont pas mises à jour, et pourquoi
