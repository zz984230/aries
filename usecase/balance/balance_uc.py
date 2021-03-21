from repository.balance_repo import BalanceSheet
from constants.constant import *
import dash_core_components as dcc
from presenter.dash_app import *
import pandas as pd


class BalanceUc(object):
    def __init__(self, cfg, presenter):
        self.__repo = BalanceSheet(cfg.src_data_dir).load()
        self.__prt = presenter
        self.__df = pd.DataFrame()

    def __get_data(self):
        self.__df = self.__repo.get_data()

    def __deal_data(self):
        pass

    def __set_layout(self):
        add_layout([
            dcc.RangeSlider(
                id='balance_slider',
                min=self.__df[BALANCE_COL_START].min().year,
                max=self.__df[BALANCE_COL_START].max().year,
                value=[self.__df[BALANCE_YEAR].min(), self.__df[BALANCE_YEAR].max()],
                marks={str(ymd): str(ymd) for ymd in self.__df[BALANCE_YEAR].unique()},
            ),
            # dcc.Dropdown(
            #     id='dataframe',
            #     options=[{'label': col, 'value': self.__df[[BALANCE_COL_START, col]]} for col in self.__repo.get_column()],
            #     value=self.__df[[BALANCE_COL_START, BALANCE_DEFAULT_DRAW]]
            # ),
            dcc.Graph(id="balance"),
        ])

    def run(self):
        self.__get_data()
        self.__deal_data()
        self.__set_layout()
        self.__prt.draw(self.__df)
