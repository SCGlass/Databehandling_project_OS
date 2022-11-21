from dash import html, dcc
import dash_bootstrap_components as dbc


class Layout:
    def layout(self):
        return dbc.Container([
            html.Div(children=[
            html.H1(children='Olympic Dashboard statistics'),

        html.Div([
            dcc.Dropdown(
                
                id=''
            ),
           
        ], style={'width': '48%', 'display': 'inline-block'}),

        html.Div([
            dcc.Dropdown(
                
                id=''
            ),
          
        ], style={'width': '48%', 'float': 'right', 'display': 'inline-block'})
    ]),

    dcc.Graph(id='indicator-graphic'),

        ])
    















            
        
        
