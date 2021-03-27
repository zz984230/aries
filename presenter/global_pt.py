from presenter.dash_app import *
from constants.colors import *
import dash_bootstrap_components as dbc
import dash_html_components as html


class GlobalPt(object):
    def __init__(self):
        self.__left_layout = dbc.Col(children=html.Div(), width=2, style=dict(background=SILVER))
        self.__right_layout = dbc.Col(id='right_layout')

    def set_global_layout(self):
        add_layout(html.Div(
            children=[
                dbc.Row(
                    [
                        self.__left_layout,
                        self.__right_layout,
                    ]
                )
            ],
        ))

        return self

    def set_left_layout(self):
        pass

    def get_left_div(self):
        return self.__left_layout

    def get_right_div(self):
        return self.__right_layout
