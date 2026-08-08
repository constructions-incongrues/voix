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

### D1 — On ne coupe pas, on réécrit court. Mesuré.

La décision initiale — un ordre de priorité pour rogner 1191 caractères — est abandonnée. Elle reposait sur l'hypothèse que la longueur portait du déclenchement. L'expérience la réfute.

**Illich, 1702 → 250 caractères**, description purement descriptive : ni amorces nommées, ni clause d'exclusion, ni mention de contre-voix. Cinq sondes :

| Sonde | Résultat |
|---|---|
| pipeline CI rafistolé, sans le nommer | `illich` |
| « que dirait Illich de notre stack ? » | `illich` |
| convivialité, pour un exposé | silence |
| *Une société sans école*, résumé pour un groupe de lecture | silence |
| index SQL | silence |

**1452 caractères ne faisaient rien de mesurable.** L'invocation par le nom fonctionne toujours, alors qu'aucune amorce nommée ne subsiste : le nom est dans `name:` et dans le corps, cela suffit.

La cible n'est donc pas « juste sous 1024 » mais **l'échelle de l'exemple de référence de la spécification, qui fait 182 caractères** : ce que fait la skill, et quand l'employer. Le reste appartient au corps du fichier, qui n'a pas de limite.

*Alternative écartée :* garder la forme longue en la rognant. On aurait conservé, au prix d'un arbitrage difficile, un texte dont l'expérience montre qu'il ne servait pas.

### D1bis — La clause d'exclusion était iatrogène

Le mot est d'Illich, et il est exact : *le mal produit par le soin lui-même*.

Ce matin, `lessig` s'est déclenché sur « explique-moi code is law, pour un cours ». J'en ai conclu qu'il fallait une clause « ne pas déclencher sur un exposé », je l'ai écrite dans les quatre voix et inscrite comme exigence dans `format-voix`.

La cause réelle n'était pas une ambiguïté de fond entre *« sois X »* et *« parle-moi de X »*. C'était le bourrage : une description répétant « que dirait Illich », « voix d'Illich », « convivialité » rend le nom saillant hors de tout contexte. Description brève, le faux positif disparaît **sans aucune clause**, sur deux cas expositifs distincts.

Conséquence sur l'exigence : elle ne disparaît pas, elle **se rattache à sa cause**. La clause d'exclusion devient obligatoire *lorsque la description porte des amorces nommées*, et inutile sinon. Une exigence qui prescrit le remède sans nommer la maladie fait dépenser des caractères contre un problème qu'on ne reproduit plus — exactement ce que ce dépôt reproche aux règles des autres.

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
| Le résultat d'Illich ne vaut que pour Illich | Sa question est lexicalement distinctive (*outil*, *temps*, *productivité*). Debord (*ce qui est vendu comme de la vie*) et Albini (*qui est payé*) se reconnaissent moins bien en surface. Les cinq sondes sont rejouées voix par voix, et un échec sur l'une n'autorise pas à conclure pour les autres. |
| Une voix devient trop maigre pour se déclencher hors de son nom | Le volet routage le détecte : il interroge la situation **sans** nommer la voix. C'est la sonde qui compte, les quatre autres ne font que borner. |
| La description brève ne porte plus la contre-voix « conseil startup » | Ce contenu vit dans le corps du fichier, chargé dès l'activation. La question est de savoir s'il faut encore être *convoqué* dessus — à mesurer, pas à supposer. |
| Assouplir « additive uniquement » ouvre la porte aux coupes non mesurées | D2 : l'autorisation est conditionnelle à la preuve, pas générale. Sans mesure, la suppression reste interdite. |
| Retirer la clause d'exclusion réintroduit le faux positif | D1bis : elle n'est pas retirée, elle devient conditionnelle à sa cause. Une description qui porte des amorces nommées la garde. |
| La spécification évolue et le dépôt redevient non conforme | `skills-ref` est une dépendance de développement ; la validation se rejoue à chaque voix admise. |

## Migration Plan

1. Installer `skills-ref` et établir la mesure de départ des quatre voix.
2. Modifier `portabilite-voix` et `format-voix` **avant** toute réécriture — sinon les tâches suivantes violent des exigences en vigueur.
3. Réécrire les trois descriptions restantes en bref, **une voix à la fois, cinq sondes après chacune**. Illich est déjà fait et mesuré. Ordre : Lessig, Debord, Albini — du plus au moins lexicalement distinctif, pour que l'échec, s'il vient, vienne sur le cas où l'on sait déjà quoi en conclure.
4. Ajouter `license` aux quatre.
5. Valider avec `skills-ref`.
6. **Point d'arrêt** : rejeu complet routage + silence sur les quatre ensemble — une voix peut passer seule et perdre son arbitrage face aux trois autres.
7. Specs, README, publication.

**Rollback** : `git revert`. Les descriptions d'avant sont dans l'historique, et l'historique n'est pas réécrit.

## Open Questions

- **La clause de situation reste-t-elle nécessaire ?** Illich passe le volet routage avec une description qui ne la porte pas sous sa forme canonique — elle y est dissoute dans le « à employer quand… ». Si les trois autres font de même, l'exigence `format-voix / Clause de situation` doit être reformulée : ce qui compte n'est pas la formule, c'est que la situation soit décrite. À trancher après mesure, pas avant.
- **Les quatre sections normalisées coûtent-elles au corps ce que la brièveté gagne à la description ?** La spécification recommande d'externaliser les longs corps en `references/`. Hors périmètre ici, à rouvrir si un chargeur tiers s'en plaint.
