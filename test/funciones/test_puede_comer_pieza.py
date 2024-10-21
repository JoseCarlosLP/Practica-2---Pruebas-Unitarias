import pytest
from unittest.mock import patch
from ajedrezoo import puede_comer_pieza, ocupadas, cocupadas

def tablero_fixture():
    for i in range(9):
        for j in range(9):
            cocupadas[i][j] = 0
    return cocupadas

@patch('ajedrezoo.comepieza')
@patch('ajedrezoo.sacapieza')
def test_puede_comer_pieza1(mock_sacapieza, mock_comepieza):
    # Precondicion
    tablero_fixture()
    ocupadas[4][4] = 1
    mock_sacapieza.return_value = 'pieza_mock'
    puede_comer_pieza(4, 4)

    mock_sacapieza.assert_called_once_with(4, 4)
    mock_comepieza.assert_called_once_with('pieza_mock')

@patch('ajedrezoo.comepieza')
@patch('ajedrezoo.sacapieza')
def test_puede_comer_pieza2(mock_sacapieza, mock_comepieza):
    # Precondiciones: la casilla (4, 4) está vacía
    tablero_fixture()
    ocupadas[4][4] = 0
    puede_comer_pieza(4, 4)

    # NO fue llamado, la condición no se cumplió
    mock_sacapieza.assert_not_called()
    mock_comepieza.assert_not_called()
