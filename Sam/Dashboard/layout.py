from dash import html, dcc
import dash_bootstrap_components as dbc


class Layout:
    def layout(self):
        return dbc.Container(

            dbc.Card(
                dbc.CardBody(html.H1("Techy stocks viewer")), className={"mt-3"})


        )
