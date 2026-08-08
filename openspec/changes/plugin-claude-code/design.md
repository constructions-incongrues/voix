## Context

État constaté, vérifié sur un plugin qui fait déjà exactement ce que la sentinelle demandera (`ponytail`, 4.8.4) :

```
.claude-plugin/plugin.json         nom, version, description, auteur, "hooks": "./hooks/…"
.claude-plugin/marketplace.json    "plugins": [{ "source": "./" }]   ← auto-hébergé
skills/<nom>/SKILL.md              emplacement attendu des skills
hooks/*.json                       SessionStart, UserPromptSubmit, PreToolUse
```

Deux constats qui commandent tout le reste :

- **`install.sh` ne peut pas installer de hooks.** Il pose des liens dans `~/.claude/skills/`. Un hook se déclare dans un manifeste de plugin, nulle part ailleurs. La sentinelle est un hook.
- **`marketplace.json` de ponytail pointe sur lui-même** (`"source": "./"`). Le dépôt est sa propre place de marché. Il n'y a pas d'index central obligatoire : l'utilisateur désigne un dépôt, et l'installe.

Coût de migration mesuré : `voix/` apparaît **20 fois dans 10 fichiers**, dont 6 fichiers dans `openspec/changes/archive/`.

Contrainte héritée : le dépôt est public depuis aujourd'hui. Un renommage de répertoire est une rupture pour quiconque a cloné.

## Goals / Non-Goals

**Goals**

- Le dépôt se charge comme plugin Claude Code, hooks compris le jour où il y en aura.
- Le manifeste est auto-hébergé, et le refus de l'index tiers est écrit et motivé.
- Le chemin clone + `install.sh` continue de fonctionner, y compris hors de Claude Code.
- Une installation existante ne se retrouve pas avec des liens morts en silence.

**Non-Goals**

- Écrire un hook. Le véhicule d'abord, la sentinelle ensuite, et dans cet ordre parce que l'inverse est impossible.
- Se faire lister ailleurs.
- Toute promotion. Un plugin n'est pas un produit parce qu'il a un `plugin.json`.

## Decisions

### D1 — `plugin.json` sans clé `hooks`

Une clé `hooks` pointant vers un fichier absent casse le chargement du plugin. Elle est ajoutée par le change qui écrira le premier hook, pas par celui-ci.

Conséquence assumée : à l'issue de ce change, le plugin ne fait rien de plus que `install.sh`. C'est normal — il rend possible ce qui ne l'était pas.

### D2 — `voix/` devient `skills/`, sans compatibilité

Le chargeur attend `skills/`. Trois options ont été pesées :

| Option | Verdict |
|---|---|
| `skills/` composé de liens vers `voix/` | Les liens en dépôt sont fragiles sous Windows et opaques à la lecture. Refusé. |
| Duplication `voix/` + `skills/` | Deux exemplaires du même fichier : la dérive garantie, celle que le choix du lien symbolique visait à éviter dès le premier change. Refusé. |
| **Renommage franc** | 20 références à corriger, une fois. Retenu. |

Le dépôt s'appelle `voix` ; que le répertoire porte le nom attendu par la plateforme n'enlève rien à ce que le dépôt est. Le nom qui porte la thèse est celui du dépôt, pas celui du dossier.

### D3 — Les fichiers archivés ne sont pas corrigés

6 des 10 fichiers concernés sont dans `openspec/changes/archive/`. Ils décrivent un état passé, où le répertoire s'appelait `voix/`. **Les réécrire serait falsifier un compte rendu**, et le dépôt vient de publier son historique complet, erreurs comprises, précisément parce qu'il soutient l'inverse.

Une note dans `README.md` signale que les archives citent l'ancien chemin. C'est la seule dette acceptable ici.

### D4 — `install.sh` détecte et répare les liens morts

Une installation antérieure pointe vers `voix/`, qui disparaît. Un lien mort dans `~/.claude/skills/` est silencieux : la voix cesse simplement d'exister, sans erreur.

`install.sh` doit donc, avant de poser ses liens, retirer ceux qui pointent vers un chemin inexistant **à l'intérieur de ce dépôt**. Il conserve son garde-fou existant : il ne touche jamais à un vrai dossier, seulement à des liens, et seulement aux siens.

