import pandas as pd
import os
from repository.repo import Repo
from constants.constant import *
from bs4 import BeautifulSoup
import requests

os.environ['NO_PROXY'] = STOCK_DOMAIN


class FinancialRatio(Repo):
    def __init__(self, stock_name):
        super(FinancialRatio, self).__init__()
        self.__proxies = {"http": None, "https": None}
        self.__code_url = CODE_URL % stock_name
        self.__df = pd.DataFrame()
        self.__stock_symbol = ""

    def set_stock_name(self, stock_name):
        self.__code_url = CODE_URL % stock_name
        return self

    def __get_stock_symbol(self):
        obj = self._make_request(self.__code_url)
        try:
            self.__stock_symbol = [v['data']['symbol'] for v in obj if
                                   v['data']['exchange'].endswith('SHSE') or v['data']['exchange'].endswith('SZSE')][0]
        except Exception as e:
            print(obj)
            print(e)

    def __get_financial_table_data(self, table):
        trs = table.find_all('tr')
        rs = []
        for c in FINANCIAL_RATIO_COL:
            for tr in trs:
                if c not in tr.get_text():
                    continue

                each = []
                tmp = []
                for td in tr.find_all('td'):
                    t = td.find_all('span')
                    if len(t) > 1:
                        each.extend(t[1])
                    else:
                        d = td.get_text(strip=True)
                        each.append(d if '--' not in d else each[-1])
                tmp.append(each[0])
                tmp.extend(each[-5:])
                rs.append(tmp)

        return rs

    def load_financial(self):
        self.__get_stock_symbol()

        try:
            r = requests.get(FINANCIAL_RATIO_URL % self.__stock_symbol, verify=False, proxies=self.__proxies)
            soup = BeautifulSoup(r.text, 'lxml')
            t = soup.find(id='albs-yearly').find('table')
            col = [th.get_text() for k, th in enumerate(t.find_all('th')[:7]) if k != 1]
            col[-1] = '近12个月'
            table_one = self.__get_financial_table_data(t)
            table_two = self.__get_financial_table_data(soup.find(id='alkey-yearly').find('table'))
            table_one.extend(table_two)
            self.__df = pd.DataFrame(table_one, columns=col)
            self.__df[col[1:]] = self.__df[col[1:]].applymap(lambda x: x.replace(',', '')).astype(float)
        except Exception as e:
            print(e)
            print(self.__df)

        return self

    def get_financial_data(self, col_name=None):
        if col_name is None:
            return self.__df

        return self.__df[col_name]
