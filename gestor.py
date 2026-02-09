# gestor.py
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