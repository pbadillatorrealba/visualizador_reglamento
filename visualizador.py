import dash_bootstrap_components as dbc
from dash import html


def visualizador(data: dict):

    layout = [html.H2("Reglamento General", className="mt-2 mb-5 h1")]

    for titulo in data:
        layout.append(html.H3(titulo["titulo"], className="h3 mb-4"))

        parrafos = titulo["parrafos"]
        for parrafo in parrafos:
            layout.append(html.Hr())
            layout.append(html.H4(str(parrafo["titulo"]), className="h6 mt-4 mb-0",))
            layout.append(
                html.H3(str(parrafo["descripcion"]), className="h4 mt-0 mb-4",)
            )
            articulos = parrafo["articulos"]

            for articulo in articulos:
                layout.append(
                    html.H5(
                        [
                            html.Span(str(articulo["titulo"]), className="text-muted",),
                            str(articulo["descripcion"]),
                        ],
                        className="h6 mb-3 mt-4",
                    )
                )

                contenidos = articulo["contenido"]
                for contenido in contenidos:
                    layout.append(html.P(contenido, className="ms-4"))

                    # if "lista" in contenido:
                    #     layout.append(html.P(contenido["lista"], className="ms-4"))

    return layout
