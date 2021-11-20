import requests
import pandas as pd
import numpy as np
import os
from datetime import datetime
from constants.constant import *

os.environ['NO_PROXY'] = STOCK_DOMAIN


class ValuationSheet(object):
    def __init__(self, stock_name):
        self.__code_url = CODE_URL % stock_name
        self.__stock_name = stock_name
        self.__valuation_df = pd.DataFrame()
        self.__roic_df = pd.DataFrame()
        self.__stock_id = ""
        self.__col_name = ['日期', '价格', '估值']

    def set_stock_name(self, stock_name):
        self.__stock_name = stock_name
        self.__code_url = CODE_URL % stock_name
        return self

    def __make_request(self, url, data=None, typ=0):
        print(url)
        if typ:
            r = requests.post(url, verify=False, data=data)
        else:
            r = requests.get(url, verify=False)
        return r.json()

    def __get_stock_id(self):
        obj = self.__make_request(self.__code_url)
        try:
            self.__stock_id = [v['data']['stockid'] for v in obj if
                               v['data']['exchange'].endswith('SHSE') or v['data']['exchange'].endswith('SZSE')][0]
        except Exception as e:
            print(obj)
            print(e)

    def __get_valuation(self):
        obj = self.__make_request(VALUATION_URL % self.__stock_id)
        medps, price = [], []
        try:
            medps, price = obj['medps'], obj['price']
        except Exception as e:
            print(obj)
            print(e)

        return medps, price

    def __get_roic(self):
        objs = self.__make_request(FINANCIAL_URL % self.__stock_id, {"type": "ANNUAL", "start": "2017-01-01", "end": "2021-09-30"}, 1)
        rs = []
        try:
            rs = [(obj['date'], obj['roic'], obj['wacc']) for obj in objs]
        except Exception as e:
            print(objs)
            print(e)

        return rs

    def __transform_valuation(self, medps, price):
        medps_list = np.array(medps).reshape(-1, 2)
        val_df = pd.DataFrame(medps_list)
        price_list = np.array(price).reshape(-1, 2)
        price_df = pd.DataFrame(price_list)
        val_df.columns, price_df.columns = [self.__col_name[0], self.__col_name[2]], self.__col_name[:2]

        self.__valuation_df = pd.merge(price_df, val_df, on=self.__col_name[0], how='outer')
        self.__valuation_df = self.__valuation_df.sort_values(by=[self.__col_name[0]])
        self.__valuation_df[self.__col_name[0]] = pd.to_datetime(self.__valuation_df[self.__col_name[0]])
        self.__valuation_df[self.__col_name[1:]] = self.__valuation_df[self.__col_name[1:]].astype(float)
        self.__valuation_df[self.__col_name[1]] = self.__valuation_df[self.__col_name[1]].interpolate()
        self.__valuation_df[self.__col_name[2]] = self.__valuation_df[self.__col_name[2]].interpolate()
        self.__valuation_df = self.__valuation_df[self.__valuation_df[self.__col_name[0]] <= datetime.today()]

    def __transform_roic(self, rs):
        self.__roic_df = pd.DataFrame(rs)
        cols = ['日期', 'ROIC', 'WACC']
        self.__roic_df.columns = cols
        self.__roic_df[cols[0]] = pd.to_datetime(self.__roic_df[cols[0]])
        self.__roic_df[cols[1:]] = self.__roic_df[cols[1:]].astype(float)
        self.__roic_df['ROIC - WACC'] = self.__roic_df[cols[1]] - self.__roic_df[cols[2]]

    def load(self):
        self.__get_stock_id()
        medps, price = self.__get_valuation()
        self.__transform_valuation(medps, price)
        rs = self.__get_roic()
        self.__transform_roic(rs)

        return self

    def get_valuation_data(self, col_name=None):
        if col_name is None:
            return self.__valuation_df

        return self.__valuation_df[col_name]

    def get_roic_data(self, col_name=None):
        if col_name is None:
            return self.__roic_df

        return self.__roic_df[col_name]

    def get_column(self) -> list:
        return list(self.__col_name)

    def get_stock(self) -> str:
        return self.__stock_name


if __name__ == '__main__':
    v = ValuationSheet('贵州茅台')
    v.load()
