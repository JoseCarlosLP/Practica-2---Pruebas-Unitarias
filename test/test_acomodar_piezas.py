import pytest
from ajedrezoo import *
from unittest import mock

@pytest.fixture
def setup_teardown():
    print("\nSetup: Inicializando tablero")
    for i in range(8):
        for j in range(8):
            ocupadas[i][j] = 0
            cocupadas[i][j] = 0

    yield  # Permitir que el test se ejecute

    print("\nTeardown: Limpiando tablero")
    for i in range(8):
        for j in range(8):
            ocupadas[i][j] = 0
            cocupadas[i][j] = 0

class TestAcomodarPiezas():
    def test_acomodar_piezas(self,setup_teardown):
        reynegro, reyblanco, reinanegra, reinablanca, peonegro, peonblanco, caballonegro, caballoblanco, alfilnegro, alfilblanco = inicializar_piezas()
        acomodar_piezas(peonegro, peonblanco, caballonegro, caballoblanco, torrenegra, torreblanca, alfilnegro, alfilblanco)
        assert peonegro!=[0]
        assert peonblanco!=[0]
        assert cocupadas == [  #color de las ocupadas
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 2, 2, 2, 2, 2, 2, 2, 2], 
            [0, 2, 2, 2, 2, 2, 2, 2, 2],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 1, 1, 1, 1, 1, 1, 1, 1],
            [0, 1, 1, 1, 1, 1, 1, 1, 1]
        ]
