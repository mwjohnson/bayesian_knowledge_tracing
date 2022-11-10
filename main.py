#!/usr/bin/env python
# -*- coding: utf-8 -*-
import logging
from timeit import default_timer
import functools
import configparser
import pandas as pd


logging.basicConfig()
logger = logging.getLogger(__name__)
logger.setLevel(level=logging.INFO)


def timer_decorator(func_to_time):
    """
    A timer decorator. Using this, like in the load_settings() function declaration below will enable a timing
    report for the function call.
    Simply include @timer_decorator before you function definition.
    @timer_decorator
    def my_timed_function():
    :param func_to_time: the function to measure the time of execution.
    :return: the wrapper - used for decoration.
    """
    @functools.wraps(func_to_time)
    def wrapper_timer(*args, **kwargs):
        start = default_timer()
        result = func_to_time(*args, **kwargs)
        end = default_timer()
        logger.info(func_to_time.__name__ + ': elapsed time: %s', end - start)
        return result

    return wrapper_timer


@timer_decorator
def load_settings():
    """
    Load settings from the input-file, config.ini
    Example settings which can be placed inside the settings dictionary.

    'string_setting': cfg.get('settings', 'some_string_setting'),
    'Integer_setting': cfg.getint('settings', 'integer_config_setting'),
    'float_setting': cfg.getfloat('settings', 'float_config_setting'),
    'boolean_setting': cfg.getboolean('settings', 'boolean_config'),

    :return: the settings dictionary.
    """
    cfg = configparser.ConfigParser()
    cfg.read_file(open('config.ini'))

    settings = {

    }

    return settings


def BKTrace(responses):
    pSlip = 0.1
    pGuess = 0.3
    pTrained = 0.1
    pLearned = 0.5

    model_values = []
    k = 0.0
    Ktm1 = pLearned

    for r in responses:
        if r:
            k = Ktm1 * (1 - pSlip) / (Ktm1 * (1 - pSlip) + pGuess * (1 - Ktm1))
        else:
            k = (Ktm1 * pSlip) / (Ktm1 * pSlip + (1 - Ktm1) * (1 - pGuess))
        Kt = k + (1 - k) * pTrained
        Ktm1 = Kt
        model_values.append(Kt)


def main():
    logger.info(__name__ + " started.")

    # reading csv file
    filename = 'E:/zinc/research/aied_2023/bkt_analysis/ds5354_student_step_All_Data_7583_2022_1013_054027.txt'
    df = pd.read_csv(filename, delimiter='\t')


    logger.info('Complete.')


if __name__ == '__main__':
    main()