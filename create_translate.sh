
# Before file tree structure example:
# translate/
# ├── ru
# │   └── LC_MESSAGES
# │       └── strings.po
# ├── en
# │   └── LC_MESSAGES
# │       └── strings.po
# ...

# After file tree structure example:
# translate/
# ├── ru
# │   └── LC_MESSAGES
# │       └── strings.po
# │       └── strings.mo
# ├── en
# │   └── LC_MESSAGES
# │       └── strings.po
# │       └── strings.mo
# ...
# ├── __init__.py
# ├── ru.bin
# ├── en.bin
# ...

# convert GNU gettext files: .po to .mo
find -name "*.po" -exec bash -c 'msgfmt "$0" -o "${0%.*}.mo"' {} \;

python ./create_translate.py
