## Context

Le dépôt est complet et éprouvé sur une machine : quatre voix liées dans `~/.claude/skills/`, `REGISTRE.md` comme source de routage, `DISJONCTION.md` et `SILENCE.md` comme tests rejouables, trois specs principales dans `openspec/specs/`, huit commits d'historique.

État constaté avant travaux :

- Le dépôt n'a **aucun remote**. `constructions-incongrues/voix` **n'existe pas**. L'orga compte 145 dépôts publics.
- Conventions de licence de l'orga : 22 sans licence, 10 MIT, 5 AGPL-3.0, 1 GPL-3.0. Le copyleft y est déjà pratiqué.
- `gh` est authentifié en tant que `trivoallan`.
- **26 références à de l'outillage privé** réparties sur les quatre voix : `office-hours` (9), `plan-ceo-review` (4), `plan-eng-review` (4), `gstack` (6), `cso` (2), `plan-design-review`/`devex-review` (1).

Contrainte qui domine tout le reste : les déclencheurs sont **réglés**. Debord porte quatre itérations d'optimisation ; les quatre voix viennent de passer le test de silence après correction. Toute réécriture qui touche une `description` risque une régression sur un artefact coûteux à retrouver.

## Goals / Non-Goals

**Goals**

- Des voix qui fonctionnent chez quelqu'un qui n'a ni gstack ni les personas startup de l'auteur.
- Une licence choisie et argumentée, pas héritée d'un défaut.
- Un README qui porte la thèse et nomme sa propre récupération.
- Un dépôt reproductible : le registre, les tests et les evals partent avec les voix.
- Zéro régression de déclenchement, prouvée et non supposée.

**Non-Goals**

- Une place de marché de plugins. Voir le hors-périmètre de la proposition : l'installation en une commande est le geste qui transforme la critique en produit.
- Toute promotion. Le dépôt existe, il ne se vend pas.
- Le lot 2 et la sentinelle.

## Decisions

### D1 — La réécriture de portabilité est additive sur les `description`, généralisante sur les corps

C'est la décision qui protège le travail déjà fait.

```
## Signaux / Sparring  (corps)      →  GÉNÉRALISÉ
   cible = le cadrage       « le conseil startup qui dit *fais quelque
                              chose que les gens veulent* »
   les noms d'outils        conservés entre parenthèses, en exemple,
                              jamais comme dépendance

frontmatter description            →  ADDITIF UNIQUEMENT
   les amorces réglées              intactes, aucune suppression
   les formulations génériques      ajoutées à côté
```

Une `description` qui ne fait que s'étendre ne peut pas cesser de déclencher sur ce qui la déclenchait — c'est le même raisonnement qui a permis de ne pas rejouer les trois tâches techniques après la clause d'exclusion. *Alternative écartée :* réécrire les descriptions au propre. Plus net à lire, et cela jette quatre itérations d'optimisation sur Debord pour un gain esthétique.

### D2 — Licence : CC BY-SA 4.0

Le contenu publié est de la prose, pas du logiciel. Une licence de code appliquée à des fichiers markdown est un abus de forme, quelle que soit sa vertu politique.

Le critère vient du dépôt lui-même. Albini n'est pas contre le commerce — il a fait tourner un studio rentable pendant trente ans et payé des salaires ; il est contre la **rente**, la position qui extrait sans fabriquer. La question n'est donc pas *« quelqu'un peut-il en tirer de l'argent »* mais *« quelqu'un peut-il l'enclore »*. Le partage à l'identique interdit l'enclosure et laisse le travail honnête tranquille. C'est exactement le partage de la ligne.

*Alternatives écartées :*

