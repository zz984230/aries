from presenter.dash_app import *
from dash.dependencies import Input, Output, State
import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc
import plotly.graph_objs as go


class ValuationPt(object):
    def __init__(self):
        self.__half_left_width_stl = dict(width='50%', float='left')
        self.__half_right_width_stl = dict(width='50%', float='right')

    def set_layout(self):
        return html.Div([
            html.Div([
                dbc.Input(id='valuation_input', placeholder="Input goes here...", value='贵州茅台', type="text",
                          style={"width": 200, 'float': 'left'}),
                dbc.Button("Search", color="secondary", id='valuation_button', className="me-1"),
            ]),
            html.Div([
                dcc.Markdown(f"### 价格与估值"),
                dcc.Graph(id="valuation1"),
            ], style=self.__half_left_width_stl),
            html.Div([
                dcc.Markdown(f"### ROIC vs WACC"),
                dcc.Graph(id="valuation2"),
            ], style=self.__half_left_width_stl),
            html.Div([
                dcc.Markdown(f"### ROE"),
                dcc.Graph(id="valuation3"),
            ], style=self.__half_left_width_stl),
        ])

    def render(self, repo):
        @app.callback([Output("valuation2", "figure"), Output("valuation3", "figure")],
                      [Input("valuation_button", "n_clicks"), State("valuation_input", "value")])
        def roic_chart(n_clicks, value):
            df = repo.set_stock_name(value).load_roic().get_roic_data()
            cols = list(df.columns)

            fig = go.Figure(
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
            fig.add_trace(go.Scatter(x=df[cols[0]], y=df[cols[-1]], name=cols[-1], marker={'color': '#6495ED'}))
            fig.add_trace(go.Bar(x=df[cols[0]], y=df[cols[1]], name=cols[1], marker={'color': '#F08080'}))
            fig.add_trace(go.Bar(x=df[cols[0]], y=-df[cols[2]], name=cols[2], marker={'color': '#66CDAA'}))

            fig.update_layout(barmode='relative')

            fig2 = go.Figure(
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
            fig2.add_trace(go.Bar(x=df[cols[0]], y=df[cols[3]], name=cols[3], marker={'color': '#F08080'}))

            return fig, fig2

        @app.callback(Output("valuation1", "figure"),
                      [Input("valuation_button", "n_clicks"), State("valuation_input", "value")])
        def valuation_chart(n_clicks, value):
            df = repo.set_stock_name(value).load_valuation().get_valuation_data()
            cols = list(df.columns)
            fig = go.Figure(
                [
                    go.Scatter(
                        name='Upper Bound',
                        x=df[cols[0]],
                        y=df[cols[2]] * 1.3,
                        mode='lines',
                        marker=dict(color="#F08080"),
                        line=dict(width=1),
                        showlegend=False
                    ),
                    go.Scatter(
                        name='估值',
                        x=df[cols[0]],
                        y=df[cols[2]],
                        mode='lines',
                        line=dict(color='#696969'),
                        fillcolor='rgba(255, 228, 225, 0.5)',
                        fill='tonexty',
                    ),
                    go.Scatter(
                        name='Lower Bound',
                        x=df[cols[0]],
                        y=df[cols[2]] * 0.7,
                        marker=dict(color="#32CD32"),
                        line=dict(width=1),
                        mode='lines',
                        fillcolor='rgba(144, 238, 144, 0.3)',
                        fill='tonexty',
                        showlegend=False
                    ),
                    go.Scatter(
                        name='价格',
                        x=df[cols[0]],
                        y=df[cols[1]],
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
