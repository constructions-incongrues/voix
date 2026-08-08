## Context

41 commits, 0 préfixe de type, 56 caractères de sujet en moyenne. Les messages sont des phrases françaises qui portent un argument plutôt qu'une catégorie — *« Contrat du hook Stop vérifié, pas supposé »*, *« Révision du design : on ne coupe pas, on réécrit court »*. Six d'entre eux (15 %) enregistrent la **correction d'une croyance antérieure**, une classe que Conventional Commits ne nomme pas.

Le dépôt versionne selon trois règles écrites au README, dont l'axe est **le registre des voix** et non le code. Aucune dépendance runtime, aucun outil de build, aucun fichier de gouvernance conventionnel. `REGISTRE.md` § Outillage exige qu'une prescription de méthode entre **par décision**, après le retrait d'`openspec-git-discipline` arrivée par effet de bord d'une installation.

Décideur unique : l'auteur. Aucun ADR antérieur — le répertoire `adr/` n'existe pas encore.

## Goals / Non-Goals

**Goals :**
- Rendre le niveau de version dérivable d'un historique par une machine.
- Faire entrer la convention par décision explicite, tracée.
- Ne rien retirer à ce que les messages savent déjà dire.

**Non-Goals :**
- Réécrire l'historique existant.
- Ajouter un outil, une dépendance ou une étape de CI en v1.
- Trancher la politique de branches — décision distincte, toujours ouverte.
- Générer un changelog automatiquement. La dérivation est rendue *possible* ; l'automatiser est une décision ultérieure.

## Decisions

### D1 — Type et scope en anglais, description en français

Les jetons `feat`/`fix` sont des identifiants de la spécification, pas de la prose : les traduire casse tout outil conforme sans rien gagner. La description reste française, comme le reste du dépôt.

*Alternative écartée :* traduire les types (`corr:`, `fonc:`). Produit une convention qui ressemble à Conventional Commits sans en être, donc le pire des deux.

### D2 — La description reste une phrase qui porte un constat

C'est la décision qui protège ce que l'adoption menace. Conventional Commits contraint le **préfixe** ; rien dans la spécification n'oblige à réduire la phrase à une étiquette. La règle est donc rendue explicite dans la spec, avec un scénario négatif (`fix(sentinelle): correction de bug` échoue).

*Alternative écartée :* laisser la description libre, sans exigence. C'est ce qui produit en pratique la dérive vers `fix: divers` — et ici la perte serait exactement les six commits de correction de croyance, c'est-à-dire les plus utiles du dépôt.

### D3 — ~~Table de correspondance, README souverain~~ → renversé par `adr/0002`

> **Renversé.** Cette décision posait le README comme source d'autorité et les types comme indicatifs. `adr/0002` a remplacé ce garde-fou : les types font autorité, la table devient la description de la configuration de release-please. Le raisonnement ci-dessous est conservé tel qu'il a été écrit — c'est ce que le changement croyait, et le dépôt tient que ça se lise.

La table relie les types aux trois niveaux du README. En cas de conflit, **le README l'emporte** et la table est corrigée.

*Pourquoi ce sens et pas l'autre :* l'axe de version du dépôt est le registre, pas le code. `feat` ne sait rien dire de *« une voix change de question »*. Faire de la table la source d'autorité inverserait la dépendance et remplacerait une règle de domaine par une taxonomie générique.

*Alternative écartée :* dériver la version uniquement des types, à la façon de `semantic-release`. Suppose que l'axe sémantique du projet est le code. Il ne l'est pas.

### D4 — Jeux fermés, élargis par commit `docs(specs):`

Six types, six scopes, tirés des objets réels du dépôt. Un ajout passe par une modification de la spec, jamais par un usage de fait.

*Pourquoi :* c'est la mécanique du registre appliquée à la convention elle-même — un jeu ouvert dérive, et personne ne remarque la dérive. `chore` est admis à contrecœur : c'est le fourre-tout de la spécification, et il faudra surveiller sa part.

### D5 — Aucun outil de vérification en v1

Pas de `commitlint` (dépendance npm, exclue par la contrainte du dépôt), pas de hook `commit-msg`.

*Pourquoi :* la convention est de toute façon appliquée par une seule personne, et `org.md` établit que les protocoles de ce dépôt **orientent sans lier**. Un hook de 20 lignes en stdlib serait cohérent avec le dépôt et reste la première chose à construire si le besoin se manifeste.

*Déclencheur de réouverture :* trois commits non conformes poussés sur `main` — le signal que la discipline seule ne suffit plus.

### D6 — Historique non réécrit

Les 41 commits existants restent tels quels. Tout outil de dérivation traite un sujet sans type comme *antérieur*, non comme *invalide*.

*Pourquoi :* la valeur déjà tenue par le dépôt sur ses archives — *« les réécrire pour qu'ils aient l'air à jour serait falsifier un dossier »*. Une réécriture casserait par ailleurs tout SHA publié.

## Risks / Trade-offs

- **La convention aplatit les messages malgré D2** → D2 est portée par une exigence testable avec un scénario négatif ; le déclencheur de D5 la surveille indirectement. Reste que rien ne l'empêche mécaniquement.
- **`chore` devient un fourre-tout** → Mitigation : mesurer sa part au premier bilan. Au-delà d'un commit sur cinq, le jeu de types est mal ajusté, pas l'auteur.
- **Les six commits de correction de croyance n'ont pas de type propre** → Ils tombent en `docs` ou `fix`, et c'est une perte de finesse assumée. Mitigation : D2 impose que le constat reste dans la phrase. Un type `revise:` hors spécification a été envisagé et écarté — il casserait la conformité, qui est le seul motif de l'adoption.
- **Deux conventions coexistent dans l'historique** → Assumé et documenté (D6). C'est la condition de l'honnêteté du dossier.
- **Le tableau du README doit être tenu à jour** → Il devient un point de dérive silencieuse, comme `REGISTRE.md` l'est déjà pour le routage. Aucune mitigation à ce stade ; à surveiller.

## Migration Plan

1. Écrire la section « Convention de commit » dans le `README.md`, avec la table.
2. Appliquer à partir du commit suivant. Aucune rétroactivité.
3. Premier bilan après 20 commits conformes : part de `chore`, conformité, et si un type manque.

## Open Questions

- La politique de branches reste non tranchée (`REGISTRE.md`, `org.md`). Elle interagit avec cette convention le jour où un changelog est généré par branche — hors périmètre ici, à trancher séparément.
- Le pied de page machine (`Registre: mineure`) a été envisagé comme alternative complète à l'adoption. Écarté par décision de l'auteur en faveur de Conventional Commits. Il resterait disponible en complément si la table D3 s'avérait insuffisante à lever une ambiguïté.
