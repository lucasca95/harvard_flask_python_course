-- Creación de tablas sin relaciones

CREATE TABLE users(
    user_id SERIAL PRIMARY KEY,
    user_fullname VARCHAR NOT NULL,
    user_email VARCHAR UNIQUE NOT NULL,
    user_password VARCHAR NOT NULL,
    user_level INTEGER NOT NULL DEFAULT 1 CHECK (user_level >= 0)
);

CREATE TABLE books(
    book_id SERIAL PRIMARY KEY,
    book_isbn VARCHAR UNIQUE NOT NULL,
    book_title VARCHAR NOT NULL,
    book_author VARCHAR NOT NULL,
    book_year INTEGER NOT NULL
);

CREATE TABLE reviews(
    review_id SERIAL PRIMARY KEY,
    review_content VARCHAR NOT NULL,
    review_rating FLOAT NOT NULL CHECK (review_rating>=0 AND review_rating<=5.0),
    user_id INTEGER NOT NULL,
    book_id INTEGER NOT NULL
);


-- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
-- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
-- Establecer relaciones con llaves foráneas
-- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
-- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
ALTER TABLE reviews
ADD FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE;

ALTER TABLE reviews
ADD FOREIGN KEY (book_id) REFERENCES books(book_id) ON DELETE CASCADE;
-- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 