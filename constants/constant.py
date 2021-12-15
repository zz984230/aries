PROJECT_NAME = 'aries'
ABNORMAL_DATA = '-99999.0'
BALANCE_COL_START = '报告日期'
BALANCE_YEAR = 'YEAR'
BALANCE_DEFAULT_DRAW = '货币资金(万元)'
BALANCE_FLOW_ASSETS_ALL = '流动资产合计(万元)'
BALANCE_FIXED_ASSETS_ALL = '非流动资产合计(万元)'

#######################################
FINANCIAL_RATIO_URL = 'https://caibaoshuo.com/companies/%s/financials'

FINANCIAL_RATIO_COL = [
    '现金与约当现金',
    '现金流量比率',
    '现金流量允当比率',
    '现金再投资比率',
    '总资产周转率',
    '应收款项周转天数',
    '存货周转天数',
    '净资产收益率',
    '毛利率',
    '营业利润率',
    '经营安全边际率',
    '负债占资产比率',
    '长期资金占重资产比率',
    '流动比率',
    '速动比率',
]

#######################################
STOCK_DOMAIN = 'www.gurufocus.cn'
# 股票编码
CODE_URL = f'https://{STOCK_DOMAIN}/search?locale=zh-hans&text=%s&type=stock'

# 估值信息
VALUATION_URL = f'https://{STOCK_DOMAIN}/_api/chart/%s/valuation?locale=zh-hans'

# 投资回报率、净资产收益率、加权平均资本成本、扣非每股收益等指标
# https://www.gurufocus.cn/_api/stock/CN0138/financial/items/cash_equivalents_marketable_securities,cash_flow_from_operations,net_income,revenue,total_debt,total_free_cash_flow,net_income_from_continuing_operations,dividends,roic,roe,wacc?locale=zh-hans
FINANCIAL_URL = f'https://{STOCK_DOMAIN}/_api/stock/%s/financial/items/roic,roe,wacc,eps_without_nri,free_cash_flow_per_share,eps_basic,roa?locale=zh-hans'

# 大盘云图
CLOUD_URL = f'https://{STOCK_DOMAIN}/_api/screener?locale=zh-hans'
ClOUD_POST_JSON = '{"per_page": 200, "exchanges": ["SHSE", "SZSE"], "fields": ["p_pct_change", "group", "sector", "mktcap_norm_cny"], "filters": [], "guru_filters": [], "inst_holding_filters": [], "insider_filters": [], "insider_trading_filters": [], "sorts": "mktcap_norm|DESC", "rank_by": "", "use_in_screener": true}'

# 公司简介
COMPANY_INFO_URL = f'https://{STOCK_DOMAIN}/_api/stock/%s/1489?locale=zh-hans'
#######################################
