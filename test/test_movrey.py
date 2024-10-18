from unittest import mock
import pytest
from ajedrezoo import metarey
from unittest.mock import MagicMock


class TestMovrey:

    @pytest.fixture
    def setup_rey(self):
        # Inicializamos el rey en su posicion inical
        return metarey(5, 1, 1)

    @mock.patch('ajedrezoo.torrenegra')
    @mock.patch('ajedrezoo.torreblanca')
    @mock.patch('ajedrezoo.metapieza.movlineal', return_value=[])
    @mock.patch('ajedrezoo.metapieza.movdiagonal', return_value=[])
    def test_rey_movido_sin_enroque(self, mock_movlineal, mock_diagonal, mock_torreblanca, mock_torrenegra, setup_rey):
        rey = setup_rey
        torres_blancas = [0, MagicMock(movida=0), MagicMock(movida=0)]
        torres_negras = [0, MagicMock(movida=0), MagicMock(movida=0)]

        mock_torrenegra.__getitem__.side_effect = torres_negras.__getitem__
        mock_torreblanca.__getitem__.side_effect = torres_blancas.__getitem__
        # Precondicion: Las torres y el rey no se movieron
        assert mock_torrenegra[1].movida == 0
        assert mock_torrenegra[2].movida == 0
        assert mock_torreblanca[1].movida == 0
        assert mock_torreblanca[2].movida == 0
        assert rey.movida == 0
        # Precondicion: El rey no puede moverse a ninguna casilla
        assert rey.movdiagonal() == []
        assert rey.movlineal() == []

        rey.movida = 1  # Avisamos que el rey se movió
        mov_posibles = rey.movrey()

        #Postcondicion: El rey no puede enrocar porque se movió
        assert rey.movida == 1
        assert mov_posibles == []
        assert rey.casposibles == []