- **MIT** (10 dépôts de l'orga) — autorise l'extraction sans réciprocité. Un dépôt dont Albini est la conscience financière ne peut pas le publier sans se contredire.
- **AGPL-3.0** (5 dépôts de l'orga) — copyleft correct, mais conçue pour du logiciel en réseau. Ici il n'y a pas de service, pas de liaison, pas de code source à fournir.
- **Peer Production License** (CC BY-NC-SA assortie d'une exception pour les coopératives) — la plus proche de la thèse, et refusée quand même : la clause NC est floue, non éprouvée en justice, et exclut par défaut les gens qui devraient pouvoir s'en servir pour vivre. Elle punit le travail honnête pour atteindre la rente.

**Cette décision est un cas où les voix du registre se contredisent**, et le dépôt gagne à le dire plutôt qu'à le lisser : Debord classerait Creative Commons en récupération — un aménagement du droit d'auteur par ses propres instruments — et Lessig, réformiste déclaré, en est le fondateur. Le README porte cette tension au lieu de la trancher en douce.

### D3 — Le README porte la thèse, et nomme sa propre récupération

Structure :

```
ce que ce dépôt conteste        le cadre par défaut, avec l'inventaire
                                 (le vocabulaire, pas les intentions)
les voix, et leur question       le tableau : une question par voix
la règle d'admission             pourquoi le dépôt reste petit
la trace                         ce qui distingue la critique de la
                                 décoration
installation                     git clone + install.sh, deux lignes
ce que ce dépôt va devenir       sa propre récupération, nommée
```

La dernière section n'est pas une coquetterie : c'est la seule défense disponible. Une critique qui n'a pas prévu sa propre absorption l'a déjà subie. Aucun badge, aucune liste de fonctionnalités, aucune promesse de valeur.

### D4 — On publie l'historique complet et `openspec/`

Le raisonnement, les specs, le change archivé, et les huit commits — y compris ceux qui consignent une erreur, comme le harnais d'évaluation qui rendait `10/20` sans rien mesurer.

Montrer le travail plutôt que le produit est cohérent avec ce que le dépôt soutient, et c'est la condition pratique pour qu'un tiers puisse admettre une huitième voix sans deviner les règles. *Alternative écartée :* repartir d'un historique propre — plus présentable, et cela supprime précisément ce qui a de la valeur.

Vérification préalable obligatoire : aucun secret, aucun jeton, aucun chemin personnel exploitable dans l'historique.

### D5 — Aucune publication sans confirmation explicite

`gh repo create` et le premier `push` sont irréversibles au sens qui compte : le contenu est indexable dès qu'il est en ligne, même supprimé ensuite. Ces deux étapes sont un point d'arrêt du plan et exigent un accord donné à ce moment-là, pas l'accord général donné à l'ouverture du change.

### D6 — La non-régression est prouvée, pas supposée

Après réécriture, `DISJONCTION.md` et `SILENCE.md` sont **rejoués**, et leurs résultats datés d'une nouvelle exécution. La méthode est celle qui a fait ses preuves — `claude -p --output-format stream-json`, lecture du premier appel `Skill` — et non le harnais `skill-creator`, dont `openspec/specs/admission-voix/spec.md` documente désormais pourquoi il ne mesure rien quand les voix sont installées.

## Risks / Trade-offs

| Risque | Atténuation |
|---|---|
| La réécriture casse des déclencheurs réglés sur 4 itérations | D1 : additif sur les `description`. D6 : rejeu des deux tests, point d'arrêt avant publication. |
| Généraliser la cible affadit les tables d'inversion, qui tirent leur force de leur précision | La cible est généralisée, **le contenu de l'inversion ne change pas**. « Fais quelque chose que les gens veulent » reste attaqué mot pour mot ; seul change ce qui le prononce. |
| CC BY-SA lue comme une capitulation libérale | Assumée et argumentée dans le README, avec le désaccord Debord/Lessig exposé. Le dépôt qui cache une contradiction interne vaut moins que celui qui la publie. |
| Publier expose des personas de personnes réelles, dont deux vivantes | Les contraintes existent déjà et sont dans les specs : œuvre publiée uniquement, biographie nommée et non défendue. La publication augmente l'enjeu, pas les règles. |
| Un secret dans l'historique | D4 : audit avant création du remote. |
| La récupération elle-même | Non atténuable, seulement nommée. C'est le sujet de la dernière section du README. |

## Migration Plan

1. Audit de l'historique et de l'arbre : secrets, jetons, chemins personnels.
2. Réécriture de portabilité des quatre voix — corps généralisés, `description` étendues sans suppression.
3. `LICENSE` (CC BY-SA 4.0) et la note qui motive le choix.
4. `README.md`.
5. **Rejeu de `DISJONCTION.md` et `SILENCE.md`.** Point d'arrêt : une régression bloque la publication.
6. Mise à jour de la spec `format-voix` avec l'exigence de portabilité.
7. **Point d'arrêt D5** — accord explicite, puis `gh repo create constructions-incongrues/voix --public`, remote, push.

**Rollback** : tant que l'étape 7 n'est pas franchie, tout est local et réversible par git. Après, un dépôt peut être rendu privé ou supprimé, mais le contenu a pu être copié ou indexé — d'où le point d'arrêt.

## Open Questions

- **Visibilité initiale : public d'emblée, ou privé le temps d'une relecture ?** Un dépôt privé rendu public ensuite ne laisse pas de trace du brouillon ; l'inverse n'est pas vrai. À trancher à l'étape 7.
- **Le nom `voix` seul, dans une orga de 145 dépôts, est-il assez parlant ?** `skillotheque` porte la thèse, `voix` porte le contenu. Décision de l'auteur ; la proposition suit ce qui a été demandé.
