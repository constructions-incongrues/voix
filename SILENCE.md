# Test de silence

Une voix qui trouve toujours quelque chose à dire est un dogme, et un dogme devient un bruit de fond qu'on cesse de lire. Seuil du registre : **au-delà d'une tâche ordinaire sur cinq, le déclenchement est cassé.**

## Le harnais `skill-creator` ne mesure rien ici — à savoir avant de le relancer

Premier passage : `run_eval.py` a rendu `10/20` pour Illich et `10/20` pour Lessig. En apparence, la moitié. En réalité **`rate=0/3` sur les quarante requêtes, positives comprises** — 120 invocations, zéro déclenchement détecté. Les seuls « succès » étaient les négatives, qui passent mécaniquement quand rien ne se déclenche jamais.

Cause : le harnais installe une copie temporaire de la skill sous le nom `<voix>-skill-<hash>` dans `.claude/commands/`, puis vérifie que le nom appelé contient ce hash. **Il suppose que la skill testée n'est pas déjà installée.** Depuis la tâche 2.4, les quatre voix sont liées dans `~/.claude/skills/` : le modèle appelle la vraie — `Skill{skill: "illich"}` — dont le nom ne contient pas le hash. Chaque déclenchement réussi est compté comme un échec.

Un score `N/20` de ce harnais n'est donc lisible que si l'on a d'abord décroché les liens. Et sa détection a un second défaut, ligne 141 de `run_eval.py` : si le premier appel d'outil n'est ni `Skill` ni `Read`, la fonction retourne `False` sans attendre la suite.

**Méthode retenue à la place :** `claude -p ... --output-format stream-json`, lecture directe du premier appel `Skill`. Un fait par requête, rien à interpréter.

## Mesure du 2026-08-08

### Tâches ordinaires — la voix doit se taire

| Requête | Avant | Après |
|---|---|---|
| segfault dans le parseur | silence | silence |
| déclaration de TVA depuis le FEC | `comptable` | `comptable` |
| renommage de fonction + appels | silence | silence |
| index SQL sur `created_at` | silence | silence |
| exposé « code is law » pour un cours | **`lessig`** ✗ | silence |
| exposé « convivialité » pour un exposé | — | silence |
| quel micro Albini sur *In Utero* | — | silence |
| dissertation sur le spectacle | — | silence |

Le déclenchement de `comptable` sur la TVA est correct : c'est la bonne skill, et aucune voix ne s'est manifestée.

Les trois tâches techniques n'ont pas été rejouées après correction : le correctif n'ajoute que des exclusions, il ne peut pas rendre bavarde une voix déjà silencieuse.

### Contrôles positifs — la voix doit déclencher

| Requête | Résultat |
|---|---|
| « ce framework est-il encore convivial, ou plus personne ne peut le réparer » | `illich` |
| « ce pipeline CI est censé nous faire gagner du temps mais on le rafistole » | `illich` |
| « blocage à 100 req/min, sans notification ni contestation » | `lessig` |

### Verdict

**0 déclenchement de voix sur 8 tâches ordinaires ou expositives. 3/3 sur les contrôles positifs.** Seuil respecté.

## Rejeu du 2026-08-08, après la réécriture de portabilité

Les quatre `description` ayant été étendues, les deux tests ont été rejoués. La méthode est la même : `claude -p --output-format stream-json`, lecture du premier appel `Skill`.

| Catégorie | Cas | Résultat |
|---|---|---|
| expositif | 4 (Lessig, Illich, Albini, Debord) | 4 silences |
| ordinaire | 3 (segfault, renommage, index SQL) | 3 silences |
| contrôles positifs | 4, un par voix | 2 succès, **2 échecs** |

**Aucune régression** : les deux échecs sont antérieurs à la réécriture. Vérifié en rejouant le cas d'Albini contre sa version d'avant portabilité — silence déjà. C'est la première fois que les quatre voix étaient éprouvées en positif, et le test l'a trouvé pour cette raison.

Le défaut et sa correction sont décrits dans [`DISJONCTION.md`](DISJONCTION.md) : les descriptions de Debord et d'Albini étaient de forme *invitation* et non de forme *situation*. Après correction, les quatre contrôles positifs passent et les sept cas de silence tiennent.

## Le défaut trouvé, et sa correction

Nommer un penseur est ambigu : *« sois Lessig »* et *« parle-moi de Lessig »* partagent le même mot. Les quatre `description` déclenchaient sur le mot-clé seul, et convoquaient donc la persona sur une demande de fiche de révision.

Les quatre portent désormais une clause d'exclusion explicite — exposé, résumé neutre, explication, fiche, pour un cours ou un article : *on parle **de** lui, pas **avec** lui*. Lessig porte en plus l'exclusion de ses deux axes coupés (choix de licence, financement politique).

C'est le mode de défaillance par défaut d'une skillothèque de personas. **Toute voix admise doit porter cette clause dès l'écriture, et être éprouvée sur au moins un cas expositif.**

> **Corrigé le même jour, plus bas.** Ce diagnostic était incomplet et sa conclusion trop large. La cause n'était pas l'ambiguïté du nom mais le **bourrage de la description** : répéter « que dirait X », « voix de X », les concepts de X rend le nom saillant hors contexte. Description brève, le faux positif disparaît sans aucune clause. La clause reste nécessaire pour une description qui porte des amorces nommées, et inutile sinon — c'est ce que dit désormais `format-voix`. Le diagnostic est conservé tel quel parce qu'il a été écrit de bonne foi sur une mesure réelle, et que le voir corrigé vaut mieux que de ne pas le voir.

## Rejeu du 2026-08-08, après réécriture brève des descriptions

Les quatre `description` sont passées de 1702-2411 caractères à 250-346, purement descriptives, sans amorces nommées ni clause d'exclusion. Rejeu complet, les quatre voix en concurrence.

| Volet | Cas | Résultat |
|---|---|---|
| routage | 4, une situation par voix, sans la nommer | 4 bonnes convocations |
| expositif | 4, un par voix | 4 silences |
| ordinaire | 3 (segfault, renommage, TVA) | aucune voix ; `superpowers:systematic-debugging` et `comptable` se déclenchent, ce qui est correct |

**11 sur 11.** Ajouté aux 20 sondes individuelles passées voix par voix pendant la réécriture, cela fait 31 mesures sans régression.

Ce que le rejeu établit : **1452 à 2101 caractères de description ne produisaient aucun déclenchement mesurable.** L'invocation par le nom fonctionne toujours alors qu'aucune amorce nommée ne subsiste — le nom est dans `name` et dans le corps, cela suffit. Et le faux positif expositif du matin, qui avait motivé une clause d'exclusion dans les quatre voix, disparaît sans elle.
