from unittest.mock import MagicMock

import pytest

from ajedrezoo import Reinablanca, comepieza, ocupadas, cocupadas, sacapieza, Reyblanco


@pytest.fixture
def setup_teardown_metapieza():
    global ocupadas, cocupadas

    print("\nSetup: Inicializando tablero")
    assert all(len(fila) == 9 for fila in ocupadas), "Error: ocupadas debe tener 9 columnas"
    assert all(len(fila) == 9 for fila in cocupadas), "Error: cocupadas debe tener 9 columnas"

    yield

    print("\nTeardown: Limpiando ocupadas y cocupadas")
    ocupadas = [[0] * 9 for _ in range(9)]
    cocupadas = [[0] * 9 for _ in range(9)]

    assert all(
        all(casilla == 0 for casilla in fila) for fila in ocupadas), "Error: ocupadas no fue limpiada correctamente"
    assert all(
        all(casilla == 0 for casilla in fila) for fila in cocupadas), "Error: cocupadas no fue limpiada correctamente"


def test_comepieza(setup_teardown_metapieza):
    # Precondicion: Instanciamos la pieza y verificamos que sus propiedades sean correctas y este en el tablero
    pieza = Reinablanca()
    assert pieza.movida == 0
    assert pieza.casx == 4
    assert pieza.casy == 8
    assert ocupadas[pieza.casy][pieza.casx] == pieza
    assert cocupadas[pieza.casy][pieza.casx] == 1

    def mock_cambiasilla(x, y):
        ocupadas[pieza.casy][pieza.casx] = cocupadas[pieza.casy][pieza.casx] = 0
        pieza.casx = x
        pieza.casy = y
        pieza.movida = 1

    pieza.cambiasilla = MagicMock(side_effect=mock_cambiasilla)
    comepieza(pieza)

    # Postcondicion: La pieza ha sido removida del tablero y la casilla que estaba ocupando se encuentra libre
    assert pieza.movida == 1
    assert pieza.casx == 9
    assert pieza.casy == 9
    assert ocupadas[8][4] == 0
    assert cocupadas[8][4] == 0



