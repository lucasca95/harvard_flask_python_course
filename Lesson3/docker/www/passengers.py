import os

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

# Conexión con BDD
conn_url = 'postgresql+psycopg2://root:root@course_db/test'
engine = create_engine(conn_url)

# El objeto db nos permite hacer las consultas
db = scoped_session(sessionmaker(bind=engine))

def main():
    flights = db.execute("SELECT * FROM flights").fetchall()
    for flight in flights:
        print(f"{flight.id}:{flight.origin} to {flight.destination}, {flight.duration} miles")

    flight_id = int(input("\nFlight ID: "))
    flight = db.execute("SELECT origin, destination, duration FROM flights WHERE flights.id = :id",
    {"id": flight_id}).fetchone()

    if flight is None:
        print("Error: No such flight.")
        return 
    
    passengers = db.execute("SELECT name FROM passengers WHERE flight_id = :flight_id",
    {"flight_id": flight_id}).fetchall()
    print("\nPassengers:")

    for p in passengers:
        print(p.name)
    
    if len(passengers) == 0:
        print("No passengers.")
    

if __name__ == "__main__":
    main()