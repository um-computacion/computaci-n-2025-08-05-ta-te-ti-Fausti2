import pytest
from clases.Tablero import Tablero, PosOcupadaException

def test_poner_la_ficha_en_posicion_vacia():
    t = Tablero()
    t.poner_la_ficha(0, 0, "X")
    assert t.contenedor[0][0] == "X"

def test_poner_la_ficha_en_posicion_ocupada_lanza_excepcion():
    t = Tablero()
    t.poner_la_ficha(0, 0, "X")
    with pytest.raises(PosOcupadaException):
        t.poner_la_ficha(0, 0, "0")

def test_hay_ganador_fila():
    t = Tablero()
    t.contenedor[1] = ["X", "X", "X"]
    assert t.hay_ganador("X") is True

def test_hay_ganador_columna():
    t = Tablero()
    t.contenedor[0][2] = "0"
    t.contenedor[1][2] = "0"
    t.contenedor[2][2] = "0"
    assert t.hay_ganador("0") is True

def test_hay_ganador_diagonal_principal():
    t = Tablero()
    t.contenedor[0][0] = "X"
    t.contenedor[1][1] = "X"
    t.contenedor[2][2] = "X"
    assert t.hay_ganador("X") is True

def test_hay_ganador_diagonal_secundaria():
    t = Tablero()
    t.contenedor[0][2] = "X"
    t.contenedor[1][1] = "X"
    t.contenedor[2][0] = "X"
    assert t.hay_ganador("X") is True

def test_no_hay_ganador():
    t = Tablero()
    t.contenedor = [
        ["X", "0", "X"],
        ["0", "X", ""],
        ["", "0", ""],
    ]
    assert t.hay_ganador("X") is False
    assert t.hay_ganador("0") is False

def test_esta_lleno_false_al_inicio_y_true_cuando_se_llena():
    t = Tablero()
    assert t.esta_lleno() is False
    t.contenedor = [
        ["X", "0", "X"],
        ["X", "0", "X"],
        ["0", "X", "0"],
    ]
    assert t.esta_lleno() is True 