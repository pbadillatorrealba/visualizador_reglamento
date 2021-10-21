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
import dash_auth
import dash_bootstrap_components as dbc
from dash import Input, Output, dcc, html

from navbar import navbar
from visualizador import visualizador

# Keep this out of source code repository - save in a file or a database
VALID_USERNAME_PASSWORD_PAIRS = {"reglamentos": "tribu__"}


app = dash.Dash(
    external_stylesheets=[dbc.themes.LUX, dbc.icons.BOOTSTRAP],
    meta_tags=[{"name": "viewport", "content": "width=device-width, initial-scale=1"},],
)

auth = dash_auth.BasicAuth(app, VALID_USERNAME_PASSWORD_PAIRS)

app.layout = html.Div(
    [
        dcc.Location(id="url"),
        navbar,
        # sidebar,
        html.Div(id="page-content"),
    ]
)

with open("./data/general.json", "r") as f:
    general = json.load(f)

with open("./data/etica.json", "r") as f:
    etica = json.load(f)

with open("./data/participacion_consulta_indigena.json", "r") as f:
    participacion_consulta_indigena = json.load(f)

with open("./data/participacion_educacion_popular.json", "r") as f:
    participacion_eduacion_popular = json.load(f)

with open("./data/asignaciones_admin.json", "r") as f:
    asignaciones_admin = json.load(f)


@app.callback(Output("page-content", "children"), [Input("url", "pathname")])
def render_page_content(pathname):
    if pathname == "/":
        return dbc.Container(
            [
                html.H2("Seleccione el reglamento que desea visualizar:"),
                dbc.Nav(
                    [
                        dbc.NavItem(dbc.NavLink("General", href="/general")),
                        dbc.NavItem(dbc.NavLink("Ética", href="/etica")),
                        dbc.NavItem(
                            dbc.NavLink(
                                "Participación y Consulta Indígena",
                                href="/participacion-consulta-indigena",
                            )
                        ),
                        dbc.NavItem(
                            dbc.NavLink(
                                "Participación y Educación Popular",
                                href="/participacion-educacion-popular",
                            )
                        ),
                        dbc.NavItem(
                            dbc.NavLink(
                                "Asignaciones y Administración",
                                href="/asignaciones-admin",
                            )
                        ),
                    ],
                    vertical="md",
                ),
            ],
            class_name="mt-5",
        )
    if pathname == "/general":
        return visualizador(general)
    elif pathname == "/etica":
        return visualizador(etica)
    elif pathname == "/participacion-consulta-indigena":
        return visualizador(participacion_consulta_indigena)
    elif pathname == "/participacion-educacion-popular":
        return visualizador(participacion_eduacion_popular)
    elif pathname == "/asignaciones-admin":
        return visualizador(asignaciones_admin)

    return html.Div(
        dbc.Container(
            [
                html.H1("404: Página no encontrada", className="display-3"),
                html.Hr(className="my-2"),
            ],
            fluid=True,
            className="py-3",
        ),
        className="p-3 bg-light rounded-3",
    )


server = app.server


if __name__ == "__main__":
    app.run_server(port=8889, debug=True)
