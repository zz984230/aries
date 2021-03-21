from presenter.dash_app import *
from dash.dependencies import Input, Output
from constants.constant import *
import plotly.express as px


class BalancePt(object):
    def draw(self, df):
        @app.callback(Output("balance", "figure"), [Input("balance_slider", "value")])
        def monetary_fund_chart(date):
            data_col = '货币资金(万元)'
            fig = px.bar(df[(df[BALANCE_YEAR] >= date[0]) & (df[BALANCE_YEAR] <= date[1])], x=BALANCE_COL_START, y=data_col, color=data_col)
            fig.update_xaxes(tickangle=45, tickformat='%Y-%m-%d')
            return fig
