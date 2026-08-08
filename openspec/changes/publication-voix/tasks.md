## 1. Audit préalable

- [x] 1.1 Inspecter l'arbre et les 8 commits d'historique : jetons, clés, chemins personnels exploitables. Consigner le résultat, y compris s'il est vide
- [x] 1.2 Vérifier que `~/.claude/skills-avant-skillotheque/` et le scratchpad ne sont pas suivis par git

## 2. Portabilité des quatre voix

- [x] 2.1 Debord — généraliser la section de sparring : viser « le conseil startup qui dit *fais quelque chose que les gens veulent* » plutôt que `office-hours` et `plan-ceo-review` nommées, en conservant les sept inversions mot pour mot
- [x] 2.2 Albini — idem sur ses cinq inversions ; conserver le passage sur la friction avec Debord, qui ne dépend d'aucun outillage
- [x] 2.3 Illich — idem ; sa section cite `office-hours`, `plan-ceo-review` et `plan-eng-review`
- [x] 2.4 Lessig — idem ; sa section cite en plus `cso`
- [x] 2.5 Étendre les quatre `description` avec des formulations génériques (« le conseil startup », « une revue de plan produit »), **sans retirer aucune amorce existante** — vérifier par diff qu'aucune ligne n'a disparu
- [x] 2.6 Vérifier qu'il ne reste aucune référence à un outil tiers formulée comme une dépendance : `grep -c 'office-hours\|plan-ceo-review\|plan-eng-review\|gstack\|cso' voix/*/SKILL.md` ne doit plus retourner que des occurrences en position d'exemple

## 3. Licence et README

- [x] 3.1 Ajouter `LICENSE` — CC BY-SA 4.0, texte complet
- [x] 3.2 Écrire la note motivant le choix : le critère est l'enclosure et non le commerce, avec MIT, AGPL-3.0 et la Peer Production License écartées et leurs motifs
- [x] 3.3 Écrire `README.md` — ce que le dépôt conteste, le tableau des voix et de leurs questions, la règle d'admission, la trace, l'installation en deux lignes
- [x] 3.4 Écrire la section « ce que ce dépôt va devenir » : sa propre récupération, nommée, et le désaccord Debord/Lessig sur Creative Commons exposé plutôt que lissé

## 4. Non-régression — point d'arrêt

- [x] 4.1 Rejouer le test de disjonction sur les quatre voix réécrites ; dater la nouvelle exécution dans `DISJONCTION.md`
- [x] 4.2 Rejouer le test de silence : les quatre cas expositifs et au moins trois tâches ordinaires, par `claude -p --output-format stream-json` et lecture du premier appel `Skill` — pas par le harnais `skill-creator`
- [x] 4.3 Rejouer les contrôles positifs des quatre voix : chacune doit encore déclencher sur un cas réel de son domaine
- [x] 4.4 Dater les résultats dans `SILENCE.md`. **Une régression bloque la publication** : corriger et rejouer avant d'aller plus loin

## 5. Specs

- [ ] 5.1 Synchroniser les deltas dans `openspec/specs/` : `portabilite-voix`, `publication-depot`, et l'exigence ajoutée à `format-voix`

## 6. Publication — accord explicite requis

- [ ] 6.1 Demander l'accord de publication, en rappelant qu'une fois en ligne le contenu est indexable même s'il est retiré ensuite, et trancher la visibilité initiale (public d'emblée ou privé le temps d'une relecture)
- [ ] 6.2 `gh repo create constructions-incongrues/voix` avec la visibilité retenue et une description d'une ligne
- [ ] 6.3 Ajouter le remote et pousser l'historique complet, sans réécriture
- [ ] 6.4 Vérifier le rendu public : README lisible, licence détectée par GitHub, `openspec/` et les tests bien présents
