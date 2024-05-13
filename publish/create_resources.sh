#!/usr/bin/env sh

FLATCAM_PATH="FlatCAM"

pyrcc5 "$FLATCAM_PATH/resources.qrc" -o "$FLATCAM_PATH/resources.py"
pyrcc5 "$FLATCAM_PATH/resources_dark.qrc" -o "$FLATCAM_PATH/resources_dark.py"
