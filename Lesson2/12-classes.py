class Point:
    # self representa al objeto en si mismo
    # el metodo init es el constructor de la clase
    def __init__(self, x, y):
        self.x = x
        self.y = y

p = Point(3, 5)
print(p.x)
print(p.y)