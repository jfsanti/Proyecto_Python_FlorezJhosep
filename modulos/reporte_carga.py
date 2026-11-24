import json
import os

CARPETA_PROYECTO = os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))
)

# Ubicacion del archivo JSON
RUTA_DATOS = os.path.join(
    CARPETA_PROYECTO,
    "datos",
    "reporte_carga_medicos.json"
)


"""
id_medico o identificación
nombre_completo
total_diagnosticos
pacientes_distintos
promedio_sintomas_por_consulta
promedio_medicamentos_por_consulta"""

def guardar_datos(datos):

    with open(RUTA_DATOS, "w", encoding="utf-8") as archivo:

        json.dump(datos, archivo, indent=4, ensure_ascii=False)

def reporte_carga():

    if not os.path.exists(RUTA_DATOS):

            datos = {
                "Lista de medicos": [],
                "resumen": []
            }
            guardar_datos(datos)

            return datos

    with open(RUTA_DATOS, "r", encoding="utf-8") as archivo:

            return json.load(archivo)

def info_medico():

      return
