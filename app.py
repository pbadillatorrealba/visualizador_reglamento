"""
This app uses NavbarSimple to navigate between three different pages.
dcc.Location is used to track the current location. A callback uses the current
location to render the appropriate page content. The active prop of each
NavLink is set automatically according to the current pathname. To use this
feature you must install dash-bootstrap-components >= 0.11.0.
For more details on building multi-page Dash applications, check out the Dash
documentation: https://dash.plot.ly/urls
"""
import json

import dash
import dash_bootstrap_components as dbc
from dash import Input, Output, dcc, html

from navbar import navbar
from sidebar import sidebar
from visualizador import visualizador

app = dash.Dash(
    external_stylesheets=[dbc.themes.LUX, dbc.icons.BOOTSTRAP],
    meta_tags=[{"name": "viewport", "content": "width=device-width, initial-scale=1"},],
)


app.layout = html.Div(
    [
        dcc.Location(id="url"),
        navbar,
        # sidebar,
        html.Div(id="page-content"),
    ]
)


with open("general.json", "r") as f:
    data = json.load(f)


@app.callback(Output("page-content", "children"), [Input("url", "pathname")])
def render_page_content(pathname):
    if pathname == "/":
        return visualizador(data)
    elif pathname == "/page-1":
        return html.P("This is the content of page 1. Yay!")
    elif pathname == "/page-2":
        return html.P("Oh cool, this is page 2!")
    # If the user tries to reach a different page, return a 404 message
    return dbc.Jumbotron(
        [
            html.H1("404: Not found", className="text-danger"),
            html.Hr(),
            html.P(f"The pathname {pathname} was not recognised..."),
        ]
    )


server = app.server


if __name__ == "__main__":
    app.run_server(port=8889, debug=True)
