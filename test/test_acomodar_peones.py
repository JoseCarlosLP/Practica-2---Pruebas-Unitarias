import pytest
from ajedrezoo import *
from unittest import mock

@pytest.fixture
def setup_teardown():
    global lpeon
    lpeon = [0, -1, 1, 5, 4]
    print("\nSetup: Inicializando tablero")
    for i in range(8):
        for j in range(8):
            ocupadas[i][j] = 0
            cocupadas[i][j] = 0

    yield  # Permitir que el test se ejecute

    print("\nSetup: Limpiando tablero")
    for i in range(8):
        for j in range(8):
            ocupadas[i][j] = 0
            cocupadas[i][j] = 0

class TestAcomodarPeones():
    @mock.patch('builtins.range', return_value=[])
    def test_acomodar_peones_p_sin_rango(self,mock_range,setup_teardown):
        peonegro=[0]
        peonblanco=[0]
        acomodar_peones(peonegro,peonblanco)
        assert peonegro==[0]
        assert peonblanco==[0]
        assert ocupadas == [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],  
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0]
        ]
        assert cocupadas == [  #color de las ocupadas
            [0, 0, 0, 0, 0, 0, 0, 0, 0], 
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0]
        ]

    def test_acomodar_peones_p_en_rango(self,setup_teardown):
        peonegro=[0]
        peonblanco=[0]
        acomodar_peones(peonegro,peonblanco)
        assert peonegro!=[0]
        assert peonblanco!=[0]
        assert isinstance(ocupadas[7][3], Peonblanco)
        assert ocupadas[7] != [0, 0, 0, 0, 0, 0, 0, 0, 0]
        assert cocupadas[7]==[0, 1, 1, 1, 1, 1, 1, 1, 1]
        assert isinstance(ocupadas[2][3], Peonegro)
        assert ocupadas[2] != [0, 0, 0, 0, 0, 0, 0, 0, 0]
        assert cocupadas[2]==[0, 2, 2, 2, 2, 2, 2, 2, 2]

        
    
        