class Libro:
    def _init_(self, titulo, autor, isbn, anio):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.anio = anio
        self.estado = "disponible"  

    def _str_(self):
        return f"'{self.titulo}' por {self.autor} (ISBN: {self.isbn}) - [{self.estado}]"