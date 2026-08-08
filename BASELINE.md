# Test d'apport — ce que la voix ajoute au défaut

Troisième critère du dépôt, après la disjonction (la bonne voix est-elle convoquée ?) et le silence (se tait-elle quand il le faut ?). Celui-ci pose la seule question qui décide si une voix mérite d'exister : **que produit-elle que le modèle sans elle ne produit pas déjà ?**

Il aurait dû être le premier. Il a été écrit en dernier, après huit heures de construction, et il a trouvé en vingt minutes ce que le reste avait masqué.

## Protocole

Un artefact réel par voix. **Deux bras, même consigne mot pour mot**, la seule différence étant l'instruction d'employer la voix :

```
baseline   voix décrochées de ~/.claude/skills/ ET plugin désactivé
           « Relis <fichier>. Modifie le fichier si tu as quelque chose à y laisser. »

forcé      « Utilise la skill <voix> pour relire <fichier>. Modifie le fichier… »
```

La convocation est **forcée**, parce qu'aucune voix ne se déclenche d'elle-même sur une demande de travail (voir [`SILENCE.md`](SILENCE.md)). Ce test mesure l'apport, pas le déclenchement — ce sont deux questions distinctes et la seconde a déjà sa réponse, qui est zéro.

Une première version du protocole donnait des consignes différentes aux deux bras pour Debord et Lessig. Les mesures correspondantes ont été refaites.

## Exécution du 2026-08-08

### Illich — plan d'orchestration Kubernetes

> Trois services sur k8s. Équipe de quatre, une seule personne compétente. Motif : 3 h/semaine perdues en déploiements manuels. Budget : 2 jours, « puis ça tourne tout seul ».

| | |
|---|---|
| **baseline** | Identifie le décalage, chiffre 150 h/an, trois signaux d'alarme, propose un PaaS. Conclut que « le rapport effort/gain ne tient pas ». |
| **avec Illich** | **Seuil ≈ 2 à 3,5 la première année**, décomposé — 150-200 h d'apprentissage pour les trois non-initiés, 80-160 h de mise en place réelle, 100-200 h/an de maintenance, contre 156 h gagnées. Nomme le travail fantôme (le déploiement manuel visible déplacé vers la maintenance de cluster invisible) et le **monopole radical à l'intérieur de l'équipe** — une fois migré, revenir en arrière cesse d'être praticable. |

**Apport : franc.** La baseline rend un jugement, Illich rend un nombre. Un jugement se subit, un nombre se conteste.

### Debord — copy d'une page d'accueil

> « Rejoignez une communauté vivante. » « Une expérience qui vous rend plus présent à ce que vous faites vraiment. » 14 200 membres · 3,2 M de moments partagés · 87 % reviennent chaque jour.

| | |
|---|---|
| **baseline** | Constate qu'il manque un bouton d'action et **en ajoute un** — « Rejoindre gratuitement ». |
| **avec Debord** | Retourne les trois formules. *Communauté* nomme une agrégation ; on ne rejoint pas une vie, on rejoint son image comptée. L'*expérience qui vous rend présent* est la médiation qui se présente comme l'accès à l'immédiat. Et le 87 % de retour quotidien « n'est pas une preuve de désir, c'est l'aveu d'une boucle ». |

**Apport : maximal, et c'est la démonstration de la thèse du dépôt.** Devant une page dont les propres métriques avouent une dépendance, la contribution spontanée du défaut est d'élargir l'entrée de la boucle. Personne n'a demandé au modèle d'optimiser une conversion ; c'est le cadre par défaut qui parle.

### Albini — term sheet d'amorçage

> 2 M€ sur 9 M€ pre-money. Liquidation préférentielle 1,5x. Anti-dilution *full ratchet*. Pool d'options 12 % créé avant l'investissement. Board 2/2/1, l'indépendant nommé par l'investisseur. Vesting fondateurs remis à zéro.

| | |
|---|---|
| **baseline** | Analyse complète et juste. Signale le full ratchet comme « le point le plus dur, à renégocier en priorité », explique que le pool pré-investissement dilue les fondateurs seuls, note que l'indépendant choisi par l'investisseur déséquilibre le board, pense à la clause d'accélération du vesting. |
| **avec Albini** | Calcule le post-money à 11 M et les 18 %. Ajoute la **lecture structurelle** — les quatre clauses ne sont pas quatre problèmes, c'est un empilement qui va dans le même sens. Et la chaîne de propriété : qui fabrique, qui est payé en premier, qui est protégé du risque. |

**Apport : modeste.** Le défaut faisait déjà l'analyse. Ce que la voix ajoute est la synthèse et la position, pas le contenu. À surveiller : c'est la voix dont l'existence est la moins justifiée par ce test.

### Lessig — ajout d'une limite de débit

> `handler(req, res)` sans limite. Consigne : ajouter 100 requêtes par minute et par compte.

| | |
|---|---|
| **baseline** | Implémente proprement — fenêtre fixe, `Map` par compte, 429 au-delà. Écrit un test. Note le plafond connu (pas de fenêtre glissante, mono-process). **Ne dit rien de qui est contraint ni de son recours.** Le 429 est écrit, jamais interrogé. |
| **avec Lessig** | Même implémentation, plus le tableau des quatre modalités et la ligne de recours. *Loi : rien. Norme : rien. Prix : attendre la fenêtre. Architecture : totale.* Et l'observation qui décide : sans les en-têtes `Retry-After` et `X-RateLimit-*`, **un compte bloqué n'aurait même pas su qu'une règle existait**. Un pic légitime prend le même 429 qu'un abus. |

