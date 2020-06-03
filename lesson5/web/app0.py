import os
import requests as req
from flask import Flask, session, render_template, request, redirect, url_for, jsonify, abort

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        # ver qué hacemos con el get
        return render_template("index.html", message="")
    elif request.method == "POST":
        return 'Index por POST'
    else:
        return 'Error en metodo HTTP'

@app.route('/convert', methods=['POST', 'GET'])
def convert():
    if request.method == 'POST':
        currency = request.form.get('currency')
        print(f'Valor de currency: {currency}')
        
        res = req.get('http://api.fixer.io/latest', params={
            'base': 'USD', 'symbols': currency })
        if res.status_code != 200:
            return jsonify({'success': False})
        data = res.json()
        if currency not in data['rates']:
            return jsonify({'success': False})
        return jsonify({'success': True, 'rate': data['rates'][currency]})
    else:
        return "<h4>Metodo no valido para /convert</h4>"

if __name__ == "__main__":
    app.run()