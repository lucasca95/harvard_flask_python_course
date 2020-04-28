import os
import sys
import requests as req
import xml.etree.ElementTree as ET
from flask import Flask, session, render_template, request, redirect, url_for, jsonify, abort
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker


if not os.getenv("DATABASE_URL"):
    raise RuntimeError("DATABASE_URL is not set")

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY")
app.config["SESSION_PERMANENT"] = False
app.config['SESSION_TYPE'] = 'filesystem'

# Set up database
engine = create_engine(os.getenv("DATABASE_URL"))
db = scoped_session(sessionmaker(bind=engine))


@app.route("/", methods=["GET", "POST"])
def index():

    print(f'\n\nIngresamos a "index" por {request.method}\n')

    if user_not_logged():
        # No hay usuario logueado
        return render_template("login.html", message="")
    
    # Index code
    # Ver quien es el usuario logueado
    user_email = session['user_email']

    if request.method == "GET":
        # ver qué hacemos con el get
        return render_template("index.html", message="")
    elif request.method == "POST":
        # ver qué hacemos con el POST
        book_isbn = request.form.get('book_isbn')
        book_title = request.form.get('book_title')
        book_author = request.form.get('book_author')

        # Mensaje de control de búsqueda
        # print(f'Buscamos ISBN: "{book_isbn}", title: "{book_title}", author: "{book_author}".', file=sys.stderr)
    
        target = ""

        # Si el usuario ingresó algo en los campos del formulario, modificamos el string para buscar con LIKE
        if book_isbn != "":
            target += f" ISBN: \n{book_isbn.upper()}\""
            book_isbn = f"%{book_isbn}%"
        if book_title != "":
            target += f" Title: \"{book_title.capitalize()}\""
            book_title = f"%{book_title.lower()}%"
        if book_author != "":
            aux = str()
            for w in book_author.split(" "):
                aux += w.capitalize() + " "
            aux = aux.rstrip()
            target += f" Author: \"{aux}\"" # msg only seen by user
            book_author = f"%{book_author.lower()}%"
        
        target += "."

        # Buscar libros en BDD que cumplan con lo pedido
        books = db.execute("SELECT book_id, book_isbn, book_title, book_author FROM books WHERE book_isbn LIKE :book_isbn OR book_title LIKE :book_title OR book_author LIKE :book_author",
        {"book_isbn": book_isbn, "book_title": book_title, "book_author": book_author}).fetchall()

        # Mensaje de control de búsqueda
        # print(f"\nNumber of results found: {len(books)}\n", file=sys.stderr)

        # si no hay resultados
        if len(books) == 0:
            return render_template("index.html", message="No results found", target=target) 
        # si existen resultados
        else:
            return render_template("index.html", message="We found some results", target=target, books=books)
    else:
        return render_template("error.html", message="Index accessed by not allowed method.")

@app.route("/login", methods=["GET","POST"])
def login():
    print(f'\n\nIngresamos a "login" por {request.method}\n')

    if request.method == "POST":
        print("Entramos a /login por POST", file=sys.stderr)
        user_email = request.form.get('user_email')
        user_password = request.form.get('user_password')
        
        # Un usuario se quiere loguear. Buscar si existe en BDD
        # INICIO Buscar usuario
        user = db.execute("SELECT user_email, user_level FROM users WHERE (users.user_email = :user_email AND users.user_password = :user_password)",
        {"user_email": user_email, "user_password": user_password}).fetchone()
        # FIN Buscar usuario

        # si no existe
        if user is None:
            return render_template("login.html", message="Your email or password is incorrect. Please try again.") 
        # si existe
        else:
            # Usuario existente logueado correctamente
            session['user_email'] = user.user_email
            session['user_level'] = user.user_level
            return redirect(url_for('index'))
            # return render_template("index.html")

    print("Entramos a /login por un método que no es POST", file=sys.stderr)
    return render_template("error.html", message="Access violation error.")

@app.route("/logout")
def logout():
    print(f'\n\nIngresamos a "logout" por {request.method}\n')
    session.clear()
    # session.pop('user_email')
    return redirect(url_for('index'))

