class Usuario:
    def __init__(self,nombre, id):
        self.nombre = nombre
        self.id= id

class Libro:
    def __init__(self, titulo, autor, id):
        self.titulo = titulo
        self.autor = autor
        self.id = id
        self.prestado = False 

class Prestamo:
    def __init__(self,usuario, libro,fecha):
        self.usuario = usuario
        self.libro = libro
        self.fecha = fecha
        self.prestado = True

    def devolucion_libro(self):
        self.libro.prestado = False


