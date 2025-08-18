import pytest
from clases.Tateti import Tateti
from clases.Tablero import PosOcupadaException 

# Helper para crear juego sin pedir input
def crear_juego(monkeypatch, nombre1="J1", nombre2="J2"):
    inputs = iter([nombre1, nombre2])
    monkeypatch.setattr("builtins.input", lambda prompt="": next(inputs))
    return Tateti()

def test_turno_alterna_correctamente(monkeypatch):
    juego = crear_juego(monkeypatch)
    # Arranca jugador X (turno = 0)
    assert juego.get_jugador_actual().get_ficha() == "X"
    juego.marcar_casilla(0, 0)  # Juega X
    assert juego.get_jugador_actual().get_ficha() == "0"
    juego.marcar_casilla(1, 1)  # Juega 0
    assert juego.get_jugador_actual().get_ficha() == "X"

def test_marcar_casilla_genera_ganador_por_fila(monkeypatch):
    juego = crear_juego(monkeypatch)
    # Secuencia: X gana en la fila 0
    juego.marcar_casilla(0, 0)  # X
    juego.marcar_casilla(1, 0)  # 0
    juego.marcar_casilla(0, 1)  # X
    juego.marcar_casilla(1, 1)  # 0
    juego.marcar_casilla(0, 2)  # X -> gana
    assert juego.ganador is not None
    assert juego.ganador.get_ficha() == "X"
    assert juego.juego_terminado() is True

def test_no_se_puede_marcar_posicion_ocupada(monkeypatch):
    juego = crear_juego(monkeypatch)
    juego.marcar_casilla(0, 0)  # X ocupa (0,0)
    with pytest.raises(PosOcupadaException):
        juego.marcar_casilla(0, 0)  # intento ocupar de nuevo

def test_empate_sin_ganador(monkeypatch):
    juego = crear_juego(monkeypatch)
    # Llenamos el tablero sin 3 en línea:
    # X O X
    # X X O
    # O X O
    movimientos = [
        (0, 0), (0, 1), (0, 2),
        (1, 1), (1, 0), (2, 0),
        (1, 2), (2, 2), (2, 1),
    ]
    for fil, col in movimientos:
        juego.marcar_casilla(fil, col)

    assert juego.ganador is None
    assert juego.juego_terminado() is True