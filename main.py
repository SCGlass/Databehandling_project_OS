import dash # import dash to make the dashboard
import os # used to import files better. tex the dataframe
from dash.dependencies import Output, Input # allows inputs and outputs for app
import plotly_express as px # used for plotting of the graphs
import pandas as pd # used to clean and analyze data
import dash_bootstrap_components as dbc # used to style the dashboard. instead of using html
from dash import html # ensures html can be used
from layout import Layout # This is the .py file with all the layout information in it
from graphs import Graphs # This is a .py file containing the graphs and data cleaning that has been done on each plot
from dash_bootstrap_templates import load_figure_template # This is used to blend in the graph function to the background


# Creating the app main frame using dash
app = dash.Dash(
    __name__, # This is important to return the app
    external_stylesheets=[dbc.themes.CERULEAN], # using a pre styled style sheet called CERULEAN from plotly dash
    meta_tags=[
        dict(name="viewport", content="width=device-width, initial-scale=1.0")], 
)       # setting the dimensions for application, In the future will add more to be used with other devices

server = app.server # created a variable so the server to deploy the app will recognize

load_figure_template('CERULEAN') # Load template CERULEAN so it will match the background theme so it will be seamless

app.layout = Layout().layout() # This brings in the layout file into the main frame

@app.callback(Output("graph","figure"),Input("gb-dropdown", "value")) # Callback function for dropdown on first tab
def update_left_graph(option): # Used a function that will take a graph function from graph.py
    if option == "medals": # The if sats will take the value from the dropdown.
        return Graphs().top_ten_gb() # If it matches it will then return the relevant graph 
    elif option == "medals_os": # This shows the next value and if that is selected it will then return a different graph to Output
        return Graphs().gb_years_medal()
    elif option == "age":
        return Graphs().gb_age()
    elif option == "height_weight":
        return Graphs().gb_height_weight()

# The next callback is layed out the same as above but using the dropdown on the second tab.
@app.callback(Output("graph-down", "figure"), Input("world-dropdown", "value"))
def update_right_graph(option):
    if option == "top_ten_medals":
        return Graphs().top_10_medals()
    elif option == "art_comp":
        return Graphs().map_medals_Art_Competitions()
    elif option == "ice_hockey":
        return Graphs().map_medals_Ice_Hockey()

    



if __name__ == "__main__": # using __ name to return to main and to be able to run the app
    app.run_server()
