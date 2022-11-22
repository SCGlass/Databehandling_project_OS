from dash import html, dcc
import dash_bootstrap_components as dbc


class Layout:
    def __init__(self) -> None:

        self.GB_stats = [
            {"label":"Sports Great Britain won the most medals in", "value":"medals" },
            {"label":"Amount of medals won per Olympic Games", "value":"medals_os" },
            {"label": "Age distribution of Athletes representing Great Britain", "value":"age"}]
        
        self.world_stats = [
            {"label": "Top Highest Ten countries medal count", "value": "top_ten_medals"},
            {"label": "Distribution of Winners in Art competitions", "value":"art_comp"},
            {"label": "Distribution of Winners in Ice Hockey", "value":"ice_hockey"}
        ]

    
    
    
    def layout(self):
        
        return dbc.Container([
            
            html.Div(children=[
            html.H1(children='Olympic Dashboard statistics'),

        html.Div([
            dcc.Dropdown(
                
                id='GB_dropdown',
                options = self.GB_stats,
                value = "medals_os"
            ),
           
        ], style={'width': '48%', 'display': 'inline-block'}),

        html.Div([
            dcc.Dropdown(
                id='world-dropdown',
                options = self.world_stats,
                value = "top_ten_medals"

            ),
          
        ], style={'width': '48%', 'float': 'right', 'display': 'inline-block'})
    ]),

    dcc.Graph(id='graph')



    

        ])
    















            
        
        
