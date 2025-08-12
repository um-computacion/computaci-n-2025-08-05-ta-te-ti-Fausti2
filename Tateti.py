from Tablero import Tablero
from Jugador import Jugador
class Tateti:
    def __init__(self):
        self.tablero = Tablero()
        nombre1 = input("Ingrese el nombre del Jugador 1 (X): ")
        nombre2 = input("Ingrese el nombre del Jugador 2 (0): ")
        self.jugadores = [
            Jugador(nombre1, "X"),
            Jugador(nombre2, "0")
        ]
        self.turno = 0 


    def get_jugador_actual(self):
        return self.jugadores[self.turno] 

    def marcar_casilla(self, fil, col):
        jugador = self.get_jugador_actual()
        self.tablero.poner_la_ficha(fil, col, jugador.get_ficha())
        self.turno = 1 - self.turnos  