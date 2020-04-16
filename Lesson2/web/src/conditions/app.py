import datetime as dt

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    now = dt.datetime.now()
    new_year = (now.month == 1 and now.dat == 1)
    new_year = True # Para probar la respuesta positiva

    return render_template("index.html", new_year=new_year)
