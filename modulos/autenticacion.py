import hashlib

from modulos.persistencia import cargar_datos


def generar_hash(contrasena):

    contrasena_hash = hashlib.sha256(
        contrasena.encode()
    ).hexdigest()

    return contrasena_hash


def iniciar_sesion():

    datos = cargar_datos()

    usuarios = datos["usuarios"]

    print("\n================================")
    print("       INICIO DE SESION")
    print("================================")

    correo = input("Correo electronico: ")
    contrasena = input("Contrasena: ")

    # Convertir la contrasena a hash
    contrasena_hash = generar_hash(contrasena)

    # Buscar el usuario
    for usuario in usuarios:

        if usuario["correo"] == correo:

            if usuario["contrasena"] == contrasena_hash:

                print("\nBienvenido", usuario["nombre"])

                return usuario

            else:

                print("\nContrasena incorrecta.")
                return None