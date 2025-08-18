Este es un proyecto de Ta-Te-Ti desarrollado en Python.  
Permite jugar de a dos personas por consola y cuenta con un conjunto de tests automatizados con pytest para validar la lógica del juego. 

## Estructura del proyecto
tateti/
│
├─ clases/
│ ├─ init.py
│ ├─ cli.py 
│ ├─ Tateti.py 
│ ├─ Tablero.py
│ ├─ Jugador.py
│ └─ sys.path 
│
├─ Tests/
│ ├─ test_jugador.py
│ ├─ test_tablero.py
│ └─ test_tateti.py
│
└─ README.md
## Requisitos

- Python 3.7 o superior
- pytest (para ejecutar los tests)

## Cómo jugar
Para jugar, basta con ejecutar el juego desde la carpeta raíz del proyecto  "python3 clases/Cli.py" 

El programa pedirá los nombres de los jugadores. 
Luego, los jugadores se turnarán colocando fichas (X y 0) en el tablero. 
Cada jugada se ingresa indicando fila y columna (valores de 0 a 2).

## Ejecutar los tests
 Ejecutar desde la carpeta raíz del proyecto  "python3 -m pytest" 

## Clases principales: 

cli.py 

Este archivo contiene el flujo principal del juego y es desde donde se inicia la partida.

Jugador:

Representa a cada jugador con su nombre y ficha (X u 0).
Métodos principales:
get_nombre()
get_ficha()

Tablero:

Representa el tablero 3x3.
Métodos principales:
poner_la_ficha(fil, col, ficha)
hay_ganador(ficha)
esta_lleno()
Incluye la excepción personalizada PosOcupadaException para evitar marcar casillas ya ocupadas.

Tateti:

Contiene la lógica principal del juego.
Alterna turnos entre jugadores.
Verifica condiciones de victoria o empate.

## Tests:

El proyecto incluye tests con pytest.

Tests incluidos:

test_jugador.py: verifica inicialización y getters de la clase Jugador.
test_tablero.py: valida la lógica de colocar fichas, detectar ganadores y tablero lleno.
test_tateti.py: prueba el flujo de turnos, la detección de ganadores, empates y casillas ocupadas.