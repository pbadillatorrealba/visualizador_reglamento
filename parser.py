import json
import re

import pandas as pd

df = pd.read_excel("./reglamentos.xlsx")

df = df.rename(
    columns={
        "REGLAMENTO GENERAL DE LA CONVENCIÓN": "titulo",
        "Unnamed: 1": "parrafos",
        "Unnamed: 2": "articulo",
        "Unnamed: 3": "contenido",
        "Unnamed: 4": "lista",
    }
)
df = df.iloc[:, 0:5]


regexp = re.compile(r"\)|\d{1,3}\.|I\.|II\.|III\.|IV\.|V\.|VI\.|VII\.|VIII.\|IX\.")


datos = []
ultimo_visto = None
lista = []

for idx, row in df.iterrows():

    try:

        # --------------------------------
        # Titulo

        if not pd.isna(row["titulo"]):
            titulo_actual = {
                "titulo": row["titulo"],
                "parrafos": [],
                "descripcion": row["parrafos"],
            }
            ultimo_visto = "titulo"

        # --------------------------------
        # Parrafo
        elif not pd.isna(row["parrafos"]):
            parrafo_actual = {
                "titulo": row["parrafos"],
                "descripcion": row["articulo"],
                "articulos": [],
            }
            ultimo_visto = "parrafo"

        # --------------------------------
        # Artículo

        elif not pd.isna(row["articulo"]):
            articulo_actual = {
                "titulo": row["articulo"],
                "descripcion": row["contenido"],
                "contenido": [],
            }
            ultimo_visto = "articulo"

        # --------------------------------
        # Contenido de un Artículo

        elif not pd.isna(row["contenido"]) and not regexp.search(row["contenido"]):
            contenido = row["contenido"]
            ultimo_visto = "contenido"

        # or pd.isna(df.iloc[idx + 1]["contenido"])
        elif not pd.isna(row["contenido"]) and regexp.search(row["contenido"]):
            nombre_punto = row["contenido"]
            contenido = {row["contenido"]: []}

            punto_lista = row["lista"]
            ultimo_visto = "lista"

        elif not pd.isna(row["lista"]):
            punto_lista = row["lista"]
            ultimo_visto = "lista"

        # ----------------------------------------------------------
        # ----------------------------------------------------------
        # Agregar al registro

        if ultimo_visto == "lista":
            contenido[nombre_punto].append(punto_lista)

        elif ultimo_visto == "contenido":
            articulo_actual["contenido"].append(contenido)

        elif ultimo_visto == "articulo":
            parrafo_actual["articulos"].append(articulo_actual)

        elif ultimo_visto == "parrafo":
            titulo_actual["parrafos"].append(parrafo_actual)

        else:
            datos.append(titulo_actual)

        # print("-" * 69 + f"\nidx={idx} | ultimo_visto={ultimo_visto}\n{row}")

    except Exception as e:
        print("!!" + "-" * 60 + f"\nidx={idx}\n{row}\n{locals().keys()}")
        # raise Exception("ERROR!!!")

with open("general.json", "w") as f:
    json.dump(datos, f, ensure_ascii=False)
