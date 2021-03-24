from presenter.dash_app import *
from dash.dependencies import Input, Output
from constants.constant import *
import dash_core_components as dcc
import plotly.express as px


class BalancePt(object):
    def set_layout(self, df):
        add_layout([
            dcc.RangeSlider(
                id='balance_slider',
                min=df[BALANCE_COL_START].min().year,
                max=df[BALANCE_COL_START].max().year,
                value=[df[BALANCE_YEAR].min(), df[BALANCE_YEAR].max()],
                marks={str(ymd): str(ymd) for ymd in df[BALANCE_YEAR].unique()},
            ),
            dcc.Graph(id="balance"),
        ])

    def draw(self, df):
        @app.callback(Output("balance", "figure"), [Input("balance_slider", "value")])
        def monetary_fund_chart(date):
            data_col = '货币资金(万元)'
            fig = px.bar(df[(df[BALANCE_YEAR] >= date[0]) & (df[BALANCE_YEAR] <= date[1])], x=BALANCE_COL_START, y=data_col, color=data_col)
            fig.update_xaxes(tickangle=45, tickformat='%Y-%m-%d')
            return fig
