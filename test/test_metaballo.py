import pytest
from ajedrezoo import metaballo,ocupadas, cocupadas

@pytest.fixture
def setup():
    global ocupadas, cocupadas
    #Precondicion
    for i in range(9):
        for j in range(9):
            ocupadas[i][j] = 0
            cocupadas[i][j] = 0

    pieza = metaballo(4, 4, 1)
    return pieza

def test_movcaballo(setup):
    pieza = setup

    # Precondición: El caballo debe estar en la posición inicial (4,4) y no debe haber movimientos posibles al inicio
    assert len(pieza.casposibles) == 0

    # Configura una situación donde el caballo puede moverse libremente
    for x in [-2, -1, 1, 2]:
        for y in [-(3 - abs(x)), 3 - abs(x)]:
            new_x = pieza.casx + x
            new_y = pieza.casy + y
            if 0 < new_x <= 8 and 0 < new_y <= 8:
                # Coloca casillas vacías o con piezas del color contrario en las posiciones posibles
                cocupadas[new_y][new_x] = 0

    # Llamada a la función movcaballo
    movimientos_posibles = pieza.movcaballo()

    # Postcondición: Verifica que el caballo tiene 8 movimientos posibles
    assert len(movimientos_posibles) == 8

    # Verifica que los movimientos sean válidos
    for (casx, casy) in movimientos_posibles:
        assert 0 < casx <= 8, f"Movimiento inválido fuera del tablero en x: {casx}"
        assert 0 < casy <= 8, f"Movimiento inválido fuera del tablero en y: {casy}"
        assert cocupadas[casy][casx] == 0 or cocupadas[casy][casx] == 2, \
            f"Movimiento no permitido a casilla ocupada por pieza del mismo color en {casx}, {casy}"

    # Verifica que todos los nodos se recorrieron correctamente
    assert len(movimientos_posibles) == 8, "No se recorrieron todas las combinaciones posibles."
