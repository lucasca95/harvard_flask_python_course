# Project 1

Web Programming with Python and JavaScript

This project is a website that allows the search of books. A user must log in to be able to browse the web pages. The home page allows you to search for books by ISBN, author title. Search words do not have to be exact. The books are searched in a cloud-based PostgreSQL database in Heroku and loaded using a ".csv" file (comma separated values)
Once the results are found, you will be allowed to access the details of a book. There you will see more information about the book. The website connects to the Goodreads API to request information about the indicated book to show it to the user, if it exists. In addition, the details of a book show the list of comments that users have made about it. If the user has not yet reviewed the book, they can do so. A user can create only one review for a book. The review involves a comment and a book score between 0.0 and 5.0.
The server backend is implemented with Flask microframework, which is written in Python. The website has an application that returns information from books in JSON format. It is accessed with the url "/ api / ISBN". If the ISBN exists the information is returned and if not, an error 404 is thrown. The entire project is dockerized to avoid the installation of tools on the development computer.
As a bonus, the level of permissions is implemented in users given that each one has a level, with level 0 being "administrator". Users can do or see different things according to their level.
Users are capable of viewing their profiles.

Missing functionalities that could be useful:
- Edit book reviews
- Delete book reviews

-------------------------------------------
-------------------------------------------

Este proyecto es un sitio web que permite la búsqueda de libros. Un usuario debe haber iniciado sesión para poder navegar por las páginas web.
La página de inicio permite buscar libros por ISBN, título o autor. Las palabras de búsqueda no tienen que ser exactas. Los libros se buscan en una base de datos PostgreSQL la cual está alocada en la nube, en Heroku, y fue cargada por medio de un archivo ".csv" (Comma Separated Values)
Una vez que se encuentren resultados se permetirá acceder a los detalles de un libro. Allí se verá más información sobre el libro. El sitio web se conecta con la API Goodreads para pedir información sobre el libro indicado para mostrarla al usuario, si existe. Además, en los detalles de un libro se muestra la lista de reseñas que hayan hecho los usuarios sobre el mismo. Si el usuario no ha hecho una reseña del libro aún, puede crearla. Un usuario puede crear sólo una reseña para un libro. La reseña implica un comentario y un puntaje del libro comprendido entre 0.0 y 5.0 .
El backend del servidor está implementado con el microframework Flask, el cual está escrito en Python.
El sitio web dispone de una api que devuelve información de libros en formato JSON. Se accede con la url "/api/ISBN". Si el ISBN existe se devuelve la información y si no, se arroja un error 404.
Todo el proyecto está dockerizado para evitar la instalación de herramientas en la computadora de desarrollo.
Como plus, está implementado el nivel de permisos en usuarios dado que cada uno tiene un nivel, siendo "administrador" el nivel 0. Los usuarios pueden hacer o ver distintas cosas según su nivel.
Los usuarios son capaces de ver sus perfiles.

Funcionalidades faltantes que podrían ser útiles:
- Editar reviews de libros
- Borrar reviews de libros