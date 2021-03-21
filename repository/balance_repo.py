import pandas as pd
from constants.constant import *


class BalanceSheet(object):
    def __init__(self, src_data_file):
        self.__src_path = src_data_file
        self.__df = pd.DataFrame()

    def __transform(self):
        old_col = self.__df[BALANCE_COL_START]
        col_name = [BALANCE_COL_START]
        col_name.extend(old_col)
        self.__df = self.__df.drop(columns=[BALANCE_COL_START]) \
            .dropna(axis=1) \
            .replace('--', 0) \
            .replace(' --', 0) \
            .T \
            .reset_index()
        self.__df.columns = col_name
        self.__df[old_col] = self.__df[old_col].astype('float')
        self.__df[BALANCE_COL_START] = pd.to_datetime(self.__df[BALANCE_COL_START])
        self.__df[BALANCE_YEAR] = self.__df[BALANCE_COL_START].dt.year

    def load(self):
        self.__df = pd.read_csv(self.__src_path, encoding='gbk')
        self.__transform()
        return self

    def get_data(self, col_name=None):
        if col_name is None:
            return self.__df

        return self.__df[col_name]

    def get_column(self) -> list:
        return list(self.__df.columns)
