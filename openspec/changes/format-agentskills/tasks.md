## 1. Outil de mesure

- [ ] 1.1 Installer `skills-ref` (npm, v0.1.5) et l'exécuter sur les quatre voix — établir la mesure de départ, verdict par voix, avant toute modification
- [ ] 1.2 Vérifier que l'outil signale bien le dépassement de `description` : s'il ne le détecte pas, ce n'est pas le bon critère et il faut le dire avant de s'appuyer dessus

## 2. Modifier la règle avant de la transgresser

- [ ] 2.1 Appliquer le delta `portabilite-voix` dans `openspec/specs/` : « additive uniquement » devient « additive par défaut, suppression permise si mesurée ». **À faire avant toute coupe** — sinon les tâches du groupe 3 violent une exigence en vigueur
- [ ] 2.2 Appliquer le delta `format-voix` : le budget de description et son ordre de priorité

## 3. Coupe des descriptions, du plus facile au plus dur

- [ ] 3.1 **Illich** (1702 → ≤1024, −678) : couper les exemples gstack, réduire les amorces à trois ou quatre, resserrer l'énumération de l'exclusion. Clause de situation intacte
- [ ] 3.2 **Lessig** (1828 → ≤1024, −804) : idem, plus la suppression des exclusions d'axes coupés (licence open source, financement politique) — le corps du fichier les porte déjà
- [ ] 3.3 **Debord** (2215 → ≤1024, −1191) : idem. Sa liste d'amorces est la plus longue du dépôt et la plus redondante
- [ ] 3.4 **Albini** (2411 → ≤1024, −1387) : le cas le plus dur. **Si deux tentatives ne passent pas sans casser le déclenchement, arrêter et rapporter** plutôt que dégrader en silence — l'arbitrage conformité contre déclenchement appartient à l'auteur
- [ ] 3.5 Vérifier après chaque coupe que la clause de situation et le fond de la clause d'exclusion sont toujours présents

## 4. Licence embarquée

- [ ] 4.1 Ajouter `license: CC-BY-SA-4.0` au frontmatter des quatre voix
- [ ] 4.2 Vérifier que le champ n'entre pas dans le décompte de la `description`

## 5. Conformité — établie par l'outil, pas par moi

- [ ] 5.1 `skills-ref validate` sur les quatre : les quatre doivent passer
- [ ] 5.2 Consigner le verdict avant / après, pour que l'écart soit lisible sans relancer l'outil

## 6. Non-régression — point d'arrêt

- [ ] 6.1 Volet routage : une requête de situation par voix, sans la nommer. Les quatre doivent gagner la leur
- [ ] 6.2 Volet silence : quatre cas expositifs, trois tâches ordinaires. Sept silences attendus
- [ ] 6.3 Méthode `claude -p --output-format stream-json`, lecture du premier appel `Skill`. **Pas** le harnais `skill-creator`, pour la raison inscrite dans `admission-voix`
- [ ] 6.4 Dater les résultats dans `DISJONCTION.md` et `SILENCE.md`. **Une régression bloque** : corriger et rejouer avant d'aller plus loin

## 7. Specs, README, publication

- [ ] 7.1 Synchroniser `conformite-agentskills` dans `openspec/specs/`
- [ ] 7.2 README : remplacer l'affirmation de portabilité par une affirmation vérifiable, avec la commande de validation
- [ ] 7.3 Version : la trace ne change pas, les déclencheurs si — corrective ou mineure selon ce que la règle du dépôt en dit, et le trancher explicitement
- [ ] 7.4 Pousser
