# Titanic Project

import pandas as pd


def get_titanic_gender_submission():
    '''
    Reads gender_submission.csv and returns a dataframe
    '''
    path = './'
    return pd.read_csv(path + 'gender_submission.csv')


def get_titanic_train():
    '''
    Reads train.csv and returns a dataframe
    '''
    path = './'
    return pd.read_csv(path + 'train.csv')


def get_titanic_test():
    '''
    Reads test.csv and returns a dataframe
    '''
    path = './'
    return pd.read_csv(path + 'test.csv')