*Alternative écartée :* laisser l'utilisateur relancer `install.sh` sans nettoyage — le lien mort survit, la voix disparaît sans bruit, et c'est exactement la panne qu'on ne diagnostique pas.

### D5 — Version `0.1.0`, et ce qu'une version veut dire ici

Un plugin porte une version. Sur un dépôt de prose, il faut décider ce qu'elle compte, sinon elle ne compte rien :

```
majeure   une voix entre ou sort du registre
mineure   une voix change de question, de compétence ou de trace
corrective  un déclencheur est ajusté, un test rejoué, une formulation corrigée
```

Départ à `0.1.0` : quatre voix sur sept, la sentinelle absente. Le dépôt n'est pas en 1.0 tant qu'il ne fait pas ce pour quoi il a été commencé.

### D6 — Manifeste auto-hébergé, index tiers refusé et motivé

`marketplace.json` avec `"source": "./"`. L'utilisateur ajoute le dépôt comme place de marché et installe. Personne ne s'intercale.

Le refus de l'index tiers est écrit dans le `README.md`, avec sa raison : **un index agrège, classe et recommande** — il place la critique dans une liste où elle est comparée, notée, adoptée par commodité. C'est là que la récupération opère, pas dans le fait d'être installable. La distinction est celle d'Albini : la technologie n'était jamais l'ennemi, c'était la couche qui extrait.

Cette position est révisable, mais elle doit alors l'être **sciemment**, comme celle-ci l'a été.

## Risks / Trade-offs

| Risque | Atténuation |
|---|---|
| Rupture silencieuse des installations existantes | D4 : `install.sh` retire ses liens morts avant de reposer les siens. |
| Le renommage casse des références dans les specs vivantes | Les 4 fichiers vivants sont corrigés ; les 6 archivés ne le sont pas, par D3, et le README le dit. |
| Le plugin ne fait rien de plus qu'`install.sh` à l'issue du change | Assumé, D1. Le véhicule précède le passager ; l'ordre inverse n'existe pas. |
| Un `plugin.json` fait ressembler le dépôt à un produit | Le README ne gagne ni badge, ni fonctionnalité, ni promesse — c'est déjà une exigence de `publication-depot`. |
| L'auto-hébergement glisse vers l'index tiers par commodité | D6 : le refus est écrit et motivé dans le README, donc réfutable et révisable, mais pas franchissable par inadvertance. |
| Deux chemins d'installation à maintenir | Le chemin `install.sh` est trois lignes et sert tous les agents non-Claude. Son coût est inférieur à celui de l'abandonner. |

## Migration Plan

1. `git mv voix skills`, puis correction des 4 fichiers vivants (`README.md`, `install.sh`, `DISJONCTION.md`, `openspec/specs/format-voix/spec.md`).
2. `.claude-plugin/plugin.json` — sans clé `hooks`.
3. `.claude-plugin/marketplace.json` — `"source": "./"`.
4. `install.sh` : chemin source, et nettoyage des liens morts de D4.
5. `README.md` : deux chemins d'installation, la note sur les archives, et le refus motivé de l'index tiers.
6. Vérification : le plugin se charge, les quatre voix apparaissent, une installation antérieure est réparée par une simple relance.
7. Rejeu du test de routage — le renommage ne touche aucune `description`, mais c'est la vérification qui le prouve, pas le raisonnement.

**Rollback** : `git revert`. Une installation cassée se répare en relançant `install.sh`.

## Open Questions

- **Le nom du plugin.** Le dépôt est `voix`, l'orga `constructions-incongrues`. Un plugin nommé `voix` dans un espace de noms plat est-il assez distinctif ? `skillotheque` porte la thèse mais n'est plus le nom du dépôt.
- **Faut-il que les quatre voix deviennent des skills de plugin plutôt que des liens ?** Installées par plugin, elles ne sont plus dans `~/.claude/skills/` : les deux chemins d'installation peuvent charger deux copies de la même voix. À vérifier à l'étape 6 — si le doublon se produit, le README doit dire de choisir un chemin et un seul.
