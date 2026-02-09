# gestor.py
from libro import Libro

class GestorInventario:
    def _init_(self):
        self.libros = []

    def agregar_libro(self, titulo, autor, isbn, anio):
        # Validacion simple (Requerimiento 8)
        if not titulo or not autor:
            print("Error: Título y Autor son obligatorios.")
            return
        nuevo = Libro(titulo, autor, isbn, anio)
        self.libros.append(nuevo)
        print(f"Libro '{titulo}' agregado.")

    def eliminar_libro(self, isbn):
        for libro in self.libros:
            if libro.isbn == isbn:
                self.libros.remove(libro)
                print(f"Libro con ISBN {isbn} eliminado.")
                return
        print("Libro no encontrado.")