@app.route("/register", methods=["GET", "POST"])
def register():
    print(f'\n\nIngresamos a "register" por {request.method}\n')

    if user_not_logged():
        # No hay usuario logueado
        return render_template("login.html", message="")

    if request.method == "GET":
        return render_template("register.html", message="")
    elif request.method == "POST":
        # tomar datos
        user_fullname = request.form.get('user_fullname')
        user_email = request.form.get('user_email')
        user_password = request.form.get('user_password')

        # Intentar meterlo a la base de datos. Corroborar si el email ya existe
        user = db.execute("SELECT user_email FROM users WHERE (users.user_email = :user_email)",
        {"user_email": user_email}).fetchone()
        # si existe ya un usuario con el mismo email
        if user:
            # No puede registrarse
            return render_template("register.html", message="Error al registrar usuario. Email ya existente")
        # sino
        else:
            print(f"{user_fullname}, {user_email}, {user_password}", file=sys.stderr)
            db.execute("INSERT INTO users (user_fullname, user_email, user_password) VALUES (:user_fullname, :user_email, :user_password)",
            {"user_fullname": user_fullname, "user_email": user_email, "user_password": user_password})
            try:
                db.commit()
                session['user_email'] = user_email
                return render_template("index.html", user_email=user_email)
            except:
                return render_template("error.html", message="Error al registrar usuario. Error de BDD.")

@app.route("/admin", methods=["GET", "POST"])
def admin():
    print(f'\n\nIngresamos a "admin" por {request.method}\n')

    if user_not_logged():
        # No hay usuario logueado
        return render_template("login.html", message="")
    
    if (user_is_admin() == False):
        # No tiene permisos para estar acá
        return render_template("error.html", message="No tiene suficientes permisos para acceder a esta página.")
    else:
        print("El usuario es admin, dentro de admin()", file=sys.stderr)
        # El usuario es admin
        return render_template("admin.html")

@app.route("/book/<int:book_id>/", methods=["GET", "POST"])
def book(book_id):
    print(f'\n\nIngresamos a "book" por {request.method}\n')

    if user_not_logged():
        # No hay usuario logueado
        return render_template("login.html", message="")

    book = db.execute("SELECT book_id, book_isbn, book_title, book_author, book_year FROM books WHERE book_id = :book_id",
            {"book_id": book_id}).fetchone()

    book_reviews = db.execute("SELECT r.user_id, u.user_fullname, r.review_rating, r.review_content, r.review_id, r.book_id FROM reviews AS r INNER JOIN books AS b ON r.book_id = b.book_id INNER JOIN users as u ON r.user_id = u.user_id WHERE b.book_id = :book_id ORDER BY r.review_id",
    {"book_id": book_id}).fetchall()

    # si existe un libro con el ID pedido
    if (book):
        api_results = get_api_results(book.book_isbn)
        return render_template("book.html", message="", book=book, book_reviews=book_reviews, can_make_review=user_can_make_review(book_id), api_results=api_results)
    else:
        return render_template("error.html", message=f"No book found with id {book.book_id}")
            
@app.route("/review/create/<int:book_id>/", methods=["GET", "POST"])
def review_create(book_id):
    print(f'\n\nIngresamos a "review_create" por {request.method}\n')

    if user_not_logged():
        # No hay usuario logueado
        return render_template("login.html", message="")

    if request.method == "GET":
        # Usuario quiere crear una review para el libro seleccionado.
        # Hay que corroborar que no haya hecho otras reviews para este libro antes.

        if (user_can_make_review(book_id)):
            book = get_book_by_id(book_id)
            if (book):
                # if book exists
                return render_template("review_create.html", message=f"", book=book)
            else:
                return render_template("error.html", message=f"No book found with ID: {book_id}.")
        else:
            return render_template("error.html", message=f"You already have written a review for this book")

    elif request.method == "POST":
        # Tomar datos del formulario
        review_rating = request.form.get("review_rating")
        review_content = request.form.get("review_content")
        book_id = request.form.get("book_id")

        db.execute("INSERT INTO reviews (review_rating, review_content, user_id, book_id) VALUES (:review_rating, :review_content, :user_id, :book_id)",
        {"review_rating": review_rating, "review_content": review_content, "user_id": actual_user_id(), "book_id": book_id})

        db.commit()

        return redirect(url_for('book', book_id=book_id))
    else:
        return render_template("error.html", message="Entramos a review/create por Método raro")

