print("Iniciar Sesión")

intentos = 0

while intentos < 3:

    user = input("Usuario: ")
    password = input("Contraseña: ")

    if user == "":
        print("El usuario no puede estar vacío.")
        intentos += 1

    elif password == "":
        print("La contraseña no puede estar vacía.")
        intentos += 1

    elif " " in password:
        print("La contraseña no debe contener espacios.")
        intentos += 1

    elif len(password) < 8:
        print("La contraseña debe tener al menos 8 caracteres.")
        intentos += 1

    elif not any(c.isdigit() for c in password):
        print("La contraseña debe contener al menos un número.")
        intentos += 1

    elif not any(c.isalpha() for c in password):
        print("La contraseña debe contener al menos una letra.")
        intentos += 1

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