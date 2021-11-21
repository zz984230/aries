from presenter.dash_app import *
from constants.colors import *
from dash.dependencies import Input, Output
import dash
import dash_bootstrap_components as dbc
import dash_html_components as html


class GlobalPt(object):
    def __init__(self, logo_file, bg_file, balance_pt, valuation_pt, cloud_pt):
        self.__logo_file = logo_file
        self.__bg_file = bg_file
        self.__labels = ['资产负债表', '利润表', '现金流量表', '价值投资']
        self.__button_group = []
        self.__clicked_button_id = ""
        self.__balance_pt = balance_pt
        self.__valuation_pt = valuation_pt
        self.__cloud_pt = cloud_pt

    def __init_layout(self):
        self.__left_layout = dbc.Col(id='left_layout', xs=1, style=dict(background=GAINSBORO))
        self.__right_layout = dbc.Col(
            html.Img(
                src=self.__bg_file,
                style={"position": "absolute", "top": "25%", "left": "30%"}
            ),
            id='right_layout',
            style=dict(background=WHITE_SMOKE),
        )

    def set_global_layout(self):
        self.__init_layout()
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
                    ],
                    style=dict(height="850px")
                )
            ],
        ))

        return self

    def __set_each_left_layout(self, i, button_group):
        return dbc.Row(
            [
                dbc.Button(self.__labels[i], id=f"collapse-button-{i}", color="dark", outline=True, block=True,
                           style={"border-style": "none"}),
                dbc.Collapse(button_group, id=f"collapse-{i}", style={"width": "100%"})
            ]
        )

    def set_left_layout(self):
        self.__button_group = [
            [
                dbc.Button("资产", id="balance-collapse-0", block=True),
                dbc.Button("负债", id="balance-collapse-1", block=True),
                dbc.Button("股东权益", id="balance-collapse-2", block=True),
            ],
            [
                dbc.Button("收入", id="profit-collapse-0", block=True),
                dbc.Button("成本", id="profit-collapse-1", block=True),
                dbc.Button("利润", id="profit-collapse-2", block=True),
                dbc.Button("每股权益", id="profit-collapse-3", block=True),
            ],
            [
                dbc.Button("经营活动", id="cash-flow-collapse-0", block=True),
                dbc.Button("投资活动", id="cash-flow-collapse-1", block=True),
                dbc.Button("筹资活动", id="cash-flow-collapse-2", block=True),
                dbc.Button("其他", id="cash-flow-collapse-3", block=True),
            ],
            [
                dbc.Button("股票估值", id="valuation-collapse-0", block=True),
                dbc.Button("大盘云图", id="valuation-collapse-1", block=True),
            ]
        ]

        self.__left_layout.children = [
            self.__set_each_left_layout(i, dbc.ButtonGroup(
                self.__button_group[i],
                vertical=True,
                style={"width": "inherit"}
            )) for i in range(len(self.__labels))
        ]
        return self

    def get_left_div(self):
        return self.__left_layout

    def get_right_div(self):
        return self.__right_layout

    def render(self):
        @app.callback(Output("right_layout", "children"),
                      [Input("balance-collapse-0", "active"),
                       Input("valuation-collapse-0", "active"),
                       Input("valuation-collapse-1", "active")])
        def set_score_layout(kind_active, valuation_active, cloud_active):
            ctx = dash.callback_context
            if not ctx.triggered:
                return self.__right_layout.children
            else:
                button_id = ctx.triggered[0]["prop_id"].split(".")[0]

            if kind_active and button_id.startswith("balance-collapse"):
                return self.__balance_pt.set_layout()
            elif button_id.startswith("valuation-collapse-0"):
                if valuation_active:
                    return self.__valuation_pt.set_layout()
                elif cloud_active:
                    return self.__cloud_pt.set_layout()

            return self.__right_layout.children

        @app.callback([Output(f"valuation-collapse-{i}", "active") for i in range(len(self.__button_group[3]))],
                      [Input(f"valuation-collapse-{i}", "n_clicks") for i in range(len(self.__button_group[3]))])
        def valuation_button_click(*args):
            ctx = dash.callback_context
            if not ctx.triggered:
                return [False for _ in range(len(args))]
            else:
                button_id = ctx.triggered[0]["prop_id"].split(".")[0]

            index = 0
            for k, v in enumerate(args):
                if v and button_id == f"valuation-collapse-{k}":
                    index = k

            return [True if index == i else False for i in range(len(args))]

        @app.callback([Output(f"balance-collapse-{i}", "active") for i in range(len(self.__button_group[0]))],
                      [Input(f"balance-collapse-{i}", "n_clicks") for i in range(len(self.__button_group[0]))])
        def balance_button_click(*args):
            ctx = dash.callback_context
            if not ctx.triggered:
                return [False for _ in range(len(args))]
            else:
                button_id = ctx.triggered[0]["prop_id"].split(".")[0]

            index = 0
            for k, v in enumerate(args):
                if v and button_id == f"balance-collapse-{k}":
                    index = k

            return [True if index == i else False for i in range(len(args))]

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

        @app.callback([Output(f"collapse-{i}", "is_open") for i in range(len(self.__labels))],
                      [Input(f"collapse-button-{i}", "n_clicks") for i in range(len(self.__labels))])
        def collapse(*args):
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
