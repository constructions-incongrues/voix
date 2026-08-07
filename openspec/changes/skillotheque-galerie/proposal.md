## Why

Le corpus de skills installé sur cette machine porte un cadre par défaut qu'aucune skill ne conteste : le vocabulaire de la croissance, de la roadmap, des parties prenantes, de la dette technique. `office-hours`, `plan-ceo-review`, `kit-product:roadmap-management` l'assument ; `engineering:tech-debt` et `stakeholder-update` le transportent dans leurs mots ; la posture serviable du modèle lui-même le rend invisible.

Deux contre-voix existent déjà (`guy-debord`, `steve-albini`) et fonctionnent, mais elles ne se déclenchent que sur invitation — une critique qu'il faut demander est une critique de loisir. L'objectif à terme est une **sentinelle** qui convoque la bonne voix sur du travail ordinaire, sans invitation. Elle n'a rien à convoquer tant que la galerie n'existe pas. Ce changement construit la galerie, et la construit *pour être convoquée*.

## What Changes

- **Un format commun de voix** en quatre champs — `question` (unique dans le dépôt), `signaux` (à quoi on reconnaît qu'elle est porteuse), `compétence` (ce qu'elle sait faire, pas ce qu'elle pense), `trace` (ce qu'elle laisse dans l'artefact). Sans ces champs, une voix n'est pas routable.
- **Une règle d'admission** : une voix entre si et seulement si elle apporte une question disjointe de toutes les autres *et* une compétence produisant une trace vérifiable. Une opinion de plus sur une question déjà posée est refusée. C'est ce qui empêche le dépôt de devenir une friperie de costumes.
- **Un mécanisme de trace** : chaque voix laisse dans le fichier de travail un marqueur nommant le coût et son porteur — l'analogue du commentaire `ponytail:` et de sa récolte par `/ponytail-debt`. Une critique qui ne laisse rien dans l'artefact est de la décoration.
- **Lot 1 : deux nouvelles voix** — Illich (le seuil de contre-productivité, la convivialité) et Lessig (code is law : la contrainte est-elle dans la loi, la norme, le prix ou l'architecture, et qui peut faire appel). Choisies parce qu'elles traitent l'outil par les deux bouts opposés — son usager, ses tiers — et éprouvent donc le format sur le cas le plus serré.
- **Rétrofit de Debord et Albini** au format commun. Leurs sections « sparring » (`guy-debord/SKILL.md:47-66`, `steve-albini/SKILL.md:49-64`) sont déjà de la procédure déguisée en voix : elles deviennent les champs `compétence` et `signaux`.
- **Le registre des voix** : la liste arrêtée et son état — Debord, Albini, Illich, Federici, Ostrom, Polanyi, Lessig. Sept est un plafond, pas un objectif.

## Capabilities

### New Capabilities

- `format-voix` : le contrat que tout fichier de voix doit satisfaire — les quatre champs, la posture non-serviable (une voix livre du travail réel sans le registre du service), le traitement explicite de la biographie de la personne, et la sortie de persona sur demande.
- `admission-voix` : la règle qui décide qu'une voix candidate entre ou est refusée — disjonction de la question, existence d'une compétence, existence d'une trace. Inclut le registre des sept et les refus motivés (Gorz, Ellul, Castoriadis sur doublon avec Illich ; Weil sur absence de trace ; Graeber sur doublon partiel Illich + Albini).
- `trace-artefact` : le marqueur laissé par une voix dans un fichier de travail, son format, et sa récolte en inventaire.

### Modified Capabilities

Aucune. `openspec/specs/` est vide ; Debord et Albini vivent hors OpenSpec et sont traités comme du rétrofit, pas comme un changement de spec.

## Impact

- **Nouveau contenu du dépôt** : les fichiers de voix, le registre, la règle d'admission. Aucun code applicatif.
- **Skills existantes touchées** : `~/.claude/skills/guy-debord/SKILL.md` et `~/.claude/skills/steve-albini/SKILL.md` — rétrofit. Elles vivent hors du dépôt : la question de savoir si le dépôt devient leur source (avec installation) ou reste une bibliothèque parallèle relève du design.
- **Outillage réutilisé** : `guy-debord-workspace/optimizer/` (evals de déclenchement, 4 itérations d'amélioration) est le modèle pour valider chaque voix.

## Hors périmètre

- **La sentinelle** (détection + convocation automatique). Elle dépend du format défini ici et fait l'objet d'un changement ultérieur. La cible « me contredire sur mes propres projets sans que je l'aie demandé » n'est donc **pas** servie par ce changement.
- **Lot 2** : Federici, Ostrom, Polanyi. Écrites après que le lot 1 ait prouvé le format.
- **La distribution.** Plugin publié ou skills locales : non tranché, et ce n'est pas un détail d'emballage. Publier ce dépôt sur une place de marché de plugins est précisément la récupération que Debord décrit — la critique revendue comme style installable. La décision est délibérément différée.
