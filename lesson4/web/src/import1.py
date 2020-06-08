import csv
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
    f = open('flights.csv')
    reader = csv.reader(f)
    for o, dest, dur in reader:
        flight = Flight(origin=o, destination=dest, duration=dur)
        db.session.add(flight)
        print(f'Added flight:\n{o},{dest},{dur}')
    db.session.commit()
    
if __name__ == "__main__":
    # La sentencia with nos permite interactuar por consola con nuestra aplicacion flask
    with app.app_context():
        main()