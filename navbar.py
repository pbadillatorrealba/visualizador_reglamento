import dash
import dash_bootstrap_components as dbc
from dash import Input, Output, html
from dash.dependencies import State

TRIBU_LOGO = "https://images.squarespace-cdn.com/content/v1/5cb97189ca525b7a4f3f5775/1606368087837-AL81YBX5KLOZJVPJFWZZ/tribu.png?format=1500w"


search_bar = dbc.Row(
    [
        dbc.Col(dbc.Input(type="search", placeholder="Artículo 1...")),
        dbc.Col(
            dbc.Button("Buscar", color="primary", className="ms-2", n_clicks=0),
            width="auto",
        ),
    ],
    className="g-0 ms-auto flex-nowrap mt-3 mt-md-0",
    align="center",
)

navbar = dbc.Navbar(
    dbc.Container(
        [
            html.A(
                # Use row and col to control vertical alignment of logo / brand
                dbc.Row(
                    [dbc.Col(html.Img(src=TRIBU_LOGO, height="30px"))],
                    align="center",
                    className="g-0",
                ),
                # href="https://plotly.com",
                style={"textDecoration": "none"},
            ),
            dbc.DropdownMenu(
                children=[
                    dbc.DropdownMenuItem("Reglamento General", href="/general"),
                    dbc.DropdownMenuItem("Ética", href="/etica"),
                    dbc.DropdownMenuItem(
                        "Participación y Consulta Indígena",
                        href="/participacion-consulta-indigena",
                    ),
                    dbc.DropdownMenuItem(
                        "Participación y Educación Popular",
                        href="/participacion-educacion-popular",
                    ),
                    dbc.DropdownMenuItem(
                        "Asignaciones y Administración", href="/asignaciones-admin"
                    ),
                    # dbc.DropdownMenuItem("", href="#"),
                ],
                nav=True,
                color="danger",
                in_navbar=True,
                label="Reglamentos",
                class_name="ms-1 text-primary",
            ),
            dbc.NavbarToggler(id="navbar-toggler", n_clicks=0),
            dbc.Collapse(search_bar, id="navbar-collapse", is_open=False, navbar=True,),
        ]
    ),
    color="black",
    class_name="sticky-top",
)


@dash.callback(
    Output("navbar-collapse", "is_open"),
    [Input("navbar-toggler", "n_clicks")],
    [State("navbar-collapse", "is_open")],
)
def toggle_navbar_collapse(n, is_open):
    if n:
        return not is_open
    return is_open
