from modulos.autenticacion import iniciar_sesion
from modulos.usuarios import registrar_usuario
from modulos.pacientes import registrar_paciente
from modulos.diagnosticos import registrar_diagnostico
from modulos.historia_clinica import consultar_historia_clinica


print("================================")
print("          CLINICA ACME")
print("    SISTEMA DE GESTION CLINICA")
print("================================")


# Iniciar sesion
usuario_actual = iniciar_sesion()


# Comprobar si el usuario ingreso correctamente
if usuario_actual is not None:

    while True:

        print("\n===== MENU PRINCIPAL =====")

        print("Usuario:", usuario_actual["nombre"])
        print("Tipo:", usuario_actual["tipo"])

        print("\n1. Registrar usuario")
        print("2. Registrar paciente")
        print("3. Diagnosticar paciente")
        print("4. Consultar historia clinica")
        print("5. Salir")

        opcion = input("\nSeleccione una opcion: ")

        if opcion == "1":

            registrar_usuario()

        elif opcion == "2":

            registrar_paciente()

        elif opcion == "3":

            registrar_diagnostico(usuario_actual)

        elif opcion == "4":

            consultar_historia_clinica()

        elif opcion == "5":

            print("\nGracias por utilizar el sistema ACME.")
            break

        else:

            print("\nOpcion incorrecta. Intente nuevamente.")

else:

    print("\nNo fue posible ingresar al sistema.")
    print("Programa finalizado.")