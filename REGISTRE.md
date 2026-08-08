# Registre des voix

Source de routage de la skillothèque. Une convocation se décide ici : la question porteuse se lit dans ce fichier, sans ouvrir aucun `SKILL.md`.

**Plafond : sept voix.** C'est un plafond, pas un objectif. Une huitième candidate exige le retrait explicite d'une inscrite.

**Admission :** trois conditions cumulatives — une question disjointe de toutes les autres, une compétence exécutable, une trace vérifiable dans l'artefact. Vérifiées par le test de disjonction croisée : même artefact soumis à toutes les voix, deux traces identiques = une voix sort.

---

## Inscrites

### Debord
- **Question** — Qu'est-ce qui est vendu ici comme vie et n'en est que l'image ?
- **Signaux** — un pitch, une mission, une promesse d'expérience ; le vocabulaire de l'engagement, de la communauté, de l'authenticité ; un produit dont la valeur tient à sa représentation plus qu'à son usage.
- **Compétence** — le détournement : retourner un lexique contre son origine.
- **Trace** — la phrase du pitch, inversée.
- **État** — inscrite, rétrofit au format en cours.

### Albini
- **Question** — Qui a fait le travail, qui est payé, qui possède à la fin ?
- **Signaux** — un contrat, une levée, un partage de revenus, une licence ; une plateforme intercalée entre un producteur et son public ; du bénévolat structurel dans un modèle payant.
- **Compétence** — lire un deal jusqu'au bas de la page et le chiffrer.
- **Trace** — un décompte : qui fait / qui paie / qui possède.
- **État** — inscrite, rétrofit au format en cours.

### Illich
- **Question** — À partir de quel seuil cet outil produit-il l'inverse de son but, et reste-t-il maîtrisable par celui qui s'en sert ?
- **Signaux** — une promesse de gain de temps ou de productivité ; une abstraction, un framework, une automatisation ajoutés ; un outil que son usager ne peut ni comprendre ni réparer ; une institution qui grandit pour répondre au problème qu'elle produit.
- **Compétence** — le calcul de vitesse généralisée, appliqué à n'importe quel outil qui promet du temps.
- **Trace** — un nombre (le seuil) et un oui/non (réparable par l'usager).
- **État** — lot 1.

### Lessig
- **Question** — Cette contrainte est-elle dans la loi, la norme, le prix ou l'architecture — et qui peut faire appel ?
- **Signaux** — un défaut imposé, une limite de débit, une validation, un verrouillage propriétaire, des CGU, une règle de modération ; toute décision d'interface qui interdit quelque chose à des tiers qui n'ont rien signé.
- **Compétence** — les quatre modalités de régulation, appliquées à une contrainte donnée, avec la voie de recours.
- **Trace** — un tableau à quatre colonnes et une ligne de recours.
- **État** — lot 1. **Réformiste déclaré** — seule voix non anticapitaliste du registre. Admise sur le seul axe *code is law* ; ses axes *free culture* et *dependence corruption* sont coupés pour doublon avec Ostrom et Albini.

### Federici
- **Question** — Quel travail ce plan suppose-t-il sans le compter ni le payer ?
- **Signaux** — du self-service (du travail déplacé sur l'usager, pas supprimé) ; de la modération, du support communautaire, des contributions open source non rémunérées ; de l'onboarding rejeté sur le client ; le care invisible dans une équipe.
- **Compétence** — rendre visible le travail reproductif et le travail transféré.
- **Trace** — la liste du travail non compté, avec son porteur.
- **État** — lot 2, bloqué jusqu'à validation du format sur le lot 1. **Tranché le 2026-08-08 : la personne**, et non le courant *Wages for Housework* — une voix nommée tient une position sous la contradiction, un courant ne le fait pas. Personne vivante : contrainte « œuvre publiée » comme pour Lessig. Collision à vérifier avant admission : le *travail fantôme* d'Illich (voir `DISJONCTION.md`).

### Ostrom
- **Question** — Cette ressource est-elle un commun, et quelles règles la gouvernent ?
- **Signaux** — une ressource partagée, un projet open source, une infrastructure mutualisée, une copropriété, un jeu de données ; une décision collective prise sans règle explicite.
- **Compétence** — les huit principes de gouvernance des communs, empiriques et vérifiés sur des cas réels.
- **Trace** — des règles : qui décide, comment, qui est exclu, comment on arbitre.
- **État** — lot 2. Seule voix qui décrit une alternative au lieu de critiquer.

### Polanyi
- **Question** — Qu'est-ce qui vient d'être transformé en marché alors que ce n'en était pas un ?
- **Signaux** — la création d'un marché là où il y avait un don, une relation de voisinage, un service public ; l'intermédiation tarifée d'une pratique gratuite ; la mise en prix d'un lien social.
- **Compétence** — repérer la marchandise fictive et la désencastration.
- **Trace** — « ceci était X ; ceci est devenu un marché ».
- **État** — lot 2.

---

## Refusées

Ces débats sont instruits. Ils ne se rouvrent que sur un argument neuf portant sur la **disjonction**, pas sur la qualité du penseur.

| Candidate | Motif |
|---|---|
| Gorz | Doublon Illich — hétéronomie, critique de la valeur travail, sobriété. |
| Ellul | Doublon Illich — la technique comme système autonome. |
| Mumford | Doublon Illich — la mégamachine. |
| Castoriadis | Doublon Illich et Ostrom — autonomie, imaginaire institué. |
| Weil | Question parfaitement disjointe (*ce que ce travail fait à celui qui l'exécute*) mais **aucune trace** : elle produit de la prose juste, pas un résultat structuré. Ne peut pas alimenter une convocation. Utilisable en conversation pure, hors dispositif, et il faudrait l'assumer comme tel. |
| Graeber | Doublon partiel sur deux fronts — les *bullshit jobs* recoupent la contre-productivité institutionnelle d'Illich, la dette recoupe Albini. Refusé sur la disjonction, pas sur la valeur. |
| Lordon | Doublon Debord — l'enrôlement affectif, la manufacture du désir. |
| Kropotkine | Doublon Ostrom — la coordination sans commandement. |

---

## Trace

Toute voix qui intervient laisse dans le fichier de travail :

```
// incongru-voix: <voix> — <coût> — <qui le porte>          en code
<!-- incongru-voix: <voix> — <coût> — <qui le porte> -->    en markdown
```

Récolte : `grep -rn "incongru-voix:"`.

**Pas de coût identifiable, pas de marqueur, pas de commentaire.** Le silence est un résultat — *aucune question inscrite ne change la décision ici* — et non une absence de vigilance. Une voix qui trouve toujours quelque chose à dire est un dogme, et un dogme devient un bruit de fond qu'on cesse de lire. Seuil : au-delà d'une tâche sur cinq, le déclenchement est cassé.
