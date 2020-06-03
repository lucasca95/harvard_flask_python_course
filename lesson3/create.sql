CREATE TABLE flights (
        id SERIAL PRIMARY KEY,
        -- NOT NULL indica que el valor no puede ser vacio
        origin VARCHAR NOT NULL,
        destination VARCHAR NOT NULL,
        duration INTEGER NOT NULL
    );

CREATE TABLE passengers (
        id SERIAL PRIMARY KEY,
        -- NOT NULL indica que el valor no puede ser vacio
        name VARCHAR NOT NULL,
        -- Generamos una relación donde un pasajero viaja en un vuelo!
        flight_id INTEGER REFERENCES flights
    );