import pandas as pd
from repository.valuation_repo import ValuationSheet


class ValuationUc(object):
    def __init__(self, prt):
        self.__repo = ValuationSheet('贵州茅台').load()
        self.__prt = prt

    def __get_data(self):
        self.__stock_name = self.__repo.get_stock()

    def __deal_data(self):
        pass

    def __set_layout(self):
        self.__prt.init_data(self.__stock_name)

    def run(self):
        self.__get_data()
        self.__deal_data()
        self.__set_layout()
        self.__prt.render(self.__repo)
