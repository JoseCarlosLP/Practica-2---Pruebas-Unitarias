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
    
    
class TestTorreBlancaInit:
    
    def test_torreblanca_init_(self, setup_teardown):
        x=8
        # Precondición:
        assert 0 <= x < 9
        ob = Torreblanca(x)
        
        # Postcondición:
        assert ob.casx < 9
        assert ob.casy == 8
        assert ob.color == 1
        assert isinstance(ob.foto, pygame.Surface)
        assert ocupadas[ob.casy][ob.casx] == ob
        assert cocupadas[ob.casy][ob.casx] == ob.color

    @mock.patch('ajedrezoo.metapieza.movlineal', return_value=[(7, 8), (8, 7),(6,8)])
    def test_puedemovera(self, mock_movlineal, setup_teardown):
        x=8
        # Precondición:
        assert 0 <= x < 9

        ob = Torreblanca(x)
        assert isinstance(ob, Torreblanca)

        mov_posibles = ob.puedemovera()

        #Postcondicion: 
        assert mov_posibles == [(7, 8), (8, 7),(6,8)]