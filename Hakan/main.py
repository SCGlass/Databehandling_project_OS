from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd
import os

df = pd.read_csv("Data/athlete_events.csv")

df_gold = df[df.Medal == "Gold"]
gold_series = df_gold.groupby("NOC").Medal.count().sort_values(ascending=False)

df_silver = df[df.Medal == "Silver"]
silver_series = df_silver.groupby("NOC").Medal.count().sort_values(ascending=False)

df_bronze = df[df.Medal == "Bronze"]
bronze_series = df_bronze.groupby("NOC").Medal.count().sort_values(ascending=False)

medal_counts = pd.DataFrame({"Gold": gold_series, "Silver": silver_series, "Bronze": bronze_series})
medal_counts.sort_values(by = "Gold", ascending=False).head(20)

top_10 = medal_counts.sort_values(by = "Gold", ascending=False).head(10)


app = Dash(__name__)

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options

fig = px.bar(top_10, barmode="group")

app.layout = html.Div(children=[
    html.H1(children='Hello Dash'),

    html.Div(children='''
        Dash: A web application framework for your data.
    '''),

    dcc.Graph(
        id='example-graph',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)