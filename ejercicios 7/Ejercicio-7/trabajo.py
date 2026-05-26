def login():
    intentos = 0

    while intentos < 3:

        user = input("Usuario: ")
        password = input("Contraseña: ")

        if user == "":
            print("El usuario no puede estar vacío.")

        elif password == "":
            print("La contraseña no puede estar vacía.")

        elif " " in password:
            print("La contraseña no debe contener espacios.")

        elif len(password) < 8:
            print("La contraseña debe tener al menos 8 caracteres.")

        elif not any(c.isdigit() for c in password):
            print("La contraseña debe contener al menos un número.")

        elif not any(c.isalpha() for c in password):
            print("La contraseña debe contener al menos una letra.")

        else:
            match (user, password):
                case ("admin", "admin2026"):
                    print("Acceso concedido")
                    return True

                case _:
                    intentos += 1
                    print("Acceso denegado")
                    print(f"Intentos: {intentos}")

    print("Demasiados intentos. Acceso bloqueado.")
    return False


def clasificar_numero():

    while True:

        numero = input("Ingrese un número (* para regresar): ")

        match numero.lower():

            case "*":
                break

            case _:
                try:
                    numero = int(numero)

                    match numero:
                        case 0:
                            print("Es 0.")

                        case n if n < 0:
                            print("Es negativo.")

                        case _:
                            print("Es positivo.")

                    match numero % 2:
                        case 0:
                            print("Es par.")
                        case _:
                            print("Es impar.")

                except:
                    print("Ingrese un número válido.")


def categoria_edad():

    edad = int(input("Ingrese su edad: "))

    match edad:

        case e if e <= 12:
            print("Categoria: Niñez")
            print("No puedes registrarte.")

        case e if 13 <= e < 18:
            print("Categoria: Adolescencia")
            print("Puedes registrarte con ayuda de un tutor")

        case e if 18 <= e < 64:
            print("Categoria: Adultez")
            print("Puedes registrarte sin tutor.")

        case _:
            print("Categoria: Adulto mayor")

    licencia = input("¿Cuentas con licencia?(s/n): ").lower()

    match licencia:
        case "s":
            print("Puede conducir.")
        case "n":
            print("No puedes conducir.")

    identificacion = input("¿Cuentas con identificación?(s/n): ").lower()

    if edad >= 21 and identificacion == "s":
        print("Tienes servicio VIP.")


def calcular_tarifa():

    precioBase = 200
    recargo = 0
    descuento = 0

    edad = int(input("Ingrese su edad: "))
    dia = input("Día de la semana (1-7): ")

    if not dia.isdigit():
        print("Ingrese un dia de la semana válido. (1-7)")
        return
    
    dia = int(dia)

    match dia:
        case 6 | 7:
            recargo += 10
        case 1 | 2 | 3 | 4 | 5:
            pass
        case _:
            print("El dia debe estar entre 1 y 7.")
            return

    estudiante = input("¿Eres estudiante? (s/n): ").lower()
    miembro = input("¿Eres miembro? (s/n): ").lower()
    metodoPago = input("Método de pago (e/t): ").lower()

    match edad:
        case e if 0 <= e <= 12:
            descuento += 50
        case e if 13 <= e <= 17:
            descuento += 20
        case e if e >= 65:
            descuento += 30

    if edad >= 13 and estudiante == "s":
        descuento += 15

    if miembro == "s":
        descuento += 10

    if descuento > 60:
        descuento = 60

    match metodoPago:
        case "e":
            recargo += 5

    recargoTotal = precioBase * recargo / 100
    descuentoTotal = precioBase * descuento / 100
    total = precioBase + recargoTotal - descuentoTotal

    print(f"Precio base: ${precioBase}")
    print(f"Recargo aplicado: {recargo}% -> ${recargoTotal}")
    print(f"Descuento aplicado: {descuento}% -> ${descuentoTotal}")
    print(f"Precio final: ${total}")


def menu():

    while True:

        print("\n1. Clasificar número")
        print("2. Categoria de edad y permisos")
        print("3. Calcular tarifa final")
        print("4. Cerrar sesión")
        print("5. Final")

        opcion = input("Seleccione una opción: ")

        if not opcion.isdigit():
            print("Error, opción inválida.")
            continue

        opcion = int(opcion)

        match opcion:

            case 1:
                clasificar_numero()

            case 2:
                categoria_edad()

            case 3:
                calcular_tarifa()

            case 4:
                print("Sesión cerrada.")
                login()

            case 5:
                print("Programa finalizado.")
                break

            case _:
                print("Error, opción inválida.")


print("Iniciar Sesión")

if login():
    menu()