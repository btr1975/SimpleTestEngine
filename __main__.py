#!/usr/bin/env python3
import logging
import sys
import os
import module as mod
from directories import Directories
__author__ = 'Benjamin P. Trachtenberg'
__copyright__ = "Copyright (c) 2017, Benjamin P. Trachtenberg"
__credits__ = 'Benjamin P. Trachtenberg'
__license__ = 'MIT'
__status__ = 'prod'
__version_info__ = (1, 0, 3, __status__)
__version__ = '.'.join(map(str, __version_info__))
__maintainer__ = 'Benjamin P. Trachtenberg'
__email__ = 'e_ben_75-python@yahoo.com'
COMPILE = False
LOGGER = logging.getLogger(__name__)


def main():
    if COMPILE:
        dirs = Directories(base_dir=os.path.dirname(os.path.realpath(sys.argv[0])))

    else:
        dirs = Directories(base_dir=os.path.dirname(os.path.realpath(__file__)))

    make_logger(dirs)
    mod.QuestionEngine(dirs=dirs)


def make_logger(dirs):
    logging.basicConfig(format='%(asctime)s: %(name)s - %(levelname)s - %(message)s',
                        filename=os.path.join(dirs.get_logging_dir(), 'logs.txt'))
    logging.getLogger().setLevel(dirs.get_logging_level())
    LOGGER.warning('Logging Started!!')


if __name__ == '__main__':
    main()
