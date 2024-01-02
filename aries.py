from configs.config import Config
from presenter.dash_app import *
from presenter.global_pt import GlobalPt
from usecase.balance.balance_uc import BalanceUc
from usecase.valuation.valuation_uc import ValuationUc
from usecase.valuation.cloud_uc import CloudUc
from usecase.valuation.financial_ratio_uc import FinancialRatioUc
from presenter.balance_pt import BalancePt
from presenter.valuation_pt import ValuationPt
from presenter.cloud_pt import CloudPt
from presenter.financial_ratio_pt import FinancialRatioPt
import fire


class Program(object):
    def __init__(self):
        self.__cfg = Config()

    def __init(self):
        self.__cfg.init()
        balance_pt = BalancePt()
        valuation_pt = ValuationPt()
        cloud_pt = CloudPt()
        financial_pt = FinancialRatioPt()

        self.__global_pt = GlobalPt(self.__cfg.logo_file, self.__cfg.bg_file, balance_pt, valuation_pt, cloud_pt,
                                    financial_pt).set_global_layout().set_left_layout().render()

        self.__balance_uc = BalanceUc(self.__cfg, balance_pt)
        self.__valuation_uc = ValuationUc(valuation_pt)
        self.__cloud_uc = CloudUc(cloud_pt)
        self.__financial_uc = FinancialRatioUc(financial_pt)

    def start(self):
        self.__init()
        print("Good")
        self.__balance_uc.run()
        self.__valuation_uc.run()
        self.__cloud_uc.run()
        self.__financial_uc.run()
        render()
        app.run_server(debug=True)


def gen_once(values):
    from repository.valuation_repo import ValuationSheet
    import plotly.graph_objs as go
    from utils.util import Util
    import time

    def gen(value):
        repo = ValuationSheet(value)
        df = repo.set_stock_name(value).load_valuation().get_valuation_data()
        df.dropna(inplace=True)
        cols = list(df.columns)
        fig = go.Figure(
            [
                go.Scatter(
                    name='Upper Bound',
                    x=df[cols[0]],
                    y=df[cols[2]] * 1.3,
                    mode='lines',
                    marker=dict(color="#F08080"),
                    line=dict(width=1),
                    showlegend=False
                ),
                go.Scatter(
                    name='估值',
                    x=df[cols[0]],
                    y=df[cols[2]],
                    mode='lines',
                    line=dict(color='#696969'),
                    fillcolor='rgba(255, 228, 225, 0.5)',
                    fill='tonexty',
                ),
                go.Scatter(
                    name='Lower Bound',
                    x=df[cols[0]],
                    y=df[cols[2]] * 0.7,
                    marker=dict(color="#32CD32"),
                    line=dict(width=1),
                    mode='lines',
                    fillcolor='rgba(144, 238, 144, 0.3)',
                    fill='tonexty',
                    showlegend=False
                ),
                go.Scatter(
                    name='价格',
                    x=df[cols[0]],
                    y=df[cols[1]],
                    mode='lines',
                    line=dict(color='#6495ED'),
                )
            ],
            layout={
                "template": "plotly_white",
                "title": {
                    "text": value.strip('%20'),
                    "x": 0.5,
                    "font": {
                        "family": "Courier New",
                        "size": 30,
                    },
                }
            },
        )
        fig.update_layout(
            yaxis_title='单位：元',
            hovermode="x",
            width=1280,
            height=800,
            # xaxis_title_text="记录投资点滴，不构成投资建议",
        )
        fig.write_image(f"./data/batch/{value.strip('%20')}.png")
        time.sleep(2)

    for v in Util.strip(values).split(','):
        gen(v)


if __name__ == "__main__":
    # fire.Fire(Program)
    gen_once('曼恩斯特')