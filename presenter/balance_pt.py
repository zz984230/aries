from dash_app import *
import plotly.express as px
from dash.dependencies import Input, Output
import dash_core_components as dcc
from repository.balance_repo import BalanceSheet

df = BalanceSheet("../data/balance_sheet.csv").load().get_data(['报告日期', '货币资金(万元)'])


class BalancePt(object):
    @staticmethod
    @app.callback(Output("balance", "figure"), [Input("dropdown", "value")])
    def update_bar_chart(self):
        return px.line(df, x='报告日期', y='货币资金(万元)')


if __name__ == "__main__":
    add_layout([
        dcc.Graph(id="balance"),
        dcc.Dropdown(
            id="dropdown",
            options=[{"label": x, "value": x} for x in df['报告日期']],
            value=df['报告日期'][:2],
            multi=True
        ),
    ])
    app.run_server(debug=True)
