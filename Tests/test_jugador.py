import pytest
from clases.Jugador import Jugador  

def test_jugador_init_y_getters():
    j = Jugador("Ana", "X")
    assert j.get_nombre() == "Ana"
    assert j.get_ficha() == "X"
    # Flags iniciales
    assert j.jugando is False
    assert j.gano is False
    assert j.perdio is False 


