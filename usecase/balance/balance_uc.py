from repository.balance_repo import BalanceSheet
import pandas as pd


class BalanceUc(object):
    def __init__(self, cfg, presenter):
        self.__repo = BalanceSheet(cfg.src_data_dir).load()
        self.__prt = presenter
        self.__df = pd.DataFrame()
        self.__cols = list()

    def __get_data(self):
        self.__df = self.__repo.get_data()
        self.__cols = self.__repo.get_column()

    def __deal_data(self):
        pass

    def __set_layout(self):
        self.__prt.set_layout(self.__df, self.__cols)

    def run(self):
        self.__get_data()
        self.__deal_data()
        self.__set_layout()
        self.__prt.draw(self.__df)
