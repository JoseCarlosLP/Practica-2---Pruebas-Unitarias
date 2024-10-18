import pytest
from ajedrezoo import metapieza, ocupadas, cocupadas

@pytest.fixture
def pieza_fixture():
    global ocupadas, cocupadas
    #Precondicion
    for i in range(9):
        for j in range(9):
            ocupadas[i][j] = 0
            cocupadas[i][j] = 0

    pieza = metapieza(1, 1, "c")
    return pieza

def test_cambiasilla(pieza_fixture):
    pieza = pieza_fixture

    # Verificar precondiciones
    assert ocupadas[1][1] == pieza, "La pieza debería estar en la posición inicial (1, 1)"
    assert cocupadas[1][1] == 1, "La casilla (1, 1) debería estar ocupada por una pieza de color 1"
    assert pieza.movida == 0, "La pieza no debería haber sido movida inicialmente"

    for i in range(9):
        for j in range(9):
            if (i, j) != (1, 1):
                assert ocupadas[i][j] == 0, f"La casilla ({i}, {j}) debería estar vacía antes del movimiento"
                assert cocupadas[i][j] == 0, f"La casilla de color ({i}, {j}) debería estar vacía antes del movimiento"

    # Cambiar la posición de la pieza a (2, 2)
    pieza.cambiasilla(2, 2)

    # Verificar postcondiciones
    assert ocupadas[1][1] == 0, "La casilla (1, 1) debería estar vacía después de mover la pieza"
    assert cocupadas[1][1] == 0, "El color de la casilla (1, 1) debería estar vacío después del movimiento"

    assert ocupadas[2][2] == pieza, "La pieza debería estar en la nueva posición (2, 2)"
    assert cocupadas[2][2] == 1, "La casilla (2, 2) debería estar ocupada por una pieza de color 1"
    
    for i in range(9):
        for j in range(9):
            if (i, j) not in [(1, 1), (2, 2)]:
                assert ocupadas[i][j] == 0, f"La casilla ({i}, {j}) debería estar vacía tras el movimiento"
                assert cocupadas[i][j] == 0, f"La casilla de color ({i}, {j}) debería estar vacía tras el movimiento"

    # Verificar estado final
    assert pieza.casx == 2, "La coordenada X de la pieza debería ser 2"
    assert pieza.casy == 2, "La coordenada Y de la pieza debería ser 2"
    assert pieza.movida == 1, "La pieza debería haber sido marcada como movida"
