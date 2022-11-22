from dash import html, dcc
import dash_bootstrap_components as dbc
from dash_bootstrap_templates import load_figure_template


class Layout:
    def __init__(self) -> None:

        self.GB_stats = [
            {"label": "Sports Great Britain won the most medals in", "value": "medals"},
            {"label": "Amount of medals won per Olympic Games", "value": "medals_os"},
            {"label": "Age distribution of Athletes representing Great Britain", "value": "age"}]

        self.world_stats = [
            {"label": "Top Highest Ten countries medal count",
                "value": "top_ten_medals"},
            {"label": "Distribution of Winners in Art competitions", "value": "art_comp"},
            {"label": "Distribution of Winners in Ice Hockey", "value": "ice_hockey"}
        ]

    def layout(self):
        load_figure_template('UX')
        return dbc.Container([

            html.Div(children=[
                html.H1(children='Olympic Dashboard statistics'),
                style={'background-image': 'url(/assets/image.jpg)',
                        'background-size': '100%',
                        'position': 'fixed',
                        'width': '100%',
                        'height': '100%'}


                dcc.Tabs([
                    dcc.Tab(label='Team Great Britain', children=[
                            dcc.Dropdown(
                                id='gb-dropdown',
                                options=self.GB_stats,
                                value="medals"
                            ),
                            dcc.Graph(id='graph'),
                            ], style={'width': '48%', 'display': 'inline-block'}),

                    dcc.Tab(label='World Olympics', children=[

                        dcc.Dropdown(
                            id='world-dropdown',
                            options=self.world_stats,
                            value="top_ten_medals"
                        ),
                        dcc.Graph(id='graph-down')
                    ], style={'width': '48%', 'display': 'inline-block'}),


                ]),





            ])
        ])
