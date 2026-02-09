class Libro:
    def __init__(self, titulo, autor, isbn, anio):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.anio = anio
        self.estado = "disponible"  

    def __str__(self):
        return f"'{self.titulo}' por {self.autor} (ISBN: {self.isbn}) - [{self.estado}]"