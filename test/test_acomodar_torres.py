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

class TestAcomodarTorres:
    def test_acomodar_torres(self,setup_teardown):
        torrenegra=[0]
        torreblanca=[0]
        acomodar_torres(torrenegra,torreblanca)
        assert torrenegra!=[0]
        assert torreblanca!=[0]
        assert isinstance(ocupadas[8][1], Torreblanca)
        
        assert isinstance(ocupadas[8][8], Torreblanca)
        assert ocupadas[8][1] !=0
        assert cocupadas[8][8]==1
        assert isinstance(ocupadas[1][1], Torrenegra)
        assert isinstance(ocupadas[1][8], Torrenegra)
        assert ocupadas[1][1] != 0
        assert cocupadas[1][8]== 2

        
    
        