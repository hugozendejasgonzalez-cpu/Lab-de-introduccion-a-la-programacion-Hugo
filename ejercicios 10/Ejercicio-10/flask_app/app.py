from flask import Flask, render_template, request, redirect, session, url_for

#cambie el proyecto de streamlit a flask

app = Flask(__name__)
app.secret_key = "clave_secreta"

# -------------------
# LOGIN
# -------------------
@app.route("/", methods=["GET", "POST"])
def login():
    if "intentos" not in session:
        session["intentos"] = 0

    if request.method == "POST":
        user = request.form.get("user")
        password = request.form.get("password")

        if session["intentos"] >= 3:
            return render_template("login.html", error="Demasiados intentos. Acceso bloqueado.")

        if user == "":
            return render_template("login.html", warning="El usuario no puede estar vacío.")
        elif password == "":
            return render_template("login.html", warning="La contraseña no puede estar vacía.")
        elif " " in password:
            return render_template("login.html", warning="La contraseña no debe contener espacios.")
        elif len(password) < 8:
            return render_template("login.html", warning="Debe tener al menos 8 caracteres.")
        elif not any(c.isdigit() for c in password):
            return render_template("login.html", warning="Debe contener al menos un número.")
        elif not any(c.isalpha() for c in password):
            return render_template("login.html", warning="Debe contener al menos una letra.")

        if user == "admin" and password == "admin2026":
            session["logged_in"] = True
            return redirect(url_for("menu"))
        else:
            session["intentos"] += 1
            return render_template("login.html", error=f"Acceso denegado. Intentos: {session['intentos']}")

    return render_template("login.html")


# -------------------
# MENÚ PRINCIPAL
# -------------------
@app.route("/menu")
def menu():
    if not session.get("logged_in"):
        return redirect(url_for("login"))
    return render_template("menu.html")


# -------------------
# ACCIONES
# -------------------
@app.route("/accion/<tipo>")
def accion(tipo):
    mensajes = {
        "numeros": "Función 'Clasificar número' activada",
        "edad": "Función 'Categoría de edad' activada",
        "tarifa": "Función 'Calcular tarifa' activada"
    }
    return mensajes.get(tipo, "Acción desconocida")


# -------------------
# LOGOUT
# -------------------
@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("login"))


if __name__ == "__main__":
    app.run(debug=True)