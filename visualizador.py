import dash_bootstrap_components as dbc
from dash import html
from unidecode import unidecode


def visualizador(data: dict):

    sidebar = dbc.Col(
        html.Ul(
            [
                html.Li(
                    [
                        html.A(
                            titulo["titulo"] + " - " + titulo["descripcion"],
                            href="#" + titulo["titulo"].replace(" ", "-"),
                            className="nav-link h6",
                        )
                    ],
                    className="nav-item",
                )
                for titulo in data
            ],
            className="nav flex-column",
        ),
        sm=2,
        class_name="bg-secondary pt-4 ps-4",
    )

    body = dbc.Container(
        [html.H2("Reglamento General", className="mt-2 mb-5 h1 text-center")],
        class_name="mt-5",
    )

    for titulo in data:
        seccion = html.Section([])
        body.children.append(seccion)
        seccion.children.append(
            html.H6(titulo["titulo"], className="h4 mt-5 mb-0 text-center")
        )
        seccion.children.append(
            html.H3(titulo["descripcion"], className="h2 mb-5 mt-0 text-center")
        )

        for parrafo in titulo["contenido"]:
            # layout.append(html.Hr())
            seccion.children.append(
                html.H4(str(parrafo["titulo"]), className="h6 mt-5 mb-0 text-center",)
            )
            href = f'#{unidecode((parrafo["titulo"] + "-" + parrafo["descripcion"]).replace(" ", "-").replace("°","").lower())}'
            seccion.children.append(
                html.H3(
                    [
                        str(parrafo["descripcion"]),
                        html.A(
                            [html.I(className="bi bi-link")],
                            href=href,
                            className="ms-1",
                        ),
                    ],
                    className="h4 mt-0 mb-5 text-center",
                    id=href,
                )
            )

            for articulo in parrafo["contenido"]:
                seccion.children.append(
                    html.H5(
                        [
                            html.Span(
                                str(articulo["titulo"]), className="text-muted me-1",
                            ),
                            str(articulo["descripcion"]),
                        ],
                        className="h5 mb-3 mt-4 text-capitalize",
                    )
                )

                for contenido in articulo["contenido"]:
                    if contenido["tipo"] == "texto":
                        seccion.children.append(
                            html.P(contenido["contenido"], className="ms-4")
                        )
                    elif contenido["tipo"] == "lista":

                        ultimo = seccion.children[-1]
                        if not isinstance(ultimo, html.Ul):
                            seccion.children.append(html.Ol([], className="ms-4"))
                            ultimo = seccion.children[-1]

                        ultimo.children.append(
                            html.Li(
                                [html.P(item) for item in contenido["contenido"]],
                                **{"data-idx": contenido["indice"]},
                            )
                        )

                    # if "lista" in contenido:
                    #     layout.append(html.P(contenido["lista"], className="ms-4"))

    return dbc.Row([sidebar, dbc.Col(body, sm=10)], class_name="w-100")
