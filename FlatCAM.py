import sys
import os
import signal
from multiprocessing import freeze_support
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtWidgets import QApplication
from appLogger import getLogger
# FlatCAM imports
from app_Main import App
from appGUI import VisPyPatches
from settings import hdpi, style


if sys.platform == "win32":
	# cx_freeze 'module win32' workaround
	pass

MIN_VERSION_MAJOR, MIN_VERSION_MINOR = 3, 10


def debug_trace():
	'''Set a tracepoint in the Python debugger that works with Qt'''

	from PyQt5.QtCore import pyqtRemoveInputHook
	# from pdb import set_trace
	pyqtRemoveInputHook()
	# set_trace()

def setup_keyboard_interrupt_handling():
	'''Setup handling of KeyboardInterrupt (Ctrl-C) for PyQt.'''

	def _interrupt_handler(signum, frame):
		print('Wait for quit')
		QApplication.quit()

	signal.signal(signal.SIGINT, _interrupt_handler)

def main():
	from sys import argv
	match argv:
		case [_, '-h' | '-H']:
			print('HELP')
			os._exit(0)
	App.version

	# All X11 calling should be thread safe otherwise we have strange issues
	# QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_X11InitThreads)
	# NOTE: Never talk to the GUI from threads! This is why I commented the above.
	freeze_support()

	setup_keyboard_interrupt_handling()

	if sys.version_info.major < MIN_VERSION_MAJOR and sys.version_info.minor < MIN_VERSION_MINOR:
		print(f'FlatCAM BETA uses Python {MIN_VERSION_MAJOR}.{MIN_VERSION_MINOR} or later.\n'
				'Your Python version is {sys.version_info.major}.{sys.version_info.minor}.')
		os._exit(-1)

	log = getLogger()

	debug_trace()
	VisPyPatches.apply_patches()

	# apply High DPI support
	if(hdpi_support := hdpi()):
		if hdpi_support == 2:
			log.debug('EnableHighDpiScaling=True')
			os.environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"
			QApplication.setAttribute(Qt.AA_EnableHighDpiScaling, True)
		else:
			log.debug('EnableHighDpiScaling=False')
			os.environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "0"
			QApplication.setAttribute(Qt.AA_EnableHighDpiScaling, False)

	app = QApplication(sys.argv)

	# apply Qt style if defined
	if(s := style()):
		app.setStyle(s)

	fc = App(qapp=app)
	sys.exit(app.exec_())

if __name__ == '__main__':
	main()
