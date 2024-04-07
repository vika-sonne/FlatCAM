#!/usr/bin/env sh

# zip -vr FlatCAM.zip *.py LICENSE appCommon/*/*.py appEditors/*/*.py appGUI/*/*.py appObjects/*/*.py appParsers/*/*.py appTools/*/*.py descartes/*/*.py locale/*/*.py preprocessors/*/*.py tclCommands/*/*.py

zip FlatCAM.zip -v `find -name "*.py" -print` `find "translate" -name "*.bin" -print`
