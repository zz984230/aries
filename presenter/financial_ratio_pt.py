from presenter.dash_app import *
from dash.dependencies import Input, Output, State
from constants.financial_ratio_map import *
import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd
import numpy as np

pd.set_option('display.max_columns', None)


class FinancialRatioPt(object):
    def __init__(self):
        self.__half_left_width_stl = dict(width='50%', float='left')
        self.__half_right_width_stl = dict(width='50%', float='right')
        self.__theta = ['现金能力', '经营能力', '盈利能力', '财务结构', '偿债能力']

    def set_layout(self):
        return html.Div([
            html.Div([
                dbc.Input(id='financial_ratio_input', placeholder="Input goes here...", value='贵州茅台', type="text",
                          style={"width": 200, 'float': 'left'}),
                dbc.Button("Search", color="secondary", id='financial_ratio_button', className="me-1"),
            ]),
            html.Div([
                dcc.Markdown(f"### 财务比率评分"),
                dcc.Tabs(id="financial_tabs", value='tab-0'),
            ], style=self.__half_left_width_stl),
        ])

    def render(self, repo):
        def cal_financial_ratio_detail_score(ori_df):
            cols = list(ori_df.columns)
            ori_df['type'] = 1
            ori_df['weight'] = 0.0
            for typ in ori_df[cols[0]]:
                for c in cols[1:]:
                    if typ not in ABILITY:
                        continue

                    duration_list = ABILITY[typ]['duration']
                    for obj in duration_list:
                        if obj['start'] <= float(ori_df[ori_df[cols[0]] == typ][c]) < obj['end']:
                            ori_df.loc[ori_df[cols[0]] == typ, c] = obj['score']
                            ori_df.loc[ori_df[cols[0]] == typ, 'type'] = ABILITY[typ]['type']
                            ori_df.loc[ori_df[cols[0]] == typ, 'weight'] = ABILITY[typ]['weight']
                            break

            return ori_df

        def cal_financial_ratio_score(ori_df):
            cols = list(ori_df.columns)
            for c in cols[1:6]:
                ori_df[f'{c}_score'] = np.array(ori_df[c]) * np.array(ori_df['weight'])

            return ori_df.groupby('type').sum()

        @app.callback(Output('financial_tabs', 'children'),
                      [Input("financial_ratio_button", "n_clicks"), State("financial_ratio_input", "value")])
        def financial_ratio_tabs(n_clicks, value):
            try:
                ori_df = repo.set_stock_name(value).load_financial().get_financial_data()
                cols = list(ori_df.columns)
                print(ori_df)
                df = cal_financial_ratio_detail_score(ori_df)
                print(df)
                df_group_by_type = cal_financial_ratio_score(df)
                print()
                print(df_group_by_type)
                children = [dcc.Tab(label=v, value=f'tab-{k}', children=[
                    dcc.Graph(figure=px.line_polar(r=list(df_group_by_type[f'{v}_score']), theta=self.__theta,
                                                   color_discrete_sequence=px.colors.sequential.Plasma_r,
                                                   template="plotly_dark",
                                                   title=value,
                                                   range_r=[0, 100], line_close=True).update_traces(fill='toself')),
                ]) for k, v in enumerate(cols[1:6])]
            except Exception as e:
                print(e)
                print(ori_df)
            return children
