import pandas as pd
import plotly_express as px

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

fig = px.bar(top_10)
fig.show()
