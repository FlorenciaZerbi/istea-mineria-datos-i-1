# Importación de la librería csv para manejar archivos CSV
import csv

# Función que solicita al usuario Presionar la tecla enter para continuar antes de volver al menú
def pausa():
    input("\t\nPresione Enter para continuar")

# Clase Libro que representa un libro con sus atributos Título, Autor, Género y Puntuación
class Libro:
    def __init__(self, titulo, autor, genero, puntuacion):
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
        self.puntuacion = puntuacion

# Lista para almacenar los libros
lista_libros = []

# Función para guardar un libro en un archivo CSV
def guardar_libro_en_csv(archivo, libro):
    try:
        with open(archivo, mode='a', encoding='utf-8', newline='') as file:
            escritor = csv.writer(file)
            escritor.writerow([libro.titulo, libro.autor, libro.genero, libro.puntuacion])
    except Exception as e:
        print(f"Ocurrió un error al guardar el libro en el archivo '{archivo}': {e}")

# Función para la carga manual de libros
def agregar_libro():
    titulo = input("Ingrese el título del libro: ").strip()
    autor = input("Ingrese el autor del libro: ").strip()
    genero = input("Ingrese el género del libro: ").strip()
    
    # Validar que la puntuación ingresada sea un número entre 0 y 5
    while True:
        try:
            puntuacion = float(input("Ingrese la puntuación del libro (0-5): ").strip())
            if 0 <= puntuacion <= 5:
                break
            else:
                print("Por favor, ingrese una puntuación entre 0 y 5.")
        except ValueError:
            print("Por favor, ingrese un número válido para la puntuación.")

    # Crear el objeto Libro y agregarlo a la lista
    nuevo_libro = Libro(titulo, autor, genero, puntuacion)
    lista_libros.append(nuevo_libro)

    # Guardar el libro en el archivo CSV
    archivo_csv = "libros.csv"
    guardar_libro_en_csv(archivo_csv, nuevo_libro)
    
    print(f"\nEl libro '{titulo}' ha sido agregado a la lista correctamente.")
    
    pausa()
        
# Función para la búsqueda de libros por género
def buscar_libros():
    buscar_genero = input("Ingrese el género que desea buscar: ").strip()

    libros_encontrados = [libro for libro in lista_libros if libro.genero.capitalize() == buscar_genero.capitalize()]

    if libros_encontrados:
        print(f"\nLibros encontrados en el género '{buscar_genero}':")
        for libro in libros_encontrados:
            print(f"Título: {libro.titulo}, Autor: {libro.autor}, Género: {libro.genero}, Puntuación: {libro.puntuacion}")
    else:
        print(f"No se encontraron libros con el género '{buscar_genero}'.")
    
    pausa()

# Función para pedir recomendación de un libro basado en el género y la puntuación más alta
def recomendar_libro():
    recomendar_genero = input("Ingrese el género que desea para la recomendación: ").strip()

    libros_en_genero = [libro for libro in lista_libros if libro.genero.capitalize() == recomendar_genero.capitalize()]

    if libros_en_genero:
        libro_recomendado = max(libros_en_genero, key=lambda x: x.puntuacion)
        print(f"\nEl libro con la mejor puntuación del género '{recomendar_genero}' es:")
        print(f"Título: {libro_recomendado.titulo}, Autor: {libro_recomendado.autor}, Género: {libro_recomendado.genero}, Puntuación: {libro_recomendado.puntuacion}")
    else:
        print(f"No se encontraron libros con el género '{recomendar_genero}'.")
    
    pausa()

# Función para cargar libros desde un archivo CSV
def cargar_libros_desde_csv(archivo):
    try:
        with open(archivo, mode='r', encoding='utf-8') as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                titulo, autor, genero, puntuacion = row
                lista_libros.append(Libro(titulo, autor, genero, float(puntuacion)))
        print(f"Se han cargado los libros desde el archivo '{archivo}' correctamente.")
    except FileNotFoundError:
        print(f"El archivo '{archivo}' no se encontró. Se usará la lista predeterminada de libros.")
    except Exception as e:
        print(f"Ocurrió un error al cargar el archivo '{archivo}': {e}")

# Función para crear el menú principal
def menu():
    archivo_csv = "libros.csv" 
    cargar_libros_desde_csv(archivo_csv)

    while True:
        print("\nMenú Recomendación de libros")
        print("1. Agregar libro")
        print("2. Buscar libros por género")
        print("3. Recomendar libro")
        print("4. Salir")

        opcion = input("Ingrese una opción: ")

        if opcion == "1":
            agregar_libro()
        elif opcion == "2":
            buscar_libros()
        elif opcion == "3":
            recomendar_libro()
        elif opcion == "4":
            print("\nMuchas gracias por usar el programa.")
            break
        else:
            print("Opción incorrecta, ingrese una opción válida.")

menu()
