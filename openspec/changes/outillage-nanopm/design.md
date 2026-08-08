## Context

La proposition établit le cas et son coût. Ce document dit comment on tranche — et il a changé d'avis en cours d'écriture, parce qu'un fichier de six lignes rendait inutile le mécanisme que la spec réclamait.

**ADR en force.** `adr/` contient trois fichiers. `adr/0002` porte `supersedes: ADR-0001` ; `adr/0003` ne supersède rien. L'ensemble en vigueur est donc **`adr/0002` et `adr/0003`**. `adr/0001` est du contexte historique. Aucun des deux ne parle d'outillage : ce design n'a rien à contredire, et `adr/0004` complétera sans superséder.

**Le `.gitignore` existe déjà, et il porte la réponse.**

```
# Outillage régénérable, non couvert par la licence du dépôt
# .claude/  : généré par `openspec init --tools claude` (fichiers MIT dOpenSpec)
# .serena/  : configuration machine locale
.claude/
.serena/
__pycache__/
```

Le dépôt a donc **déjà une catégorie écrite** pour ce cas — « outillage régénérable, non couvert par la licence du dépôt » — assortie d'un motif par entrée. La question n'est pas d'inventer un mécanisme d'exclusion : elle est de reconnaître celui qui est là.

**Et il rend une ligne du hook inutile.** `travail_en_cours()` appelle `git ls-files --others --exclude-standard`, puis saute `nom.startswith(".serena/")`. Or `--exclude-standard` applique déjà `.gitignore`. Vérifié par sonde : un fichier déposé dans `.serena/` **n'apparaît pas** dans la sortie. La ligne en dur du hook est du **code mort** — vestige, probablement, du jour où l'exclusion a été posée avant l'entrée `.gitignore`.

`.nanopm/`, lui, apparaît — parce qu'il n'est pas ignoré. Toute la capture de routage tient à cette seule différence.

## Goals / Non-Goals

**Goals :**

- Trancher `.nanopm/` par une décision écrite plutôt que par l'oubli.
- Supprimer la capture de routage — 12 convocations sur 16 — sans ajouter de mécanisme.
- Faire passer la règle d'admission de l'outillage de la prose de `REGISTRE.md` à une capacité, avec un périmètre qui ne nomme plus de répertoire.
- Laisser une trace exploitable : le motif du verdict, quel qu'il soit.

**Non-Goals :**

- Désinstaller la skill `nanopm` de la machine. Ce qui est décidé ici, c'est ce qui appartient au dépôt, pas ce que l'auteur a le droit d'exécuter.
- Juger la qualité du produit `nanopm`. Le jam d'aujourd'hui a rendu quelque chose ; le verdict porte sur l'appartenance au dépôt, pas sur l'utilité de l'outil.
- Réécrire le préfiltre de la sentinelle. Une ligne disparaît, aucune n'est ajoutée.

## Decisions

### D1 — `.nanopm/` est classé méthode prescrite

`NANOPM-WIKI.md` fait 15 533 octets et décrit trois couches, des sections calquées sur des phases, des types de page, des arêtes typées, une provenance obligatoire, un journal append-only. Ce n'est pas une capacité rendue possible : c'est un ordre de travail, un vocabulaire et des gabarits.

Le test de la spec s'applique sans hésiter, et la règle du doute n'a même pas à jouer.

*Contre-argument à traiter honnêtement :* le jam du 2026-08-08 a produit des mesures réelles — couverture de routage à 50 %, six termes manquants à `lessig`, la part des convocations qui changent une décision. Cette valeur est réelle. Mais **elle n'a rien dû aux artefacts installés** : zéro page a été lue, parce que zéro page existait. Les 15 533 octets de schéma n'ont contribué à aucune ligne du résultat. Ce qui a produit la valeur est la conversation et la lecture du dépôt, disponibles sans rien poser dans l'arbre.

### D2 — `.nanopm/` n'entre pas au dépôt, et le motif est inscrit

Il rejoint le `.gitignore` sous la catégorie déjà écrite — outillage régénérable, non couvert par la licence — avec sa ligne de motif à côté de `.claude/` et `.serena/`. Le tableau d'outillage de `REGISTRE.md` gagne son entrée : **non admis**, avec ce qu'il prescrivait.

Ce n'est ni « supprimer » ni « commiter ». C'est la troisième voie, et c'est celle que le dépôt s'était déjà donnée pour `.claude/` — un répertoire dont il se sert tous les jours et qu'il ne versionne pas.

*Alternatives.* **Commiter** — rejeté : 28 ko de schéma d'un fournisseur, sous une licence qui n'est pas celle du dépôt, pour zéro page de contenu. **Supprimer les fichiers** — rejeté : la skill les recrée à la prochaine invocation, et supprimer sans inscrire au tableau viole l'exigence « un refus se consigne ». **Admettre par ADR** — rejeté par D1 et par la mesure de routage ; réouvrable si l'auteur adopte réellement la méthode, et le motif inscrit dira alors quoi réexaminer.

### D3 — L'exclusion de routage passe par `.gitignore`, et le hook perd une ligne

