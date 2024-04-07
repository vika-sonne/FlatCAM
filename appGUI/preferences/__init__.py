import builtins
from PyQt5.QtCore import QSettings
import appTranslation as fcTranslate
from appGUI.GUIElements import *


if '_' not in builtins.__dict__:
	_ = fcTranslate.apply_language()

settings = QSettings("Open Source", "FlatCAM")
if settings.contains("machinist"):
	machinist_setting = settings.value('machinist', type=int)
else:
	machinist_setting = 0
