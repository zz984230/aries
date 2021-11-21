import pandas as pd
import numpy as np
import os
import json
from datetime import datetime
from repository.repo import Repo
from constants.constant import *

os.environ['NO_PROXY'] = STOCK_DOMAIN
PER_SIZE = 200


class CloudSheet(Repo):
    def __init__(self, cloud_data_path=os.path.join(os.path.abspath('.'), 'data', 'cloud')):
        super(CloudSheet, self).__init__()
        self.__df = pd.DataFrame()
        self.__cols = ['行业', '行业细分', '公司', '涨跌幅', '市值']
        self.__json_req = json.loads(ClOUD_POST_JSON)
        self.__data_path = os.path.join(cloud_data_path, f'{datetime.today().strftime("%Y-%m-%d")}.csv')

    def __get_cloud(self):
        page = 0
        total = 999999
        rs = []
        while page * PER_SIZE <= total:
            page += 1
            self.__json_req.update({'page': page})
            print(f'page: {page}, total: {total}')
            objs = self._make_request(CLOUD_URL, typ=1, json_data=self.__json_req)
            total = objs['total']
            tmp = []
            try:
                tmp = [(obj['sector'], obj['group'], obj['company'], obj['p_pct_change'], obj['mktcap_norm_cny']) for obj in objs['data']]
            except Exception as e:
                print(objs)
                print(e)

            rs.extend(tmp)

        return rs

    def __transform_cloud(self, rs):
        rs_list = np.array(rs).reshape((-1, len(self.__cols)))
        self.__df = pd.DataFrame(rs_list)
        self.__df.columns = self.__cols
        self.__df[self.__cols[3:]] = self.__df[self.__cols[3:]].astype(float)
        # self.__df['color'] = self.__df[self.__cols[3]]
        # self.__df['color'][self.__df['color'] > 10] = 10
        # self.__df['color'][self.__df['color'] < -10] = -10

    def __save_cloud(self):
        self.__df.to_csv(self.__data_path, index=False)

    def load_cloud(self):
        if os.path.exists(self.__data_path):
            self.__df = pd.read_csv(self.__data_path)
            self.__df[self.__cols[3:]] = self.__df[self.__cols[3:]].astype(float)
            # self.__df['color'] = self.__df[self.__cols[3]]
            # self.__df['color'][self.__df['color'] > 10] = 10
            # self.__df['color'][self.__df['color'] < -10] = -10
            return self

        self.__transform_cloud(self.__get_cloud())
        self.__save_cloud()
        return self

    def get_cloud_data(self):
        return self.__df


if __name__ == '__main__':
    c = CloudSheet()
    c.load_cloud()
