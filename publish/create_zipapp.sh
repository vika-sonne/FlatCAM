#!/usr/bin/env sh

# zip -vr FlatCAM.zip *.py LICENSE appCommon/*/*.py appEditors/*/*.py appGUI/*/*.py appObjects/*/*.py appParsers/*/*.py appTools/*/*.py descartes/*/*.py locale/*/*.py preprocessors/*/*.py tclCommands/*/*.py

VERSION="2024_4"
BUILD_PATH="_build"
ZIPAPP_FILEPATH="$BUILD_PATH/FlatCAM_$VERSION.zip"
FLATCAM_PATH="FlatCAM"

mkdir "$BUILD_PATH"

if [ -f $ZIPAPP_FILEPATH ]; then
	rm -rfv "$ZIPAPP_FILEPATH"
fi

zip "$ZIPAPP_FILEPATH" -v __main__.py `find "$FLATCAM_PATH" -name "*.py" -print` `find "$FLATCAM_PATH/translate" -name "*.bin" -print`