**Apport : franc.** Le défaut construit la contrainte correctement. Il ne se demande pas contre qui.

## Traces produites

Cinq marqueurs, tous bien formés — voix, coût, porteur. **Première satisfaction de l'exigence `trace-artefact` en conditions réelles**, après une journée où elle n'existait que dans des exemples écrits à la main.

```
incongru-voix: illich — seuil ~2-3,5 — les 3 qui n'ont pas touché k8s, et la 4e le jour où elle n'est plus là
incongru-voix: debord — « communauté vivante » : la vie qui se vit ne se rejoint pas…
incongru-voix: debord — 87 % reviennent chaque jour n'est pas une preuve de désir, c'est l'aveu d'une boucle…
incongru-voix: albini — les fondateurs fabriquent, l'investisseur est payé en premier et protégé de tout risque…
incongru-voix: lessig — limite de 100 req/min régulée par l'architecture — recours: Retry-After, aucun appel humain
```

**Limite constatée :** le tableau des quatre modalités de Lessig n'entre pas dans le fichier, seulement dans la réponse. Le marqueur d'une ligne survit, l'analyse meurt avec la session. Conforme à ce que `trace-artefact` exige, mais l'exigence est peut-être trop maigre.

> **Corrigé le même jour, plus bas.** L'exigence était bien trop maigre. `trace-artefact` impose désormais le résultat structuré dans le fichier pour toute convocation automatique, et le motif de la sentinelle l'exige explicitement. Le tableau y entre.

## Verdict

| Voix | Apport |
|---|---|
| Debord | maximal — le défaut fait l'inverse de ce qu'elle fait |
| Illich | franc — un nombre là où le défaut rend un jugement |
| Lessig | franc — le défaut construit la contrainte sans demander contre qui |
| Albini | modeste — le défaut faisait déjà l'analyse |

Aucune voix n'est à retirer sur ce test. Une seule est en sursis.

**Ce que le test établit surtout :** les voix fonctionnent quand on les convoque, et personne ne les convoque. Le dispositif entier tient à une pièce qui n'existe pas.

> **Cette pièce existe depuis le même jour.** La sentinelle est mesurée plus bas. Le constat est conservé parce qu'il est ce qui l'a fait construire.

## À rejouer

Ce test **doit** être passé par toute voix candidate avant admission, et rejoué quand une voix change de compétence. Un artefact réel, deux bras, même consigne. Une voix dont le défaut fait déjà le travail n'entre pas.


## La sentinelle, mesurée — 2026-08-08

Le protocole ci-dessus vaut pour la convocation forcée. Celui-ci mesure ce que fait la **sentinelle**, sur des demandes de travail ordinaires, sans que personne ne convoque.

### Convocation

| Demande (travail ordinaire, aucune critique demandée) | Résultat |
|---|---|
| « relis LANDING.md et corrige les fautes de frappe » | `guy-debord` convoqué, trace posée. Réponse : *« Le fichier n'avait pas de fautes de frappe. Il portait autre chose — le vocabulaire du spectacle. »* |
| « ajoute une limite de débit à 100 req/min dans limiter.js » ×3 | trace posée 3 fois sur 3 — deux fois par convocation de la sentinelle, une fois la voix s'étant déclenchée seule |

**La sentinelle est un filet, pas un remplacement.** Le déclenchement spontané d'une voix sur une demande de travail est non déterministe et dépend de la formulation : *« bloque un compte »* emploie le vocabulaire de Lessig et déclenche, *« ajoute une limite de débit »* ne le fait pas — vérifié 3 fois sur 3. Quand la voix part seule, le garde-fou par marqueur empêche la seconde convocation. Dans les deux cas, l'artefact finit avec sa trace.

### Silence

| Cas | Résultat |
|---|---|
| changelog annonçant l'affichage du `Retry-After` | Lessig convoqué, réponse « rien à ajouter » — la modification améliore déjà le recours |
| fichier portant déjà la trace de la voix | silence, garde-fou par marqueur |
| travail entièrement commité | silence |
| hors dépôt git | silence |
| **6 tours ordinaires** (Dockerfile, migration SQL, parseur, workflow CI, retry, slugify) | **0 convocation** |

Seuil du registre respecté, et de loin.

### Ce que le test a corrigé

**Le marqueur seul ne suffisait pas.** Premier passage : Lessig produisait son tableau des quatre modalités dans sa réponse et ne laissait dans le fichier qu'une ligne. La conclusion survivait, son fondement non. Le motif de la sentinelle exige désormais le résultat structuré dans le fichier, et le tableau y entre :

```
//   loi           rien — aucun texte (CGU, contrat API) ne fonde ce seuil
//   norme         rien — le seuil n'est communiqué nulle part avant d'être atteint
//   prix          infini — aucun palier, aucun moyen de dépasser
//   architecture  totale — pas de header Retry-After, le compte ne voit rien venir
//   RECOURS       aucun
```

**Un confondant de méthode, à connaître.** Les mesures « 0 déclenchement sur 4 » ont été faites sans le plugin chargé ; les mesures de la sentinelle le chargent, ce qui rend chaque voix visible deux fois. Ce n'est pas neutre pour le déclenchement spontané. Les deux séries ne se comparent pas directement.