C'est la décision qui a changé en cours d'écriture. La spec de ce changement exige que la liste d'exclusion soit **déclarée au registre** plutôt que codée en dur. L'intention est juste — une décision de routage doit se lire là où les décisions se lisent — mais le moyen est de trop : `.gitignore` est déjà cet endroit, il porte déjà un motif par entrée, et `git ls-files --exclude-standard` l'applique gratuitement.

Conséquences, dans cet ordre :

1. `.nanopm/` entre au `.gitignore` (D2) — et cesse par là même d'être vu par la sentinelle. **Aucune ligne de hook n'est écrite pour ça.**
2. La ligne `nom.startswith(".serena/")` du hook est **supprimée** : elle est morte depuis que `.serena/` est ignoré, et la garder laisserait croire que le hook tient sa propre liste.
3. L'exigence de spec est corrigée pour désigner `.gitignore` comme le lieu de déclaration, l'interdiction du codage en dur restant inchangée.

*Ce que ça préserve.* Un fichier neuf écrit par l'auteur n'est pas ignoré : il reste examiné. La distinction n'est pas *suivi / non suivi* — c'est *à vous / régénérable*, et `.gitignore` la porte déjà exactement.

*Alternative.* **Une liste dans `REGISTRE.md`, lue par le hook** — rejetée : elle dupliquerait `.gitignore` en s'en écartant au premier oubli, et ajouterait du code de lecture pour reproduire ce que git fait déjà. Le registre est exécutable pour les termes de routage parce que rien d'autre ne les porte ; ici quelque chose les porte.

### D4 — La mesure de routage est portée par l'ADR

L'exigence est écrite dans la spec : un outil qui capte le routage prive le travail réel des voix, et ce coût se chiffre. `adr/0004` portera **16 convocations, 12 déclenchées par `.nanopm/`, 8 `guy-debord` dont 6 sur des jeux de fichiers quasi identiques, sur 202 tours**.

Elle a aussi une valeur de contrôle après coup : le même journal, relu après le `.gitignore`, doit montrer la part retomber à zéro.

## Risks / Trade-offs

- **Ignorer, c'est rendre invisible.** Un outil qui prescrit et qu'on ne voit plus prescrit toujours. → La ligne au tableau d'outillage est la trace ; c'est précisément ce que l'exigence « un refus se consigne » impose, et pourquoi le `.gitignore` seul ne suffirait pas.
- **La skill recrée les fichiers à chaque invocation.** `.gitignore` ne l'empêche pas, il l'ignore. → Assumé : le dépôt décide de ce qu'il versionne, pas de ce que l'auteur exécute. Le coût résiduel est un répertoire de 28 ko sur le disque.
- **`--exclude-standard` dépend du `.gitignore` du dépôt, donc du clone.** Un contributeur avec des exclusions locales différentes verrait un routage différent. → Réel et non mitigé. La sentinelle n'a jamais prétendu être reproductible entre machines ; c'est un dispositif d'accompagnement, pas un contrôle de conformité. À reprendre si elle devient bloquante en CI.
- **La catégorie « régénérable » finira par accueillir ce qui ne l'est pas.** → Le motif écrit par entrée est le garde-fou, et c'est celui que `.gitignore` porte déjà.
- **Le verdict ferme une porte que personne n'a essayé d'ouvrir.** Le dépôt n'a jamais fait tourner la chaîne Define. → C'est assumé et daté : le motif inscrit doit dire ce qui rouvrirait la question, faute de quoi le refus se durcit tout seul.

## Migration Plan

1. **`.gitignore`** — ajouter `.nanopm/` avec sa ligne de motif, dans le bloc existant.
2. **`hooks/sentinelle.py`** — supprimer le saut `.serena/` en dur, devenu mort.
3. **`REGISTRE.md`** — la règle d'outillage renvoie à la capacité `admission-outillage` ; le tableau gagne la ligne `nanopm`, statut non admis, avec ce qu'il prescrivait et ce qui rouvrirait la question.
4. **`adr/0004`** — la décision, avec la mesure de routage.
5. **Contrôle** — le journal de la sentinelle, après coup : aucune convocation déclenchée par `.nanopm/`.

**Rollback.** Une ligne de `.gitignore` à retirer. La ligne de hook supprimée est du code mort ; la remettre ne changerait rien.

## Open Questions

- **L'exigence de spec « déclaré au registre » est à corriger avant l'ADR.** D3 établit que `.gitignore` est le lieu, et que la duplication dans `REGISTRE.md` coûterait sans rendre. L'intention — pas de codage en dur — est conservée. À reprendre par `/opsx:update` sur `specs`, avant que l'ADR ne fige un instrument que le design vient de contredire.
- **Le verdict de D1 et D2 appartient à l'auteur.** Le design le recommande sur la mesure et sur la règle que le dépôt s'est donnée ; l'ADR peut trancher dans l'autre sens, auquel cas D2 devient une admission et le tableau porte l'entrée inverse, avec le coût de routage inscrit comme coût accepté.
