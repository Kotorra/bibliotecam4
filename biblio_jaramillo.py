class Libro:
    disponible = True
    def __init__(self, titulo, autor, codigo_libro):
        self.__titulo = titulo.upper()
        self.__autor = autor.upper()
        self.__codigo_libro = codigo_libro

    def mostrar_informacion_libro(self):
        estado = "Disponible" if self.disponible else "Prestado"
        print(f"Título: {self.__titulo} - Autor: {self.__autor} - Estado: {estado}")
        print("----------------------------------------")

    def obtener_titulo(self):
        return self.__titulo

    def obtener_codigo(self):
        return self.__codigo_libro


class Usuario:
    def __init__(self, nombre_usuario, codigo_usuario):
        self.__nombre_usuario = nombre_usuario.upper()
        self.__codigo_usuario = codigo_usuario
        self.libros_prestados = []

    def mostrar_libros_prestados(self):
        if len(self.libros_prestados) == 0:
            print(f"El usuario {self.__nombre_usuario} no tiene libros prestados.")
        else:
            print(f"El usuario {self.__nombre_usuario} tiene los siguientes libros prestados:")
            for libro in self.libros_prestados:
                libro.mostrar_informacion_libro()

    def obtener_nombre(self):
        return self.__nombre_usuario

    def obtener_codigo(self):
        return self.__codigo_usuario


class Prestamo:
    def __init__(self, libro, usuario):
        self.libro_prestado = libro
        self.usuario_prestamo = usuario

    def realizar_prestamo(self):
        if self.libro_prestado.disponible:
            self.libro_prestado.disponible = False
            self.usuario_prestamo.libros_prestados.append(self.libro_prestado)
            print(f"El libro '{self.libro_prestado.obtener_titulo()}' ha sido prestado a {self.usuario_prestamo.obtener_nombre()}.")
        else:
            print(f"El libro '{self.libro_prestado.obtener_titulo()}' ya está prestado.")

    def devolver_prestamo(self):
        if self.libro_prestado in self.usuario_prestamo.libros_prestados:
            self.libro_prestado.disponible = True
            self.usuario_prestamo.libros_prestados.remove(self.libro_prestado)
            print(f"El libro '{self.libro_prestado.obtener_titulo()}' ha sido devuelto por {self.usuario_prestamo.obtener_nombre()}.")
        else:
            print(f"El usuario {self.usuario_prestamo.obtener_nombre()} no tiene prestado el libro '{self.libro_prestado.obtener_titulo()}'.")


class AdministradorLibros:
    def registrar_libro(self):
        print("Estás registrando un libro nuevo.")
        titulo_nuevo = input("Ingresa el título del libro: ")
        autor_nuevo = input("Ingresa el autor del libro: ")
        codigo_nuevo_libro = input("Ingresa el código del libro: ")
        nuevo_libro = Libro(titulo_nuevo, autor_nuevo, codigo_nuevo_libro)
        lista_libros.append(nuevo_libro)
        print("Libro registrado con éxito.")


class AdministradorUsuarios:
    def registrar_usuario(self):
        print("Estás registrando un nuevo usuario.")
        nombre_usuario = input("Ingresa el nombre del usuario: ")
        codigo_usuario = input("Ingresa el código del usuario: ")
        nuevo_usuario = Usuario(nombre_usuario, codigo_usuario)
        lista_usuarios.append(nuevo_usuario)
        print("Usuario registrado con éxito.")


# Crear instancias de administradores
administrador_libros = AdministradorLibros()
administrador_usuarios = AdministradorUsuarios()

# Inicializar la biblioteca con algunos libros
libro_1 = Libro("La peste", "Albert Camus", "00001")
libro_2 = Libro("Noches Blancas", "Fiodor Dostoievski", "00002")
libro_3 = Libro("El extranjero", "Albert Camus", "00003")
libro_4 = Libro("El túnel", "Ernesto Sábato", "00004")

lista_libros = [libro_1, libro_2, libro_3, libro_4]
lista_usuarios = []

# Menú principal
while True:
    print("\n'Tu Libro' \nMenú de opciones:")
    print("1.- Mostrar libros disponibles.")
    print("2.- Crear Usuario.")
    print("3.- Registrar un libro nuevo.")
    print("4.- Prestar un libro.")
    print("5.- Devolver un libro.")
    print("6.- Cerrar programa")

    opcion_menu = input("Ingresa la opción: ")

    if opcion_menu == "6":
        print("El programa se despide")
        print("Creado por Jorge Jaramillo para bootcamp.")
        break

    elif opcion_menu == "1":
        if len(lista_libros) > 0:
            print("Los libros disponibles son: ")
            for libro in lista_libros:
                libro.mostrar_informacion_libro()
        else:
            print("No hay libros disponibles en este momento.")

    elif opcion_menu == "2":
        administrador_usuarios.registrar_usuario()

    elif opcion_menu == "3":
        administrador_libros.registrar_libro()

    elif opcion_menu == "4":
        # Prestar un libro
        codigo_usuario = input("Ingresa el código del usuario: ")
        usuario_encontrado = next((usuario for usuario in lista_usuarios if usuario.obtener_codigo() == codigo_usuario), None)

        if usuario_encontrado:
            codigo_libro = input("Ingresa el código del libro: ")
            libro_encontrado = next((libro for libro in lista_libros if libro.obtener_codigo() == codigo_libro), None)

            if libro_encontrado:
                prestamo = Prestamo(libro_encontrado, usuario_encontrado)
                prestamo.realizar_prestamo()
            else:
                print("El libro no se encontró.")
        else:
            print("El usuario no se encontró.")

    elif opcion_menu == "5":
        # Devolver un libro
        codigo_usuario = input("Ingresa el código del usuario: ")
        usuario_encontrado = next((usuario for usuario in lista_usuarios if usuario.obtener_codigo() == codigo_usuario), None)

        if usuario_encontrado:
            codigo_libro = input("Ingresa el código del libro a devolver: ")
            libro_encontrado = next((libro for libro in usuario_encontrado.libros_prestados if libro.obtener_codigo() == codigo_libro), None)

            if libro_encontrado:
                prestamo = Prestamo(libro_encontrado, usuario_encontrado)
                prestamo.devolver_prestamo()
            else:
                print("El usuario no tiene ese libro prestado.")
        else:
            print("El usuario no se encontró.")

    else:
        print("Opción no válida.")
