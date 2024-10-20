import pytest
from ajedrezoo import *
from unittest import mock

@pytest.fixture
def setup_teardown():
    global ocupadas, cocupadas,lpeon
    lpeon = [0, -1, 1, 5, 4]

    print("\nSetup: Inicializando tablero")
    assert all(len(fila) == 9 for fila in ocupadas), "Error: ocupadas debe tener 9 columnas"
    assert all(len(fila) == 9 for fila in cocupadas), "Error: cocupadas debe tener 9 columnas"
    
    
    yield
    
    print("\nTeardown: Limpiando ocupadas y cocupadas")
    ocupadas = [[0]*9 for _ in range(9)]
    cocupadas = [[0]*9 for _ in range(9)]
    
    assert all(all(casilla == 0 for casilla in fila) for fila in ocupadas), "Error: ocupadas no fue limpiada correctamente"
    assert all(all(casilla == 0 for casilla in fila) for fila in cocupadas), "Error: cocupadas no fue limpiada correctamente"
    
    
class TestMovpeon:
    # C1
    def test_movpeon_sin_casillas_adelante(self,setup_teardown):
    # Setup 
       x=0
       y=0
       color=1
    # Precondición:
       assert 0 <= x < 9
       assert 0 <= y < 9 

          
       ob=metapeon(x,y,color)
       ob.casposibles=ob.movpeon()
    # Poscondición:
    #    Verificar el avance hacia adelante
       assert 0>ob.casy+lpeon[ob.color]
       assert ob.casposibles==[]
    
    #C2
    def test_movpeon_fuera_de_tablero_en_x(self,setup_teardown):
    # Setup 
       x=9
       y=7
       color=1
    # Precondición:
       assert  x > 8
       assert 0 <= y < 9 

          
       ob=metapeon(x,y,color)
       ob.casposibles=ob.movpeon()
    # Poscondición:
    #    Verificar el avance hacia adelante
       assert 0<ob.casy+lpeon[ob.color]<=8
       assert ob.casx>8
       assert ob.casposibles==[]
    
    #C3
    def test_movpeon_casilla_del_frente_ocupada(self,setup_teardown):
    # Setup 
       x=8
       y=1
       color=1
       cocupadas[0][8]=2
    # Precondición:
       assert 0 <= x < 9
       assert 0 <= y < 9 

       ob=metapeon(x,y,color)
       ob.movpeon()
    # Poscondición:
    #    Verificar el avance hacia adelante
       assert 0<=ob.casy+lpeon[ob.color]<=8
       assert 0 <ob.casx<=8
    #    Verificar que la casilla del frente está ocupada
       assert cocupadas[ob.casy+lpeon[ob.color]][ob.casx]!=0
    #    Verificar si no hay espacio a la izquierda
       assert ob.casx+1>8
    #    Verificar que si hay espacio a la derecha
       assert ob.casx-1<=8
    #    Verificar que NO hay enemigo en diagonal derecha
       assert cocupadas[ob.casy + lpeon[ob.color]][ob.casx - 1] != 3 - ob.color
       print(ob.casposibles)       
       assert ob.casposibles==[]
    #C4
    
    # C12
    @mock.patch('ajedrezoo.metapeon.movpeon', return_value=[(4,6),(4,5),(5,6),(3,6)])
    def test_movpeon_movimiento_inicial_y_capturas_a_derecha_e_izquierda(self, mock_movpeon,setup_teardown):
    # Setup 
       x=4
       y=7
       color=1
       cocupadas[6][5]=2
       cocupadas[6][3]=2
    # Precondición:
       assert 0 <= x < 9
       assert 0 <= y < 9 

          
       ob=metapeon(x,y,color)
       ob.casposibles=ob.movpeon()
    # Poscondición:
    #    Verificar el avance hacia adelante
       assert 0<ob.casy+lpeon[ob.color]<=8
       assert 0 <ob.casx<=8
    #    Verificar que la casilla del frente está vacía
       assert cocupadas[ob.casy+lpeon[ob.color]][ob.casx]==0
    #    verificar que se añade la casilla del frente vacía
       assert (ob.casx,ob.casy+lpeon[ob.color]) in ob.casposibles
    #    Verificar si se puede hacer doble movimiento inicial
       assert ob.movida==0
       assert cocupadas[lpeon[ob.color + 2]][ob.casx] == 0
    #    Verificar que se añade la segunda casilla al frente
       assert (ob.casx, lpeon[ob.color + 2]) in ob.casposibles
    #    Verificar si se puede hacer captura diagonal derecha
       assert 0 < ob.casy + lpeon[ob.color] <= 8
       assert 0 < ob.casx + 1 <= 8
    #    Verificar si hay enemigo derecha
       assert cocupadas[ob.casy + lpeon[ob.color]][ob.casx + 1] == 3 - ob.color
    # Verificar que se añada al casilla diagonal derecha
       assert (ob.casx + 1, ob.casy + lpeon[ob.color]) in ob.casposibles
    #    Verificar que se puede hacer captura diagonal izquierda
       assert 0 < ob.casy + lpeon[ob.color] <= 8
       assert 0 < ob.casx - 1 <= 8
    #    Verificar si hay enemigo izquierda
       assert cocupadas[ob.casy + lpeon[ob.color]][ob.casx - 1] == 3 - ob.color
    #    Verificar que se añada diagonal
       assert (ob.casx - 1, ob.casy + lpeon[ob.color]) in ob.casposibles
    # C11
    @mock.patch('ajedrezoo.metapeon.movpeon', return_value=[(4,6),(4,5),(5,6)])
    def test_movpeon_movimiento_inicial_y_captura_a_derecha__sin_enemigo_a_izquierda(self, mock_movpeon,setup_teardown):
    # Setup 
       x=4
       y=7
       color=1
       cocupadas[6][1]=2
    #    cocupadas[6][3]=0
    # Precondición:
       assert 0 <= x < 9
       assert 0 <= y < 9 
          
       ob=metapeon(x,y,color)
       ob.casposibles=ob.movpeon()
    # Poscondición:
       assert (ob.casx,ob.casy+lpeon[ob.color]) in ob.casposibles
    #    Verificar que se añade la segunda casilla al frente
       assert (ob.casx, lpeon[ob.color + 2]) in ob.casposibles
    #    Verificar si hay enemigo a la diagonal derecha
       assert (ob.casx + 1, ob.casy + lpeon[ob.color]) in ob.casposibles
    #    Verificar que NO hay enemigo izquierda
       assert 0 < ob.casx - 1 <= 8
    #    Verificar que no se añada enemigo de diagonal izquierda
       assert (ob.casx - 1, ob.casy + lpeon[ob.color]) not in ob.casposibles
    # c10
    @mock.patch('ajedrezoo.metapeon.movpeon', return_value=[(0,6),(0,5),(1,6)])
    def test_movpeon_movimiento_inicial_y_captura_a_derecha_sin_espacio_a_izquierda(self, mock_movpeon,setup_teardown):
    # Setup 
       x=0
       y=7
       color=1
       cocupadas[6][1]=2
    # Precondición:
       assert 0 <= x < 9
       assert 0 <= y < 9 
          
       ob=metapeon(x,y,color)
       ob.casposibles=ob.movpeon()
    # Poscondición:
       assert (ob.casx,ob.casy+lpeon[ob.color]) in ob.casposibles
    #    Verificar que se añade la segunda casilla al frente
       assert (ob.casx, lpeon[ob.color + 2]) in ob.casposibles
    #    Verificar si hay enemigo a la diagonal derecha
       assert (ob.casx + 1, ob.casy + lpeon[ob.color]) in ob.casposibles
    #    Verificar que NO hay espacio a la izquierda
       assert 0 > ob.casx - 1 <= 8
    #    Verificar que no se añada enemigo de diagonal izquierda
       assert (ob.casx - 1, ob.casy + lpeon[ob.color]) not in ob.casposibles

       
