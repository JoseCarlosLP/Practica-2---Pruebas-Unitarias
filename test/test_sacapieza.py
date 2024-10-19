import pytest

from ajedrezoo import ocupadas, cocupadas, sacapieza, Reyblanco


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


def test_sacapieza(setup_teardown_metapieza):
    # Precondicion: Instanciamos la pieza y verificamos que sus propiedades sean correctas y este en el tablero
    pieza = Reyblanco()
    assert pieza.movida == 0
    assert pieza.casx == 5
    assert pieza.casy == 8
    assert ocupadas[pieza.casy][pieza.casx] == pieza

    resultado = sacapieza(5, 8)

    # Postcondicion: La pieza resultado obtenida de sacar la pieza del tablero, debe ser la misma que se instancio
    assert resultado is pieza
    assert resultado.movida == 0
    assert resultado.casx == 5
    assert resultado.casy == 8
