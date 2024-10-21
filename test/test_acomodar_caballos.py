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

class TestAcomodarCaballos:
    def test_acomodar_caballos_c_en_rango(self,setup_teardown):
        caballonegro=[0]
        caballoblanco=[0]
        acomodar_caballos(caballonegro,caballoblanco)
        assert caballonegro!=[0]
        assert caballoblanco!=[0]
        assert isinstance(ocupadas[8][2], Caballoblanco)
        
        assert isinstance(ocupadas[8][7], Caballoblanco)
        assert ocupadas[8][2] !=0
        assert cocupadas[8][2]==1
        assert isinstance(ocupadas[1][2], Caballonegro)
        assert isinstance(ocupadas[1][7], Caballonegro)
        assert ocupadas[1][7] != 0
        assert cocupadas[1][7]== 2

        
    
        