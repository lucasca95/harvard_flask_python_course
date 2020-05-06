from flask import Flask, render_template

app = Flask(__name__)
app.config['ENV'] = 'development'
app.config['DEBUG'] = True


@app.route('/')
def first():
    return render_template('first.html')

@app.route('/second')
def second():
    return render_template('second.html')

@app.route('/third')
def third():
    return render_template('third.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)