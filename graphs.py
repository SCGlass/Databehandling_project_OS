import pandas as pd
import plotly_express as px
import os


class Graphs:

    def top_10_medals(self):

        data_folder = os.path.abspath("./Data")
        data_athletes = os.path.join(data_folder, "athlete_events.csv")
        df = pd.read_csv(data_athletes)
        df_gold = df[df.Medal == "Gold"]
        gold_series = df_gold.groupby(
            "NOC").Medal.count().sort_values(ascending=False)
        df_silver = df[df.Medal == "Silver"]
        silver_series = df_silver.groupby(
            "NOC").Medal.count().sort_values(ascending=False)
        df_bronze = df[df.Medal == "Bronze"]
        bronze_series = df_bronze.groupby(
            "NOC").Medal.count().sort_values(ascending=False)
        medal_counts = pd.DataFrame(
            {"Gold": gold_series, "Silver": silver_series, "Bronze": bronze_series})
        medal_counts.sort_values(by="Gold", ascending=False).head(20)

        top_10 = medal_counts.sort_values(by="Gold", ascending=False).head(10)
        return px.bar(top_10, barmode="group", title="Top ranking countries medal count")

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

        fig = px.choropleth(df_merge, locations="ISO 3166-1 alpha3", locationmode="ISO-3",
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

        fig = px.choropleth(df_merge, locations="ISO 3166-1 alpha3", locationmode="ISO-3",
                            color="Total",
                            hover_name="NOC",
                            color_continuous_scale="Viridis",
                            title="Ice Hockey - medals per country")

        return fig

    def top_ten_gb(self):
        data_folder = os.path.abspath("./Data")
        data_athletes = os.path.join(data_folder, "athlete_events.csv")
        df = pd.read_csv(data_athletes)

        df = df[df["Team"] == "Great Britain"]
        df = df.loc[df["Medal"].notna(), ["Sport", "Medal"]]
        df = df.groupby(["Sport", "Medal"]).Medal.count(
        ).reset_index(name="Total")
        df = df.set_index(['Sport', 'Medal']).unstack('Medal', fill_value=0)
        df.columns = df.columns.droplevel(0)  # Dropped the Total index column
        df = df.rename_axis(None, axis=1)
        df["Total Medals"] = df.sum(axis=1, numeric_only=True)
        df = df.reindex(columns=['Bronze', 'Silver', 'Gold', 'Total Medals'])
        df.sort_values(by="Total Medals", ascending=False, inplace=True)
        df = df[0:10].reset_index()

        fig = px.bar(df,
                     x="Sport",
                     y=["Bronze", "Silver", "Gold", "Total Medals"],
                     title="Sports that Great Britain has the most medals in",
                     barmode="group")

        return fig

    def gb_years_medal(self):
        data_folder = os.path.abspath("./Data")
        data_athletes = os.path.join(data_folder, "athlete_events.csv")
        df = pd.read_csv(data_athletes)

        df_years = df.loc[df["Medal"].notna(), ["Games", "Medal"]]
        df_years = df_years.groupby(
            ["Games", "Medal"]).Medal.count().reset_index(name="Total")
        df_years = df_years.set_index(
            ['Games', 'Medal']).unstack('Medal', fill_value=0)
        df_years.columns = df_years.columns.droplevel(
            0)  # Dropped the Total index column
        df_years = df_years.rename_axis(None, axis=1)
        df_years["Total Medals"] = df_years.sum(axis=1, numeric_only=True)
        df_years = df_years[df_years.columns.reindex(
            ['Bronze', 'Silver', 'Gold', 'Total Medals'])[0]]
        df_years.sort_values(by="Total Medals", ascending=False, inplace=True)
        df_years = df_years.reset_index()

        fig = px.bar(
            df_years,
            x="Games",
            y="Total Medals",
            title="Total medals per year ")

        return fig

    def gb_age(self):

        data_folder = os.path.abspath("./Data")
        data_athletes = os.path.join(data_folder, "athlete_events.csv")
        df = pd.read_csv(data_athletes)

        df_age = df[df["Team"] == "Great Britain"]
        df_age = df_age.loc[df["Age"].notna(), ["Age"]]
        df_age = df_age.groupby(["Age"]).Age.count().reset_index(name="Total")
        df_age['Age'] = df_age['Age'].astype('Int64')

        fig = px.histogram(df_age, x="Age", y="Total", nbins=84, labels={
            "sum of Total": "Total athletes", "Age": "Age of athlete"},
            title="Ages of participating Athletes from Great Britain who competed in the previous Olympics")

        return fig

    def gb_height_weight(self):
        
        data_folder = os.path.abspath("./Data")
        data_athletes = os.path.join(data_folder, "athlete_events.csv")
        df = pd.read_csv(data_athletes)

        df_height_weight = df[df["Team"] == "Great Britain"]
        df_height_weight = df_height_weight[["Sport", "Height","Weight"]]
        df_height_weight = df_height_weight.dropna()
        df_height_weight = df_height_weight.groupby(["Sport"]).mean().reset_index()
        
        fig = px.scatter(df_height_weight, x="Height", y="Weight", color="Sport")

        return fig

