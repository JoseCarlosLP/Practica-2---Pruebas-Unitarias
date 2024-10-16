import pytest
from ajedrezoo import metapieza, ocupadas,cocupadas
@pytest.fixture
def setup_teardown_metapieza():
    # Setup: Preparando el entorno
    global ocupadas, cocupadas
    ocupadas = ocupadas
    cocupadas = cocupadas
    print("\n",ocupadas)
    print("\nSetup: Inicializando ocupadas y cocupadas")
    
    yield  # Aquí se ejecuta la prueba

    # Teardown: Limpiando el entorno
    ocupadas =  [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],  #esta linia y el 0 de mas es para kitar el 0 de los indices
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]
    cocupadas =  [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],  #esta linia y el 0 de mas es para kitar el 0 de los indices
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]
    
    print("\nTeardown: Limpiando ocupadas y cocupadas")
    print("\n",ocupadas)

class TestMetapiezaInit:
    def test_metapieza_dentro_de_posisiones_validas(self, setup_teardown_metapieza):
        ob=metapieza(8,2,"c")
        assert ob.casx<9
        assert ob.casy<9
        assert ob.color == "c"
        assert ocupadas[ob.casy][ob.casx]==ob
        assert cocupadas[ob.casy][ob.casx]==ob.color
        
    def test_metapieza_fuera_del_limite_y(self, setup_teardown_metapieza):
        ob=metapieza(8,10,"c")
        assert ob.casx<9
        assert ob.casy>9
        assert ob.color == "c"
        assert ob not in ocupadas
        assert ob.color not in cocupadas 
    def test_metapieza_fuera_del_limite_x(self, setup_teardown_metapieza):
        ob=metapieza(10,2,"c")
        assert ob.casx>9
        assert ob.casy<9
        assert ob.color == "c"
        assert ob not in ocupadas
        assert ob.color not in cocupadas 
        
