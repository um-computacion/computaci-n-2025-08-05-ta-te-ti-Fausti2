class Jugador:

        def __init__(self, nombre, ficha):
         self.nombre = nombre
         self.ficha = ficha
         self.jugando = False
         self.gano = False
         self.perdio = False

        def get_nombre(self):
           return self.nombre

        def get_ficha(self):
           return self.ficha  
