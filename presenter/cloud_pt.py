from presenter.dash_app import *
from dash.dependencies import Input, Output, State
import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc
import plotly.express as px


class CloudPt(object):
    def __init__(self):
        self.__color = [
            '#FF2D2D',
            '#ff7575',
            '#FFFFFF',
            '#95CACA',
            '#6FB7B7']

    def set_layout(self):
        return html.Div([
            dcc.Markdown(f"### 大盘云图"),
            dbc.Input(id='cloud_input', placeholder="Input goes here...", value=1e+5, type="text",
                      style={"width": 200, 'float': 'left'}),
            dbc.Button("Show Cloud Figure", color="secondary", id='cloud_button', className="me-1"),
            dcc.Graph(id="cloud1"),
        ])

    def render(self, repo):
        @app.callback(Output("cloud1", "figure"),
                      [Input("cloud_button", "n_clicks"), State("cloud_input", "value")])
        def cloud_chart(n_clicks, market_value):
            df = repo.load_cloud().get_cloud_data()
            col_sector, col_group, col_company, col_rise_fall, col_market_value = list(df.columns)
            df = df[df[col_market_value] >= market_value]

            fig = px.treemap(df,
                             path=[col_sector, col_group, col_company],
                             values=col_market_value,
                             labels=col_company,
                             color=col_rise_fall,
                             color_continuous_midpoint=0.0,
                             color_continuous_scale=self.__color[::-1],
                             maxdepth=3)
            fig.update_traces(textfont=dict(size=15),
                              texttemplate='%{label}<br>%{customdata:.2f}%',
                              textposition='middle center')
            fig.update_layout(
                margin=dict(t=50, l=25, r=25, b=25),
                width=1600,
                height=800,
            )

            return fig
