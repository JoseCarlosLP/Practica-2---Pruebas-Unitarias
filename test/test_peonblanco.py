import pytest
from ajedrezoo import *
import pygame
from unittest import mock

@pytest.fixture
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
    
    def test_peonblanco_init_(self, setup_teardown):
        x=6
        # Precondición:
        assert 0 <= x < 9
        ob = Peonblanco(x)
        # Postcondición:
        assert ob.casx < 9
        assert ob.casy == 7
        assert ob.color == 1
        assert isinstance(ob.foto, pygame.Surface)
        assert ocupadas[ob.casy][ob.casx] == ob
        assert cocupadas[ob.casy][ob.casx] == ob.color

    @mock.patch('ajedrezoo.metapeon.movpeon', return_value=[(6,6),(6,7)])
    def test_puedemovera(self, mock_movpeon, setup_teardown):
        x=6
        # Precondición:
        assert 0 <= x < 9

        ob = Peonblanco(x)
        assert isinstance(ob, Peonblanco)

        mov_posibles = ob.puedemovera()

        #Postcondicion: 
        assert mov_posibles == [(6,6),(6,7)]