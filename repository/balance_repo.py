import pandas as pd


class BalanceSheet(object):
    def __init__(self, src_data_file):
        self.__src_path = src_data_file
        self.__df = pd.DataFrame()

    def __transform(self):
        col_name = self.__df['报告日期']
        self.__df = self.__df.drop(columns=['报告日期']).dropna(axis=1).replace('--', 0).T
        self.__df.columns = col_name

    def load(self):
        self.__df = pd.read_csv(self.__src_path, encoding='gbk')
        self.__transform()
        print(self.__df.head())

    def get_data(self, col_name=None):
        if col_name is None:
            return self.__df

        return self.__df[col_name]

    def get_index(self) -> list:
        return list(self.__df.index)

    def get_column(self) -> list:
        return list(self.__df.columns)
