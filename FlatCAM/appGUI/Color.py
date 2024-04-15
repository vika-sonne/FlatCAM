# ###########################################################
# FlatCAM: 2D Post-processing for Manufacturing             #
# http://flatcam.org                                        #
# Author: vika-sonne (c)                            #
# Date: 6/5/2023                                            #
# MIT Licence                                               #
# ###########################################################

from random import uniform
# FlatCAM imports
from settings import is_theme_black


def get_rand_fg_color(app: object | None = None) -> str | tuple[float, float, float, float]:
	'Return RGBA'

	def get_color() -> tuple[float, float, float, float]:
		if is_theme_black():
			return (uniform(.5, 1), uniform(.5, 1), uniform(.5, 1), 1)
		else:
			return (uniform(0, .5), uniform(0, .5), uniform(0, .5), 1)

	c = get_color()
	if app and app.is_legacy is False:
		return c
	return f'#{int(c[0]*255):02x}{int(c[1]*255):02x}{int(c[2]*255):02x}{int(c[3]*255):02x}'

def get_fg_blue() -> str:
	return '#7777FF' if is_theme_black else '#0000FF'
