## 1. Renommage

- [x] 1.1 `git mv voix skills` — un seul emplacement, pas de duplication ni de liens en dépôt
- [x] 1.2 Corriger les 4 fichiers vivants qui citent `voix/` : `README.md`, `install.sh`, `DISJONCTION.md`, `openspec/specs/format-voix/spec.md`
- [x] 1.3 Vérifier qu'aucun fichier vivant ne cite plus `voix/`, et que les 6 fichiers de `openspec/changes/archive/` sont **inchangés** — les corriger falsifierait un compte rendu

## 2. Manifeste

- [x] 2.1 `.claude-plugin/plugin.json` : nom, version `0.1.0`, description, auteur. **Sans clé `hooks`** — une référence vers un fichier absent casse le chargement du plugin entier
- [x] 2.2 `.claude-plugin/marketplace.json` : `"source": "./"`, le dépôt comme sa propre place de marché
- [x] 2.3 Vérifier les deux fichiers en JSON valide, et que le nom du plugin est cohérent entre les deux

## 3. install.sh

- [x] 3.1 Mettre à jour le chemin source `voix/` → `skills/`
- [x] 3.2 Ajouter le retrait des liens morts : avant de poser les siens, `install.sh` retire de `~/.claude/skills/` les liens qui pointent vers un chemin inexistant **de ce dépôt** — un lien mort ne produit aucune erreur, la voix disparaît en silence
- [x] 3.3 Vérifier que le garde-fou existant tient : un vrai dossier est signalé, jamais écrasé
- [x] 3.4 Éprouver la réparation pour de vrai : partir d'une installation pointant vers `voix/`, relancer, constater que les quatre liens sont réparés sans intervention

## 4. README

- [x] 4.1 Documenter les deux chemins d'installation, dire lequel convient à quel agent, et avertir de n'en cumuler aucun
- [x] 4.2 Écrire le refus motivé de l'inscription dans un index tiers : un index agrège, classe et recommande — c'est là qu'opère la récupération, pas dans le fait d'être installable. Position révisable, mais sciemment
- [x] 4.3 Signaler que les documents archivés citent des chemins périmés, et pourquoi ils ne sont pas corrigés
- [x] 4.4 Dire ce que compte la version : majeure = une voix entre ou sort, mineure = une question, une compétence ou une trace change, corrective = un déclencheur ou une formulation

## 5. Vérification

- [x] 5.1 Charger le dépôt comme plugin et constater que les quatre voix apparaissent
- [x] 5.2 **Question ouverte du design à trancher ici** : vérifier si l'installation par plugin et celle par `install.sh` chargent deux copies de la même voix. Si oui, le README doit l'interdire explicitement plutôt que le déconseiller
- [x] 5.3 Rejouer le test de routage sur les quatre voix : le renommage ne touche aucune `description`, mais c'est la vérification qui le prouve, pas le raisonnement
- [x] 5.4 Vérifier qu'`install.sh` fonctionne toujours sur une machine sans support des plugins

## 6. Specs et publication

- [x] 6.1 Synchroniser les deltas dans `openspec/specs/` : `paquet-plugin`, et les deux exigences ajoutées à `publication-depot`
- [x] 6.2 Pousser. Le dépôt est public : le renommage est une rupture pour qui a déjà cloné, et le message de commit doit le dire
