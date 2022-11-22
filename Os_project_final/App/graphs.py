import pandas as pd
import plotly_express as px
import os

class Graphs:

    def top_10_medals(self):

        data_folder = os.path.abspath("./Data")
        data_athletes = os.path.join(data_folder, "athlete_events.csv")
        df = pd.read_csv(data_athletes)
        df_gold = df[df.Medal == "Gold"]
        gold_series = df_gold.groupby("NOC").Medal.count().sort_values(ascending=False)
        df_silver = df[df.Medal == "Silver"]
        silver_series = df_silver.groupby("NOC").Medal.count().sort_values(ascending=False)
        df_bronze = df[df.Medal == "Bronze"]
        bronze_series = df_bronze.groupby("NOC").Medal.count().sort_values(ascending=False)
        medal_counts = pd.DataFrame({"Gold": gold_series, "Silver": silver_series, "Bronze": bronze_series})
        medal_counts.sort_values(by = "Gold", ascending=False).head(20)

        top_10 = medal_counts.sort_values(by = "Gold", ascending=False).head(10)
        return px.bar(top_10, barmode="group")

    def map_medals_Art_Competitions(self):

        data_folder = os.path.abspath("./Data")
        data_athletes = os.path.join(data_folder, "athlete_events.csv")
        df = pd.read_csv(data_athletes)

        df1 = df[df["Sport"] == "Art Competitions"]
        df1 = df1[df1.Medal.notna()]
        df1 = df1.groupby("NOC").Medal.count().reset_index(name="Total")

        df_iso = pd.read_html("https://www.worlddata.info/countrycodes.php")[0]
        df_iso.set_index("IOC", inplace=True)
        df_iso = df_iso.reset_index()
        df_iso = df_iso.rename(columns={"IOC": "NOC"})
        df_iso = df_iso[["NOC", "ISO 3166-1 alpha3"]]
        df_merge = df1.merge(df_iso)

        fig = px.choropleth(df_merge, locations="ISO 3166-1 alpha3", locationmode= "ISO-3",
                            color="Total",
                            hover_name="NOC",
                            color_continuous_scale="Viridis",
                            title="Art Competition - medals per country")
        
        return fig

    def map_medals_Ice_Hockey(self):

        data_folder = os.path.abspath("./Data")
        data_athletes = os.path.join(data_folder, "athlete_events.csv")
        df = pd.read_csv(data_athletes)

        df1 = df[df["Sport"] == "Ice Hockey"]
        df1 = df1[df1.Medal.notna()]
        df1 = df1.groupby("NOC").Medal.count().reset_index(name="Total")

        df_iso = pd.read_html("https://www.worlddata.info/countrycodes.php")[0]
        df_iso.set_index("IOC", inplace=True)
        df_iso = df_iso.reset_index()
        df_iso = df_iso.rename(columns={"IOC": "NOC"})
        df_iso = df_iso[["NOC", "ISO 3166-1 alpha3"]]
        df_merge = df1.merge(df_iso)

        fig = px.choropleth(df_merge, locations="ISO 3166-1 alpha3", locationmode= "ISO-3",
                            color="Total",
                            hover_name="NOC",
                            color_continuous_scale="Viridis",
                            title="Ice Hockey - medals per country")
        
        return fig