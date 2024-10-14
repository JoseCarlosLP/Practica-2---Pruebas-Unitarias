import pytest
from ajedrezoo import *

class TestMetapiezaInit:
    def test_metapieza_dentro_de_posisiones_validas(self):
        ob=metapieza(8,2,"c")
        assert ob.casx<9
        assert ob.casy<9
        assert ob.color == "c"
        assert ocupadas[ob.casy][ob.casx]==ob
        assert cocupadas[ob.casy][ob.casx]==ob.color
        
    def test_metapieza_fuera_del_limite_y(self):
        ob=metapieza(8,10,"c")
        assert ob.casx<9
        assert ob.casy>9
        assert ob.color == "c"
        assert ob not in ocupadas
        assert ob.color not in cocupadas 
    def test_metapieza_fuera_del_limite_x(self):
        ob=metapieza(10,2,"c")
        assert ob.casx>9
        assert ob.casy<9
        assert ob.color == "c"
        assert ob not in ocupadas
        assert ob.color not in cocupadas 
        
   

        