#!/usr/bin/env bash
# Erstellt die Abgabe-ZIP für die Sprecherin der Gruppe 308.
# Ausgabe: KI1_308_Code.zip (im Stammverzeichnis des Projekts)
#
# Verwendung:
#   cd /pfad/zu/ki-308
#   bash portfolio/create_submission_zip.sh

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
ZIP_NAME="KI1_308_Code.zip"

echo "Erstelle $ZIP_NAME ..."

cd "$REPO_ROOT"

# Sicherstellen, dass Notebook-Outputs bereinigt sind
if command -v nbstripout &>/dev/null; then
    echo "Bereinige Notebook-Outputs (nbstripout) ..."
    find notebooks -name "*.ipynb" -exec nbstripout {} \;
    nbstripout data.ipynb
else
    echo "WARNUNG: nbstripout nicht gefunden. Outputs werden nicht bereinigt."
    echo "  Installieren: pip install nbstripout"
fi

# ZIP erstellen (ohne .git, .venv, __pycache__, results)
zip -r "$ZIP_NAME" \
    data.ipynb \
    requirements.txt \
    README.md \
    utils/ \
    notebooks/ \
    portfolio/Logbuch_Template.md \
    -x "**/__pycache__/*" \
    -x "**/.ipynb_checkpoints/*" \
    -x "**/.*"

echo ""
echo "Fertig: $ZIP_NAME ($(du -sh "$ZIP_NAME" | cut -f1))"
echo "Abgabe-Dateiname: KI1_308_Code.zip"
echo "Hochladen auf: Stud.IP → Abgabeordner"
