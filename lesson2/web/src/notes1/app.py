# Ahora las variables de session perteneceran a un unico usuario
# esto es gracias a tener "session" importada
from flask import Flask, render_template, request, session
# con Session podemos tener mas control sobre nuestras variables
# de sesión.
from flask_session import Session

app = Flask(__name__)

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Espacio para variables globales (a todos los usuarios)

@app.route("/", methods=["GET", "POST"])
def index():
    # si no hay notas aun, crear la variable de sesion para notas
    if session.get("notes") is None:
        session["notes"] = []

    if request.method == "POST":
        note = request.form.get("note")
        session["notes"].append(note)

    return render_template("index.html", notes=session["notes"])