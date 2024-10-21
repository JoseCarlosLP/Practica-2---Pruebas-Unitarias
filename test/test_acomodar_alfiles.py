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

class TestAcomodarAlfiles:
    def test_acomodar_alfiles(self,setup_teardown):
        alfilnegro=[0]
        alfilblanco=[0]
        acomodar_alfiles(alfilnegro,alfilblanco)
        assert alfilnegro!=[0]
        assert alfilblanco!=[0]
        assert isinstance(ocupadas[8][3], Alfilblanco)
        
        assert isinstance(ocupadas[8][6], Alfilblanco)
        assert ocupadas[8][3] !=0
        assert cocupadas[8][3]==1
        assert isinstance(ocupadas[1][3], Alfilnegro)
        assert isinstance(ocupadas[1][6], Alfilnegro)
        assert ocupadas[1][6] != 0
        assert cocupadas[1][6]== 2

        
    
        