import dash
import os
from dash.dependencies import Output, Input
import plotly_express as px
import pandas as pd
import dash_bootstrap_components as dbc
from dash import html
from layout import Layout
from graphs import Graphs


app = dash.Dash(
    __name__,
    external_stylesheets=[dbc.themes.MATERIA],
    meta_tags=[dict(name="viewport", content="width=device-width, initial-scale=1.0")],
)

app.layout = Layout().layout()




@app.callback(Output("graph", "figure"), Input("GB_dropdown", "value"))
def update_left_graph(option):
    if option == "top_ten_medals":
        return Graphs().top_10_medals()
    elif option == "sport_statistics":
        return Graphs().sport_statistics()





if __name__ == "__main__":
    app.run_server(debug=True)