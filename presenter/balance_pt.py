from presenter.dash_app import *
from dash.dependencies import Input, Output
from constants.constant import *
import dash_html_components as html
import dash_core_components as dcc
import plotly.express as px
import pandas as pd


class BalancePt(object):
    def __init__(self, base_layout):
        self.__base_layout = base_layout
        self.__half_left_width_stl = dict(width='50%', float='left')
        self.__half_right_width_stl = dict(width='50%', float='right')
        self.__df = pd.DataFrame()
        self.__cols = []

    def init_data(self, df, cols):
        self.__df = df
        self.__cols = cols

    def __set_layout(self):
        return html.Div([
            dcc.Markdown("# 资产负债表"),
            dcc.Markdown("## 1. 基本信息"),
            html.Div([
                dcc.Markdown("### 流动资产信息"),
                dcc.RangeSlider(
                    id='balance_slider1',
                    min=self.__df[BALANCE_COL_START].min().year,
                    max=self.__df[BALANCE_COL_START].max().year,
                    value=[self.__df[BALANCE_YEAR].min(), self.__df[BALANCE_YEAR].max()],
                    marks={str(ymd): str(ymd) for ymd in self.__df[BALANCE_YEAR].unique()},
                ),
                dcc.Dropdown(
                    id='balance_dropdown1',
                    options=[{'label': c, 'value': c} for c in self.__cols[:24]],
                    value=self.__cols[0],
                    multi=False),
                dcc.Graph(id="balance1"),
                dcc.Graph(id="balance1_1"),
            ], style=self.__half_left_width_stl),
            html.Div([
                dcc.Markdown("### 非流动资产信息"),
                dcc.RangeSlider(
                    id='balance_slider2',
                    min=self.__df[BALANCE_COL_START].min().year,
                    max=self.__df[BALANCE_COL_START].max().year,
                    value=[self.__df[BALANCE_YEAR].min(), self.__df[BALANCE_YEAR].max()],
                    marks={str(ymd): str(ymd) for ymd in self.__df[BALANCE_YEAR].unique()},
                ),
                dcc.Dropdown(
                    id='balance_dropdown2',
                    options=[{'label': c, 'value': c} for c in self.__cols[25:51]],
                    value=self.__cols[25],
                    multi=False),
                dcc.Graph(id="balance2"),
                dcc.Graph(id="balance2_1"),
            ], style=self.__half_right_width_stl),
        ])

    def render(self, df):
        @app.callback(Output("right_layout", "children"),
                      Input("balance-collapse-0", "active"))
        def set_balance_layout(active):
            children = self.__set_layout()
            if active:
                return children

            return self.__base_layout.children

        @app.callback(Output("balance1", "figure"),
                      [Input("balance_slider1", "value"), Input("balance_dropdown1", "value")])
        def floating_assets_chart(date, data_col):
            fig = px.bar(df[(df[BALANCE_YEAR] >= date[0]) & (df[BALANCE_YEAR] <= date[1])], x=BALANCE_COL_START,
                         y=data_col, color=data_col)
            fig.update_xaxes(tickangle=45, tickformat='%Y-%m-%d')
            return fig

        @app.callback(Output("balance1_1", "figure"), [Input("balance_slider1", "value")])
        def floating_assets_all_chart(date):
            fig = px.bar(df[(df[BALANCE_YEAR] >= date[0]) & (df[BALANCE_YEAR] <= date[1])], x=BALANCE_COL_START,
                         y=BALANCE_FLOW_ASSETS_ALL, color=BALANCE_FLOW_ASSETS_ALL)
            fig.update_xaxes(tickangle=45, tickformat='%Y-%m-%d')
            return fig

        @app.callback(Output("balance2", "figure"),
                      [Input("balance_slider2", "value"), Input("balance_dropdown2", "value")])
        def fixed_assets_chart(date, data_col):
            fig = px.bar(df[(df[BALANCE_YEAR] >= date[0]) & (df[BALANCE_YEAR] <= date[1])], x=BALANCE_COL_START,
                         y=data_col, color=data_col)
            fig.update_xaxes(tickangle=45, tickformat='%Y-%m-%d')
            return fig

        @app.callback(Output("balance2_1", "figure"), [Input("balance_slider2", "value")])
        def fixed_assets_all_chart(date):
            fig = px.bar(df[(df[BALANCE_YEAR] >= date[0]) & (df[BALANCE_YEAR] <= date[1])], x=BALANCE_COL_START,
                         y=BALANCE_FIXED_ASSETS_ALL, color=BALANCE_FIXED_ASSETS_ALL)
            fig.update_xaxes(tickangle=45, tickformat='%Y-%m-%d')
            return fig
