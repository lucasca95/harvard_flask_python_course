import csv
import os

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

# Check for environment variable
if not os.getenv("DATABASE_URL"):
    raise RuntimeError("DATABASE_URL is not set")

# Set up database
engine = create_engine(os.getenv("DATABASE_URL"))
db = scoped_session(sessionmaker(bind=engine))

def main():
    try:
        file_name = "books.csv"
        f = open(file_name)
        reader = csv.reader(f)
        print("Se abre el archivo .csv")
        line = 0
        for book_isbn, book_title, book_author, book_year in reader:
            if line == 0:
                print(book_isbn, book_title, book_author, book_year)
                line += 1
            else:
                # format data before adding to db
                book_isbn = book_isbn.lower()
                book_title = book_title.lower()
                book_author = book_author.lower()

                db.execute("INSERT INTO books (book_isbn, book_title, book_author, book_year) VALUES (:book_isbn, :book_title, :book_author, :book_year)",
                {"book_isbn": book_isbn, "book_title": book_title, "book_author": book_author, "book_year": book_year})
                print(f"\nSe agrega libro: {book_isbn}, {book_title}, {book_author}, {book_year}\n")
        db.commit()
        print("Libros agregados a BDD")
        f.close()
        print("Archivo cerrado.")
    except FileNotFoundError as e:
        print(f"Hubo error al abrir archivo: \n{e}.")

if __name__ == "__main__":
    main()