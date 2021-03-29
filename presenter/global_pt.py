from presenter.dash_app import *
from constants.colors import *
from dash.dependencies import Input, Output
import dash
import dash_bootstrap_components as dbc
import dash_html_components as html


class GlobalPt(object):
    def __init__(self, logo_file):
        self.__left_layout = dbc.Col(id='left_layout', xs=1, style=dict(background=GAINSBORO))
        self.__right_layout = dbc.Col(id='right_layout', style=dict(background=WHITE_SMOKE))
        self.__labels = ['资产负债表', '利润表', '现金流量表']
        self.__logo_file = logo_file

    def set_global_layout(self):
        add_layout(html.Div(
            children=[
                dbc.Row(
                    dbc.Navbar(
                        [
                            dbc.Col(html.Img(src=self.__logo_file, height="40px")),
                            dbc.Col(dbc.NavbarBrand("Aries")),
                            dbc.Col()
                        ],
                        color=LIMBO_BLACK,
                        dark=True,
                    ),
                    style=dict(background=LIMBO_BLACK)
                ),
                dbc.Row(
                    [
                        self.__left_layout,
                        self.__right_layout,
                    ]
                )
            ],
        ))

        return self

    def __set_each_left_layout(self, num):
        return [
            dbc.Row(
                [
                    dbc.Button(self.__labels[i], id=f"collapse-button-{i}", color="dark", outline=True, block=True, style={"border-style": "none"}),
                    dbc.Collapse(dbc.CardBody(f"This is the content of group {i}..."), id=f"collapse-{i}")
                ]
            ) for i in range(num)
        ]

    def set_left_layout(self):
        self.__left_layout.children = self.__set_each_left_layout(len(self.__labels))
        return self

    def get_left_div(self):
        return self.__left_layout

    def get_right_div(self):
        return self.__right_layout

    def render(self):
        @app.callback([Output(f"collapse-button-{i}", "active") for i in range(len(self.__labels))],
                      [Input(f"collapse-button-{i}", "n_clicks") for i in range(len(self.__labels))])
        def click(*args):
            ctx = dash.callback_context
            if not ctx.triggered:
                return [False for _ in range(len(args))]
            else:
                button_id = ctx.triggered[0]["prop_id"].split(".")[0]

            index = 0
            for k, v in enumerate(args):
                if v and button_id == f"collapse-button-{k}":
                    index = k

            return [True if index == i else False for i in range(len(args))]

        return self
