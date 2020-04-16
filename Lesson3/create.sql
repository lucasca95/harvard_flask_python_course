CREATE TABLE flights (
        id SERIAL PRIMARY KEY,
        -- NOT NULL indica que el valor no puede ser vacio
        origin VARCHAR NOT NULL,
        destination VARCHAR NOT NULL,
        duration INTEGER NOT NULL
    );