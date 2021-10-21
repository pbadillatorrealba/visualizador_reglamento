import math

import dash_bootstrap_components as dbc
from dash import html
from unidecode import unidecode


def adaptar_str_href(s: str) -> str:
    processed_str = (
        unidecode(s)
        .replace(" ", "-")
        .replace(" ", "°")
        .lower()
        .translate(str.maketrans("", "", "!\"#$%&\\'()*+,./:;<=>?@[\\]^_`{|}~"))
    )
    href = f"#{processed_str}"
    return href


def visualizador(reglamento: dict):

    # sidebar = dbc.Col(
    #     html.Ul(
    #         [
    #             # html.Li(
    #             #     [
    #             #         html.A(
    #             #             str(titulo["titulo"]) + " - " + str(titulo["texto"]),
    #             #             href="#" + titulo["titulo"].replace(" ", "-"),
    #             #             className="nav-link h6",
    #             #         )
    #             #     ],
    #             #     className="nav-item",
    #             # )
    #             # for titulo in data
    #         ],
    #         className="nav flex-column",
    #     ),
    #     sm=2,
    #     class_name="bg-secondary pt-4 ps-4",
    # )

    body = dbc.Container(
        [html.H2(reglamento["titulo"], className="mt-2 mb-5 h2 text-center")],
        class_name="mt-5",
    )

    for titulo in reglamento["hijos"]:
        seccion = html.Section([])
        body.children.append(seccion)

        # -----------------------------------------------------------------------
        # Preámbulo
        # -----------------------------------------------------------------------
        if titulo["tipo"] == "preambulo":
            seccion.children.append(
                html.H3(titulo["titulo"], className="h3 mb-5 mt-0 text-center")
            )
            seccion.children.append(html.P(titulo["texto"], className="ms-4"))

        # -----------------------------------------------------------------------
        # Titulo
        # -----------------------------------------------------------------------
        else:
            seccion.children.append(
                html.H6(titulo["titulo"], className="h4 mt-5 mb-0 text-center")
            )
            seccion.children.append(
                html.H3(titulo["texto"], className="h3 mb-5 mt-0 text-center")
            )

            # -----------------------------------------------------------------------
            # Parrafo
            # -----------------------------------------------------------------------
            for parrafo in titulo["hijos"]:

                if parrafo["tipo"] == "parrafo":
                    # layout.append(html.Hr())
                    seccion.children.append(
                        html.H4(
                            str(parrafo["titulo"]),
                            className="h6 mt-5 mb-0 text-center",
                        )
                    )
                    href = adaptar_str_href(
                        str(parrafo["titulo"]) + "-" + str(parrafo["texto"])
                    )
                    seccion.children.append(
                        html.H3(
                            [
                                str(parrafo["texto"]),
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

                # -----------------------------------------------------------------------
                # Artículo
                # -----------------------------------------------------------------------
                for articulo in parrafo["hijos"]:

                    # Artículos transitorios sin títulos.
                    if articulo["texto"] is None or str(articulo["texto"]) == "nan":
                        seccion.children.append(
                            html.H5(
                                [
                                    html.Span(
                                        str(articulo["titulo"]),
                                        className="text-muted me-1",
                                    ),
                                ],
                                className="h5 mb-3 mt-4 text-capitalize",
                            )
                        )

                    # Artículos comunes con título
                    else:
                        seccion.children.append(
                            html.H5(
                                [
                                    html.Span(
                                        str(articulo["titulo"]),
                                        className="text-muted me-1",
                                    ),
                                    str(articulo["texto"]),
                                ],
                                className="h5 mb-3 mt-4 text-capitalize",
                            )
                        )

                    # -----------------------------------------------------------------------
                    # Contenido
                    # -----------------------------------------------------------------------

                    for item in articulo["hijos"]:

                        # Caso 1: Texto
                        if item["tipo"] == "texto":
                            seccion.children.append(
                                html.P(item["texto"], className="ms-4")
                            )

                        # Caso 2: Lista
                        elif item["tipo"] == "lista":

                            ultimo = seccion.children[-1]
                            if not isinstance(ultimo, html.Ul):
                                seccion.children.append(html.Ol([], className="ms-4"))
                                ultimo = seccion.children[-1]

                            ultimo.children.append(
                                html.Li(
                                    [
                                        html.P(item_lista)
                                        for item_lista in item["hijos"]
                                    ],
                                    **{"data-idx": item["texto"]},
                                )
                            )

                        # if "lista" in contenido:
                        #     layout.append(html.P(contenido["lista"], className="ms-4"))

    return dbc.Row([dbc.Col(body)], class_name="w-100")

