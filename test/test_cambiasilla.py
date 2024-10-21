import pytest
from unittest.mock import MagicMock
from ajedrezoo import metapieza, ocupadas, cocupadas

@pytest.fixture(scope="function")
def tablero_fixture():
    for i in range(9):
        for j in range(9):
            cocupadas[i][j] = 0
    return cocupadas

def test_cambiasilla(tablero_fixture):
    #Precondición
    pieza = metapieza(2, 1, 1)
    assert pieza.movida == 0
    assert pieza.casx == 2
    assert pieza.casy == 1
    assert cocupadas[pieza.casy][pieza.casx] == 1

    def mock_cambiasilla(x, y):
        ocupadas[pieza.casy][pieza.casx] = cocupadas[pieza.casy][pieza.casx] = 0
        pieza.casx = x
        pieza.casy = y
        ocupadas[pieza.casy][pieza.casx] = cocupadas[pieza.casy][pieza.casx] = 1
        pieza.movida = 1

    pieza.cambiasilla = MagicMock(side_effect=mock_cambiasilla)
    pieza.cambiasilla(2, 2)
    
    #Postcondicion
    assert pieza.movida == 1
    assert cocupadas[2][2] == 1
    assert cocupadas[1][2] == 0
    assert pieza.casy == 2
    assert pieza.casx == 2