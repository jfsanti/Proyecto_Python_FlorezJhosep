import json
import os
from datetime import datetime

from modulos.persistencia import cargar_datos, guardar_datos


# Obtener la carpeta principal del proyecto
CARPETA_PROYECTO = os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))
)


def registrar_diagnostico(usuario_actual):

    # Verificar que el usuario sea medico
    if usuario_actual["tipo"] != "medico":

        print("\nSolo los medicos pueden registrar diagnosticos.")
        return

    # Cargar informacion del archivo JSON
    datos = cargar_datos()

    pacientes = datos["pacientes"]

    print("\n================================")
    print("       DIAGNOSTICO DE PACIENTES")
    print("================================")

    # Solicitar identificacion del paciente
    identificacion = input("Identificacion del paciente: ")

    # Buscar al paciente
    paciente_encontrado = None

    for paciente in pacientes:

        if paciente["identificacion"] == identificacion:

            paciente_encontrado = paciente
            break

    # Comprobar si existe el paciente
    if paciente_encontrado is None:

        print("\nEl paciente no esta registrado.")
        return

    print("\nPaciente encontrado:")
    print("Nombre:", paciente_encontrado["nombre"])
    print("Apellidos:", paciente_encontrado["apellidos"])

    # Registrar sintomas
    sintomas = input("\nDescriba los sintomas del paciente: ")

    # Registrar diagnostico
    diagnostico = input("Describa el diagnostico medico: ")

    # Crear lista de medicamentos
    medicamentos = []

    while True:

        print("\n===== PRESCRIPCION MEDICA =====")

        medicamento = input("Nombre del medicamento: ")
        cantidad = input("Cantidad: ")
        dosis = input("Dosis diaria: ")
        tiempo = input("Tiempo de aplicacion en dias: ")

        nuevo_medicamento = {

            "medicamento": medicamento,
            "cantidad": cantidad,
            "dosis": dosis,
            "tiempo_aplicacion": tiempo

        }

        medicamentos.append(nuevo_medicamento)

        continuar = input(
            "\n¿Desea agregar otro medicamento? (si/no): "
        ).lower()

        if continuar != "si":

            break

    # Obtener fecha y hora de la consulta
    fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Crear registro del diagnostico
    nuevo_diagnostico = {

        "fecha": fecha,

        "paciente": {
            "identificacion": paciente_encontrado["identificacion"],
            "nombre": paciente_encontrado["nombre"],
            "apellidos": paciente_encontrado["apellidos"]
        },

        "medico": {
            "identificacion": usuario_actual["identificacion"],
            "nombre": usuario_actual["nombre"],
            "apellidos": usuario_actual["apellidos"],
            "correo": usuario_actual["correo"]
        },

        "sintomas": sintomas,
        "diagnostico": diagnostico,
        "medicamentos": medicamentos

    }

    # Agregar diagnostico a la lista general
    datos["diagnosticos"].append(nuevo_diagnostico)

    # Guardar en el archivo principal
    guardar_datos(datos)

    # Crear carpeta de prescripciones si no existe
    carpeta_prescripciones = os.path.join(
        CARPETA_PROYECTO,
        "prescripciones"
    )

    os.makedirs(carpeta_prescripciones, exist_ok=True)

    # Crear nombre del archivo JSON
    fecha_archivo = datetime.now().strftime("%Y%m%d_%H%M%S")

    nombre_archivo = (
        "prescripcion_"
        + identificacion
        + "_"
        + fecha_archivo
        + ".json"
    )

    ruta_archivo = os.path.join(
        carpeta_prescripciones,
        nombre_archivo
    )

    # Guardar prescripcion en un archivo JSON independiente
    with open(ruta_archivo, "w", encoding="utf-8") as archivo:

        json.dump(
            nuevo_diagnostico,
            archivo,
            indent=4,
            ensure_ascii=False
        )

    print("\nDiagnostico registrado correctamente.")
    print("Prescripcion guardada en:", nombre_archivo)