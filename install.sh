#!/bin/sh
# Lie chaque voix du dépôt dans ~/.claude/skills/. Réexécutable sans dommage.
# ponytail: liens et non copies — une édition dans voix/ est active immédiatement,
#           donc rien à synchroniser, donc pas de dérive possible.
set -e
cd "$(dirname "$0")/voix"

for v in */; do
	n=${v%/}
	d="$HOME/.claude/skills/$n"
	# Un vrai dossier à cet emplacement est peut-être l'original non encore copié :
	# on ne l'écrase jamais, on le signale.
	if [ -e "$d" ] && [ ! -L "$d" ]; then
		echo "refus  $n — $d est un vrai dossier, pas un lien. Déplacez-le d'abord." >&2
		continue
	fi
	ln -sfn "$PWD/$n" "$d"
	echo "lié    $n"
done
