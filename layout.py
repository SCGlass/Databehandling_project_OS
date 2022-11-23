from dash import html, dcc
import dash_bootstrap_components as dbc



class Layout:
    def __init__(self) -> None:

        self.GB_stats = [
            {"label": "Sports Great Britain won the most medals in", "value": "medals"},
            {"label": "Amount of medals won per Olympic Games", "value": "medals_os"},
            {"label": "Age distribution of Athletes representing Great Britain", "value": "age"},
            {"label": "Height and Weight averages of Different sports in Great Britain Team", "value":"height_weight"}
        ]

        self.world_stats = [
            {"label": "Top ranking countries medal count", "value": "top_ten_medals"},
            {"label": "Distribution of Winners in Art competitions", "value": "art_comp"},
            {"label": "Distribution of Winners in Ice Hockey", "value": "ice_hockey"}
        ]

    def layout(self):
        
        return dbc.Container([
             

            html.Div(
                children=[
                html.H1(children='Olympic Games Statistics'),
                


                dcc.Tabs([
                    dcc.Tab(label='Team Great Britain',children=[
                            dcc.Dropdown(
                                id='gb-dropdown',
                                options=self.GB_stats,
                                value="medals"
                            ),
                            dcc.Graph(id='graph'),
                            ], style={'width': '50%', 'display': 'inline-block'}),

                    dcc.Tab(label='World Olympics', children=[

                        dcc.Dropdown(
                            id='world-dropdown',
                            options=self.world_stats,
                            value="top_ten_medals"
                        ),
                        dcc.Graph(id='graph-down')
                    ], style={'width': '50%', 'display': 'inline-block'}),


                ]),




            ])
        ])
