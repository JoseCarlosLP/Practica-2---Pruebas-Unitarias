import pytest
from ajedrezoo import metapieza, ocupadas, cocupadas

@pytest.fixture
def setup_teardown_metapieza():
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
    
    
class TestMetapiezaInit:
    
    def test_metapieza_dentro_de_posisiones_validas(self, setup_teardown_metapieza):
        casx=8
        casy=2
        # Precondición:
        assert 0 <= casx < 9, "Error: casx fuera del rango"
        assert 0 <= casy < 9, "Error: casy fuera del rango"

        ob = metapieza(casx, casy, "c")
        
        # Postcondición:
        assert ob.casx < 9
        assert ob.casy < 9
        assert ob.color == "c"
        assert ocupadas[ob.casy][ob.casx] == ob
        assert cocupadas[ob.casy][ob.casx] == ob.color
        
    def test_metapieza_fuera_del_limite_y(self, setup_teardown_metapieza):
        casx=8
        casy=10
        # Precondición:
        assert 0 <= casx < 9, "Error: casx fuera del rango"
        assert casy >= 9, "Error: casx debería estar fuera del límite"
        
        ob = metapieza(casx, casy, "c")
        
        # Postcondición: 
        assert ob.casx < 9
        assert ob.casy >= 9
        assert ob.color == "c"
        assert ob not in ocupadas, "Error: la pieza no debería estar en ocupadas"
        assert ob.color not in cocupadas, "Error: el color de la pieza no debería estar en cocupadas"
        
    def test_metapieza_fuera_del_limite_x(self, setup_teardown_metapieza):
        # Precondición:
        casx=10
        casy=2
        assert casx >= 9, "Error: casx debería estar fuera del límite"
        assert 0 <= casy < 9, "Error: casy fuera del rango"
        
        ob = metapieza(casx, casy, "c")
        
        # Postcondición: 
        assert ob.casx >= 9
        assert ob.casy < 9
        assert ob.color == "c"
        assert ob not in ocupadas, "Error: la pieza no debería estar en ocupadas"
        assert ob.color not in cocupadas, "Error: el color de la pieza no debería estar en cocupadas"
