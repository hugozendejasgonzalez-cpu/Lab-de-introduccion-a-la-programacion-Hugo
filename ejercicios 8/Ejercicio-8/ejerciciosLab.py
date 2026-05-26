def validarEntradaInt(mensaje):
    while True:
        try:
            n = int(input(mensaje))

            if n < 0:
                print("El número debe ser mayor a 0.")
                continue
            return n
        except ValueError:
            print("Ingrese una cantidad válida.")
        
def validarEntradaFloat(mensaje):
    while True:
        try:
            n = float(input(mensaje))

            if n < 0:
                print("La cantidad debe ser mayor o igual a 0.")
                continue
            return n
        except ValueError:
            print("Ingrese una cantidad válida.")

def imprimirDiezVeces():
    palabra = input("Ingrese una palabra: ")

    for i in range(10):
        print(palabra)

def añosCumplidos():
    edad = validarEntradaInt("Ingrese su edad:")

    for i in range(1, edad + 1):
        print(i)

def numerosImpares():
    numero = validarEntradaInt("Ingrese un número positivo: ")

    print(", ".join(str(i) for i in range(0, numero + 1) if i % 2 != 0))

def cuentaAtras():
    numero = validarEntradaInt("Ingrese un número positivo: ")

    print(", ".join(str(i) for i in range(numero, -1, -1)))

def capitalObtenido():
    capitalInicial = validarEntradaFloat("Ingrese el capital inicial: ")
    interesAnual = validarEntradaFloat("Ingrese el interes anual: ")
    añosInversion = validarEntradaInt("Ingrese el número de años de la inversión: ")

    for i in range(1, añosInversion + 1):
        capitalObtenido = capitalInicial * (1 + interesAnual / 100)**i
        print(f"Año {i}: {capitalObtenido:.2f}")

def trianguloRectangulo():
    altura = validarEntradaInt("Ingrese la altura: ")
    
    for i in range(0, altura + 1):
        print("*" * i)

def tablaUnoDiez():
    for i in range(0, 11):
        print()
        print(f"Tabla de multiplicar del {i}")
        for j in range(0, 11):
            resultado = i * j
            print(f"{i} x {j} = {resultado}")

def trianguloImpares():
    altura = validarEntradaInt("Ingrese la altura: ")

    for i in range(1, altura + 1):
        for j in range(2*i -1, 0, -2):
            print(j, end=" ")
        print()

def contraseñaCorrecta():
    contraseña = "python123"

    while True:
        entrada = input("Ingrese la contraseña: ")

        if entrada != contraseña:
            print("Contraseña incorrecta.")
            continue

        if entrada == contraseña:
            print("Contraseña correcta.")
            break

def numeroPrimo():
    numero = validarEntradaInt("Ingrese un número primo: ")

    esPrimo = True

    if numero <= 1:
        esPrimo = False
    else:
        for i in range(2, int(numero ** 0.5) + 1):
            if numero % i == 0:
                esPrimo = False
    
    if esPrimo:
        print("Es primo.")
    else:
        print("No es primo.")

def palabraInversa():
    palabra = input("Ingrese una palabra: ")

    for letra in palabra[::-1]:
        print(letra)

def letraEnFrase():
    frase = input("Ingrese una frase: ").lower()
    letraBuscar = input("Letra: ").lower()

    cantidad = 0

    for letra in frase:
        if letra == letraBuscar:
            cantidad += 1

    print(f"La letra '{letraBuscar.upper()}' se encuentra {cantidad} veces en la frase '{frase}'")

def eco():
    while True:
        entrada = input("Escribe algo o 'salir' para salir: ")

        if entrada.lower() == "salir":
            print("Programa finalizado")
            break

        print(f"eco: {entrada}")

while True:
    print()
    print()
    print()
    print("Menu")
    print("1.- Mostrar 10 veces una palabra.")
    print("2.- Año que has cumplido.")
    print("3.- Números impares")
    print("4.- Cuenta atras.")
    print("5.- Capital obtenido.")
    print("6.- Triangulo rectangulo de *")
    print("7.- Tablas de multiplicar del 1 al 10.")
    print("8.- Triangulo rectangulo numeros impares.")
    print("9.- Contraseña.")
    print("10.- Número primo o no primo.")
    print("11.- Letras de palabra invertida.")
    print("12.- Cuantas veces aparece la letra.")
    print("13.- Eco.")
    print("e.- salir")

    opcion = input("Seleccione una opción: ")

    match opcion:
        case "1": imprimirDiezVeces()
        case "2": añosCumplidos()
        case "3": numerosImpares()
        case "4": cuentaAtras()
        case "5": capitalObtenido()
        case "6": trianguloRectangulo()
        case "7": tablaUnoDiez()
        case "8": trianguloImpares()
        case "9": contraseñaCorrecta()
        case "10": numeroPrimo()
        case "11": palabraInversa()
        case "12": letraEnFrase()
        case "13": eco()
        case "e" | "E":
            break
        case _:
            print("opción no válida")