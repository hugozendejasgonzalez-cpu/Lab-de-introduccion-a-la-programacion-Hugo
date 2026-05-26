print("Iniciar Sesión")

intentos = 0
acceso = 0
subMenus = 0

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

    elif user == "admin" and password == "admin2026":
        print("Acceso concedido")
        acceso = 1
    
    else:
        print("Acceso denegado")
        intentos += 1
        print(f"Intentos: {intentos}")

    if intentos >= 3:
        print("Demasiados intentos. Acceso bloqueado.")
        break

    while acceso == 1:
        print("1. Clasificar número.")
        print("2. Categoria de edad y permisos.")
        print("3. Calcular tarifa final.")
        print("4. Cerrar sesión.")
        print("5. Final")

        opcion = input("Seleccione una opción: ")

        if not opcion.isdigit():
            print("Error, opción inválida.")
            continue

        opcion = int(opcion)

        if opcion == 1:
            subMenus = 1
            print("Clasificar número.")

            while subMenus == 1:
                numero = input("Ingrese un número (e para regresar): ")

                if numero.lower() == "e":
                    subMenus = 0

                else:
                    try:
                        numero = int(numero)

                        if numero == 0:
                            print("Es 0.")
                        elif numero < 0:
                            print("Es negativo.")
                        else:
                            print("Es positivo.")

                        if numero % 2 == 0:
                            print("Es par.")
                        else:
                            print("Es impar.")

                    except:
                        print("Ingrese un número válido.")

        elif opcion == 2:
            print("Categoria de edad y permisos.")
            edad = int(input("Ingrese su edad: "))

            if edad <= 12:
                print("Categoria: Niñez")
                print("No puedes registrarte.")

            elif 13 <= edad < 18:
                print("Categoria: Adolescencia")
                print("Puedes registrarte con ayuda de un tutor")

            elif 18 <= edad < 64:
                print("Categoria: Adultez")
                print("Puedes registrarte sin tutor.")

            licencia = input("¿Cuentas con licencia? (s/n): ").lower()

            if licencia == "s":
                print("Puede conducir.")
            else:
                print("No puedes conducir.")

            identificacion = input("¿Cuentas con identificación? (s/n): ").lower()

            if edad >= 21 and identificacion == "s":
                print("Tienes servicio VIP.")
            else:
                print("No tienes servicios VIP")

        elif opcion == 3:
            print("Calcular tarifa final.")

            precioBase = 200
            recargo = 0
            descuento = 0

            edad = int(input("Ingrese su edad: "))
            dia = int(input("Día de la semana (1-7): "))
            estudiante = input("¿Eres estudiante? (s/n): ").lower()
            miembro = input("¿Eres miembro? (s/n): ").lower()
            metodoPago = input("Método de pago (e/t): ").lower()

            if dia in [6, 7]:
                recargo += 10

            if 0 <= edad <= 12:
                descuento += 50
            elif 13 <= edad <= 17:
                descuento += 20
            elif edad >= 65:
                descuento += 30

            if edad >= 13 and estudiante == "s":
                descuento += 15

            if miembro == "s":
                descuento += 10

            if descuento > 60:
                descuento = 60

            if metodoPago == "e":
                recargo += 5

            recargoTotal = precioBase * recargo / 100
            descuentoTotal = precioBase * descuento / 100
            total = precioBase + recargoTotal - descuentoTotal

            print(f"Precio base: ${precioBase}")
            print(f"Recargo aplicado: {recargo}% -> ${recargoTotal}")
            print(f"Descuento aplicado: {descuento}% -> ${descuentoTotal}")
            print(f"Precio final: ${total}")

        elif opcion == 4:
            print("Sesión cerrada.")
            acceso = 0

        elif opcion == 5:
            acceso = -1
            break

        else:
            print("Error, opción inválida.")

    if acceso == -1:
        print("Programa Finalizado.")
        break