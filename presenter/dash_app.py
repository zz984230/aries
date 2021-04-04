from dash import Dash
import dash_html_components as html

# __CSS = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
__CSS = "https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css"
app = Dash(external_stylesheets=[__CSS])
__children = []


def add_layout(layouts):
    if type(layouts) == list:
        __children.extend(layouts)
    else:
        __children.append(layouts)


def render():
    app.layout = html.Div(__children)


def show_children():
    print(__children)


def clear_layout():
    global __children
    __children = []
