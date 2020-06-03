import os

from flask import Flask, render_template, request
from config_file import DevelopmentConfig as DC
from models import *

app = Flask(__name__)
config = DC()
app.config.from_object(config)

# Viene definida en models.py
# Asociar esta base de datos a la aplicacion
db.init_app(app)

def main():
    db.create_all()

if __name__ == "__main__":
    # La sentencia with nos permite interactuar por consola con nuestra aplicacion flask
    with app.app_context():
        main()