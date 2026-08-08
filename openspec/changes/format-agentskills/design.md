## Context

Spécification relevée sur `agentskills.io/specification.md`, et contrainte pertinente pour ce dépôt :

| Champ | Requis | Contrainte |
|---|---|---|
| `name` | oui | 1-64 car., minuscules `a-z0-9` et tirets, ni au début ni à la fin, pas de tiret double, **doit correspondre au nom du répertoire parent** |
| `description` | oui | **1-1024 caractères** |
| `license` | non | nom de licence ou renvoi à un fichier fourni |
| `compatibility` | non | 1-500 car., uniquement si l'environnement l'exige |
| `metadata` | non | table chaîne → chaîne |
| `allowed-tools` | non | expérimental |

État mesuré :

```
  name == répertoire      4/4 conformes
  champs présents         name, description — et rien d'autre
  description             2215 / 2411 / 1828 / 1702  →  toutes hors limite
```

Validation de référence : `skills-ref` (npm, v0.1.5), dépôt `agentskills/agentskills` accessible.

Contrainte héritée qui domine : la `description` est ce que deux changes successifs ont réglé et mesuré. Toute coupe est un risque de régression sur un artefact coûteux.

## Goals / Non-Goals

**Goals**

- Quatre voix conformes, prouvé par l'outil de référence et non par un contrôle maison.
- Aucune régression de routage ni de silence, prouvée par rejeu.
- Une règle de coupe écrite, pour que la prochaine voix naisse conforme au lieu d'être corrigée après.

**Non-Goals**

- Découper les corps en `references/`.
- Ajouter des champs facultatifs sans nécessité.
- Toute inscription où que ce soit.

## Decisions

### D1 — Ordre de priorité de la description, et ce qu'on coupe en premier

Couper 1191 caractères sans règle revient à couper au hasard. L'ordre suit ce que le dépôt a mesuré, du plus au moins établi :

```
  1. CLAUSE DE SITUATION        intouchable
     « à convoquer chaque fois que le travail porte sur… même
       quand X n'est pas nommé »
     → c'est elle qui rend la voix convocable sans son nom. Sans elle,
       une autre voix remporte ses requêtes par défaut (mesuré le 08-08).
       Toute la sentinelle en dépend.

  2. CLAUSE D'EXCLUSION         intouchable, compressible
     « ne pas déclencher sur un exposé, un résumé neutre… »
     → seul faux positif jamais observé en conditions réelles.
       Le fond reste ; l'énumération des cas peut se réduire.

  3. AMORCES NOMMÉES            garder 3 à 4, dont une en anglais
     → « que dirait X », « voix de X », « bring in X »
       Les listes de dix variantes coûtent cher et se recouvrent.

  4. CONTRE-VOIX CONSEIL STARTUP  réduire à une phrase
     → le fond appartient au corps du fichier, pas au déclencheur.

  5. EXEMPLES D'OUTILLAGE TIERS   couper entièrement
     → « (chez certains : les skills gstack office-hours, …) »
       Ce sont des exemples, jamais des dépendances — `portabilite-voix`
       l'exige déjà. Ils coûtent 150 à 250 caractères par voix pour
       zéro déclenchement propre.
```

*Alternative écartée :* couper au plus court en gardant la forme actuelle et en supprimant des phrases entières au jugé. Rapide, et impossible à défendre quand un déclenchement tombe.

### D2 — La règle « additive uniquement » devient « additive par défaut »

`portabilite-voix` dispose aujourd'hui qu'une réécriture *« MUST étendre la description sans en retirer d'amorce existante »*. La règle était juste dans son contexte — une réécriture de portabilité n'avait aucune raison de retirer quoi que ce soit, et l'interdiction évitait de détruire un réglage par mégarde.

Elle rend la conformité impossible. Elle devient : **toute suppression d'amorce est permise si elle est suivie d'une mesure qui prouve l'absence de régression.** Ce n'est pas un affaiblissement : l'ancienne règle protégeait par l'interdiction, la nouvelle protège par la preuve, ce qui est plus fort et plus coûteux.

C'est aussi le premier changement d'exigence du dépôt, et il est motivé par une contrainte externe qu'aucune décision interne ne pouvait anticiper.

### D3 — `license` dans chaque `SKILL.md`

