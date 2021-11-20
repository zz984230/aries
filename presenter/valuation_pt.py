from presenter.dash_app import *
from dash.dependencies import Input, Output, State
import dash_html_components as html
import dash_core_components as dcc
import plotly.express as px
import plotly.graph_objs as go
import pandas as pd


class ValuationPt(object):
    def __init__(self):
        self.__half_left_width_stl = dict(width='50%', float='left')
        self.__half_right_width_stl = dict(width='50%', float='right')
        self.__df = pd.DataFrame()
        self.__cols = []
        self.__stock_name = ""

    def init_data(self, df, cols, stock_name):
        self.__df = df
        self.__cols = cols
        self.__stock_name = stock_name

    def set_layout(self):
        return html.Div([
            html.Div([
                dcc.Markdown(f"### 价格与估值"),
                dcc.Input(id='valuation_input', value='贵州茅台', type='text'),
                html.Button('Search', id='valuation_button', n_clicks=0),
                dcc.Graph(id="valuation1"),
            ], style=self.__half_left_width_stl),
        ])

    def render(self, repo):
        @app.callback(Output("valuation1", "figure"),
                      [Input("valuation_button", "n_clicks"), State("valuation_input", "value")])
        def floating_valuation_chart2(n_clicks, value):
            df = repo.set_stock_name(value).load().get_data()
            fig = go.Figure(
                [
                    go.Scatter(
                        name='Upper Bound',
                        x=df[self.__cols[0]],
                        y=df[self.__cols[2]] * 1.3,
                        mode='lines',
                        marker=dict(color="#F08080"),
                        line=dict(width=1),
                        showlegend=False
                    ),
                    go.Scatter(
                        name='估值',
                        x=df[self.__cols[0]],
                        y=df[self.__cols[2]],
                        mode='lines',
                        line=dict(color='#696969'),
                        fillcolor='rgba(255, 228, 225, 0.5)',
                        fill='tonexty',
                    ),
                    go.Scatter(
                        name='Lower Bound',
                        x=df[self.__cols[0]],
                        y=df[self.__cols[2]] * 0.7,
                        marker=dict(color="#32CD32"),
                        line=dict(width=1),
                        mode='lines',
                        fillcolor='rgba(144, 238, 144, 0.3)',
                        fill='tonexty',
                        showlegend=False
                    ),
                    go.Scatter(
                        name='价格',
                        x=df[self.__cols[0]],
                        y=df[self.__cols[1]],
                        mode='lines',
                        line=dict(color='#6495ED'),
                    )
                ],
                layout={
                    "template": "plotly_white",
                    "title": {
                        "text": value,
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
                hovermode="x"
            )
            return fig
