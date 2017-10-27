#!/usr/bin/env python3
import logging
import os
from random import choice
import menusys as mnu
import persistentdatatools as pdt
import yaml
__author__ = 'Benjamin P. Trachtenberg'
__copyright__ = "Copyright (c) 2017, Benjamin P. Trachtenberg"
__credits__ = 'Benjamin P. Trachtenberg'
__license__ = 'MIT'
__status__ = 'prod'
__version_info__ = (1, 0, 0, __status__)
__version__ = '.'.join(map(str, __version_info__))
__maintainer__ = 'Benjamin P. Trachtenberg'
__email__ = 'e_ben_75-python@yahoo.com'

LOGGER = logging.getLogger(__name__)


class QuestionEngine(object):

    def __init__(self, dirs):
        self.dirs = dirs
        self.unanswered_questions = self.__select_questions().get('questions')
        self.answered_questions = list()
        self.__ask_random_question()
        self.__give_results()

    def __select_questions(self):
        """
        Method to load question set from yml file
        :return:
            A question set
        """
        LOGGER.debug('Starting Method __select_questions in Class: {}'.format(type(self)))
        mnu.clear_screen()
        question_file_names = pdt.list_files_in_directory(self.dirs.get_input_dir())
        question_file_names_menu = mnu.make_menu_dict_from_list(question_file_names)
        file_opt = int(mnu.menu(question_file_names_menu, 'Choose a Test Set', allow_sys_exit=True))
        return self.__get_questions_yml(question_file_names_menu.get(file_opt).get('MENU'))

    def __get_questions_yml(self, yml_file_name):
        """
        Method to get and return the yml data
        :param yml_file_name: The name of the file
        :return:
            A question set
        """
        LOGGER.debug('Starting Method __get_questions_yml in Class: {}'.format(type(self)))
        yml_data = os.path.join(self.dirs.get_input_dir(), yml_file_name)
        a = yaml.safe_load(self.__stream_yml(yml_data))
        question_sets = a.get('question_sets')
        if len(question_sets) > 1:
            temp_list = list()
            for question_set in question_sets:
                temp_list.append(question_set.get('question_set'))

            question_set_names_menu = mnu.make_menu_dict_from_list(temp_list)
            set_opt = int(mnu.menu(question_set_names_menu, 'Choose a Question Set', allow_sys_exit=True))

            for question_set in question_sets:
                if question_set.get('question_set') == question_set_names_menu.get(set_opt).get('MENU'):
                    LOGGER.debug('Question data retrieved:\n {}'.format(yaml.dump(question_set,
                                                                                  default_flow_style=False,
                                                                                  indent=4)))
                    return question_set

        else:
            LOGGER.debug('Question data retrieved:\n {}'.format(yaml.dump(question_sets[0],
                                                                          default_flow_style=False, indent=4)))
            return question_sets[0]

    @staticmethod
    def __stream_yml(yml_data):
        """
        Method to retrieve yml stream
        :param yml_data: The yml data
        :return:
            A Stream
        """
        LOGGER.debug('Starting Method __stream_yml in Class: <class \'module.question_engine.QuestionEngine\'>')
        read_file = open(yml_data, 'r')
        temp_stream = read_file.read()
        read_file.close()
        return temp_stream

    def __ask_random_question(self):
        """
        Method to ask the questions randomly
        :return:
            None
        """
        LOGGER.debug('Starting Method __ask_random_question in Class: {}'.format(type(self)))
        while len(self.unanswered_questions) > 0:
            mnu.clear_screen()
            correct = False
            random_question = choice(self.unanswered_questions)

            if random_question.get('answer_opts'):
                temp_q_menu = mnu.make_menu_dict_from_list(random_question.get('answer_opts'))
                answer_opt = int(mnu.menu(temp_q_menu, random_question.get('question'), no_quit=True))
                if temp_q_menu.get(answer_opt).get('MENU') == random_question.get('answer'):
                    if random_question.get('feedback'):
                        print(random_question.get('feedback').get('correct_answer'))

                    else:
                        print('CORRECT!!')

                    correct = True

                else:
                    if random_question.get('feedback'):
                        print(random_question.get('feedback').get('incorrect_answer'))

                    else:
                        print('SORRY THAT IS NOT CORRECT!!')

            else:
                answer = input('{question}: '.format(question=random_question.get('question')))
                answer = pdt.remove_extra_spaces(answer)
                if isinstance(random_question.get('answer'), list):
                    for correct_answer in random_question.get('answer'):
                        if answer.lower() == correct_answer.lower():
                            if random_question.get('feedback'):
                                print(random_question.get('feedback').get('correct_answer'))

                            else:
                                print('CORRECT!!')

                            correct = True
                            break

                    if not correct:
                        if random_question.get('feedback'):
                            print(random_question.get('feedback').get('incorrect_answer'))

                        else:
                            print('SORRY THAT IS NOT CORRECT!!')

                else:
                    if answer.lower() == random_question.get('answer').lower():
                        if random_question.get('feedback'):
                            print(random_question.get('feedback').get('correct_answer'))

                        else:
                            print('CORRECT!!')

                        correct = True

                    else:
                        if random_question.get('feedback'):
                            print(random_question.get('feedback').get('incorrect_answer'))

                        else:
                            print('SORRY THAT IS NOT CORRECT!!')

            for index, answered_q in enumerate(self.unanswered_questions):
                if random_question.get('question') == answered_q.get('question'):
                    random_question['correct'] = correct
                    self.answered_questions.append(random_question)
                    self.unanswered_questions.pop(index)
                    break

            input('PRESS <ENTER> TO CONTINUE')

    def __give_results(self):
        """
        Method to give the results of the test
        :return:
            None
        """
        LOGGER.debug('Starting Method __give_results in Class: {}'.format(type(self)))
        output_list = list()
        correct_answers = 0
        display_correct_answers = list()
        incorrect_answers = 0
        display_incorrect_answers = list()
        for result in self.answered_questions:
            if result.get('correct'):
                correct_answers += 1
                display_correct_answers.append('{question}: {answer}'.format(question=result.get('question'),
                                                                             answer=result.get('answer')))

            elif not result.get('correct'):
                incorrect_answers += 1
                display_incorrect_answers.append('{question}: {answer}'.format(question=result.get('question'),
                                                                               answer=result.get('answer')))

        mnu.clear_screen()
        output_list.append('------------------------------------------------------')
        output_list.append('Correct: {}'.format(correct_answers))
        for item in display_correct_answers:
            output_list.append(item)

        output_list.append('\n------------------------------------------------------')
        output_list.append('Incorrect: {}'.format(incorrect_answers))
        for item in display_incorrect_answers:
            output_list.append(item)

        output_list.append('\n------------------------------------------------------')
        output_list.append('Final Score')
        output_list.append('%{:.2f} Correct'.format(correct_answers / len(self.answered_questions) * 100))

        for line in output_list:
            print(line)

        output_file_name = 'ScoreReport.txt'
        info = pdt.list_to_file(output_list, pdt.file_name_increase(output_file_name, self.dirs.get_output_dir()),
                                self.dirs.get_output_dir())

        print('Output score to {}'.format(os.path.join(self.dirs.get_output_dir(), info)))
