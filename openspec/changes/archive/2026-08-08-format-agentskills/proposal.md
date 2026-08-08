## Why

Les voix sont écrites pour un chargeur : celui de Claude Code. Le dépôt affirme pourtant, dans son README et dans deux specs, qu'elles sont *« des fichiers markdown, utilisables par tout agent qui charge des skills »*. Cette affirmation n'a jamais été vérifiée contre une norme — elle reposait sur le fait que le format semblait simple.

Il existe une spécification publique, `agentskills.io`, avec une bibliothèque de validation (`skills-ref`, publiée sur npm). Mesuré contre elle, **les quatre voix sont non conformes**, et pas à la marge :

```
                description   limite : 1024 caractères
  guy-debord         2215      dépasse de 1191   (×2,2)
  steve-albini       2411      dépasse de 1387   (×2,4)
  lessig             1828      dépasse de  804
  illich             1702      dépasse de  678
```

L'affirmation de portabilité était donc fausse. Un chargeur qui applique la spécification rejette ou tronque les quatre.

Ce n'est pas une correction cosmétique, parce que la `description` est **l'artefact le plus réglé du dépôt** : quatre itérations d'optimisation sur Debord, une clause d'exclusion et une clause de situation ajoutées et mesurées aujourd'hui. Il faut en retirer entre 40 et 58 % sans perdre le déclenchement — et la clause de situation, dont dépend toute la sentinelle à venir, doit survivre à la coupe.

**S'y conformer n'engage aucune inscription.** `agentskills.io` publie une norme et une bibliothèque de validation, pas un annuaire de skills. Le refus de l'index tiers inscrit dans `paquet-plugin` n'est pas concerné et reste entier.

## What Changes

- **Les quatre `description` passent sous 1024 caractères.** Ordre de priorité établi et motivé, parce que couper sans règle revient à couper au hasard : la clause de situation d'abord, l'exclusion expositive ensuite, puis les amorces nommées, puis la contre-voix, et les exemples d'outillage tiers en dernier.
- **BREAKING pour `portabilite-voix`.** Son exigence *« Extension additive des déclencheurs »* interdit aujourd'hui de retirer une amorce. Ce change ne peut pas se faire sans la modifier : la règle devient *additive par défaut, et toute suppression exige une nouvelle mesure*.
- **Champs de conformité ajoutés** — `license` dans chaque `SKILL.md`, pour que la licence voyage avec le fichier quand la voix est copiée hors du dépôt. Le fichier `LICENSE` reste à la racine, mais un fichier détaché ne l'emporte pas avec lui.
- **Un budget de description devient une exigence de `format-voix`.** Les clauses obligatoires du dépôt et la limite de la norme doivent tenir ensemble ; sans budget écrit, la prochaine voix repassera au-dessus.
- **Validation par l'outil de référence** — `skills-ref validate` remplace mes `grep` maison comme critère de conformité. Un contrôle que j'écris moi-même n'est pas un contrôle.
- **Non-régression obligatoire** — le test de routage et le test de silence sont rejoués après coupe. Une régression bloque.

## Capabilities

### New Capabilities

- `conformite-agentskills` : ce que le dépôt doit satisfaire pour être conforme à la spécification publique — limites de champs, correspondance nom/répertoire, licence embarquée, et la validation par l'outil de référence plutôt que par un contrôle maison.

### Modified Capabilities

- `portabilite-voix` : l'interdiction de retirer une amorce de déclenchement devient une obligation de re-mesurer. La règle actuelle rend toute mise en conformité impossible.
- `format-voix` : la `description` reçoit un budget et un ordre de priorité. Le format impose aujourd'hui deux clauses obligatoires — situation et exclusion — sans dire comment elles cohabitent avec une limite de taille.

## Impact

- **Les quatre `skills/*/SKILL.md`** — réécriture des `description`, de 40 à 58 % de coupe. C'est le travail réel de ce change, et le seul risqué.
- **Risque de régression sur des déclencheurs mesurés** — `DISJONCTION.md` et `SILENCE.md` doivent être rejoués, avec un point d'arrêt avant de conclure.
- **`openspec/specs/portabilite-voix/spec.md`** — une exigence modifiée.
- **`openspec/specs/format-voix/spec.md`** — une exigence ajoutée.
- **`README.md`** — l'affirmation de portabilité devient vérifiable, avec la commande qui la vérifie.
- **Dépendance de développement** — `skills-ref` (npm), utilisée pour valider, non requise à l'exécution.
- **Aucun code applicatif.**

## Hors périmètre

- **Le découpage des corps en `references/`.** La spécification note qu'un `SKILL.md` entier est chargé à l'activation et suggère d'externaliser les longs contenus. Nos fichiers font 10 à 14 Ko. C'est un vrai sujet, mais il touche à la façon dont une voix travaille une fois convoquée, pas à sa conformité — et mélanger les deux rendrait la non-régression illisible.
- **`metadata`, `compatibility`, `allowed-tools`.** Facultatifs, et la spécification dit elle-même que la plupart des skills n'ont pas besoin de `compatibility`. Rien ne les justifie ici.
- **La sentinelle** et **le lot 2**.
