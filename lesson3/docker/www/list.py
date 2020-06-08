import os

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

# Conexión con BDD
conn_url = 'postgresql+psycopg2://root:root@course_db/test'
engine = create_engine(conn_url)

# El objeto db nos permite hacer las consultas
db = scoped_session(sessionmaker(bind=engine))

def main():
    flights = db.execute("SELECT origin, destination, duration FROM flights").fetchall()
    for flight in flights:
        print(f"{flight.origin} to {flight.destination}, {flight.duration} miles")

if __name__ == "__main__":
    main()