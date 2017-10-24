#!/usr/bin/env python3
import logging
import os
import menusys as mnu
import persistentdatatools as pdt
import yaml
__author__ = 'Benjamin P. Trachtenberg'
__copyright__ = "Copyright (c) 2017, Benjamin P. Trachtenberg"
__credits__ = 'Benjamin P. Trachtenberg'
__license__ = 'MIT'
__status__ = 'dev'
__version_info__ = (1, 0, 0, __status__)
__version__ = '.'.join(map(str, __version_info__))
__maintainer__ = 'Benjamin P. Trachtenberg'
__email__ = 'e_ben_75-python@yahoo.com'

LOGGER = logging.getLogger(__name__)


class QuestionEngine(object):

    def __init__(self, dirs):
        self.dirs = dirs
        self.select_questions()

    def select_questions(self):
        mnu.clear_screen()
        question_file_names = pdt.list_files_in_directory(self.dirs.get_input_dir())
        question_file_names_menu = mnu.make_menu_dict_from_list(question_file_names)
        file_opt = int(mnu.menu(question_file_names_menu, 'Choose a Test Set', allow_sys_exit=True))
        self.get_questions_yml(question_file_names_menu.get(file_opt).get('MENU'))

    def get_questions_yml(self, yml_file_name):
        """
        Method to get and return the yml data
        :param yml_file_name: The name of the file
        :return:

        """
        yml_data = os.path.join(self.dirs.get_input_dir(), yml_file_name)
        a = yaml.safe_load(self.stream_yml(yml_data))
        question_sets = a.get('question_sets')
        if len(question_sets) > 1:
            temp_list = list()
            for question_set in question_sets:
                temp_list.append(question_set.get('question_set'))

            mnu.make_menu_dict_from_list(temp_list)

        else:
            return question_sets[0]

    def stream_yml(self, yml_data):
        """
        Method to retrieve yml stream
        :param yml_data: The yml data
        :return:
            A Stream
        """
        read_file = open(yml_data, 'r')
        temp_stream = read_file.read()
        read_file.close()
        return temp_stream