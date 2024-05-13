
from logging import getLogger as logging_getLogger, root, StreamHandler, Formatter, DEBUG, INFO, WARNING, ERROR, CRITICAL
from os import name


class CustomFormatterLinux(Formatter):
	WHITE = '\033[97m'
	YELLOW = '\033[33m'
	LIGHT_RED = '\033[91m'
	RED = '\033[31m'
	LIGHT_GRAY = '\033[37m'
	DARK_GRAY = '\033[90m'
	ENDC = '\033[0m'
	BOLD = '\033[1m'
	UNDERLINE = '\033[4m'
	ITALIC = '\033[3m'
	FORMATS = {
		DEBUG: Formatter(f'{DARK_GRAY}%(relativeCreated)f D {LIGHT_GRAY}{ITALIC}%(filename)s:%(lineno)d:%(funcName)s{ENDC} {LIGHT_GRAY}%(message)s{ENDC}'),
		INFO: Formatter(f'{DARK_GRAY}%(relativeCreated)f I {BOLD}{LIGHT_GRAY}{ITALIC}%(filename)s:%(lineno)d:%(funcName)s{ENDC} {BOLD}{LIGHT_GRAY}%(message)s{ENDC}'),
		WARNING: Formatter(f'{DARK_GRAY}%(relativeCreated)f W {YELLOW}{ITALIC}%(filename)s:%(lineno)d:%(funcName)s{ENDC} {YELLOW}%(message)s{ENDC}'),
		ERROR: Formatter(f'{DARK_GRAY}%(relativeCreated)f E {BOLD}{LIGHT_RED}{ITALIC}%(filename)s:%(lineno)d:%(funcName)s{ENDC} {BOLD}{LIGHT_RED}%(message)s{ENDC}'),
		CRITICAL: Formatter(f'{DARK_GRAY}%(relativeCreated)f C {BOLD}{RED}{ITALIC}%(filename)s:%(lineno)d:%(funcName)s{ENDC} {BOLD}{RED}%(message)s{ENDC}'),
	}

	def format(self, record):
		return self.FORMATS.get(record.levelno).format(record)


class CustomFormatterWindows(Formatter):
	FORMATS = {
		DEBUG: Formatter(f'%(relativeCreated)f D %(filename)s:%(lineno)d:%(funcName)s %(message)s'),
		INFO: Formatter(f'%(relativeCreated)f I %(filename)s:%(lineno)d:%(funcName)s %(message)s'),
		WARNING: Formatter(f'%(relativeCreated)f W %(filename)s:%(lineno)d:%(funcName)s%(message)s'),
		ERROR: Formatter(f'%(relativeCreated)f E %(filename)s:%(lineno)d:%(funcName)s %(message)s'),
		CRITICAL: Formatter(f'%(relativeCreated)f C %(filename)s:%(lineno)d:%(funcName)s %(message)s'),
	}

	def format(self, record):
		return self.FORMATS.get(record.levelno).format(record)


log = logging_getLogger('base')
log.setLevel(DEBUG)
log_handler = StreamHandler()
log_handler.setLevel(DEBUG)
log_handler.setFormatter(CustomFormatterWindows() if name == 'nt' else CustomFormatterLinux())
# log.addHandler(log_handler)
root.addHandler(log_handler)

def getLogger(name: str | None = 'base'):
	return logging_getLogger(name)
