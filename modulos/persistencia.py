import json
import os


# Obtener la ubicacion principal del proyecto
CARPETA_PROYECTO = os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))
)

# Ubicacion del archivo JSON
RUTA_DATOS = os.path.join(
    CARPETA_PROYECTO,
    "datos",
    "datos.json"
)


def guardar_datos(datos):

    with open(RUTA_DATOS, "w", encoding="utf-8") as archivo:

        json.dump(datos, archivo, indent=4, ensure_ascii=False)


def cargar_datos():

    if not os.path.exists(RUTA_DATOS):

        datos = {
            "usuarios": [],
            "pacientes": [],
            "diagnosticos": []
        }

        guardar_datos(datos)

        return datos

    with open(RUTA_DATOS, "r", encoding="utf-8") as archivo:

        return json.load(archivo)