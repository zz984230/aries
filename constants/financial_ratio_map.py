import sys

MAX = sys.maxsize
MIN = -MAX

ABILITY = {
    '现金与约当现金(%)': {
        'duration': [
            {
                'start': MIN,
                'end': 0,
                'score': 0
            },
            {
                'start': 0,
                'end': 5,
                'score': 40
            },
            {
                'start': 5,
                'end': 10,
                'score': 60
            },
            {
                'start': 10,
                'end': 15,
                'score': 70
            },
            {
                'start': 15,
                'end': 20,
                'score': 80
            },
            {
                'start': 20,
                'end': 25,
                'score': 90
            },
            {
                'start': 25,
                'end': MAX,
                'score': 100
            },
        ],
        'weight': 0.25,
        'type': 1,
    },
    '现金流量比率(%)': {
        'duration': [
            {
                'start': MIN,
                'end': 50,
                'score': 25
            },
            {
                'start': 50,
                'end': 60,
                'score': 50
            },
            {
                'start': 60,
                'end': 70,
                'score': 60
            },
            {
                'start': 70,
                'end': 80,
                'score': 70
            },
            {
                'start': 80,
                'end': 90,
                'score': 80
            },
            {
                'start': 90,
                'end': 100,
                'score': 90
            },
            {
                'start': 100,
                'end': MAX,
                'score': 100
            },
        ],
        'weight': 0.25,
        'type': 1,
    },
    '现金流量允当比率(%)': {
        'duration': [
            {
                'start': MIN,
                'end': 50,
                'score': 0
            },
            {
                'start': 50,
                'end': 60,
                'score': 10
            },
            {
                'start': 60,
                'end': 70,
                'score': 20
            },
            {
                'start': 70,
                'end': 80,
                'score': 40
            },
            {
                'start': 80,
                'end': 90,
                'score': 60
            },
            {
                'start': 90,
                'end': 100,
                'score': 80
            },
            {
                'start': 100,
                'end': MAX,
                'score': 100
            },
        ],
        'weight': 0.25,
        'type': 1,
    },
    '现金再投资比率(%)': {
        'duration': [
            {
                'start': MIN,
                'end': 0,
                'score': 0
            },
            {
                'start': 0,
                'end': 5,
                'score': 20
            },
            {
                'start': 5,
                'end': 10,
                'score': 40
            },
            {
                'start': 10,
                'end': 15,
                'score': 60
            },
            {
                'start': 15,
                'end': 20,
                'score': 80
            },
            {
                'start': 20,
                'end': MAX,
                'score': 100
            },
        ],
        'weight': 0.25,
        'type': 1,
    },
    '总资产周转率(次/年)': {
        'duration': [
            {
                'start': MIN,
                'end': 1,
                'score': 30
            },
            {
                'start': 1,
                'end': 1.3,
                'score': 60
            },
            {
                'start': 1.3,
                'end': 1.6,
                'score': 75
            },
            {
                'start': 1.6,
                'end': 2,
                'score': 85
            },
            {
                'start': 2,
                'end': MAX,
                'score': 100
            },
        ],
        'weight': 0.4,
        'type': 2,
    },
    '应收款项周转天数(天)': {
        'duration': [
            {
                'start': MIN,
                'end': 30,
                'score': 100
            },
            {
                'start': 30,
                'end': 60,
                'score': 80
            },
            {
                'start': 60,
                'end': 90,
                'score': 60
            },
            {
                'start': 90,
                'end': 150,
                'score': 40
            },
            {
                'start': 150,
                'end': MAX,
                'score': 20
            },
        ],
        'weight': 0.3,
        'type': 2,
    },
    '存货周转天数(天)': {
        'duration': [
            {
                'start': MIN,
                'end': 90,
                'score': 100
            },
            {
                'start': 90,
                'end': 120,
                'score': 90
            },
            {
                'start': 120,
                'end': 150,
                'score': 80
            },
            {
                'start': 150,
                'end': 180,
                'score': 70
            },
            {
                'start': 180,
                'end': 210,
                'score': 60
            },
            {
                'start': 210,
                'end': MAX,
                'score': 30
            },
        ],
        'weight': 0.3,
        'type': 2,
    },
    'ROE=净资产收益率(%)': {
        'duration': [
            {
                'start': MIN,
                'end': 0,
                'score': 0
            },
            {
                'start': 0,
                'end': 10,
                'score': 25
            },
            {
                'start': 10,
                'end': 15,
                'score': 50
            },
            {
                'start': 15,
                'end': 20,
                'score': 60
            },
            {
                'start': 20,
                'end': 30,
                'score': 80
            },
            {
                'start': 30,
                'end': MAX,
                'score': 100
            },
        ],
        'weight': 0.3,
        'type': 3,
    },
    '毛利率(%)': {
        'duration': [
            {
                'start': MIN,
                'end': 0,
                'score': 0
            },
            {
                'start': 0,
                'end': 10,
                'score': 25
            },
            {
                'start': 10,
                'end': 30,
                'score': 40
            },
            {
                'start': 20,
                'end': 50,
                'score': 60
            },
            {
                'start': 50,
                'end': 70,
                'score': 80
            },
            {
                'start': 70,
                'end': 90,
                'score': 90
            },
            {
                'start': 90,
                'end': MAX,
                'score': 100
            },
        ],
        'weight': 0.25,
        'type': 3,
    },
    '营业利润率(%)': {
        'duration': [
            {
                'start': MIN,
                'end': 10,
                'score': 0
            },
            {
                'start': 10,
                'end': 20,
                'score': 60
            },
            {
                'start': 20,
                'end': 40,
                'score': 70
            },
            {
                'start': 40,
                'end': 60,
                'score': 85
            },
            {
                'start': 60,
                'end': MAX,
                'score': 100
            },
        ],
        'weight': 0.25,
        'type': 3,
    },
    '经营安全边际率(%)': {
        'duration': [
            {
                'start': MIN,
                'end': 5,
                'score': 0
            },
            {
                'start': 5,
                'end': 20,
                'score': 25
            },
            {
                'start': 20,
                'end': 35,
                'score': 40
            },
            {
                'start': 35,
                'end': 50,
                'score': 55
            },
            {
                'start': 50,
                'end': 65,
                'score': 70
            },
            {
                'start': 65,
                'end': 80,
                'score': 85
            },
            {
                'start': 80,
                'end': MAX,
                'score': 100
            },
        ],
        'weight': 0.2,
        'type': 3,
    },
    '负债占资产比率(%)': {
        'duration': [
            {
                'start': MIN,
                'end': 10,
                'score': 100
            },
            {
                'start': 10,
                'end': 20,
                'score': 85
            },
            {
                'start': 20,
                'end': 30,
                'score': 70
            },
            {
                'start': 30,
                'end': 40,
                'score': 55
            },
            {
                'start': 40,
                'end': 50,
                'score': 40
            },
            {
                'start': 50,
                'end': MAX,
                'score': 0
            },
        ],
        'weight': 0.6,
        'type': 4,
    },
    '长期资金占重资产比率(%)': {
        'duration': [
            {
                'start': MIN,
                'end': 50,
                'score': 0
            },
            {
                'start': 50,
                'end': 70,
                'score': 25
            },
            {
                'start': 70,
                'end': 100,
                'score': 40
            },
            {
                'start': 100,
                'end': 200,
                'score': 60
            },
            {
                'start': 200,
                'end': 300,
                'score': 75
            },
            {
                'start': 300,
                'end': 400,
                'score': 90
            },
            {
                'start': 400,
                'end': MAX,
                'score': 100
            },
        ],
        'weight': 0.4,
        'type': 4,
    },
    '流动比率(%)': {
        'duration': [
            {
                'start': MIN,
                'end': 0,
                'score': 0
            },
            {
                'start': 0,
                'end': 100,
                'score': 25
            },
            {
                'start': 100,
                'end': 150,
                'score': 60
            },
            {
                'start': 150,
                'end': 200,
                'score': 75
            },
            {
                'start': 200,
                'end': 250,
                'score': 90
            },
            {
                'start': 250,
                'end': MAX,
                'score': 100
            },
        ],
        'weight': 0.5,
        'type': 5,
    },
    '速动比率(%)': {
        'duration': [
            {
                'start': MIN,
                'end': 0,
                'score': 0
            },
            {
                'start': 0,
                'end': 50,
                'score': 40
            },
            {
                'start': 50,
                'end': 100,
                'score': 60
            },
            {
                'start': 100,
                'end': 150,
                'score': 80
            },
            {
                'start': 100,
                'end': MAX,
                'score': 100
            },
        ],
        'weight': 0.5,
        'type': 5,
    }
}

#######################################
CASH_ABILITY_WEIGHT = 0.35
BIZ_ABILITY_WEIGHT = 0.15
PROFIT_ABILITY_WEIGHT = 0.3
FINANCIAL_STRUCTURE_WEIGHT = 0.1
DEBT_PAYING_ABILITY_WEIGHT = 0.1
