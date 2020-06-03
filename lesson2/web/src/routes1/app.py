from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello!"

# Empezamos a construir url dinamicas
# esperamos un elemento de tipo string al que almacenaremos en la variable
# que llamamos "name"
@app.route("/<string:name>")
def hello(name):
    name = name.capitalize()
    return f"<h1>Hello, {name}!</h1>"