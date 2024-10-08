#Clase Usuario con metodo contructor y mostarUsuario
class Usuario:
    def __init__(self,nombre, id):
        self.nombre = nombre
        self.id= id

    def mostrarUsuario(self):
        print("--------------------------------")
        print("Usuarios:")
        for usuario in self.usuarios:
            print(f"Nombre: {usuario.nombre}")
        print("--------------------------------")
        

#Clase Libro con metodo contructor y mostarLibro     
class Libro:
    def __init__(self, titulo, autor, id):
        self.__titulo = titulo
        self.__autor = autor
        self.id = id
        self.prestado = False ##Agradecimientos a miguel por dame la idea del booleano
        
    def mostrarLibro(self):
        print("------------------------------------------------")
        print(f"Título: {self.__titulo} - Autor: {self.__autor}")
        print("------------------------------------------------")

#Clase Prestamo con metodo constructor y devolucionLibro
class Prestamo:
    def __init__(self,usuario, libro,fecha):
        self.usuario = usuario
        self.libro = libro
        self.fecha = fecha
        self.prestado = True

    def devolucionLibro(self):
        self.libro.prestado = False

#Clase Biblioteca con metodo contructor y metodos para agregar usuarios y argegar libros
class Biblioteca:
    def __init__(self):
        self.libros = []
        self.usuarios = []
        self.prestamos = []

    def agregar_usuario(self, usuario):
        self.usuarios.append(usuario)
        print(f"Usuario {usuario.nombre}, Ingresado!")
        Usuario.mostrarUsuario(self)

    def agregar_libro(self, libro):
        self.libros.append(libro)
        
###################### Datos #####################
usuario1 = Usuario("Martin", 5)

libro1=Libro("La peste","Albert Camus","wfjdsaXD")
libro2=Libro("Noches Blancas","Fiodor Dostoievski","fjfdsaf")


biblioteca = Biblioteca()
biblioteca.agregar_libro(libro1)
biblioteca.agregar_libro(libro2)

#biblioteca.agregar_usuario(usuario1)

prestamo1 = Prestamo("Martin","El Tunel","07-10-2024")

######################### Interfaz de Bastian ###################

class Interfaz():
    print("\n Bienvenidos a la biblioteca 'El Saber'.")
    while True:
        print("\nMenú de opciones: ")
        print("1.- Mostrar libros disponibles.")
        print("2.- Crear Usuario.")
        print("3.- Crear registro de un libro nuevo")
        print("4.- Prestar un libro.")
        print("5.- Devolver un libro.")
        print("6.- Cerrar programa")

        opcion=input("Ingresa la opción: ")

        if opcion=="6":
            print("El programa se despide")
            print("Desarrollado por TonyStark Industries.")
            break

        elif opcion=="1":
            print("Los libros disponibles son: ")
            for i in biblioteca.libros:
                i.mostrarLibro()

        elif opcion == "2":
            nombre = input("Ingresa el Nombre de usuario: ")
            nuevousuario = Usuario(nombre, 5)
            biblioteca.agregar_usuario(nuevousuario)

        elif opcion=="3":
            nombre = input("Ingresa el Titulo del Libro: ")
            titulo = input("Ingresa el Autor de Libro: ")
            nuevoulibro = Libro(nombre, titulo, 15)
            biblioteca.agregar_libro(nuevoulibro)

        # elif opcion=="4":
        #     pass

        # elif opcion=="5":
        #     pass

        # else:
        #     print("Revísate")



