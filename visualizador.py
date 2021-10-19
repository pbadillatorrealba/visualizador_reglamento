import dash_bootstrap_components as dbc
from dash import html
from unidecode import unidecode


def visualizador(data: dict):

    layout = [html.H2("Reglamento General", className="mt-2 mb-5 h1")]

    for titulo in data:
        seccion = html.Section([])
        layout.append(seccion)
        seccion.children.append(html.H3(titulo["titulo"], className="h3 mb-4"))

        for parrafo in titulo["contenido"]:
            # layout.append(html.Hr())
            seccion.children.append(
                html.H4(str(parrafo["titulo"]), className="h6 mt-4 mb-0",)
            )
            href = f'#{unidecode(parrafo["titulo"].replace(" ", "-").replace("°","").lower())}'
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
                    className="h4 mt-0 mb-4",
                    id=href,
                )
            )

            for articulo in parrafo["contenido"]:
                seccion.children.append(
                    html.H5(
                        [
                            html.Span(str(articulo["titulo"]), className="text-muted",),
                            str(articulo["descripcion"]),
                        ],
                        className="h5 mb-3 mt-4",
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

    return layout
