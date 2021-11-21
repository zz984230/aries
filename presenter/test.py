import pandas as pd
from datetime import datetime

def t():
    a = pd.DataFrame([['2012', 1], ['2014', 2]])
    a.columns = ['year', 'v']
    b = pd.DataFrame([['2014', 44], ['2013', 55]])
    b.columns = ['year', 'vv']
    z = pd.merge(a, b, on='year', how='outer')
    print(z)
    z['v'] = z['v'].fillna(method='ffill')
    z['vv'] = z['vv'].fillna(method='ffill')
    z = z.sort_values(by=['year'])
    print(z)
    print(list(z.columns))
    print(datetime.today().strftime("%Y-%m-%d"))


if __name__ == '__main__':
    t()