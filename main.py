from gestor import GestorInventario
from usuario import Usuario

def menu():
    gestor = GestorInventario()
    gestor.cargar_libros() # Cargar al inicio
    
    # Usuario de prueba
    user = Usuario("Estudiante", "001")

    while True:
        print("\n--- BIBLIOTECA ---")
        print("1. Agregar Libro")
        print("2. Buscar Libro")
        print("3. Prestar Libro")
        print("4. Guardar y Salir")
        
        opcion = input("Seleccione: ")

        if opcion == "1":
            t = input("Título: ")
            a = input("Autor: ")
            i = input("ISBN: ")
            y = input("Año: ")
            gestor.agregar_libro(t, a, i, y)
        
        elif opcion == "2":
            c = input("Buscar por título/autor: ")
            resultados = gestor.buscar_libros(c)
            for r in resultados:
                print(r)

        elif opcion == "3":
            isbn = input("ISBN del libro a prestar: ")
            gestor.prestar_libro(user, isbn)

        elif opcion == "4":
            gestor.guardar_libros()
            break

if __name__ == "__main__":
    menu()