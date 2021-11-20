import requests
import pandas as pd
import numpy as np
import os
from datetime import datetime
from constants.constant import *

os.environ['NO_PROXY'] = STOCK_DOMAIN


class ValuationSheet(object):
    def __init__(self, stock_name):
        self.__code_url = f'{CODE_URL_PREFIX}&text={stock_name}&type=stock'
        self.__valuation_url = ''
        self.__stock_name = stock_name
        self.__df = pd.DataFrame()
        self.__stock_id = ""
        self.__col_name = ['日期', '价格', '估值']

    def set_stock_name(self, stock_name):
        self.__stock_name = stock_name
        self.__code_url = f'{CODE_URL_PREFIX}&text={stock_name}&type=stock'
        return self

    def __make_request(self, url):
        print(url)
        r = requests.get(url, verify=False)
        return r.json()

    def __get_stock_id(self):
        obj = self.__make_request(self.__code_url)
        try:
            self.__stock_id = [v['data']['stockid'] for v in obj if v['data']['exchange'].endswith('SHSE') or v['data']['exchange'].endswith('SZSE')][0]
        except Exception as e:
            print(obj)
            print(e)

    def __get_valuation(self):
        self.__valuation_url = f'{VALUATION_URL_PREFIX}/{self.__stock_id}/valuation?locale=zh-hans'
        obj = self.__make_request(self.__valuation_url)
        medps, price = [], []
        try:
            medps, price = obj['medps'], obj['price']
        except Exception as e:
            print(obj)
            print(e)

        return medps, price

    def __transform(self, medps, price):
        medps_list = np.array(medps).reshape(-1, 2)
        val_df = pd.DataFrame(medps_list)
        price_list = np.array(price).reshape(-1, 2)
        price_df = pd.DataFrame(price_list)
        val_df.columns, price_df.columns = [self.__col_name[0], self.__col_name[2]], self.__col_name[:2]

        self.__df = pd.merge(price_df, val_df, on=self.__col_name[0], how='outer')
        self.__df = self.__df.sort_values(by=[self.__col_name[0]])
        self.__df[self.__col_name[0]] = pd.to_datetime(self.__df[self.__col_name[0]])
        self.__df[self.__col_name[1:]] = self.__df[self.__col_name[1:]].astype(float)
        self.__df[self.__col_name[1]] = self.__df[self.__col_name[1]].interpolate()
        self.__df[self.__col_name[2]] = self.__df[self.__col_name[2]].interpolate()
        self.__df = self.__df[self.__df[self.__col_name[0]] <= datetime.today()]

    def load(self):
        self.__get_stock_id()
        medps, price = self.__get_valuation()
        self.__transform(medps, price)
        return self

    def get_data(self, col_name=None):
        if col_name is None:
            return self.__df

        return self.__df[col_name]

    def get_column(self) -> list:
        return list(self.__col_name)

    def get_stock(self) -> str:
        return self.__stock_name


if __name__ == '__main__':
    v = ValuationSheet('贵州茅台')
    v.load()
