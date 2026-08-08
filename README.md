# Voix

Une skillothèque : des voix qui contestent le cadre par défaut des assistants de code, et de la plupart des skills qu'on leur installe.

Quatre voix sont écrites et éprouvées. Le registre en prévoit sept, et pas une de plus.

---

## Ce que ce dépôt conteste

Pas les intentions de qui que ce soit. Le **vocabulaire**, et ce qu'il rend pensable.

Un corpus de skills installé sur une machine de développeur porte un cadre que rien ne conteste. Certaines l'assument — conseil startup, revue de plan en mode fondateur, priorisation de roadmap. D'autres le transportent dans leurs mots sans le dire :

| Le mot | Ce qu'il rend pensable | Ce qu'il rend impensable |
|---|---|---|
| dette technique | *ce code coûte des intérêts* | *ce code est laid* |
| ressources humaines | *une ligne de coût à optimiser* | *des gens* |
| parties prenantes | *des positions à arbitrer* | *ceux qui portent le coût sans être dans la pièce* |
| acquisition d'utilisateurs | *un entonnoir à élargir* | *des personnes qu'on recrute* |

Et une troisième couche, la plus difficile à voir : la posture par défaut de l'assistant lui-même. Serviable, optimisante, capable de présenter trois options avec leurs compromis — jamais de dire *ne fais pas ça*, jamais de dire *c'est laid*, jamais de refuser le cadre de la question.

Ces voix n'ajoutent pas un avis de plus. Chacune apporte une **compétence** que le défaut n'a pas.

## Les voix, et la question de chacune

Une question par voix, et aucune ne recouvre celle d'une autre. C'est la règle qui tient tout le reste.

| Voix | La question qu'elle seule pose | État |
|---|---|---|
| **Debord** | Qu'est-ce qui est vendu ici comme vie et n'en est que l'image ? | écrite |
| **Albini** | Qui a fait le travail, qui est payé, qui possède à la fin ? | écrite |
| **Illich** | À partir de quel seuil cet outil produit-il l'inverse de son but — et reste-t-il réparable par celui qui s'en sert ? | écrite |
| **Lessig** | Cette contrainte est-elle dans la loi, la norme, le prix ou l'architecture — et qui peut faire appel ? | écrite |
| **Federici** | Quel travail ce plan suppose-t-il sans le compter ni le payer ? | prévue |
| **Ostrom** | Cette ressource est-elle un commun, et quelles règles la gouvernent ? | prévue |
| **Polanyi** | Qu'est-ce qui vient d'être transformé en marché alors que ce n'en était pas un ? | prévue |

Chacune sait *faire* quelque chose, pas seulement penser quelque chose. Illich applique le calcul de vitesse généralisée d'*Énergie et équité* — celui qui établit qu'une automobile roule à 6 km/h une fois compté le temps de travail nécessaire à la payer — à n'importe quel outil qui promet du temps. Lessig remplit les quatre modalités de régulation et la ligne de recours. Albini suit l'argent jusqu'au bas de la page. Debord retourne un lexique contre son origine.

**Lessig est le seul non-anticapitaliste du registre**, et son fichier le déclare : il répare le cadre au lieu de le contester, et cette position est peut-être exactement ce qui permet au cadre de durer. Une voix réformiste non déclarée est la sortie de secours qu'on attrape sous pression.

## Pourquoi le dépôt reste petit

Une voix entre si elle satisfait **trois conditions**, pas deux : une question disjointe de toutes les autres, une compétence exécutable, une trace vérifiable dans le fichier de travail.

La disjonction n'est pas une déclaration d'intention, c'est un test : le même artefact est soumis à toutes les voix, et **si deux produisent la même trace, l'une des deux sort**. Voir [`DISJONCTION.md`](DISJONCTION.md).

Refusés à ce jour, avec leur motif : Gorz, Ellul, Mumford et Castoriadis pour doublon avec Illich ; Graeber pour doublon partiel avec Illich et Albini ; Lordon avec Debord ; Kropotkine avec Ostrom ; Simone Weil pour absence de trace — sa question est parfaitement disjointe, elle ne produit aucun résultat structuré. Ces refus portent sur la disjonction, jamais sur la valeur du penseur. Le registre complet est dans [`REGISTRE.md`](REGISTRE.md).

Sept est un plafond, pas un objectif. Au-delà, plus rien ne se route et le coût d'entretien dépasse ce qui est tenable.

## La trace, et le silence

Une voix qui intervient laisse une ligne dans le fichier :

```
// incongru-voix: illich — seuil 2.1 (6 h/sem de reprise pour 3 h évitées) — qui perd : l'astreinte
```

Le coût, et qui le porte. C'est ce champ qui distingue la critique de la décoration : une critique qui ne modifie pas l'artefact n'a produit qu'un commentaire, et un commentaire ne survit pas à la session. L'inventaire se récolte avec `grep -rn "incongru-voix:"`, sans outil.

**Pas de coût identifiable, pas de marqueur, pas de commentaire.** Le silence est un résultat — *aucune question inscrite ne change la décision ici* — et non une absence de vigilance. Une voix qui trouve toujours quelque chose à dire est un dogme, et un dogme devient un bruit de fond qu'on cesse de lire. Le seuil est mesuré : au-delà d'une tâche ordinaire sur cinq, le déclenchement est cassé. Voir [`SILENCE.md`](SILENCE.md), qui consigne aussi une mesure ratée et pourquoi elle l'était.

## Installation

