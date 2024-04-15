# ###########################################################
# FlatCAM: 2D Post-processing for Manufacturing             #
# http://flatcam.org                                        #
# Author: vika-sonne (c)                                    #
# Date: 6/5/2023                                            #
# MIT Licence                                               #
# ###########################################################

from PyQt5.QtCore import QSettings


THEME_BLACK = 'black'
THEME_WHITE = 'white'
DEFAULT_THEME = THEME_BLACK

DEFAULT_AXIS_FONT_SIZE = 8


settings = QSettings("Open Source", "FlatCAM")

def save():
	settings.sync()

def theme() -> str:
	return settings.value('theme', defaultValue=DEFAULT_THEME, type=str)

def set_theme(value: str) -> bool:
	if theme() == value:
		return False
	settings.setValue('theme', value)
	save()
	return True

def is_theme_black() -> bool:
	return theme() == THEME_BLACK

def is_theme_white() -> bool:
	return not is_theme_black()

def style() -> str | None:
	return settings.value('style', type=str)

def hdpi() -> int:
	return settings.value('hdpi', defaultValue=0, type=int)

def axis_font_size() -> int:
	return settings.value('axis_font_size', defaultValue=DEFAULT_AXIS_FONT_SIZE, type=int)

def set_axis_font_size(value: int = DEFAULT_AXIS_FONT_SIZE) -> int:
	return settings.setValue('axis_font_size', value)
