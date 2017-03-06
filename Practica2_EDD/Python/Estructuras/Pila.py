class NodoPila:
	#NODO DE LA PILA
	def __init__(self, numero):
		self.numero = numero
		self.siguiente = None
	
class Pila:
	def __init__(self):
		self.cabeza = None
		self.ultimo = None
	
	def estaVacia(self):
		if self.cabeza == None:
			return True
		else:
			return False
	
	def push(self, Nodo):
		if self.estaVacia()== True:
			self.cabeza = Nodo
			self.ultimo = Nodo
			self.cabeza.siguiente = self.ultimo
		else:
			Nodo.siguiente = self.cabeza
			self.cabeza = Nodo

	def pop(self):
		if self.estaVacia()==True:
			return "Pila Vacía!"
		else:
			if self.cabeza == self.ultimo:
				retorno = self.cabeza.numero
				self.cabeza = None
				self.ultimo = None
				return retorno
			else:
				retorno = self.cabeza.numero
				self.cabeza = self.cabeza.siguiente
				return retorno
	