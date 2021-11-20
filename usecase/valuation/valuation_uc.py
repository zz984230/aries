import pandas as pd
from repository.valuation_repo import ValuationSheet


class ValuationUc(object):
    def __init__(self, prt):
        self.__repo = ValuationSheet('贵州茅台').load()
        self.__prt = prt
        self.__df = pd.DataFrame()
        self.__cols = list()

    def __get_data(self):
        self.__df = self.__repo.get_data()
        self.__cols = self.__repo.get_column()
        self.__stock_name = self.__repo.get_stock()

    def __deal_data(self):
        pass

    def __set_layout(self):
        self.__prt.init_data(self.__df, self.__cols, self.__stock_name)

    def run(self):
        self.__get_data()
        self.__deal_data()
        self.__set_layout()
        self.__prt.render(self.__repo)
