import pandas as pd
import numpy as np
import os
from repository.repo import Repo
from datetime import datetime
from constants.constant import *

os.environ['NO_PROXY'] = STOCK_DOMAIN


class ValuationSheet(Repo):
    def __init__(self, stock_name):
        super(ValuationSheet, self).__init__()
        self.__code_url = CODE_URL % stock_name
        self.__valuation_df = pd.DataFrame()
        self.__roic_df = pd.DataFrame()
        self.__stock_id = ""
        self.__col_name = ['日期', '价格', '估值']
        self.__company_description = ""

    def set_stock_name(self, stock_name):
        self.__code_url = CODE_URL % stock_name
        return self

    def __get_stock_id(self):
        obj = self._make_request(self.__code_url)
        try:
            self.__stock_id = [v['data']['stockid'] for v in obj if
                               v['data']['currency'] == '¥'][0]
            # self.__stock_id = [v['data']['stockid'] for v in obj if
            #                    v['data']['exchange'].endswith('SHSE') or v['data']['exchange'].endswith('SZSE')][0]
        except Exception as e:
            print(obj)
            print(e)

    def __get_valuation(self):
        obj = self._make_request(VALUATION_URL % self.__stock_id)
        medps, price = [], []
        try:
            medps, price = obj['medps'], obj['price']
        except Exception as e:
            print(obj)
            print(e)

        return medps, price

    def __get_roic(self):
        objs = self._make_request(FINANCIAL_URL % self.__stock_id, json_data={"type": "ANNUAL"}, typ=1)
        rs = []
        try:
            for obj in objs:
                d = obj.get('date', "")
                roic = obj.get('roic', 0.0)
                wacc = obj.get('wacc', 0.0)
                roe = obj.get('roe', 0.0)
                eps_without_nri = obj.get('eps_without_nri', 0.0)
                free_cash_flow_per_share = obj.get('free_cash_flow_per_share', 0.0)
                eps_basic = obj.get('eps_basic', 0.0)
                roa = obj.get('roa', 0.0)
                rs.append([d, roic, wacc, roe, eps_without_nri, free_cash_flow_per_share, eps_basic, roa])
        except Exception as e:
            print(objs)
            print(e)

        return rs

    def __get_company_info(self):
        obj = self._make_request(COMPANY_INFO_URL % self.__stock_id)
        self.__company_description = obj['business_descrpt']['descrpt']

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
        cols = ['日期', 'ROIC', 'WACC', 'ROE', '扣非每股收益', '每股自由现金流', '基本每股收益', 'ROA']
        self.__roic_df.columns = cols
        self.__roic_df[cols[0]] = pd.to_datetime(self.__roic_df[cols[0]])
        self.__roic_df[cols[1:]] = self.__roic_df[cols[1:]].astype(float)

    def load_valuation(self):
        self.__get_stock_id()
        medps, price = self.__get_valuation()
        self.__transform_valuation(medps, price)

        return self

    def load_roic(self):
        self.__get_stock_id()
        rs = self.__get_roic()
        self.__transform_roic(rs)

        return self

    def load_company_info(self):
        self.__get_stock_id()
        self.__get_company_info()

        return self

    def get_valuation_data(self, col_name=None):
        if col_name is None:
            return self.__valuation_df

        return self.__valuation_df[col_name]

    def get_roic_data(self, col_name=None):
        if col_name is None:
            return self.__roic_df

        return self.__roic_df[col_name]

    def get_company_data(self):
        return self.__company_description
