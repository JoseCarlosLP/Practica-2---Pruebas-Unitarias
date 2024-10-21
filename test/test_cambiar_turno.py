import pytest
from ajedrezoo import ocupadas, cocupadas, metapieza, cambiar_turno

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

def test_turno_negras(setup_teardown_metapieza):
    #Precondicion: Cuando el color de fichamover vale 1 significa que es el turno de las negras
    x = 4
    y = 4
    color = 1
    fichamover = metapieza(x, y, color)
    assert isinstance(fichamover, metapieza)
    assert fichamover.color == 1

    turno = cambiar_turno(fichamover)

    #Postcondicion: La casilla correspondiente a las coordenadas del mouse debe ser la 8, 8
    assert turno == "negras"

def test_turno_blancas(setup_teardown_metapieza):
    #Precondicion: Cuando el color de fichamover vale 2 significa que es el turno de las blancas 
    x = 4
    y = 4
    color = 2
    fichamover = metapieza(x, y, color)
    assert isinstance(fichamover, metapieza)
    assert fichamover.color == 2

    turno = cambiar_turno(fichamover)

    #Postcondicion: La casilla correspondiente a las coordenadas del mouse debe ser la 8, 8
    assert turno == "blancas"