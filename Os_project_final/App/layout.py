from dash import html, dcc
import dash_bootstrap_components as dbc


class Layout:
    def __init__(self) -> None:

        self.GB_stats = [
            {"label":"graph1", "value":"graph2" },{"label":"graph2", "value":"graph4" } ]
        
        self.world_stats = [
            {"label": "Top Ten medals", "value": "graph_2"}
        ]

    def layout(self):
        return dbc.Container([
            html.Div(children=[
            html.H1(children='Olympic Dashboard statistics'),

        html.Div([
            dcc.Dropdown(
                
                id='GB_dropdown',
                options = self.GB_stats
            ),
           
        ], style={'width': '48%', 'display': 'inline-block'}),

        html.Div([
            dcc.Dropdown(
                id='medals',
                options = self.world_stats,
                

            ),
          
        ], style={'width': '48%', 'float': 'right', 'display': 'inline-block'})
    ]),

    dcc.Graph(id='graph'),

    

        ])
    















            
        
        