Le fichier `LICENSE` est à la racine. Une voix copiée seule — ce qui est le mode de circulation naturel d'un fichier markdown — quitte le dépôt sans lui.

`license: CC-BY-SA-4.0` dans le frontmatter fait voyager la provenance avec le fichier. Coût : une ligne, hors du budget de la `description`. C'est la position d'Albini appliquée au dépôt lui-même — savoir à qui appartient une chose qui circule.

### D4 — La conformité se mesure avec l'outil de référence, pas avec mes greps

`skills-ref validate ./skills/<voix>` devient le critère. Mes contrôles maison ont déjà menti une fois aujourd'hui : le `grep 'voix/'` qui déclarait l'arbre propre alors qu'`install.sh` contenait `cd "$(dirname "$0")/voix"` sans barre finale.

Un contrôle écrit par celui qui écrit le code teste ce qu'il a pensé, pas ce que la norme dit.

### D5 — Point d'arrêt de non-régression, avec le même protocole que les fois précédentes

Après coupe : rejeu du volet routage (une requête de situation par voix, sans la nommer) et du volet silence (quatre cas expositifs, trois tâches ordinaires). Méthode `claude -p --output-format stream-json`, lecture du premier appel `Skill` — jamais le harnais `skill-creator`, pour la raison inscrite dans `admission-voix`.

**Une régression bloque et se corrige avant de continuer.** C'est ce protocole qui a trouvé, aux deux changes précédents, un faux positif systématique puis deux voix inconvocables.

### D6 — L'affirmation de portabilité devient vérifiable dans le README

Le README affirme que les voix fonctionnent avec tout agent qui charge des skills. C'était une supposition. Elle devient une affirmation testable, avec la commande qui la teste, ou elle disparaît.

## Risks / Trade-offs

| Risque | Atténuation |
|---|---|
| Une coupe de 58 % détruit un déclenchement réglé sur 4 itérations | D1 : ordre de priorité motivé, le plus mesuré coupé en dernier. D5 : rejeu obligatoire, point d'arrêt. |
| La clause de situation est sacrifiée au budget | D1 : intouchable, rang 1. C'est la condition d'existence de la sentinelle. |
| Assouplir « additive uniquement » ouvre la porte aux coupes non mesurées | D2 : l'autorisation est conditionnelle à la preuve, pas générale. Sans mesure, la suppression reste interdite. |
| Une voix devient trop maigre pour se déclencher hors de son nom | Le test de routage le détecte : il interroge précisément la situation sans nommer la voix. |
| La spécification évolue et le dépôt redevient non conforme | `skills-ref` est une dépendance de développement ; la validation se rejoue à chaque voix admise. |
| 1024 caractères est peut-être infranchissable pour Albini (2411) | Si la coupe casse le déclenchement après deux tentatives, **arrêter et rapporter** plutôt que dégrader en silence. Une voix non conforme et fonctionnelle vaut mieux qu'une voix conforme et muette — mais la décision revient à l'auteur, pas à l'implémentation. |

## Migration Plan

1. Installer `skills-ref` et établir la mesure de départ des quatre voix.
2. Modifier `portabilite-voix` **avant** toute coupe — sinon les tâches suivantes violent une exigence en vigueur.
3. Couper les quatre `description` selon D1, dans l'ordre croissant de difficulté : Illich (−678), Lessig (−804), Debord (−1191), Albini (−1387).
4. Ajouter `license` aux quatre.
5. Valider avec `skills-ref`.
6. **Point d'arrêt** : rejeu routage + silence. Une régression bloque.
7. Specs, README, publication.

**Rollback** : `git revert`. Les descriptions d'avant sont dans l'historique, et l'historique n'est pas réécrit.

## Open Questions

- **Que faire si Albini est irréductible ?** 2411 caractères pour un plafond de 1024, avec deux clauses obligatoires à préserver. Le risque est traité en D5/tableau, mais l'arbitrage — conformité contre déclenchement — appartient à l'auteur si le cas se présente.
- **Les quatre sections normalisées coûtent-elles au corps ce que le budget coûte à la description ?** La spécification recommande d'externaliser les longs corps en `references/`. Hors périmètre ici, à rouvrir si un chargeur tiers s'en plaint.
