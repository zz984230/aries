from presenter.dash_app import *
from dash.dependencies import Input, Output, State
import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc
import plotly.express as px
import plotly.graph_objs as go


class CloudPt(object):
    def __init__(self):
        self.__color = [
            '#ff7575',
            '#FF9797',
            '#FFB5B5',
            '#FFD2D2',
            '#FFECEC',
            '#D1E9E9',
            '#C4E1E1',
            '#B3D9D9',
            '#A3D1D1',
            '#95CACA']

    def set_layout(self):
        return html.Div([
            dcc.Markdown(f"### 大盘云图"),
            dbc.Input(id='cloud_input', placeholder="Input goes here...", value=3e+10, type="text",
                      style={"width": 200, 'float': 'left'}),
            dbc.Button("Show Cloud Figure", color="secondary", id='cloud_button', className="me-1"),
            dcc.Graph(id="cloud1"),
        ])

    def render(self, repo):
        @app.callback(Output("cloud1", "figure"),
                      [Input("cloud_button", "n_clicks"), State("cloud_input", "value")])
        def cloud_chart(n_clicks, market_value):
            df = repo.load_cloud().get_cloud_data()
            col_sector, col_group, col_company, col_rise_fall, col_market_value, col_color = list(df.columns)
            df = df[df[col_market_value] >= market_value]

            fig = px.treemap(df,
                             path=[col_sector, col_group, col_company],
                             values=col_market_value,
                             color=col_color,
                             color_continuous_midpoint=0.0,
                             color_continuous_scale=self.__color[::-1],
                             maxdepth=3)
            fig.update_layout(
                margin=dict(t=50, l=25, r=25, b=25),
                width=1600,
                height=800,
            )

            return fig
