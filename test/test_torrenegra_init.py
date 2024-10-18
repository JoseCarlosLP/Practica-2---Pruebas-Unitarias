import pytest
from ajedrezoo import torrenegra, ocupadas, cocupadas

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
    
    def test_metapieza_dentro_de_posisiones_validas(self, setup_teardown_torre_negra):
        x=8
        y=2
        color="c"
        # Precondición:
        assert 0 <= x < 9
        assert 0 <= y < 9

        ob = metapieza(x, y, color)
        
        # Postcondición:
        assert ob.casx < 9
        assert ob.casy < 9
        assert ob.color == "c"
        assert ocupadas[ob.casy][ob.casx] == ob
        assert cocupadas[ob.casy][ob.casx] == ob.color