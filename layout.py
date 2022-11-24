from dash import html, dcc # importing dash html components as dcc so can use python code with html actions 
import dash_bootstrap_components as dbc #importing bootstrap components to style the dashboard 


# creating the class Layout to use within the main main.py
class Layout:
    def __init__(self) -> None: 

        # This attribute is a dictionary to return what the titles in the first dropdown is and the value to return to the input callbacks
        self.GB_stats = [
            {"label": "Sports Great Britain won the most medals in", "value": "medals"},
            {"label": "Amount of medals won per Olympic Games", "value": "medals_os"},
            {"label": "Age distribution of Athletes representing Great Britain", "value": "age"},
            {"label": "Height and Weight averages of Different sports in Great Britain Team", "value":"height_weight"}
        ]
        # This is the attribute is for the world stats drop down on the second tab
        self.world_stats = [
            {"label": "Top ranking countries medal count", "value": "top_ten_medals"},
            {"label": "Distribution of Winners in Art competitions", "value": "art_comp"},
            {"label": "Distribution of Winners in Ice Hockey", "value": "ice_hockey"}
        ]

    # This is now the layout function that will contain all the style, positioning and functions of the app
    def layout(self):
        
        return dbc.Container([ # Container is where the whole layout has to be contained in.
             

            html.Div( # use of a div tag to group sets or sections of functions of the app 
                children=[
                html.H1(children='Olympic Games Statistics'), # This shows the title bar of the Dashboard
                

                # now adding in tab decorator 
                dcc.Tabs([
                    dcc.Tab(label='Team Great Britain',children=[ # This is the first tab on the right
                            dcc.Dropdown( # adding a drop down decorator 
                                id='gb-dropdown', # this is its id which will be recognized in the callbacks
                                options=self.GB_stats, # This is the dictionary of the dropdown menu it will select the required drop down
                                value="medals" # This will return the value to the callback to activate the output
                            ),
                            dcc.Graph(id='graph'), # This is the graph decorator which allows a graph to be shown
                            ], style={'width': '50%', 'display': 'inline-block'}), # This sets the width and styling of the dropdown menu

                    dcc.Tab(label='World Olympics', children=[ # The code is the same with the next tab, however the values and ids will be different

                        dcc.Dropdown(
                            id='world-dropdown', # change of id 
                            options=self.world_stats, # chamge of option
                            value="top_ten_medals" # change of value
                        ),
                        dcc.Graph(id='graph-down')
                    ], style={'width': '50%', 'display': 'inline-block'}),


                ]),




            ])
        ])
