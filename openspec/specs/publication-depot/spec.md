# publication-depot

## Purpose

Ce qui est publié, et sous quelles conditions. Publier une critique la rend consommable : ces exigences ne l'empêchent pas, elles décident de la forme qui y résiste le mieux — une licence qui refuse l'enclosure, un README qui porte la thèse et nomme sa propre absorption, et l'appareil qui permet à un tiers de reproduire le travail plutôt que de seulement l'installer.

## Requirements

### Requirement: Licence non-permissive et motivée

Le dépôt MUST porter une licence qui interdit l'enclosure, et le choix MUST être motivé dans le dépôt lui-même et non seulement déposé en fichier. La licence retenue est CC BY-SA 4.0 : le contenu est de la prose, et le critère issu du registre porte sur l'enclosure et non sur le commerce — la voix d'Albini vise la rente, la position qui extrait sans fabriquer, pas le travail honnête payé correctement.

#### Scenario: Réutilisation avec partage à l'identique
- **QUAND** un tiers reprend une voix du dépôt et la modifie
- **ALORS** la licence l'oblige à publier son dérivé aux mêmes conditions

#### Scenario: Motivation consultable
- **QUAND** un lecteur veut savoir pourquoi cette licence plutôt qu'une permissive
- **ALORS** l'argument est écrit dans le dépôt, avec les alternatives écartées et leur motif

### Requirement: README portant la thèse, non le produit

Le `README.md` MUST énoncer ce que le dépôt conteste, la question propre à chaque voix, la règle d'admission et le rôle de la trace. Il MUST NOT contenir de badges, de liste de fonctionnalités ni de promesse de valeur : la forme de la plaquette produit est précisément ce que le dépôt conteste.

#### Scenario: Lecture par un tiers non informé
- **QUAND** quelqu'un découvre le dépôt sans contexte préalable
- **ALORS** il comprend ce qui est contesté et pourquoi le dépôt reste petit, sans avoir à ouvrir un fichier de voix

### Requirement: Récupération nommée dans le README

Le `README.md` MUST comporter une section qui nomme sa propre récupération — l'absorption de la critique et sa revente comme style. Une critique qui n'a pas prévu son absorption l'a déjà subie, et c'est la seule défense disponible contre un sort qu'aucune licence n'empêche.

#### Scenario: Section présente et située
- **QUAND** le README est publié
- **ALORS** il comporte une section explicite sur ce que le dépôt est en train de devenir en étant publié

### Requirement: Appareil de reproduction publié avec les voix

Le dépôt publié MUST inclure `REGISTRE.md`, les enregistrements des tests de disjonction et de silence, et les jeux d'evals de déclenchement de chaque voix. Sans eux, un tiers peut consommer les voix mais ne peut ni en admettre une nouvelle ni vérifier que le silence tient.

#### Scenario: Admission d'une voix par un tiers
- **QUAND** un tiers veut proposer une voix supplémentaire
- **ALORS** il dispose de la règle d'admission, du test de disjonction et d'un jeu d'evals de référence, sans avoir à les reconstituer

### Requirement: Raisonnement publié avec le résultat

Le dépôt publié MUST inclure `openspec/` — les specs principales et les changes archivés — ainsi que l'historique git complet, y compris les commits consignant des erreurs. Montrer le travail plutôt que le produit est la position que le dépôt soutient par ailleurs.

#### Scenario: Erreur conservée dans l'historique
- **QUAND** l'historique contient un commit documentant une mesure invalide et sa correction
- **ALORS** ce commit est publié tel quel, sans réécriture d'historique

### Requirement: Audit avant première publication

Le dépôt et son historique MUST être audités pour secrets, jetons et chemins personnels exploitables avant la création du dépôt distant.

#### Scenario: Audit préalable
- **QUAND** la création du dépôt distant est préparée
- **ALORS** l'arbre et l'historique ont été inspectés et le résultat de cette inspection est explicite

### Requirement: Publication soumise à accord explicite au moment de l'acte

La création du dépôt distant et le premier envoi MUST être précédés d'un accord donné à ce moment-là. Un accord général donné à l'ouverture du change NE DOIT PAS en tenir lieu : une fois en ligne, le contenu est indexable et copiable même s'il est retiré ensuite.

#### Scenario: Accord non encore donné
- **QUAND** toutes les étapes préparatoires sont terminées
- **ALORS** aucune commande de création ou d'envoi n'est exécutée et l'accord est demandé

### Requirement: Les deux chemins d'installation documentés, et leur exclusivité

Le `README.md` MUST documenter les deux chemins d'installation — plugin, et clone avec liens symboliques — MUST indiquer d'en choisir un seul, et MUST dire comment défaire celui qu'on ne garde pas.

Mesuré par convocation réelle : les deux chemins **se cumulent**. Chaque voix existe alors en double sous deux noms distincts — `<voix>` pour le clone, `<plugin>:<voix>` pour le plugin — les deux sont visibles simultanément, et **rien ne détermine laquelle répond**. Aucune erreur n'est émise.

#### Scenario: Lecteur choisissant son installation
- **QUAND** quelqu'un veut installer les voix
- **ALORS** le README lui donne les deux chemins, dit lequel convient à son agent, l'avertit du doublon, et indique comment retirer l'un des deux

#### Scenario: Les deux chemins actifs
- **QUAND** un lien de `~/.claude/skills/` et une voix de plugin portent la même voix
- **ALORS** les deux sont convocables sous des noms différents, et laquelle répond n'est pas déterminé

### Requirement: Chemins périmés des archives signalés

Le `README.md` MUST signaler que les documents archivés dans `openspec/changes/archive/` citent des chemins qui ne sont plus ceux du dépôt. Ces documents décrivent un état passé : les corriger falsifierait un compte rendu, alors que le dépôt publie son historique complet, erreurs comprises, précisément parce qu'il soutient l'inverse.

#### Scenario: Lecteur suivant un chemin cité dans une archive
- **QUAND** un document archivé désigne un fichier à un emplacement qui n'existe plus
- **ALORS** le README a prévenu que les archives ne sont pas mises à jour, et pourquoi
