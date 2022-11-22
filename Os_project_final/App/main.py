import dash
import os
from dash.dependencies import Output, Input
import plotly_express as px
import pandas as pd
import dash_bootstrap_components as dbc
from dash import html
from layout_copy import Layout
from graphs import Graphs


app = dash.Dash(
    __name__,
    external_stylesheets=[dbc.themes.MATERIA],
    meta_tags=[
        dict(name="viewport", content="width=device-width, initial-scale=1.0")],
)

app.layout = Layout().layout()

@app.callback(Output("graph","figure"),Input("gb-dropdown", "value"))
def update_left_graph(option):
    if option == "medals":
        return Graphs().top_ten_gb()
    elif option == "medals_os":
        return Graphs().gb_years_medal()
    elif option == "age":
        return Graphs().gb_age()

@app.callback(Output("graph-down", "figure"), Input("world-dropdown", "value"))
def update_right_graph(option):
    if option == "top_ten_medals":
        return Graphs().top_10_medals()
    elif option == "art_comp":
        return Graphs().map_medals_Art_Competitions()
    elif option == "ice_hockey":
        return Graphs().map_medals_Ice_Hockey()

    



if __name__ == "__main__":
    app.run_server(debug=True)
