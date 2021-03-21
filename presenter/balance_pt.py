from dash_app import *
import plotly.express as px
from dash.dependencies import Input, Output
import dash_core_components as dcc
from repository.balance_repo import BalanceSheet
from constants.constant import *

df = BalanceSheet("../data/balance_sheet.csv").load().get_data()


class BalancePt(object):
    @staticmethod
    @app.callback(Output("balance", "figure"), [Input("balance_slider", "value")])
    def monetary_fund_chart(date):
        data_col = '货币资金(万元)'
        fig = px.bar(df[(df[BALANCE_YEAR] >= date[0]) & (df[BALANCE_YEAR] <= date[1])], x=BALANCE_COL_START, y=data_col, color=data_col)
        fig.update_xaxes(tickangle=45, tickformat='%Y-%m-%d')
        return fig


if __name__ == "__main__":
    add_layout([
        dcc.Graph(id="balance"),
        dcc.RangeSlider(
            id='balance_slider',
            min=df[BALANCE_COL_START].min().year,
            max=df[BALANCE_COL_START].max().year,
            value=[df[BALANCE_YEAR].min(), df[BALANCE_YEAR].max()],
            marks={str(ymd): str(ymd) for ymd in df[BALANCE_YEAR].unique()},
        ),
    ])
    app.run_server(debug=True)
