from dash import Dash
import dash_html_components as html

__CSS = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = Dash(__name__, external_stylesheets=__CSS)
app.layout = html.Div()
__children = []


def add_layout(layouts):
    if type(layouts) == list:
        __children.extend(layouts)
    else:
        __children.append(layouts)

    app.layout = html.Div(__children)


def clear_layout():
    global __children
    __children = []
