from bs4 import BeautifulSoup
import requests

URL = 'https://caibaoshuo.com/companies/002020/financials'

COL = [
    '现金与约当现金',
    '现金流量比率',
    '现金流量允当比率',
    '现金再投资比率',
    '总资产周转率',
    '应收账款周转天数',
    '存货周转天数',
    '净资产收益率',
    '毛利率',
    '营业利润率',
    '经营安全边际率',
    '资产负债率',
    '长期资金占重资产比率',
    '流动比率',
    '速动比率',
]


# def table_data(table):
#     rows = []
#     trs = table.find_all('tr')
#     headerow = [td.get_text(strip=True) for td in trs[0].find_all('th')]
#     if headerow:
#         rows.append(headerow)
#         trs = trs[1:]
#     for tr in trs:
#         tds = []
#         for td in tr.find_all('td'):
#             t = td.find_all('span')
#             if len(t) > 1:
#                 tds.extend(t[1])
#             else:
#                 tds.append(td.get_text(strip=True))
#         rows.append(tds)
#     return rows


def get_table_data(table):
    trs = table.find_all('tr')
    rs = []
    for c in COL:
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


if __name__ == '__main__':
    proxies = {"http": None, "https": None}
    r = requests.get(URL, verify=False, proxies=proxies)
    soup = BeautifulSoup(r.text, 'lxml')
    table_one = get_table_data(soup.find(id='albs-yearly').find('table'))

    table_two = get_table_data(soup.find(id='alkey-yearly').find('table'))
    table_one.extend(table_two)

    import pandas as pd
    col = ['类别', '2017', '2018', '2019', '2020', '近12个月']
    df = pd.DataFrame(table_one, columns=col)
    df[col[1:]] = df[col[1:]].astype(float)
    print(df)
