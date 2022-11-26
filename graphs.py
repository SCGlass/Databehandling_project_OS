import pandas as pd # importing pandas to do data analysis
import plotly_express as px # importing plotly to plot graphs
import os # used to help with path names for dataframe

# creating class Graphs to use in main frame and visualize graphs. 
class Graphs:
    #TODO Håkan can commetn here on his function
    
    def top_10_medals(self):
        """Graph of top ten countries medal count""" 
        
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

    #TODO Håkan can comment on his function here
    
    def map_medals_Art_Competitions(self):
        """World visualization of total medals won in Art competitions"""
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

    #TODO Håkan can comment here
    def map_medals_Ice_Hockey(self):
        """World graph showing the most medals won in Ice hockey"""
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
        """Graph showing top ten sports Great Britain won medals in"""
        data_folder = os.path.abspath("./Data") # creating a path for data folder
        data_athletes = os.path.join(data_folder, "athlete_events.csv") # joining file into the folder
        df = pd.read_csv(data_athletes) # reading the .csv file and creating a dataframe

        df = df[df["Team"] == "Great Britain"] # Extracting only the information about "Great Britain"
        df = df.loc[df["Medal"].notna(), ["Sport", "Medal"]] # extracting Sport and medal column and removing non values
        df = df.groupby(["Sport", "Medal"]).Medal.count().reset_index(name="Total") # grouping sports with medals than adding a total column
        df = df.set_index(['Sport', 'Medal']).unstack('Medal', fill_value=0) # This then unstacks the Gold, Silver,Bronze total to separate columns 
        df.columns = df.columns.droplevel(0)  # Dropped the Total index column as cant be plotted
        df = df.rename_axis(None, axis=1) # This removes the first index row
        df["Total Medals"] = df.sum(axis=1, numeric_only=True) # Adding in again a total medals column from sum of the axis
        df = df.reindex(columns=['Bronze', 'Silver', 'Gold', 'Total Medals']) # This resets the index so that the medals are in order
        df.sort_values(by="Total Medals", ascending=False, inplace=True) # Sorts the dataframe total medals from highest to lowest
        df = df[0:10].reset_index() # This selects the first 10 sports

        # plotting the data as a bar chart
        fig = px.bar(df,
                     x="Sport",
                     y=["Bronze", "Silver", "Gold", "Total Medals"], 
                     title="Sports that Great Britain has the most medals in",
                     barmode="group") # used group to have the bars groped as 3 instead of being stacked

        return fig # return the graph in the function to be used in the app graph area

    def gb_years_medal(self):
        """Graph showing medals won over years by Great Britain"""
        # This function had the same attributes as the top ten medals by sport. However this only plotted total medals
        data_folder = os.path.abspath("./Data")
        data_athletes = os.path.join(data_folder, "athlete_events.csv")
        df = pd.read_csv(data_athletes)

        df_years = df.loc[df["Medal"].notna(), ["Games", "Medal"]]
        df_years = df_years.groupby(
            ["Games", "Medal"]).Medal.count().reset_index(name="Total")
        df_years = df_years.set_index(
            ['Games', 'Medal']).unstack('Medal', fill_value=0)
        df_years.columns = df_years.columns.droplevel(0)  # Dropped the Total index column
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
        """Graph showing age of Athletes in Great Britain team"""
        data_folder = os.path.abspath("./Data")
        data_athletes = os.path.join(data_folder, "athlete_events.csv")
        df = pd.read_csv(data_athletes)

        df_age = df[df["Team"] == "Great Britain"]
        df_age = df_age.loc[df["Age"].notna(), ["Age"]] # extracting age columm and removing non values
        df_age = df_age.groupby(["Age"]).Age.count().reset_index(name="Total") # grouping the ages with a total amount
        df_age['Age'] = df_age['Age'].astype('Int64') # Changing the floats in to int

        # Usingf a histogram to visualize added nbins so the plot didnt look so crowded
        fig = px.histogram(df_age, x="Age", y="Total", nbins=84, labels={
            "sum of Total": "Total athletes", "Age": "Age of athlete"},
            title="Ages of participating Athletes from Great Britain who competed in the previous Olympics")

        return fig 

    def gb_height_weight(self):
        """Graph of height and weight averages by sport in Great Britain team"""
        data_folder = os.path.abspath("./Data")
        data_athletes = os.path.join(data_folder, "athlete_events.csv")
        df = pd.read_csv(data_athletes)

        df_height_weight = df[df["Team"] == "Great Britain"] # filtering so only Great Britain data is shown
        df_height_weight = df_height_weight[["Sport", "Height","Weight"]] # selecting the Sport weight and height columns
        df_height_weight = df_height_weight.dropna() # dropping all none values to achieve a good average
        df_height_weight = df_height_weight.groupby(["Sport"]).mean().reset_index() # grouping the sports and then averaging the height and weight bu mean
        
        # using a scatter graph to show results
        fig = px.scatter(df_height_weight, x="Height", y="Weight", color="Sport")

        return fig


