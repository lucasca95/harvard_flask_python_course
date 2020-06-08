# generic idea of what a flight is
class Flight:
    # constructor de un objeto Flight
    # los "atributos" de java en python son "propiedades"
    def __init__(self, origin, destination, duration):
        self.origin = origin
        self.destination = destination
        self.duration = duration
    
    def print_info(self):
        print(f'Flight origin: {self.origin}')
        print(f'Flight destination: {self.destination}')
        print(f'Flight duration: {self.duration}\n')
        
        
def main():

    f1 = Flight(origin="New York", destination="Paris", duration=540)
    f1.print_info()

    f2 = Flight(origin="Tokyop", destination="Shanghai", duration=185)
    f2.print_info()


# Si estoy ejecutando ESTE archivo particularmente, ejecutar main()
if __name__ == "__main__":
    main()