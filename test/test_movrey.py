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

        # Postcondicion: El rey no puede enrocar porque se movió
        assert rey.movida == 1
        assert mov_posibles == []
        assert rey.casposibles == []

    @mock.patch('ajedrezoo.cocupadas')
    @mock.patch('ajedrezoo.torrenegra')
    @mock.patch('ajedrezoo.torreblanca')
    @mock.patch('ajedrezoo.metapieza.movlineal', return_value=[])
    @mock.patch('ajedrezoo.metapieza.movdiagonal', return_value=[])
    def test_no_puede_enrocar_a_ningun_lado(self, mock_movlineal, mock_diagonal, mock_torreblanca, mock_torrenegra, mock_cocupadas, setup_rey):
        rey = setup_rey
        torres_blancas = [0, MagicMock(movida=1), MagicMock(movida=0)]
        torres_negras = [0, MagicMock(movida=1), MagicMock(movida=0)]
        mock_torrenegra.__getitem__.side_effect = torres_negras.__getitem__
        mock_torreblanca.__getitem__.side_effect = torres_blancas.__getitem__

        mock_cocupadas = [[0] * 8 for _ in range(8)]
        mock_cocupadas[rey.casy][rey.casx + 2] = 1

        # Precondicion: Las torres en el lado izquierdo del tablero se movieron, las torres en el lado derecho y el
        # rey no se movieron
        assert mock_torrenegra[1].movida == 1
        assert mock_torrenegra[2].movida == 0
        assert mock_torreblanca[1].movida == 1
        assert mock_torreblanca[2].movida == 0
        assert rey.movida == 0
        # Precondicion: Dos casillas a la derecha del rey esta ocupada, no permite enroque a ese lado, solo al lado izquierdo
        assert mock_cocupadas[rey.casy][rey.casx + 2] == 1
        assert mock_cocupadas[rey.casy][rey.casx - 2] == 0

        mov_posibles = rey.movrey()

        # Postcondicion: El rey no puede enrocar porque las torres de la izq se movieron y las casilla [casx+2] esta ocupada
        assert rey.movida == 0
        assert mov_posibles == []
        assert rey.casposibles == []

    @mock.patch('ajedrezoo.torrenegra')
    @mock.patch('ajedrezoo.torreblanca')
    @mock.patch('ajedrezoo.metapieza.movlineal', return_value=[])
    @mock.patch('ajedrezoo.metapieza.movdiagonal', return_value=[])
    def test_todas_las_torres_movidas(self, mock_movlineal, mock_diagonal, mock_torreblanca, mock_torrenegra, setup_rey):
        rey = setup_rey
        torres_blancas = [0, MagicMock(movida=1), MagicMock(movida=1)]
        torres_negras = [0, MagicMock(movida=1), MagicMock(movida=1)]
        mock_torrenegra.__getitem__.side_effect = torres_negras.__getitem__
        mock_torreblanca.__getitem__.side_effect = torres_blancas.__getitem__

        # Precondicion: Todas las torres se movieron menos el rey
        assert mock_torrenegra[1].movida == 1
        assert mock_torrenegra[2].movida == 1
        assert mock_torreblanca[1].movida == 1
        assert mock_torreblanca[2].movida == 1
        assert rey.movida == 0

        mov_posibles = rey.movrey()

        # Postcondicion: El rey no puede enrocar porque las torres fueron movidas
        assert rey.movida == 0
        assert mov_posibles == []
        assert rey.casposibles == []

    @mock.patch('ajedrezoo.cocupadas')
    @mock.patch('ajedrezoo.torrenegra')
    @mock.patch('ajedrezoo.torreblanca')
    @mock.patch('ajedrezoo.metapieza.movlineal', return_value=[])
    @mock.patch('ajedrezoo.metapieza.movdiagonal', return_value=[])
    def test_sin_enroque_torres_izq_movidas_casillas_dere_ocupadas(self, mock_movlineal, mock_diagonal, mock_torreblanca,
                                                                  mock_torrenegra, mock_cocupadas, setup_rey):
        rey = setup_rey
        torres_blancas = [0, MagicMock(movida=1), MagicMock(movida=0)]
        torres_negras = [0, MagicMock(movida=1), MagicMock(movida=1)]
        mock_torrenegra.__getitem__.side_effect = torres_negras.__getitem__
        mock_torreblanca.__getitem__.side_effect = torres_blancas.__getitem__

        mock_cocupadas = [[0] * 8 for _ in range(8)]
        mock_cocupadas[rey.casy][rey.casx + 2] = 1

        # Precondicion: Las torres en el lado izquierdo del tablero se movieron, las torres en el lado derecho y el
        # rey no se movieron
        assert mock_torrenegra[1].movida == 1
        assert mock_torrenegra[2].movida == 1
        assert mock_torreblanca[1].movida == 1
        assert mock_torreblanca[2].movida == 0
        assert rey.movida == 0
        # Precondicion: Dos casillas a la derecha del rey esta ocupada, no permite enroque a ese lado, solo al lado izquierdo
        assert mock_cocupadas[rey.casy][rey.casx + 2] == 1
        assert mock_cocupadas[rey.casy][rey.casx - 2] == 0

        mov_posibles = rey.movrey()

        # Postcondicion: El rey no puede enrocar porque las torres de la izq se movieron y las casilla [casx+2] esta ocupada
        assert rey.movida == 0
        assert mov_posibles == []
        assert rey.casposibles == []
