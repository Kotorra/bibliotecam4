class Libro():
	estadoDeUso=False
	def __init__(self,tituloLibro,autorLibro,idLibro):
		self.__tituloLibro=tituloLibro.upper()
		self.__autorLibro=autorLibro.upper()
		self.__idLibro=idLibro
	def mostrarLibro(self):
		print(f"Título: {self.__tituloLibro} - Autor: {self.__autorLibro}")
		print("----------------------------------------")

class Usuario():
	librosEnUso=[]
	def __init__(self,nombre,idUsuario):
		self.__nombre=nombre.upper()
		self.__idUsuario=idUsuario

	def mostrarLibrosUsuario():
		if (len(librosEnUso)==0):
			print(f"El usuario {self.__nombre} no tiene libros en uso.")
		else:
			print(f"El usuario {self.__nombre} tiene los siguientes libros en uso:")
			for i in librosEnUso:
				pass

class Prestamo():

	def __init__(self,libroSolicitado,usuarioActual):
		self.libroSolicitado=libroSolicitado
		self.usuarioActual=usuarioActual

	def prestarLibro(self):
		if libroSolicitado:
			pass


class Creador():
	def crearLibro(self):
		print("Estás registrando un libro.")
		titulo=input("Ingresa el título del libro: ")
		autor=input("Ingresa el autor del libro: ")
		idRegistroLibro=input("Ingresa el ID del libro: ")
		libro=Libro(titulo,autor,idRegistroLibro)
		listaLibros.append(libro)
creadorMagico=Creador()


libro1=Libro("La peste","Albert Camus","wfjdsaXD")
libro2=Libro("Noches Blancas","Fiodor Dostoievski","fjfdsaf")
libro3=Libro("El extranjero","Albert Camus","1j3fjasf")
libro4=Libro("El túnel","Ernesto Sábato","wejfajaf")

listaLibros=[libro1,libro2,libro3,libro4]

print("Bienvenidos a la biblioteca 'El Saber'.")
while True:
	print("Library Software 0.0.0.1 - 'El Saber' \nMenú de opciones: ")
	print("1.- Mostrar libros disponibles.")
	print("2.- Crear Usuario.")
	print("3.- Crear registro de un libro nuevo.")
	print("4.- Prestar un libro.")
	print("5.- Devolver un libro.")
	print("6.- Cerrar programa")

	opcion=input("Ingresa la opción: ")

	if opcion=="6":
		print("El programa se despide")
		print("Desarrollado por LadPython INC.")
		break

	elif opcion=="1":
		print("Los libros disponibles son: ")
		for i in listaLibros:
			i.mostrarLibro()

	elif opcion=="2":
		pass

	elif opcion=="3":
		creadorMagico.crearLibro()

	elif opcion=="4":
		pass

	elif opcion=="5":
		pass

	else:
		print("Revísate")