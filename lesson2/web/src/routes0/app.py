from flask import Flask

# Indicamos a Flask por medio de "__name__" que este archivo "application.py"
# sera una aplicacion web.
app = Flask(__name__)

# el decorador permite indicar que hacer cuando se quiere acceder a la ruta indicada
# en este caso, "/"
@app.route("/")
def index():
    return "Hello!"

@app.route("/david")
def david():
    return "Hello, David!"