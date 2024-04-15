
from os.path import join
from zipimport import zipimporter
from sys import path
if type(__loader__) is zipimporter:
	path.insert(0, join(__loader__.archive, 'FlatCAM'))
else:
	path.insert(0, './FlatCAM')
from FlatCAM import main

main()
