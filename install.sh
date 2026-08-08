#!/bin/sh
# Lie chaque voix du dépôt dans ~/.claude/skills/. Réexécutable sans dommage.
# ponytail: liens et non copies — une édition dans skills/ est active immédiatement,
#           donc rien à synchroniser, donc pas de dérive possible.
set -e

REPO=$(cd "$(dirname "$0")" && pwd)
DEST="$HOME/.claude/skills"
mkdir -p "$DEST"

# Un lien mort ne produit aucune erreur : la voix cesse simplement d'exister,
# et la panne est indiagnosticable. On retire donc les nôtres devenus morts —
# les nôtres seulement : un lien mort vers ailleurs ne nous regarde pas.
for l in "$DEST"/*; do
	[ -L "$l" ] && [ ! -e "$l" ] || continue
	case "$(readlink "$l")" in
	"$REPO"/*) rm "$l" && echo "retiré $(basename "$l") — lien mort vers ce dépôt" ;;
	esac
done

cd "$REPO/skills"
for v in */; do
	n=${v%/}
	d="$DEST/$n"
	# Un vrai dossier à cet emplacement est peut-être un original non sauvegardé :
	# on ne l'écrase jamais, on le signale.
	if [ -e "$d" ] && [ ! -L "$d" ]; then
		echo "refus  $n — $d est un vrai dossier, pas un lien. Déplacez-le d'abord." >&2
		continue
	fi
	ln -sfn "$PWD/$n" "$d"
	echo "lié    $n"
done
