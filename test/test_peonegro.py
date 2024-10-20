import pytest
from ajedrezoo import Peonegro, ocupadas, cocupadas
import pygame
from unittest import mock

@pytest.fixture(scope="function")
def setup_teardown():
    global ocupadas, cocupadas

    print("\nSetup: Inicializando tablero")
    assert all(len(fila) == 9 for fila in ocupadas), "Error: ocupadas debe tener 9 columnas"
    assert all(len(fila) == 9 for fila in cocupadas), "Error: cocupadas debe tener 9 columnas"
    
    
    yield
    
    print("\nTeardown: Limpiando ocupadas y cocupadas")
    ocupadas = [[0]*9 for _ in range(9)]
    cocupadas = [[0]*9 for _ in range(9)]
    
    assert all(all(casilla == 0 for casilla in fila) for fila in ocupadas), "Error: ocupadas no fue limpiada correctamente"
    assert all(all(casilla == 0 for casilla in fila) for fila in cocupadas), "Error: cocupadas no fue limpiada correctamente"
    
    
class TestPeonBlanco:
    
    def test_peonblanco_init_(self):
        x=6
        # Precondición:
        assert 0 <= x < 9
        ob = Peonegro(x)
        # Postcondición:
        assert ob.casx < 9
        assert ob.casy == 2
        assert ob.color == 2
        assert isinstance(ob.foto, pygame.Surface)
        assert ocupadas[ob.casy][ob.casx] == ob
        assert cocupadas[ob.casy][ob.casx] == ob.color

    @mock.patch('ajedrezoo.metapeon.movpeon', return_value=[(6, 3),(6, 4)])
    def test_puedemovera(self, mock_movpeon):
        x=6
        # Precondición:
        assert 0 <= x < 9

        ob = Peonegro(x)
        assert isinstance(ob, Peonegro)

        mov_posibles = ob.puedemovera()

        #Postcondicion: 
        assert mov_posibles == [(6, 3),(6, 4)]