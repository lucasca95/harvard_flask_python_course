class Flight:

    # Llevar un contador que es accesible a todos los objetos
    counter = 1
    
    def __init__(self, origin, destination, duration):
        # el usuario no se preocupa por el id del flight
        self.id = Flight.counter
        Flight.counter += 1

        self.passengers = []

        self.origin = origin
        self.destination = destination
        self.duration = duration
    
    def print_info(self):
        print(f'Flight origin: {self.origin}')
        print(f'Flight destination: {self.destination}')
        print(f'Flight duration: {self.duration}\n')
        print(f'Passengers:')
        for p in self.passengers:
            print(f'{p.name}')
    
    def delay(self, amount):
        self.duration += amount
    
    def addPassenger(self, p):
        self.passengers.append(p)
        p.flight_id = self.id

class Passenger:

    def __init__(self, name):
        self.name = name

def main():

    f1 = Flight(origin="New York", destination="Paris", duration=540)
    
    lucas = Passenger(name='Lucas')
    agustina = Passenger(name='Agustina')

    f1.addPassenger(lucas)
    f1.addPassenger(agustina)

    f1.print_info()


# Si estoy ejecutando ESTE archivo particularmente, ejecutar main()
if __name__ == "__main__":
    main()