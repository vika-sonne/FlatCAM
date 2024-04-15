# ##########################################################
# FlatCAM: 2D Post-processing for Manufacturing            #
# http://flatcam.org                                       #
# File Author: Matthieu Berthomé                           #
# Date: 5/26/2017                                          #
# MIT Licence                                              #
# ##########################################################

from abc import ABCMeta, abstractmethod

# module-root dictionary of preprocessors

from appLogger import getLogger


SEARCH_PATH = 'preprocessors'

log = getLogger('base')
preprocessors: dict[str, object] = {}  # preprocessor classes


class ABCPreProcRegister(ABCMeta):
	# handles preprocessors registration on instantiation
	def __new__(cls, clsname, bases, attrs):
		newclass = super(ABCPreProcRegister, cls).__new__(cls, clsname, bases, attrs)
		if object not in bases:
			if newclass.__name__ in preprocessors:
				log.warning(f'Preprocessor has been overriden: {newclass.__name__}')
			else:
				log.info(f'Add preprocessor: {newclass.__name__}')
			preprocessors[newclass.__name__] = newclass()  # here is your register function
		return newclass


class PreProc(object, metaclass=ABCPreProcRegister):
	@abstractmethod
	def start_code(self, p):
		pass

	@abstractmethod
	def lift_code(self, p):
		pass

	@abstractmethod
	def down_code(self, p):
		pass

	@abstractmethod
	def toolchange_code(self, p):
		pass

	@abstractmethod
	def up_to_zero_code(self, p):
		pass

	@abstractmethod
	def rapid_code(self, p):
		pass

	@abstractmethod
	def linear_code(self, p):
		pass

	@abstractmethod
	def end_code(self, p):
		pass

	@abstractmethod
	def feedrate_code(self, p):
		pass

	@abstractmethod
	def spindle_code(self, p):
		pass

	@abstractmethod
	def spindle_stop_code(self, p):
		pass


class AppPreProcTools(object, metaclass=ABCPreProcRegister):
	@abstractmethod
	def start_code(self, p):
		pass

	@abstractmethod
	def lift_code(self, p):
		pass

	@abstractmethod
	def down_z_start_code(self, p):
		pass

	@abstractmethod
	def lift_z_dispense_code(self, p):
		pass

	@abstractmethod
	def down_z_stop_code(self, p):
		pass

	@abstractmethod
	def toolchange_code(self, p):
		pass

	@abstractmethod
	def rapid_code(self, p):
		pass

	@abstractmethod
	def linear_code(self, p):
		pass

	@abstractmethod
	def end_code(self, p):
		pass

	@abstractmethod
	def feedrate_xy_code(self, p):
		pass

	@abstractmethod
	def z_feedrate_code(self, p):
		pass

	@abstractmethod
	def feedrate_z_dispense_code(self, p):
		pass

	@abstractmethod
	def spindle_fwd_code(self, p):
		pass

	@abstractmethod
	def spindle_rev_code(self, p):
		pass

	@abstractmethod
	def spindle_off_code(self, p):
		pass

	@abstractmethod
	def dwell_fwd_code(self, p):
		pass

	@abstractmethod
	def dwell_rev_code(self, p):
		pass


def load_preprocessors():
	# searches in subfolder and loads modules with classes inherited with ABCPreProcRegister
	from sys import modules
	from importlib import resources
	from importlib.util import find_spec
	from pathlib import Path

	for p in (Path(x.name) for x in resources.files(SEARCH_PATH).iterdir() if x.is_file()):
		if p.suffix == '.py' and p.stem != '__init__':
			module_name = f'{SEARCH_PATH}.{p.stem}'
			spec = find_spec(module_name)
			modules[module_name] = spec.loader.load_module(module_name)

	return preprocessors
