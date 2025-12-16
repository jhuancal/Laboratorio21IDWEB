from geometria import Rectangulo, Triangulo, Circulo

figuras = [
    Rectangulo(10, 5),
    Triangulo(6, 4),
    Circulo(7)
]

for figura in figuras:
    print(f"{figura.__class__.__name__}:")
    print(f"  Area = {figura.area():.2f}")
    print(f"  Perimetro = {figura.perimetro():.2f}\n")



