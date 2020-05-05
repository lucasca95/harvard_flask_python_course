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

# Las variables de esa seccion permanecen activas
# hasta que muera el servidor
votes = {'yes': 0, 'no': 0, 'maybe': 0}

@app.route('/')
def index():
    return render_template('index_vote1.html', votes=votes)

# El socket recibe de parte del cliente un evento de nombre 'submit vote'
@socketio.on('submit_vote')
def vote(data):
    print(f'Se imprime data: {data}')
    selection = data["selection"]
    votes[selection] += 1
    # Emitimos un evento, una señal, de nombre 'announce vote'
    # el parametro broadcast=True permite enviar la informacion a todos los sockets que esten escuchando, incluyendo el usuario actual
    emit('announce vote', {'yes': votes['yes'], 'no': votes['no'], 'maybe': votes['maybe']}, broadcast=True)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)