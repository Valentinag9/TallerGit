# usuario.py
class Usuario:
    def __init__(self, nombre, id_usuario):
        self.nombre = nombre
        self.id_usuario = id_usuario
        self.libros_prestados = []

    def mostrar_info(self):
        print(f"Usuario: {self.nombre} | ID: {self.id_usuario}")
        print("Libros prestados:")
        for libro in self.libros_prestados:
            print(f" - {libro.titulo}")