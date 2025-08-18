class PosOcupadaException(Exception):
    pass

class Tablero:
    def __init__(self):
        self.contenedor = [   
            ["", "", ""],
            ["", "", ""],
            ["", "", ""],
        ]

    def poner_la_ficha(self, fil, col, ficha):
        if self.contenedor[fil][col] == "":
            self.contenedor[fil][col] = ficha
        else:
            raise PosOcupadaException("Posición ocupada!") 
        
    def hay_ganador(self, ficha):
        for fila in self.contenedor:
            if all(c == ficha for c in fila):
                return True
        for c in range(3):
            if all(self.contenedor[f][c] == ficha for f in range(3)):
                return True 
        if all(self.contenedor[i][i] == ficha for i in range(3)):
            return True
        if all(self.contenedor[i][2 - i] == ficha for i in range(3)):
            return True
        return False

    def esta_lleno(self):
        return all(c != "" for fila in self.contenedor for c in fila) 