from flask import Flask, render_template

app = Flask(__name__)
app.config['ENV'] = 'development'
app.config['DEBUG'] = True

# Este proyecto controla la vista de la url aun siendo una aplicacion 
# single-page utilizando HTML5 History API.

@app.route('/')
def index():
    return render_template('index.html')

texts = ['Aunque la frase no tiene sentido, tiene una larga historia. Durante varios siglos, los tipógrafos han utilizado esta frase para mostrar las características más distintivas de sus fuentes. Se utiliza porque las letras que contiene y el espaciado entre caracteres de esas combinaciones revelan de la mejor forma posible el espesor, el diseño y otras características importantes del tipo de letra.', 
'Un ejemplar de 1994 de la revista "Before & After" asocia "Lorem ipsum ..." a una versión latina revuelta de un pasaje de de Finibus Bonorum et Malorum, un tratado sobre la teoría de la ética escrito por Cicerón en el año 45 A.C. El pasaje "Lorem ipsum..." se ha extraído del texto que dice "Neque porro quisquam est qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit...", que se traduciría como "No hay nadie que ame el dolor mismo, que lo busque y lo quiera tener, simplemente porque es el dolor...".', 
'Durante los años 1500, una imprenta adaptó el texto de Cicerón para elaborar una página de ejemplos de tipografía. Desde entonces, el texto en latín ha sido la norma del sector de la tipografía para simular texto. Antes de que existiera la publicación electrónica, los diseñadores gráficos tenían que simular diseños utilizando líneas ficticias para indicar texto. La llegada de hojas autoadhesivas preimpresas con "Lorem ipsum" ofreció una manera más realista de indicar dónde debería ir el texto en una página.']

@app.route('/first')
def first():
    return texts[0]

@app.route('/second')
def second():
    return texts[1]

@app.route('/third')
def third():
    return texts[2]

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)