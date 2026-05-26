##  Descripción General

Este programa simula un sistema básico de inicio de sesión (login) en
consola.\
Permite hasta **3 intentos** para ingresar un usuario y contraseña
válidos, aplicando varias validaciones de seguridad sobre la contraseña.

------------------------------------------------------------------------

##  1. Mensaje Inicial

``` python
print("Loggin")
```

Muestra en pantalla el título del programa.

------------------------------------------------------------------------

##  2. Variable de Control de Intentos

``` python
intentos = 0
```

Se crea una variable llamada `intentos` que controla cuántas veces el
usuario ha intentado iniciar sesión.

------------------------------------------------------------------------

##  3. Bucle Principal

``` python
while intentos < 3:
```

El programa se ejecuta dentro de un bucle `while` que permite un máximo
de **3 intentos**.

------------------------------------------------------------------------

##  4. Entrada de Datos

``` python
user = input("Usuario: ")
password = input("Contraseña: ")
```

Se solicitan al usuario: - Nombre de usuario - Contraseña

------------------------------------------------------------------------

##  5. Validaciones

El programa valida la información en el siguiente orden:

### 5.1 Usuario vacío

``` python
if user == "":
```

Si el usuario está vacío: - Muestra un mensaje de error - Suma un
intento

------------------------------------------------------------------------

### 5.2 Contraseña vacía

``` python
elif password == "":
```

Verifica que la contraseña no esté vacía.

------------------------------------------------------------------------

### 5.3 Espacios en la contraseña

``` python
elif " " in password:
```

No permite espacios dentro de la contraseña.

------------------------------------------------------------------------

### 5.4 Longitud mínima

``` python
elif len(password) < 8:
```

La contraseña debe tener **mínimo 8 caracteres**.

------------------------------------------------------------------------

### 5.5 Debe contener al menos un número

``` python
elif not any(c.isdigit() for c in password):
```

-   `any()` verifica si existe al menos un carácter que sea número.
-   `isdigit()` comprueba si un carácter es un dígito.

------------------------------------------------------------------------

### 5.6 Debe contener al menos una letra

``` python
elif not any(c.isalpha() for c in password):
```

-   `isalpha()` verifica si el carácter es una letra.

------------------------------------------------------------------------

### 5.7 Credenciales correctas

``` python
elif user == "admin" and password == "admin2026":
```

Si el usuario es `"admin"` y la contraseña `"admin2026"`: - Se concede
acceso - Se rompe el bucle con `break`

------------------------------------------------------------------------

### 5.8 Caso contrario

``` python
else:
```

Si ninguna condición anterior se cumple: - Acceso denegado - Se suma un
intento

------------------------------------------------------------------------

##  6. Mostrar Intentos

``` python
print(f"Intentos: {intentos}")
```

Muestra cuántos intentos se han realizado hasta el momento.

------------------------------------------------------------------------

##  7. Bloqueo por Demasiados Intentos

``` python
if intentos >= 3:
    print("Demasiados intentos. Acceso bloqueado.")
```

Si el usuario alcanza 3 intentos fallidos: - El sistema bloquea el
acceso - Muestra un mensaje final
