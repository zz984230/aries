from dash_app import *
import plotly.express as px


class BalancePt(object):
    def __init__(self, df, dim):
        self.__df = df
        self.__dim = dim

    @app.callback()
    def update_bar_chart(self, dims):
        return px.scatter_matrix(self.__df, dimensions=dims)
