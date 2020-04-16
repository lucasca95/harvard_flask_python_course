from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    headline = "Hello world from a variable!"
    # headline de la izq es el nombre de la variable en la vista
    # headline de la der es el nombre de la variable en el server
    return render_template("index.html", headline=headline)

# Ahora usamos el mismo idex.html pero con un contenido distinto!
@app.route("/bye/")
def bye():
    headline = "Goodbye!"
    return render_template("index.html", headline=headline)