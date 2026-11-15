from modulos.persistencia import cargar_datos


def consultar_historia_clinica():

    # Cargar informacion del sistema
    datos = cargar_datos()

    pacientes = datos["pacientes"]
    diagnosticos = datos["diagnosticos"]

    print("\n================================")
    print("       HISTORIA CLINICA")
    print("================================")

    # Solicitar identificacion del paciente
    identificacion = input(
        "\nIngrese la identificacion del paciente: "
    )

    # Buscar al paciente
    paciente_encontrado = None

    for paciente in pacientes:

        if paciente["identificacion"] == identificacion:

            paciente_encontrado = paciente
            break

    # Verificar si existe el paciente
    if paciente_encontrado is None:

        print("\nEl paciente no se encuentra registrado.")
        return

    # Mostrar datos personales
    print("\n================================")
    print("       DATOS DEL PACIENTE")
    print("================================")

    print("Identificacion:",
          paciente_encontrado.get("identificacion", "No registrado"))

    print("Nombre:",
          paciente_encontrado.get("nombre", "No registrado"))

    print("Apellidos:",
          paciente_encontrado.get("apellidos", "No registrado"))

    # Mostrar otros datos personales registrados
    campos_basicos = ["identificacion", "nombre", "apellidos"]

    for campo, valor in paciente_encontrado.items():

        if campo not in campos_basicos:

            print(campo.capitalize() + ":", valor)

    # Buscar diagnosticos del paciente
    print("\n================================")
    print("       REGISTRO DE CONSULTAS")
    print("================================")

    historial_encontrado = False

    for registro in diagnosticos:

        paciente_registro = registro.get("paciente") or {}

        if paciente_registro.get("identificacion") == identificacion:

            historial_encontrado = True

            # Mostrar fecha
            print("\nFecha de consulta:",
                  registro.get("fecha", "No registrada"))

            # Mostrar informacion del medico
            medico = registro.get("medico") or {}

            print("\nMedico responsable:")
            print("Nombre:",
                  medico.get("nombre", "No registrado"),
                  medico.get("apellidos", ""))

            print("Identificacion:",
                  medico.get("identificacion", "No registrada"))

            # Mostrar sintomas
            print("\nSintomas:")
            print(registro.get("sintomas", "No registrados"))

            # Mostrar diagnostico
            print("\nDiagnostico medico:")
            print(registro.get("diagnostico", "No registrado"))

            # Mostrar medicamentos
            print("\nMedicamentos registrados:")

            medicamentos = registro.get("medicamentos", [])

            if medicamentos:

                for medicamento in medicamentos:

                    print("\nMedicamento:",
                          medicamento.get("medicamento", ""))

                    print("Cantidad:",
                          medicamento.get("cantidad", ""))

                    print("Dosis:",
                          medicamento.get("dosis", ""))

                    print("Tiempo de aplicacion:",
                          medicamento.get("tiempo_aplicacion", ""),
                          "dias")

            else:

                print("No hay medicamentos registrados.")

            print("\n--------------------------------")

    # Verificar si existen consultas
    if not historial_encontrado:

        print("\nEl paciente no tiene consultas registradas.")

    print("\n================================")
    print("     FIN DE HISTORIA CLINICA")
    print("================================")