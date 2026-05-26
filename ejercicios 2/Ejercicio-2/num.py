def convertir(numero):
    return {
        "Binario": bin(numero),
        "Hexadecimal": hex(numero),
        "Octal": oct(numero),
        "Booleano": bool(numero)
    }

def menu():
    while True:
        print("\nCONVERSOR DE NÚMEROS")
        print("1. Convertir")
        print("2. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "2":
            print("Saliendo.")
            break

        if opcion == "1":
            try:
                numero = int(input("Ingrese un número decimal: "))
                resultados = convertir(numero)

                print("\n/// RESULTADS ///")
                for tipo, valor in resultados.items():
                    print(f"{tipo}: {valor}")

            except ValueError:
                print("Entrada inválida.")

        else:
            print("Opción no válida.")


menu()