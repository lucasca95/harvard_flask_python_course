import time

from flask import Flask, render_template, jsonify, request

app = Flask(__name__)
app.config['ENV'] = 'development'
app.config['DEBUG'] = True

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/posts', methods=['POST'])
def posts():
    start = int(request.form.get('start') or 0)
    end = int(request.form.get('end') or (start+9))

    # Generar lista de posts
    data = []
    for i in range(start, end+1):
        data.append(f'Post #{i}')

    # simulamos un retardo
    time.sleep(1)

    # devolver lista de posts en formato JSON
    return jsonify(data)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)