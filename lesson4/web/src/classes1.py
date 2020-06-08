# generic idea of what a flight is
class Flight:
    # constructor de un objeto Flight
    # los "atributos" de java en python son "propiedades"
    def __init__(self, origin, destination, duration):
        self.origin = origin
        self.destination = destination
        self.duration = duration
        
def main():
    f = Flight(origin="New York", destination="Paris", duration=540)

    f.duration += 10

    print(f.origin)
    print(f.destination)
    print(f.duration)

# Si estoy ejecutando ESTE archivo particularmente, ejecutar main()
if __name__ == "__main__":
    main()