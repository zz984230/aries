import pandas as pd


class BalanceSheet(object):
    def __init__(self, src_data_file):
        self.__src_path = src_data_file
        self.__df = pd.DataFrame()

    def __transform(self):
        old_col = self.__df['报告日期']
        col_name = ['报告日期']
        col_name.extend(old_col)
        self.__df = self.__df.drop(columns=['报告日期']).dropna(axis=1).replace('--', 0).replace(' --', 0).T.reset_index()
        self.__df.columns = col_name
        self.__df[old_col] = self.__df[old_col].astype('float')

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
