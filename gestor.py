# gestor.py
import csv
from libro import Libro

class GestorInventario:

    def __init__(self):

        self.libros = []

    def agregar_libro(self, titulo, autor, isbn, anio):
        # Validacion simple (Requerimiento 8)
        if not titulo or not autor:
            print("Error: Título y Autor son obligatorios.")
            return
        nuevo = Libro(titulo, autor, isbn, anio)
        self.libros.append(nuevo)
        print(f"Libro '{titulo}' agregado.")

        
        # Código de Persona B
    def buscar_libros(self, criterio):
        resultados = [l for l in self.libros if criterio.lower() in l.titulo.lower() or criterio.lower() in l.autor.lower()]
        return results


    def eliminar_libro(self, isbn):
        for libro in self.libros:
            if libro.isbn == isbn:
                self.libros.remove(libro)
                print(f"Libro con ISBN {isbn} eliminado.")
                return
        print("Libro no encontrado.")


    def prestar_libro(self, usuario, isbn):
        for libro in self.libros:
            if libro.isbn == isbn:
                if libro.estado == "disponible":
                    libro.estado = "prestado"
                    usuario.libros_prestados.append(libro)
                    print(f"Libro '{libro.titulo}' prestado a {usuario.nombre}")
                    return
                else:
                    print("El libro ya está prestado.")
                    return
        print("Libro no encontrado.")

    def devolver_libro(self, usuario, isbn):
        # Lógica inversa a prestar (intenta implementarla tú basándote en la de arriba)
        pass

    def guardar_libros(self, archivo="inventario.csv"):
        with open(archivo, mode='w', newline='') as file:
            writer = csv.writer(file)
            for libro in self.libros:
                writer.writerow([libro.titulo, libro.autor, libro.isbn, libro.anio, libro.estado])
        print("Datos guardados.")

    def cargar_libros(self, archivo="inventario.csv"):
        try:
            with open(archivo, mode='r') as file:
                reader = csv.reader(file)
                self.libros = []
                for row in reader:
                    if row:
                        l = Libro(row[0], row[1], row[2], row[3])
                        l.estado = row[4]
                        self.libros.append(l)
            print("Datos cargados.")
        except FileNotFoundError:
            print("No hay archivo previo.")
