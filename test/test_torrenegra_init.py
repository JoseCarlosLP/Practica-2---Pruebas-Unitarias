import pytest
from ajedrezoo import Torrenegra, ocupadas, cocupadas
import pygame

@pytest.fixture
def setup_teardown_torre_negra():
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
    
    
class TestTorreNegraInit:
    
    def test_crear_torre(self, setup_teardown_torre_negra):
        
        x=8
        # Precondición:
        assert 0 <= x < 9
        ob = Torrenegra(x)
        
        # Postcondición:
        assert ob.casx < 9
        assert ob.casy == 1
        assert ob.color == 2
        assert isinstance(ob.foto, pygame.Surface)
        assert ocupadas[ob.casy][ob.casx] == ob
        assert cocupadas[ob.casy][ob.casx] == ob.color