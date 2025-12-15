import math

class Poligono:
    def __init__(self, base=0, altura=0):
        self.base = base
        self.altura = altura

    def area(self):
        return 0
    
    def perimetro(self):
        return 0


class Rectangulo(Poligono):
    def area(self):
        return self.base * self.altura
    
    def perimetro(self):
        return 2 * (self.base + self.altura)


class Triangulo(Poligono):
    def area(self):
        return (self.base * self.altura) / 2
    
    def perimetro(self):
        lado = math.sqrt((self.base / 2) ** 2 + self.altura ** 2)
        return self.base + 2 * lado


class Circulo:
    def __init__(self, radio):
        self.radio = radio

    def area(self):
        return math.pi * (self.radio ** 2)
    
    def perimetro(self):
        return 2 * math.pi * self.radio


figuras = [
    Rectangulo(10, 5),
    Triangulo(6, 4),
    Circulo(7)
]

for figura in figuras:
    print(f"{figura.__class__.__name__}:")
    print(f"  Area = {figura.area():.2f}")
    print(f"  Perimetro = {figura.perimetro():.2f}\n")
