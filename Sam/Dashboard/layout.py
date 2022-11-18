from dash import html, dcc
import dash_bootstrap_components as dbc


class Layout:
    def layout(self):
        return dbc.Container(
            [
                dbc.Card(
                    dbc.CardBody
                        ((html.H1("Olympic Games Dashboard")),
                        (html.Img(src="assets/olympic-logo.png"))), className="rounded float-right")
                        
                        
                        ]
                    )
