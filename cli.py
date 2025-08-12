from Tateti import Tateti
def main():
    print("Bienvenidos al Tateti")
    juego = Tateti()
    while True:
        print("Tablero: ")
        print(juego.tablero.contenedor)
        jugador = juego.get_jugador_actual()
        print(f"Turno de {jugador.get_nombre()} ({jugador.get_ficha()})")
        try:
            fil = int(input("Ingrese fila: "))
            col = int(input("Ingrese col: "))
            juego.marcar_casilla(fil, col)
        except Exception as e:
            print(e)

if __name__ == '__main__':
    main()