class NodoLista:
	def __init__(self, palabra):
		self.palabra = palabra
		self.siguiente = None
	
class Lista:
	def __init__(self):
		self.cabeza = None
		self.ultimo = None
	
	def estaVacia(self):
		if self.cabeza == None:
			return True
		else:
			return False

	def insertarALista(self, palabra):
		nuevo=NodoLista(palabra)
		if self.estaVacia()==True:
			self.cabeza = nuevo
			self.ultimo = nuevo
			self.cabeza.siguiente = self.ultimo
		else:
			self.ultimo.siguiente = nuevo
			self.ultimo = nuevo
	
	def buscarPalabra(self, palabra):
		bandera = False
		if self.estaVacia()==True:
			return "Lista Vacia!"
		else:
			contador = 0
			aux = self.cabeza
			while aux != None:
				if aux.palabra == palabra:
					bandera = True
				aux = aux.siguiente
				contador = contador+1
			if bandera == True:
				return contador
			else:
				return "No se encontro la palabra"
	
	def eliminarDeLista(self, index):
		if self.estaVacia()==True:
			return "Lista Vacia"
		else:
			if index == 0:
				self.cabeza = self.cabeza.siguiente
				return "Elemento Eliminado"
			else:
				contador = 1
				aux = self.cabeza
				aux2 = self.cabeza
				while aux.siguiente!=None:
					aux = aux.siguiente
					if index == contador:
						break
					aux2 = aux2.siguiente
					contador = contador + 1
				aux2.siguiente = aux.siguiente
				return "Elemento eliminado en Indice" + str(contador)
				
	
	def showList(self):
		if self.estaVacia()==True:
			return "Lista Vacia"
		else:
			retorno = ""
			aux = self.cabeza
			while aux != None:
				retorno = retorno + " | " + str(aux.palabra) + " |---->"
				aux = aux.siguiente
			return retorno
	
lis=Lista()
lis.eliminarDeLista(3)
	