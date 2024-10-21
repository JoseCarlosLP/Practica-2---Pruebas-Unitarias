import pytest
from ajedrezoo import metaballo,ocupadas, cocupadas

@pytest.fixture(scope="function")
def tablero_fixture():
    for i in range(9):
        for j in range(9):
            cocupadas[i][j] = 0
    return cocupadas

#C1: I-1-2-3-4-5-6-7-8-3-2-9-F
def test_movcaballo1(tablero_fixture):
    pieza = metaballo(4, 4, 1)
    movimientos_esperados = [(2, 3), (6, 3), (3, 2), (5, 2), (2, 5), (6, 5), (3, 6), (5, 6)]
    assert sorted(pieza.movcaballo()) == sorted(movimientos_esperados)

#C2: I-1-2-3-4-5-6-7-3-2-9-F
def test_movcaballo2(tablero_fixture):
    pieza = metaballo(4, 4, 1)
    cocupadas[3][2] = 1
    cocupadas[3][6] = 1
    cocupadas[2][3] = 1
    cocupadas[2][5] = 1
    cocupadas[5][2] = 1
    cocupadas[5][6] = 1
    cocupadas[6][3] = 1
    cocupadas[6][5] = 1
    assert pieza.movcaballo() == []

#C3: I-1-2-3-4-5-6-8-3-2-9-F
def test_movcaballo3(tablero_fixture):
    pieza = metaballo(4, 4, 1)
    cocupadas[3][2] = 1
    cocupadas[2][3] = 1
    cocupadas[5][2] = 1
    cocupadas[6][3] = 1
    cocupadas[2][5] = 1
    cocupadas[3][6] = 1
    movimientos = pieza.movcaballo()
    assert (6, 5) in movimientos
    assert (5, 6) in movimientos
    assert len(movimientos) == 2

#C4: I-1-2-3-4-5-3-2-9-F
def test_movcaballo4(tablero_fixture):
    pieza = metaballo(8, 4, 1)

    movimientos = pieza.movcaballo()
    movimientos_esperados = [(7, 2), (6, 3), (6, 5), (7, 6)]

    for movimiento in movimientos_esperados:
        assert movimiento in movimientos

    movimientos_no_validos = [(9, 2), (10, 3),(10, 5),(9, 6)]
    for movimiento in movimientos_no_validos:
        assert movimiento not in movimientos

    assert len(movimientos) == len(movimientos_esperados)

#C5: I-1-2-3-4-3-2-9-F
def test_movcaballo5(tablero_fixture):
    pieza = metaballo(7, 8, 1)

    movimientos = pieza.movcaballo()
    movimientos_esperados = [(6, 6), (8, 6), (5, 7)]

    for movimiento in movimientos_esperados:
        assert movimiento in movimientos

    movimientos_no_validos = [(9, 7), (5, 9)]
    for movimiento in movimientos_no_validos:
        assert movimiento not in movimientos

    assert len(movimientos) == len(movimientos_esperados)