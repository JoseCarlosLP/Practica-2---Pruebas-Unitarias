import pytest
from ajedrezoo import metapieza, cocupadas

def tablero_fixture():
    for i in range(9):
        for j in range(9):
            cocupadas[i][j] = 0
    return cocupadas

#C1: I-1-2-3-4-5-6-7-8-9-10-11-12-13-14-15-16-17-18-19-20-21-22-2-23-F
def test_metapieza_movlineal1():
    #Precondicion
    tablero_fixture()
    pieza = metapieza(4, 4, 1)
    movimientos_esperados = [(3, 4), (4, 3), (4, 5), (5, 4)]
    #Postcondicion
    assert sorted(pieza.movlineal(1)) == sorted(movimientos_esperados)

#C2: I-1-2-3-4-5-6-7-8-9-10-11-12-13-14-15-16-17-18-19-20-21-2-23-F
def test_metapieza_movlineal2():
    #Precondicion
    tablero_fixture()
    pieza = metapieza(4, 4, 1)
    cocupadas[5][4] = 1
    movimientos_esperados = [(3, 4), (4, 3), (5, 4)]
    #Postcondicion
    assert sorted(pieza.movlineal(1)) == sorted(movimientos_esperados)

#C3: I-1-2-3-4-5-6-7-8-9-10-11-12-13-14-15-16-17-18-19-20-2-23-F
def test_metapieza_movlineal3():
    #Precondicion
    tablero_fixture()
    pieza = metapieza(4, 4, 1)
    cocupadas[5][4] = 1
    movimientos_esperados = [(2, 4), (3, 4), (4, 2), (4, 3), (5, 4), (6, 4)]
    #Postcondicion
    assert sorted(pieza.movlineal(2)) == sorted(movimientos_esperados)

#C5: I-1-2-3-4-5-6-7-8-9-10-11-12-13-14-15-16-17-18-2-23-F
def test_metapieza_movlineal5():
    #Precondicion
    tablero_fixture()
    pieza = metapieza(4, 8, 1)
    movimientos_esperados = [(3, 8), (4, 7), (5, 8)]
    #Postcondicion
    assert sorted(pieza.movlineal(1)) == sorted(movimientos_esperados)

#C6: I-1-2-3-4-5-6-7-8-9-10-11-12-13-14-15-16-18-2-23-F
def test_metapieza_movlineal6():
    #Precondicion
    tablero_fixture()
    pieza = metapieza(4, 8, 1)
    cocupadas[7][4] = 1 
    movimientos_esperados = [(3, 8), (5, 8)]
    #Postcondicion
    assert sorted(pieza.movlineal(1)) == sorted(movimientos_esperados)

#C7: I-1-2-3-4-5-6-7-8-9-10-11-12-13-14-15-18-2-23-F
def test_metapieza_movlineal7():
    #Precondicion
    tablero_fixture()
    pieza = metapieza(4, 8, 1)
    cocupadas[7][4] = 1 
    movimientos_esperados = [(2, 8), (3, 8), (5, 8), (6, 8)]
    #Postcondicion
    assert sorted(pieza.movlineal(2)) == sorted(movimientos_esperados)

#C9: I-1-2-3-4-5-6-7-8-9-10-11-12-13-18-19-20-21-2-23-F
def test_metapieza_movlineal9():
    #Precondicion
    tablero_fixture()
    pieza = metapieza(4, 1, 1)
    for x in range(9):
        cocupadas[2][x] = 1
    movimientos_esperados = [(3, 1), (5, 1)]
    #Postcondicion
    assert sorted(pieza.movlineal(1)) == sorted(movimientos_esperados)

#C10: I-1-2-3-4-5-6-7-8-9-10-11-13-14-15-18-19-20-2-23-F
def test_metapieza_movlineal10():
    #Precondicion
    tablero_fixture()
    pieza = metapieza(6, 4, 1)
    cocupadas[3][6] = 1
    cocupadas[5][6] = 1
    cocupadas[4][7] = 1
    movimientos_esperados = [(5, 4)]
    #Postcondicion
    assert sorted(pieza.movlineal(1)) == sorted(movimientos_esperados)

#C11: I-1-2-3-4-5-6-7-8-9-10-13-14-15-18-19-20-2-23-F
def test_metapieza_movlineal11():
    #Precondicion
    tablero_fixture()
    pieza = metapieza(6, 4, 1)
    cocupadas[3][6] = 1
    cocupadas[4][7] = 1
    cocupadas[5][6] = 1
    movimientos_esperados = [(4, 4), (5, 4)]
    #Postcondicion
    assert sorted(pieza.movlineal(2)) == sorted(movimientos_esperados)

#C12: I-1-2-3-4-5-6-8-9-13-18-19-20-21-2-23-F
def test_metapieza_movlineal12():
    #Precondicion
    tablero_fixture()
    pieza = metapieza(8, 1, 1)
    movimientos_esperados = [(7, 1), (8, 2)]
    #Postcondicion
    assert sorted(pieza.movlineal(1)) == sorted(movimientos_esperados)

#C14: I-1-2-3-4-5-6-8-9-10-11-12-13-14-15-16-17-18-19-20-21-22-2-23-F
def test_metapieza_movlineal14():
    #Precondicion
    tablero_fixture()
    pieza = metapieza(3, 4, 1)
    cocupadas[4][2] = 1
    movimientos_esperados = [(3, 3), (3, 5), (4, 4)]
    #Postcondicion
    assert sorted(pieza.movlineal(1)) == sorted(movimientos_esperados)

#C15: I-1-2-3-4-5-6-8-9-10-11-12-13-14-15-16-17-18-19-20-21-22-2-23-F
def test_metapieza_movlineal15():
    #Precondicion
    tablero_fixture()
    pieza = metapieza(3, 4, 1)
    cocupadas[4][2] = 1
    movimientos_esperados = [(3, 2), (3, 3), (3, 5), (3, 6), (4, 4), (5, 4)]
    #Postcondicion
    assert sorted(pieza.movlineal(2)) == sorted(movimientos_esperados)

#C16: I-1-2-3-4-8-9-10-11-12-13-14-15-16-17-18-19-20-21-22-2-23-F
def test_metapieza_movlineal16():
    #Precondicion
    tablero_fixture()
    pieza = metapieza(1, 4, 1)
    movimientos_esperados = [(1, 3), (1, 5), (2, 4)]
    #Postcondicion
    assert sorted(pieza.movlineal(1)) == sorted(movimientos_esperados)

#C18: I-1-2-23-F
def test_metapieza_movlineal18():
    #Precondicion
    tablero_fixture()
    pieza = metapieza(4, 4, 1)
    #Postcondicion
    assert pieza.movlineal(0)==[]

