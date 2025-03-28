def pausa():
    input("\tPresione enter para continuar")

class libro:
    def __init__(self, titulo, autor, genero, puntuacion):
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
        self.puntuacion = puntuacion

lista_libros = [libro("Cien años de soledad", "Gabriel García Márquez", "Ficción", 4.5),
libro("1984", "George Orwell", "Ciencia Ficción", 4.3),
libro("El Hobbit", "J.R.R. Tolkien", "Fantasía", 4.7),
libro("Orgullo y Prejuicio", "Jane Austen", "Romance", 4.2),
libro("Crimen y Castigo", "Fiódor Dostoyevski", "Clásico", 4.4),
libro("Los Juegos del Hambre", "Suzanne Collins", "Juvenil", 4.1),
libro("Don Quijote de la Mancha", "Miguel de Cervantes", "Clásico", 4.6),
libro("Harry Potter y la Piedra Filosofal", "J.K. Rowling", "Fantasía", 4.8),
libro("Los Pilares de la Tierra", "Ken Follett", "Histórica", 4.4),
libro("Cazadores de Sombras: Ciudad de Hueso", "Cassandra Clare", "Fantasía", 4.0)]

def agregar_libro():
    titulo = input("Ingrese el titulo del libro: ")
    autor = input("Ingrese el autor del libro: ")
    genero = input("Ingrese el genero del libro: ")
    puntuacion = float(input("Ingrese la puntuacion del libro: "))
    pausa()
    
    lista_libros.append(libro(titulo, autor, genero, puntuacion))

def buscar_libros():
    buscar_genero = input("Ingrese el género que desea buscar: ")
    
    libros_encontrados = [libro for libro in lista_libros if libro.genero.capitalize() == buscar_genero.capitalize()]
    
    if libros_encontrados:
        for libro in libros_encontrados:
            print("Título:", libro.titulo, ", " "Autor:", libro.autor, ",", "Género:", libro.genero, ",", "Puntuación:", libro.puntuacion)
    else:
        print("No se encontraron libros con ese género")
    pausa()

def recomendar_libro():
    recomendar_genero = input("Ingrese el género que desea buscar: ")
    
    libros_en_genero = [libro for libro in lista_libros if libro.genero.capitalize() == recomendar_genero.capitalize()]
    
    if libros_en_genero:
        libro_recomendado = max(libros_en_genero, key=lambda x: x.puntuacion)
        print("El libro con la mejor puntuación del género", recomendar_genero, "es: ")
        print("Título:", libro_recomendado.titulo, ", " "Autor:", libro_recomendado.autor, ",", "Género:", libro_recomendado.genero, ",", "Puntuación:", libro_recomendado.puntuacion)
    else:
        print("No se encontraron libros con ese género")
    pausa()

def menu():
    while True:
        print("Menú Recomendación de libros")
        print("1. Agregar libro")
        print("2. Buscar libros por género")
        print("3. Recomendar libro")
        print("4. Salir")
        
        opcion = int(input("Ingrese una opción: "))
        
        if opcion == 1:
            agregar_libro()
        elif opcion == 2:
            buscar_libros()
        elif opcion == 3:
            recomendar_libro()
        elif opcion == 4:
            print("Muchas gracias por usar el programa")
            break
        else:
            print("Opción incorrecta, Ingrese una opción válida")

menu()
