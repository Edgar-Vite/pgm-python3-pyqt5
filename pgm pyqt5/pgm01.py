# importaciones
import sqlite3

class ayudante:
	# constructor
	def __init__(self, nombd=None):
		self.conn  = None
		self.cursuor = None

		if nombd:
			self.abrir(nombd)
	# funcion abrir bd
	def abrir(self, nombd):
		try:
			self.conn = sqlite3.connect(nombd)
			self.cursor = self.conn.cursor()
			#print(sqlite3.version)
		except sqlite3.Error as e:
			print("no abre la base")
	# funcion editar		
	def editar(self,query,parameters = ()):
		c = self.cursor
		r = c.execute(query, parameters)
		self.conn.commit()
		return r
	# funcion seleccionar
	def select(self,query):
		c = self.cursor
		c.execute(query)
		self.conn.commit()
		return c.fetchall()

test = ayudante("pgmDB")

#print(test.select("SELECT * FROM Contactos"))