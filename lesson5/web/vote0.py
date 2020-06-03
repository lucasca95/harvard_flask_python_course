import os
import requests as req
from flask import Flask, render_template, request, jsonify, abort

# enviar y recibir web socket events
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'maisicretki'
app.config['ENV'] = 'development'
app.config['DEBUG'] = True
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html')

# El socket recibe de parte del cliente un evento de nombre 'submit vote'
@socketio.on('submit_vote')
def vote(data):
    print(f'Se imprime data: {data}')
    selection = data["selection"]

    # Emitimos un evento, una señal, de nombre 'announce vote'
    # el parametro broadcast=True permite enviar la informacion a todos los sockets que esten escuchando, incluyendo el usuario actual
    emit('announce vote', {'selection': selection}, broadcast=True)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)