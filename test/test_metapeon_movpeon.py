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
   def test_sin_casillas_adelante(self,setup_teardown):
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
    
   def test_fuera_de_tablero_en_x(self,setup_teardown):
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
    
   def test_casilla_del_frente_ocupada(self,setup_teardown):
       x=8
       y=1
       color=1
       cocupadas[0][8]=1
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
   
   def test_puede_avanzar_hacia_adelante_pero_no_es_su_primera_movida_sin_enemigo_a_diagonal_izquierda_y_sin_espacio_en_diagonal_derecha(self,setup_teardown):
       x=8
       y=7
       color=1
    # Precondición:
       assert 0 <= x < 9
       assert 0 <= y < 9 

          
       ob=metapeon(x,y,color)
       ob.movida=2
       ob.movpeon()
      #  Poscondición
    #    verificar que se añade la casilla del frente vacía
       assert (ob.casx,ob.casy+lpeon[ob.color]) in ob.casposibles
    #    Verificar que NO se añade la segunda casilla al frente
       assert (ob.casx, lpeon[ob.color + 2]) not in ob.casposibles
    #    Verificar que NO se hacer captura diagonal derecha
       assert 0 < ob.casx + 1 >= 8
    #    Verificar que se puede hacer captura diagonal izquierda
       assert 0 < ob.casy + lpeon[ob.color] <= 8
       assert 0 < ob.casx - 1 <= 8
    #    Verificar que NO hay enemigo izquierda
       assert cocupadas[ob.casy + lpeon[ob.color]][ob.casx - 1] != 3 - ob.color
   # Verificar que solo se añadió la casilla que se encuentra en frente
       assert ob.casposibles==[(8,6)]

   @mock.patch('ajedrezoo.metapeon.movpeon', return_value=[(8,6),(7,6)])
   def test_puede_avanzar_hacia_adelante_pero_no_es_su_primera_movida_con_enemigo_a_diagonal_izquierda_y_sin_espacio_en_diagonal_derecha(self,setup_teardown):
       x=8
       y=7
       color=1
       cocupadas[y-1][x-1]=2
    # Precondición:
       assert 0 <= x < 9
       assert 0 <= y < 9 
          
       ob=metapeon(x,y,color)
       ob.movida=2
       ob.casposibles=ob.movpeon()
      #  Poscondición
    #    verificar que se añade la casilla del frente vacía
       assert (ob.casx,ob.casy+lpeon[ob.color]) in ob.casposibles
    #    Verificar que NO se añade la segunda casilla al frente
       assert (ob.casx, lpeon[ob.color + 2]) not in ob.casposibles
    #    Verificar que NO se hacer captura diagonal derecha
       assert 0 < ob.casx + 1 >= 8
    #    Verificar que se puede hacer captura diagonal izquierda
       assert 0 < ob.casy + lpeon[ob.color] <= 8
       assert 0 < ob.casx - 1 <= 8
   # Verificar que se se añadió la casilla que se encuentra en frente y diagonal izquierda
       assert ob.casposibles==[(8,6),(7,6)]

   @mock.patch('ajedrezoo.metapeon.movpeon', return_value=[(0,6)])
   def test_movimiento_inicial_pero_ocupado_y_espacio_para_diagonal_derecha_sin_enemigo_y_sin_espacio_en_diagonal_izquierda(self,mock_movpeon,setup_teardown):
       x=0
       y=7
       color=1
       cocupadas[5][0]=2
    # Precondición:
       assert 0 <= x < 9
       assert 0 <= y < 9 
       ob=metapeon(x,y,color)
       ob.casposibles=ob.movpeon()
    # Poscondición:
    #    verificar que se añade la casilla del frente vacía
       assert (ob.casx,ob.casy+lpeon[ob.color]) in ob.casposibles
    #    Verificar si se puede hacer doble movimiento inicial
       assert ob.movida==0
    #    Verificar que NO se añade la segunda casilla al frente
       assert (ob.casx, lpeon[ob.color + 2])not in ob.casposibles
    #    Verificar que si se puede hacer captura diagonal derecha
       assert 0 < ob.casx + 1 <= 8
    #    Verificar que NO hay enemigo derecha
       assert cocupadas[ob.casy + lpeon[ob.color]][ob.casx + 1] != 3 - ob.color
    #    Verificar que NO se puede hacer captura diagonal izquierda
       assert 0 > ob.casx - 1

       assert ob.casposibles==[(0,6)]

   @mock.patch('ajedrezoo.metapeon.movpeon', return_value=[(0,6),(1,6)])
   def test_movimiento_inicial_pero_ocupado_y_enemigo_en_diagonal_derecha_sin_espacio_en_diagonal_izquierda(self,mock_movpeon,setup_teardown):
       x=0
       y=7
       color=1
       cocupadas[5][0]=2
       cocupadas[6][1]=2
    # Precondición:
       assert 0 <= x < 9
       assert 0 <= y < 9 
       ob=metapeon(x,y,color)
       ob.casposibles=ob.movpeon()
    # Poscondición:
    #    verificar que se añade la casilla del frente vacía
       assert (ob.casx,ob.casy+lpeon[ob.color]) in ob.casposibles
    #    Verificar si se puede hacer doble movimiento inicial
       assert ob.movida==0
    #    Verificar que NO se añade la segunda casilla al frente
       assert (ob.casx, lpeon[ob.color + 2])not in ob.casposibles
    #    Verificar que si se puede hacer captura diagonal derecha
       assert 0 < ob.casx + 1 <= 8
    #    Verificar que hay enemigo derecha
       assert cocupadas[ob.casy + lpeon[ob.color]][ob.casx + 1] == 3 - ob.color
    #    Verificar que NO se puede hacer captura diagonal izquierda
       assert 0 > ob.casx - 1
       
       assert ob.casposibles==[(0,6), (1,6)]

   def test_movimiento_inicial_doble_sin_enemigo_a_diagonal_izquierda_y_sin_espacio_en_diagonal_derecha(self,setup_teardown):
       x=8
       y=7
       color=1
    # Precondición:
       assert 0 <= x < 9
       assert 0 <= y < 9           
       ob=metapeon(x,y,color)
       ob.movpeon()
      #  Poscondición
    #    verificar que se añade la casilla del frente vacía
       assert (ob.casx,ob.casy+lpeon[ob.color]) in ob.casposibles
    #    Verificar que se añade la segunda casilla al frente
       assert (ob.casx, lpeon[ob.color + 2]) in ob.casposibles
    #    Verificar que NO se hacer captura diagonal derecha
       assert 0 < ob.casx + 1 >= 8
    #    Verificar que se puede hacer captura diagonal izquierda
       assert 0 < ob.casy + lpeon[ob.color] <= 8
       assert 0 < ob.casx - 1 <= 8
    #    Verificar que NO hay enemigo izquierda
       assert cocupadas[ob.casy + lpeon[ob.color]][ob.casx - 1] != 3 - ob.color
   # Verificar que solo se añadió la casilla que se encuentra en frente
       assert ob.casposibles==[(8,6),(8,5)]

   @mock.patch('ajedrezoo.metapeon.movpeon', return_value=[(0,6),(0,5)])
   def test_movimiento_inicial_y_espacio_para_diagonal_derecha_sin_enemigo_y_sin_espacio_en_diagonal_izquierda(self,mock_movpeon,setup_teardown):
       x=0
       y=7
       color=1
    # Precondición:
       assert 0 <= x < 9
       assert 0 <= y < 9 
       ob=metapeon(x,y,color)
       ob.casposibles=ob.movpeon()
    # Poscondición:
    #    verificar que se añade la casilla del frente vacía
       assert (ob.casx,ob.casy+lpeon[ob.color]) in ob.casposibles
    #    Verificar que se añade la segunda casilla al frente
       assert (ob.casx, lpeon[ob.color + 2]) in ob.casposibles
    #    Verificar que si se puede hacer captura diagonal derecha
       assert 0 < ob.casx + 1 <= 8
    #    Verificar que NO hay enemigo derecha
       assert cocupadas[ob.casy + lpeon[ob.color]][ob.casx + 1] != 3 - ob.color
    #    Verificar que NO se puede hacer captura diagonal izquierda
       assert 0 > ob.casx - 1
       assert ob.casposibles==[(0,6),(0,5)]

   @mock.patch('ajedrezoo.metapeon.movpeon', return_value=[(0,6),(0,5),(1,6)])
   def test_movimiento_inicial_y_captura_a_derecha_sin_espacio_en_diagonal_izquierda(self, mock_movpeon,setup_teardown):
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
       assert cocupadas[ob.casy + lpeon[ob.color]][ob.casx + 1] == 3 - ob.color
    #    Verificar que NO hay espacio a  izquierda
       assert 0 > ob.casx - 1
    #    Verificar que no se añada enemigo de diagonal izquierda
       assert (ob.casx - 1, ob.casy + lpeon[ob.color]) not in ob.casposibles
       assert ob.casposibles ==[(0,6),(0,5),(1,6)]  


   @mock.patch('ajedrezoo.metapeon.movpeon', return_value=[(4,6),(4,5),(5,6)])
   def test_movpeon_movimiento_inicial_y_captura_a_derecha_sin_enemigo_a_izquierda(self, mock_movpeon,setup_teardown):
       x=4
       y=7
       color=1
       cocupadas[6][5]=2
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

   def test_movimiento_inicial_y_capturas_a_derecha_e_izquierda(self,setup_teardown):
       x=4
       y=7
       color=1
       cocupadas[6][5]=2
       ocupadas[6][5]=metapieza(5,6,2)
       cocupadas[6][3]=2
       ocupadas[6][3]=metapieza(3,6,2)
    # Precondición:
       assert 0 <= x < 9
       assert 0 <= y < 9 
          
       ob=metapeon(x,y,color)
       ob.movpeon()
    # Poscondición:
    #    verificar que se añade la casilla del frente vacía
       assert (ob.casx,ob.casy+lpeon[ob.color]) in ob.casposibles
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
    
