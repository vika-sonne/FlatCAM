#!/usr/bin/env sh

# zip -vr FlatCAM.zip *.py LICENSE appCommon/*/*.py appEditors/*/*.py appGUI/*/*.py appObjects/*/*.py appParsers/*/*.py appTools/*/*.py descartes/*/*.py locale/*/*.py preprocessors/*/*.py tclCommands/*/*.py

ZIPAPP_FILEPATH="publish/FlatCAM.zip"
FLATCAM_PATH="FlatCAM"

cd ..

if [ -f $ZIPAPP_FILEPATH ]; then
	rm -rfv "$ZIPAPP_FILEPATH"
fi

zip "$ZIPAPP_FILEPATH" -v __main__.py `find "$FLATCAM_PATH" -name "*.py" -print` `find "$FLATCAM_PATH/translate" -name "*.bin" -print`
