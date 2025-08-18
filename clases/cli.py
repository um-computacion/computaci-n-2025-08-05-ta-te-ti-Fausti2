
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))) 
from Tateti import Tateti 
def main():
    print("Bienvenidos al Tateti")
    juego = Tateti()
    while not juego.juego_terminado():
        print("Tablero:")
        for fila in juego.tablero.contenedor:
            print(fila)
        jugador = juego.get_jugador_actual()
        print(f"Turno de {jugador.get_nombre()} ({jugador.get_ficha()})")
        try:
            fil = int(input("Ingrese fila (0-2): "))
            col = int(input("Ingrese col (0-2): "))
            juego.marcar_casilla(fil, col)
        except Exception as e:
            print(e)

    print("Tablero final:")
    for fila in juego.tablero.contenedor:
        print(fila)

    if juego.ganador:
        print(f"Jugador {juego.ganador.get_nombre()}! Ganador.")
    else:
        print("Empate.") 

if __name__ == '__main__':
    main() 

    