@app.route("/api/<api_isbn>", methods=["GET"])
def api(api_isbn):
    api_results = get_more_api_results(api_isbn)
    if (api_results):
        return jsonify(api_results)
    else:
        abort(404)

@app.route("/profile", methods=["GET"])
def profile():
    if user_not_logged():
        return render_template('login.html', message='You need to be logged in to access "/profile".')

    user = db.execute("SELECT * FROM users WHERE user_id = :user_id",
    {"user_id": actual_user_id()}).fetchone()

    return render_template("profile.html", user=user)

@app.errorhandler(404)
def isbn_not_found(error):
    return render_template("error.html", message="Error 404. ISBN not found on Goodreads API.")

#########################################################################################
#########################################################################################
#########################################################################################

def user_not_logged():
    return (session.get('user_email') is None)

def user_is_admin():
    return (session['user_level'] == 0)

def actual_user_id():
    u = db.execute("SELECT user_id FROM users WHERE user_email = :user_email",
    {"user_email": session['user_email']}).fetchone()
    return u.user_id

def user_can_make_review(book_id):
    result = db.execute("SELECT * FROM reviews AS r WHERE r.user_id = :user_id AND r.book_id = :book_id",
    {"user_id": actual_user_id(), "book_id": book_id}).fetchone()
    if (result):
        # print(f"\nEl usuario con ID={actual_user_id()} NO PUEDE crear una review\n", file=sys.stderr)
        return False
    else:
        # print(f"\nEl usuario con ID={actual_user_id()} TIENE PERMITIDO crear una review\n", file=sys.stderr)
        return True    

def get_book_by_id(book_id):
    return db.execute("SELECT book_id, book_isbn, book_title, book_author, book_year FROM books WHERE book_id = :book_id",
    {"book_id": book_id}).fetchone()


# Uses https://hackersandslackers.com/xml-in-python/ to adapt XML to Python
def get_api_results(book_isbn):
    api_results = {}

    response = req.get(f"https://www.goodreads.com/search/index.xml?key={os.environ.get('GOODREADS_KEY')}&q={book_isbn}")
    
    # Creamos objeto e para leer árbol XML
    # Un objeto e tiene atributos útiles: tag, attrib y text.
    e = ET.fromstring(response.content)

    # e             -> <GoodreadsResponse>
    # e[1]          -> <search>
    # e[1][3]       -> <total-results>
    # e[1][6]       -> <results>
    # e[1][6][0]    -> <work>
    # e[1][6][0].find('tag_name')
    # e[1][6][0].findall('tag_name')

    # if we got results...
    if (int(e[1][3].text) != 0):
        api_results['average_rating'] = float(e[1][6][0].find('average_rating').text)
        api_results['ratings_count'] = int(e[1][6][0].find('ratings_count').text)
    
    return api_results

# Uses https://hackersandslackers.com/xml-in-python/ to adapt XML to Python
def get_more_api_results(book_isbn):
    api_results = {}

    response = req.get(f"https://www.goodreads.com/search/index.xml?key={os.environ.get('GOODREADS_KEY')}&q={book_isbn}")
    

    e = ET.fromstring(response.content)

    # if we got results...
    if (int(e[1][3].text) != 0):
        # e[1][6][0][8] -> <best_book>
        api_results['title'] = e[1][6][0][8][1].text
        api_results['author'] = e[1][6][0][8][2][1].text
        api_results['year'] = int(e[1][6][0][4].text)
        api_results['isbn'] = book_isbn
        api_results['review_count'] = int(e[1][6][0][3].text)
        api_results['average_rating'] = float(e[1][6][0][7].text)

        print(f"\n{api_results}\n", file=sys.stderr)
    
    return api_results