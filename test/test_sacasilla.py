import pytest

from ajedrezoo import ocupadas, cocupadas, sacasilla


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


def test_camino_1(setup_teardown_metapieza):
    #Precondicion: Generamos coordenadas del mouse en x y en y
    posratox_x = 500
    posratox_y = 500
    posraton = (posratox_x, posratox_y)

    casilla = sacasilla(posraton)

    #Postconidcion: La casilla correspondiente a las coordenadas del mouse debe ser la 8, 8
    assert casilla == (8, 8)

def test_camino2(setup_teardown_metapieza):
    #Precondicion: Generamos coordenadas del mouse en x y en y
    posratox_x = 500
    posratox_y = 1000
    posraton = (posratox_x, posratox_y)

    #El resultado obtenido debe ser un error ya que el juego solo valida las coordenadas hasta 999
    with pytest.raises(UnboundLocalError):
        casilla = sacasilla(posraton)

def test_camino3(setup_teardown_metapieza):
    #Precondicion: Generamos coordenadas del mouse en x y en y
    posratox_x = 1000
    posratox_y = 1000
    posraton = (posratox_x, posratox_y)

    #El resultado obtenido debe ser un error ya que el juego solo valida las coordenadas hasta 999
    with pytest.raises(UnboundLocalError):
        casilla = sacasilla(posraton)