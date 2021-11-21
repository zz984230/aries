PROJECT_NAME = 'aries'
BALANCE_COL_START = '报告日期'
BALANCE_YEAR = 'YEAR'
BALANCE_DEFAULT_DRAW = '货币资金(万元)'
BALANCE_FLOW_ASSETS_ALL = '流动资产合计(万元)'
BALANCE_FIXED_ASSETS_ALL = '非流动资产合计(万元)'

STOCK_DOMAIN = 'www.gurufocus.cn'
CODE_URL = f'https://{STOCK_DOMAIN}/search?locale=zh-hans&text=%s&type=stock'
VALUATION_URL = f'https://{STOCK_DOMAIN}/_api/chart/%s/valuation?locale=zh-hans'
# https://www.gurufocus.cn/_api/stock/CN0138/financial/items/cash_equivalents_marketable_securities,cash_flow_from_operations,net_income,revenue,total_debt,total_free_cash_flow,net_income_from_continuing_operations,dividends,roic,roe,wacc?locale=zh-hans
FINANCIAL_URL = f'https://{STOCK_DOMAIN}/_api/stock/%s/financial/items/roic,roe,wacc?locale=zh-hans'
CLOUD_URL = f'https://{STOCK_DOMAIN}/_api/screener?locale=zh-hans'
ClOUD_POST_JSON = '{"per_page": 200, "exchanges": ["SHSE", "SZSE"], "fields": ["pchange_1w", "group", "sector", "mktcap_norm_cny"], "filters": [], "guru_filters": [], "inst_holding_filters": [], "insider_filters": [], "insider_trading_filters": [], "sorts": "mktcap_norm|DESC", "rank_by": "", "use_in_screener": true}'