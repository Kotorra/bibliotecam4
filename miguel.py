# Definicio de la class libro
class Libro:

    #tiene 3 atributos (Titulo, autor y id)
    def init(self, titulo, autor, id):
        self.titulo = titulo
        self.autor = autor
        self.id = id
        self.prestado = False
   
    #metodo (prestar)
    def prestar(self):
        if not self.prestado:
            self.prestado = True
            return True
        return False
    
    # Metodo (devolver)
    def devolver(self):
        self.prestado = False

    def esta_prestado(self):
        return self.prestado

# Definicio de la class usuario

class Usuario:
    #tiene 2 atributos (nombre y id)
    def init(self, nombre, id):
        self.nombre = nombre
        self.id = id
    
    #metodo (solicitar_prestamo)
    def solicitar_prestamo(self, libro):
        return libro.prestar()
    
    #metodo (devolver_libro)
    def devolver_libro(self, libro):
        libro.devolver()

# Definicio de la class prestamo

class Prestamo:

    #tiene 3 atributos (usuario, libro y fecha)
    def init(self, usuario, libro, fecha):
        self.usuario = usuario
        self.libro = libro
        self.fecha = fecha
