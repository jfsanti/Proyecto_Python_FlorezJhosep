from modulos.persistencia import guardar_datos, cargar_datos
from modulos.autenticacion import generar_hash


def registrar_usuario():

    datos = cargar_datos()

    usuarios = datos["usuarios"]

    print("\n===== REGISTRO DE USUARIOS =====")

    identificacion = input("Numero de identificacion: ")

    # Verificar identificaciones duplicadas
    for usuario in usuarios:

        if usuario["identificacion"] == identificacion:

            print("Error: Esta identificacion ya existe.")
            return

    nombre = input("Nombres: ")
    apellidos = input("Apellidos: ")
    telefono = input("Numero de telefono: ")
    correo = input("Correo electronico: ")
    direccion = input("Direccion: ")
    contrasena = input("Contrasena: ")

    tipo = input("Tipo de usuario (medico/administrativo): ").lower()

    if tipo != "medico" and tipo != "administrativo":

        print("Tipo de usuario incorrecto.")
        return

    # Generar hash de la contrasena
    contrasena_hash = generar_hash(contrasena)

    nuevo_usuario = {

        "identificacion": identificacion,
        "nombre": nombre,
        "apellidos": apellidos,
        "telefono": telefono,
        "correo": correo,
        "direccion": direccion,
        "contrasena": contrasena_hash,
        "tipo": tipo

    }

    usuarios.append(nuevo_usuario)

    guardar_datos(datos)

    print("\nUsuario registrado correctamente.")