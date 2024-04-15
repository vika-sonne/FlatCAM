# Converts GNU gettext .po files to .py package.
# Author: Victoria Danchenko
# Date: 31/03/2024
# 
# Before file tree structure example:
# locale/
# ├── ru
# │   └── LC_MESSAGES
# │       └── strings.mo
# ├── en
# │   └── LC_MESSAGES
# │       └── strings.mo
# ├── de
# │   └── LC_MESSAGES
# │       └── strings.mo
# ...
# 
# After file tree structure example:
# locale/
# ├── ru.bin
# ├── en.bin
# ├── de.bin
# ...

from pathlib import Path
from gettext import GNUTranslations
from pickle import dump


locale_path = Path('translate')

# create package
locale_path.joinpath('__init__.py').open('w')

# create .bin file for each locale
for p in (x for x in locale_path.iterdir() if x.is_dir()):
	# iter locale codes: ru, en, de, e.t.c.
	print(f'{p.name}')
	for pp in (x for x in p.iterdir() if x.is_dir()):
		with pp.joinpath('strings.mo').open('rb') as fp:
			t = GNUTranslations(fp)
			with locale_path.joinpath(f'{p.name}.bin').open('wb') as fpy:
				dump(t._catalog, fpy)
