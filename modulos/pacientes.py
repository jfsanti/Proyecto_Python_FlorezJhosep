from modulos.persistencia import guardar_datos, cargar_datos


def registrar_paciente():

    # Cargar la informacion del archivo JSON
    datos = cargar_datos()

    pacientes = datos["pacientes"]

    print("\n================================")
    print("       REGISTRO DE PACIENTES")
    print("================================")

    # Solicitar identificacion
    identificacion = input("Numero de identificacion: ")

    # Comprobar si el paciente ya existe
    for paciente in pacientes:

        if paciente["identificacion"] == identificacion:

            print("\nError: Este paciente ya esta registrado.")
            return

    # Solicitar los datos personales
    nombre = input("Nombres: ")
    apellidos = input("Apellidos: ")
    telefono = input("Numero de telefono: ")
    correo = input("Correo electronico: ")
    direccion = input("Direccion: ")

    print("\nSeleccione el genero:")
    print("1. Masculino")
    print("2. Femenino")
    print("3. Otro")

    opcion_genero = input("Opcion: ")

    if opcion_genero == "1":

        genero = "Masculino"

    elif opcion_genero == "2":

        genero = "Femenino"

    elif opcion_genero == "3":

        genero = "Otro"

    else:

        print("Opcion de genero incorrecta.")
        return

    print("\nSeleccione el estado civil:")
    print("1. Soltero")
    print("2. Casado")
    print("3. Divorciado")
    print("4. Viudo")
    print("5. Union libre")

    opcion_estado = input("Opcion: ")

    if opcion_estado == "1":

        estado_civil = "Soltero"

    elif opcion_estado == "2":

        estado_civil = "Casado"

    elif opcion_estado == "3":

        estado_civil = "Divorciado"

    elif opcion_estado == "4":

        estado_civil = "Viudo"

    elif opcion_estado == "5":

        estado_civil = "Union libre"

    else:

        print("Opcion de estado civil incorrecta.")
        return

    # Crear el diccionario del paciente
    nuevo_paciente = {

        "identificacion": identificacion,
        "nombre": nombre,
        "apellidos": apellidos,
        "telefono": telefono,
        "correo": correo,
        "direccion": direccion,
        "genero": genero,
        "estado_civil": estado_civil
    }

    # Agregar el paciente a la lista
    pacientes.append(nuevo_paciente)

    # Guardar toda la informacion
    guardar_datos(datos)

    print("\nPaciente registrado correctamente.")