Deux chemins. **Choisissez-en un seul**, et la raison n'est pas celle qu'on croit : ils ne se cumulent pas en double, ils s'éclipsent. Un lien posé dans `~/.claude/skills/` masque la voix du même nom fournie par le plugin — sans erreur, sans avertissement. Vous croyez employer l'un, vous employez l'autre.

**Comme plugin Claude Code** — le dépôt est sa propre place de marché.

```
/plugin marketplace add constructions-incongrues/voix
/plugin install constructions-incongrues-voix
```

Les voix apparaissent alors sous l'espace de noms du plugin : `incongru-voix:guy-debord`, `incongru-voix:illich`, et ainsi de suite.

**Par clone et liens symboliques** — pour tout autre agent qui charge des skills, ou si vous préférez voir ce qui est posé chez vous.

```
git clone https://github.com/constructions-incongrues/voix
cd voix && ./install.sh
```

Le script lie chaque voix dans `~/.claude/skills/`, retire ses propres liens devenus morts, et refuse d'écraser un dossier qui n'est pas un lien. Les voix sont des fichiers markdown : elles n'exigent aucun autre outillage.

Pour retrouver les commandes OpenSpec utilisées ici : `openspec init --tools claude`.

### Pourquoi vous ne le trouverez pas dans un index de plugins

Ce dépôt n'est inscrit dans aucun index tiers, et ne le sera pas par commodité.

Être installable n'est pas le problème — le manifeste est ici, vous le désignez, personne ne s'intercale. C'est ce que fait un artisan qui traite en direct. **Un index, lui, agrège, classe et recommande.** Il place la critique dans une liste où elle est comparée, notée, adoptée parce qu'elle était à côté d'autre chose. C'est là qu'opère la récupération, pas dans le fait qu'une commande l'installe.

La position est révisable. Elle devra alors l'être par une décision explicite, comme celle-ci l'a été.

## Versions

La version est dans `.claude-plugin/plugin.json`, et elle compte quelque chose :

| | |
|---|---|
| **majeure** | une voix entre au registre, ou en sort |
| **mineure** | une voix change de question, de compétence ou de trace |
| **corrective** | un déclencheur est ajusté, un test rejoué, une formulation corrigée |

`0.1.0` : quatre voix sur sept, pas de sentinelle. Le dépôt ne passera pas en `1.0` tant qu'il ne fera pas ce pour quoi il a été commencé.

## Une note sur les archives

`openspec/changes/archive/` contient le raisonnement complet, changement par changement. Ces documents citent des choses qui ne sont plus vraies : le répertoire `voix/` avant qu'il ne devienne `skills/`, et le jeton de trace `skillotheque:` avant qu'il ne devienne `incongru-voix:`.

Ils ne sont pas corrigés, et ne le seront pas. Ce sont des comptes rendus d'un état passé ; les réécrire pour qu'ils aient l'air à jour serait falsifier un dossier. Le dépôt publie son historique entier, erreurs comprises, précisément parce qu'il soutient l'inverse.

## Licence

**CC BY-SA 4.0.** Le critère vient du registre lui-même, pas d'une préférence.

Albini n'est pas contre le commerce — il a fait tourner un studio rentable pendant trente ans et payé des salaires. Il est contre la **rente** : la position qui extrait de la valeur du travail des autres sans rien fabriquer. La question n'est donc pas *quelqu'un peut-il en tirer de l'argent* mais *quelqu'un peut-il l'enclore*. Le partage à l'identique interdit l'enclosure et laisse le travail honnête tranquille.

Écartées :

- **MIT** — autorise l'extraction sans réciprocité. Un dépôt dont Albini est la conscience financière ne peut pas le publier sans se contredire.
- **AGPL-3.0** — copyleft correct, mais conçue pour du logiciel en réseau. Ici il n'y a ni service, ni liaison, ni code source à fournir : c'est de la prose.
- **Peer Production License** — la plus proche de la thèse, et refusée quand même. Sa clause non-commerciale est floue, non éprouvée en justice, et exclut par défaut les coopératives et les gens qui voudraient en vivre. Elle punit le travail honnête pour atteindre la rente.

Les fichiers tiers présents dans l'historique portent leur propre licence et ne sont pas couverts par celle-ci.

## Ce que ce dépôt va devenir

Il faut le dire ici plutôt que de le laisser arriver.

`skills/guy-debord/SKILL.md` définit la récupération comme *la manière dont le spectacle absorbe toute révolte, toute avant-garde, tout geste authentique, et la revend comme style — le destin qui attend tout ce qui réussit*. Un dépôt de critique anticapitaliste publié sur GitHub, clonable, installable, listable à côté d'un auditeur SEO, en est l'illustration littérale. Ce n'est pas un risque à mitiger : c'est ce qui est en train de se passer.

Deux choses seulement y résistent un peu. La **trace** : une voix qui ne change pas l'artefact échoue à son propre test, et le dépôt entier est bâti pour rendre cet échec visible. Et le fait de le **nommer** : une critique qui n'a pas prévu son absorption l'a déjà subie.

Il reste une contradiction que ce dépôt ne résout pas et refuse de lisser. Creative Commons est un aménagement du droit d'auteur par ses propres instruments — Debord y verrait une récupération exemplaire, et Lessig, réformiste déclaré du registre, en est le fondateur. Le dépôt est publié sous la licence de l'une de ses propres voix, celle qui répare le cadre. C'est écrit ici pour que ça se discute, pas pour que ça passe.
