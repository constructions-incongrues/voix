## Why

Le dépôt s'installe aujourd'hui par `git clone` puis `install.sh`, qui pose des liens symboliques dans `~/.claude/skills/`. Ça marche, et ça suffit tant que le dépôt ne contient que des voix.

Ça cesse de suffire à la marche suivante : **`install.sh` peut installer des skills, il ne peut pas installer de hooks.** Or la sentinelle — quelle que soit la forme retenue, injection au démarrage de session ou classification en fin de tour — *est* un hook. Le plugin est le seul véhicule qui en transporte.

C'est la raison de ce change, et elle est technique avant d'être une question de confort d'installation. Le format plugin n'est pas une vitrine, c'est le préalable à la cible 3.

Reste ce que ce dépôt a mis deux fois hors périmètre : la place de marché comme geste qui transforme la critique en produit. Deux constats l'ont déplacé sans l'annuler.

D'abord, un `marketplace.json` déclare `"source": "./"` : **le manifeste est auto-hébergé.** On ne se fait pas lister dans l'index d'un tiers, on publie son propre manifeste et l'utilisateur le désigne. C'est *supprimer le parasite et traiter en direct* — la position d'Albini, pas son contraire. La récupération que le dépôt nommait visait la soumission à un index agrégé ; c'est une autre opération, et ce change ne la fait pas.

Ensuite, `plugin.json` et `marketplace.json` sont deux fichiers distincts et deux décisions distinctes. Ce change les sépare explicitement au lieu de les subir ensemble.

## What Changes

- **Format plugin** — `.claude-plugin/plugin.json` : nom, version, description, auteur. Pas de clé `hooks` tant qu'aucun hook n'existe : une clé pointant vers un fichier absent casse le chargement.
- **Manifeste auto-hébergé** — `.claude-plugin/marketplace.json` avec `"source": "./"`. Le dépôt est sa propre place de marché. **Aucune soumission à un index tiers** : c'est une décision distincte, non prise ici, et le dépôt doit dire pourquoi.
- **`voix/` devient `skills/`** — le chargeur de plugins attend les skills à cet emplacement. 20 occurrences dans 10 fichiers, dont l'historique archivé qu'on ne réécrit pas. **BREAKING** pour quiconque a déjà cloné et lancé `install.sh`.
- **Versionnement** — un plugin porte une version. Introduit la discipline correspondante : une version, un journal des changements, et la question de ce qui constitue une version dans un dépôt de prose.
- **`install.sh` survit** — les voix sont des fichiers markdown, utilisables par tout agent qui charge des skills. Le chemin clone + liens reste le seul disponible hors de Claude Code, et il doit continuer de fonctionner.
- **README** — deux chemins d'installation, et la raison écrite du choix de ne pas se faire lister ailleurs.

## Capabilities

### New Capabilities

- `paquet-plugin` : ce que le dépôt doit satisfaire pour être chargé comme plugin — emplacement des skills, contenu du manifeste, et la règle qui sépare le manifeste auto-hébergé de toute inscription dans un index tiers.

### Modified Capabilities

- `publication-depot` : le périmètre publié comportait un chemin d'installation ; il en comporte deux, et la position sur les index tiers devient une exigence explicite plutôt qu'une mention de hors-périmètre.

## Impact

- **Renommage `voix/` → `skills/`** — 20 références dans 10 fichiers. Les fichiers archivés (`openspec/changes/archive/`) ne sont **pas** réécrits : ils décrivent un état passé, et les corriger serait falsifier un compte rendu.
- **Nouveaux fichiers** — `.claude-plugin/plugin.json`, `.claude-plugin/marketplace.json`, un fichier de version.
- **`install.sh`** — chemin source mis à jour, comportement inchangé.
- **`README.md`** — installation, et la raison du refus de l'index tiers.
- **Rupture pour les installations existantes** — les liens symboliques pointent vers `voix/`, qui disparaît. `install.sh` doit détecter et réparer plutôt que laisser des liens morts.
- **Aucun code applicatif.**

## Hors périmètre

- **La sentinelle elle-même.** Ce change prépare le véhicule ; il n'écrit aucun hook. `plugin.json` reste sans clé `hooks` jusqu'à ce qu'il y en ait un.
- **L'inscription dans un index de plugins tiers.** Décision distincte, non prise ici. Le manifeste auto-hébergé n'y engage pas.
- **Le lot 2** — Federici, Ostrom, Polanyi.
