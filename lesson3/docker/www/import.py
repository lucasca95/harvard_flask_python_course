import csv # leer archivos Coma Separated Values
import os

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

# Conexión con BDD
# conn_url = 'postgresql+psycopg2://userName:userPass@dockerContainerName/DBName'
conn_url = 'postgresql+psycopg2://root:root@course_db/test'
engine = create_engine(conn_url)

# El objeto db nos permite hacer las consultas
db = scoped_session(sessionmaker(bind=engine))

def main():
    f = open("flights.csv")
    reader = csv.reader(f)
    
    for origin, destination, duration in reader:
        db.execute("INSERT INTO flights (origin, destination, duration)VALUES(:origin, :destination, :duration)",
        {"origin": origin, "destination": destination, "duration": duration})
        print(f"Added flight from {origin} to {destination} lasting {duration}")
        
        # Aplicar los cambios en la BDD
        db.commit()

if __name__ == "__main__":
    main()