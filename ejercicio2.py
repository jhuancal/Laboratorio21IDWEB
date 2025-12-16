class Libro:
    def __init__(self, titulo, autor, anio):
        self.titulo = titulo
        self.autor = autor
        self.anio = anio
        self.disponible = True

    def prestar(self):
        if self.disponible:
            self.disponible = False
            print(f"El libro '{self.titulo}' ha sido prestado.")
        else:
            print(f"El libro '{self.titulo}' ya esta prestado.")

    def devolver(self):
        if not self.disponible:
            self.disponible = True
            print(f"El libro '{self.titulo}' ha sido devuelto.")
        else:
            print(f"El libro '{self.titulo}' ya estaba disponible.")

    def __str__(self):
        estado = "Disponible" if self.disponible else "Prestado"
        return f"{self.titulo} - {self.autor} ({self.anio}) [{estado}]"


class LibroDigital(Libro):
    def __init__(self, titulo, autor, anio, formato, tamanioMB):
        super().__init__(titulo, autor, anio)
        self.formato = formato
        self.tamanioMB = tamanioMB

    def prestar(self):
        print(f"El libro digital '{self.titulo}' en formato {self.formato} esta disponible")

    def __str__(self):
        return f"{self.titulo} - {self.autor} ({self.anio}) [Digital: {self.formato}, {self.tamanioMB}MB]"


class Biblioteca:
    def __init__(self):
        self.libros = []

    def agregar_libro(self, libro):
        self.libros.append(libro)

    def listar_libros(self):
        print("\nLista de libros en la biblioteca:")
        for libro in self.libros:
            print(libro)

    def buscar_por_autor(self, autor):
        encontrados = [libro for libro in self.libros if libro.autor.lower() == autor.lower()]
        if encontrados:
            print(f"\nLibros encontrados de {autor}:")
            for libro in encontrados:
                print(libro)
        else:
            print(f"\nNo se encontraron libros del autor {autor}.")

    def prestar_libro(self, titulo):
        for libro in self.libros:
            if libro.titulo.lower() == titulo.lower():
                libro.prestar()
                return
        print(f"No se encontro el libro '{titulo}'.")


def crear_libro_fisico():
    titulo = input("Titulo del libro: ")
    autor = input("Autor: ")
    anio = int(input("Año: "))
    return Libro(titulo, autor, anio)

def crear_libro_digital():
    titulo = input("Titulo del libro digital: ")
    autor = input("Autor: ")
    anio = int(input("Año: "))
    formato = input("Formato (PDF, EPUB, etc.): ")
    tamanioMB = int(input("Tamaño en MB: "))
    return LibroDigital(titulo, autor, anio, formato, tamanioMB)


b = Biblioteca()

b.agregar_libro(Libro("La Iliada", "Homero", 1500))
b.agregar_libro(Libro("La Odisea", "Homero", 1600))
b.agregar_libro(Libro("La metamorfosis", "Ovidio", 1663))
b.agregar_libro(LibroDigital("Crimen y Castigo", "Fiodor", 1537, "PDF", 5))
b.agregar_libro(LibroDigital("Orgullo y Prejuicio", "Jane Austen", 1752, "EPUB", 3))

while True:
    print("\nMenu:")
    print("1. Agregar libro fisico")
    print("2. Agregar libro virtual")
    print("3. Mostrar libros")
    print("4. Prestar Libro")
    print("5. Buscar por autor")
    print("6. Salir")

    opcion = input("Opcion: ")

    if opcion == "1":
        libro = crear_libro_fisico()
        b.agregar_libro(libro)
    elif opcion == "2":
        libro = crear_libro_digital()
        b.agregar_libro(libro)
    elif opcion == "3":
        b.listar_libros()
    elif opcion == "4":
        titulo = input("Ingrese el nombre del libro")
        b.prestar_libro(titulo)
    elif opcion == "5":
        autor = input("Ingrese el nombre del autor")
        b.buscar_por_autor(autor)
    elif opcion == "6":
        break
    else:
        print("Opcion invalida.")

