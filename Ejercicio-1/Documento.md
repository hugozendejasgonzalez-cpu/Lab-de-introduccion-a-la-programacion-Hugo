# Crear un entorno virtual en Python con VS Code (Windows)

Esta guía explica **de forma sencilla** cómo crear y usar un entorno virtual de Python en **Visual Studio Code** si usas **Windows**.

---

## ¿Qué es un entorno virtual y por qué usarlo?

Un entorno virtual es básicamente un **espacio aislado** para tu proyecto.

Sirve para:

* No mezclar librerías entre proyectos
* Evitar errores raros
* Tener todo más ordenado

En resumen: **usa entornos virtuales siempre**.

---

## Cosas que necesitas antes

Asegúrate de tener instalado:

* **Python 3**
* **Visual Studio Code**
* **Extensión de Python en VS Code** (la de Microsoft)

Para comprobar que Python está bien instalado, abre la terminal y escribe:

```bash
python --version
```

Si sale algo tipo `Python 3.x.x`, como lo siguiente, todo bien.

![Captura de pantalla](Assets/IMG/Captura%20de%20pantalla%202026-02-10%20190826.png)

---

## 1. Crear la carpeta del proyecto

1. Crea una carpeta (por ejemplo: `mi_proyecto_python`)

![Captura de pantalla](Assets/IMG/Captura%20de%20pantalla%202026-02-10%20191426.png)


2. Ábrela en **VS Code** (`Archivo → Abrir carpeta`)

![Captura de pantalla](Assets/IMG/Captura%20de%20pantalla%202026-02-10%20105705.png)

---

## 2. Abrir la terminal en VS Code

Dentro de VS Code:

* Presiona **Ctrl + Ñ**
* Se abrirá una terminal abajo

Asegúrate de que estés dentro de la carpeta del proyecto.

![Captura de pantalla](Assets/IMG/Captura%20de%20pantalla%202026-02-10%20105745.png)

---

## 3. Crear el entorno virtual

En la terminal escribe:

```bash
python -m venv venv
```

![Captura de pantalla](Assets/IMG/Captura%20de%20pantalla%202026-02-10%20191944.png)

Esto crea una carpeta llamada `venv` donde vive el entorno virtual.

![Captura de pantalla](Assets/IMG/Captura%20de%20pantalla%202026-02-10%20191859.png)

---

## 4. Activar el entorno virtual

### Si usas PowerShell (lo normal en VS Code):

```bash
venv\Scripts\Activate.ps1
```

### Si usas CMD:

```bash
venv\Scripts\activate
```

Si todo salió bien, verás algo así:

```text
(venv) C:\tu\proyecto>
```

![Captura de pantalla](Assets/IMG/Captura%20de%20pantalla%202026-02-10%20192139.png)

Ese `(venv)` significa que **ya estás dentro del entorno virtual**.

---

## 5. Decirle a VS Code qué Python usar

Esto es importante para que VS Code no se confunda.

1. Presiona **Ctrl + Shift + P**
2. Escribe: `Python: Select Interpreter`
3. Elige el que diga algo como:

```text
venv\Scripts\python.exe
```

![Captura de pantalla](Assets/IMG/Captura%20de%20pantalla%202026-02-10%20192317.png)

Listo, VS Code ya sabe qué Python usar 

---

## 6. Instalar librerías

Con el entorno activado, instala librerías, por ejemplo:

```bash
pip install numpy
```

![Captura de pantalla](Assets/IMG/Captura%20de%20pantalla%202026-02-10%20192502.png)

Para ver lo que tienes instalado:

```bash
pip list
```

![Captura de pantalla](Assets/IMG/Captura%20de%20pantalla%202026-02-10%20192559.png)

## Resumen

```bash
python -m venv venv
venv\Scripts\activate
pip install lo_que_necesites
```

![Captura de pantalla](Assets/IMG/123.png)