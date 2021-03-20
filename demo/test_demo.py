# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

from dash import Dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = Dash(__name__, external_stylesheets=external_stylesheets)

markdown_text = '''
### Dash and Markdown

Dash apps can be written in Markdown.
Dash uses the [CommonMark](http://commonmark.org/)
specification of Markdown.
Check out their [60 Second Markdown Tutorial](http://commonmark.org/help/)
if this is your first introduction to Markdown!
'''

all_dims = ['sepal_length', 'sepal_width',
            'petal_length', 'petal_width']

app.layout = html.Div([
    dcc.Markdown(children=markdown_text),
    dcc.Dropdown(
        id="dropdown",
        options=[{"label": x, "value": x} for x in all_dims],
        value=all_dims[:2],
        multi=True
    ),
    dcc.Graph(id="splom"),
])

df = px.data.iris()


@app.callback(Output("splom", "figure"), [Input("dropdown", "value")])
def update_bar_chart(dims):
    fig = px.scatter_matrix(df, dimensions=dims, color="species")
    return fig


if __name__ == '__main__':
    a = "Aaa"
    print(f"{a}:vvv")
    app.run_server(debug=True)
