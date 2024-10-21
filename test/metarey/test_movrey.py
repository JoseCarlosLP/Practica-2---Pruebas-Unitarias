from unittest import mock
import pytest
from ajedrezoo import metarey
from unittest.mock import MagicMock


class TestMovrey:

    @pytest.fixture
    def setup_teardown_rey(self):
        print("\nInicializando rey...")
        rey = metarey(5, 1, 1)
        yield rey
        print("Limpiando rey...")

    @pytest.fixture
    def setup_teardown_cocupadas(self):
        print("Inicializando cocupadas...")
        matriz_cocupadas = [[0] * 8 for _ in range(8)]
        yield matriz_cocupadas
        print("\nLimpiando cocupadas...")
        matriz_cocupadas = [[0] * 8 for _ in range(8)]
        assert all(
            all(casilla == 0 for casilla in fila) for fila in matriz_cocupadas), "Error: cocupadas no fue limpiada correctamente"

    @mock.patch('ajedrezoo.torrenegra')
    @mock.patch('ajedrezoo.torreblanca')
    @mock.patch('ajedrezoo.metapieza.movlineal', return_value=[])
    @mock.patch('ajedrezoo.metapieza.movdiagonal', return_value=[])
    def test_rey_movido_sin_enroque(self, mock_movlineal, mock_diagonal, mock_torreblanca, mock_torrenegra,
                                    setup_teardown_rey):
        rey = setup_teardown_rey
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
    def test_no_puede_enrocar_a_ningun_lado(self, mock_movlineal, mock_diagonal, mock_torreblanca, mock_torrenegra,
                                            mock_cocupadas, setup_teardown_rey, setup_teardown_cocupadas):
        rey = setup_teardown_rey
        torres_blancas = [0, MagicMock(movida=1), MagicMock(movida=0)]
        torres_negras = [0, MagicMock(movida=1), MagicMock(movida=0)]
        mock_torrenegra.__getitem__.side_effect = torres_negras.__getitem__
        mock_torreblanca.__getitem__.side_effect = torres_blancas.__getitem__

        matriz_cocupadas = setup_teardown_cocupadas
        mock_cocupadas.__getitem__.side_effect = matriz_cocupadas.__getitem__
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
    def test_todas_las_torres_movidas(self, mock_movlineal, mock_diagonal, mock_torreblanca, mock_torrenegra,
                                      setup_teardown_rey):
        rey = setup_teardown_rey
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
    def test_sin_enroque_torres_izq_movidas_casillas_dere_ocupadas(self, mock_movlineal, mock_diagonal,
                                                                   mock_torreblanca,
                                                                   mock_torrenegra, mock_cocupadas, setup_teardown_rey,
                                                                   setup_teardown_cocupadas):
        rey = setup_teardown_rey
        torres_blancas = [0, MagicMock(movida=1), MagicMock(movida=0)]
        torres_negras = [0, MagicMock(movida=1), MagicMock(movida=1)]
        mock_torrenegra.__getitem__.side_effect = torres_negras.__getitem__
        mock_torreblanca.__getitem__.side_effect = torres_blancas.__getitem__

        matriz_cocupadas = setup_teardown_cocupadas
        mock_cocupadas.__getitem__.side_effect = matriz_cocupadas.__getitem__
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

    @mock.patch('ajedrezoo.cocupadas')
    @mock.patch('ajedrezoo.torrenegra')
    @mock.patch('ajedrezoo.torreblanca')
    @mock.patch('ajedrezoo.metapieza.movlineal', return_value=[])
    @mock.patch('ajedrezoo.metapieza.movdiagonal', return_value=[])
    def test_sin_enroque_torres_izq_movidas_una_casilla_dere_ocupada(self, mock_movlineal, mock_diagonal,
                                                                     mock_torreblanca,
                                                                     mock_torrenegra, mock_cocupadas,
                                                                     setup_teardown_rey,
                                                                     setup_teardown_cocupadas):
        rey = setup_teardown_rey
        torres_blancas = [0, MagicMock(movida=1), MagicMock(movida=0)]
        torres_negras = [0, MagicMock(movida=1), MagicMock(movida=1)]
        mock_torrenegra.__getitem__.side_effect = torres_negras.__getitem__
        mock_torreblanca.__getitem__.side_effect = torres_blancas.__getitem__

        matriz_cocupadas = setup_teardown_cocupadas
        mock_cocupadas.__getitem__.side_effect = matriz_cocupadas.__getitem__
        mock_cocupadas[rey.casy][rey.casx + 1] = 1  # Marcamos como ocupada la casilla

        # Precondicion: Las torres en el lado izquierdo del tablero se movieron, las torres en el lado derecho y el
        # rey no se movieron
        assert mock_torrenegra[1].movida == 1
        assert mock_torrenegra[2].movida == 1
        assert mock_torreblanca[1].movida == 1
        assert mock_torreblanca[2].movida == 0
        assert rey.movida == 0
        # Precondicion: Una casilla a la derecha del rey esta ocupada, no permite enroque a ese lado, solo al lado izquierdo
        assert mock_cocupadas[rey.casy][rey.casx + 2] == 0
        assert mock_cocupadas[rey.casy][rey.casx + 1] == 1
        assert mock_cocupadas[rey.casy][rey.casx - 2] == 0

        mov_posibles = rey.movrey()

        # Postcondicion: El rey no puede enrocar porque las torres de la izq se movieron y las casilla [casx+1] esta ocupada
        assert rey.movida == 0
        assert mov_posibles == []
        assert rey.casposibles == []
    #
    @mock.patch('ajedrezoo.cocupadas')
    @mock.patch('ajedrezoo.torrenegra')
    @mock.patch('ajedrezoo.torreblanca')
    @mock.patch('ajedrezoo.metapieza.movlineal', return_value=[])
    @mock.patch('ajedrezoo.metapieza.movdiagonal', return_value=[])
    def test_3_casillas_izq_ocupada_y_enroque_derecha(self, mock_movlineal, mock_diagonal, mock_torreblanca,
                                                      mock_torrenegra, mock_cocupadas, setup_teardown_rey,
                                                      setup_teardown_cocupadas):
        rey = setup_teardown_rey
        torres_blancas = [0, MagicMock(movida=1), MagicMock(movida=0)]
        torres_negras = [0, MagicMock(movida=0), MagicMock(movida=1)]
        mock_torrenegra.__getitem__.side_effect = torres_negras.__getitem__
        mock_torreblanca.__getitem__.side_effect = torres_blancas.__getitem__

        matriz_cocupadas = setup_teardown_cocupadas
        mock_cocupadas.__getitem__.side_effect = matriz_cocupadas.__getitem__
        mock_cocupadas[rey.casy][rey.casx - 3] = 1  # Marcamos como ocupada la casilla

        # Precondicion: Las torres en el lado izquierdo del tablero se movieron, las torres en el lado derecho y el
        # rey no se movieron
        assert mock_torrenegra[1].movida == 0
        assert mock_torrenegra[2].movida == 1
        assert mock_torreblanca[1].movida == 1
        assert mock_torreblanca[2].movida == 0
        assert rey.movida == 0
        # Precondicion: Una casilla a la izquierda del rey esta ocupada, no permite enroque a ese lado, solo al lado derecho
        assert mock_cocupadas[rey.casy][rey.casx + 2] == 0
        assert mock_cocupadas[rey.casy][rey.casx + 1] == 0
        assert mock_cocupadas[rey.casy][rey.casx - 3] == 1

        mov_posibles = rey.movrey()

        # Postcondicion: Si se puede hacer enroque al lado derecho porque la torre no se movio y las casillas no estan ocupadas
        assert rey.movida == 0
        assert mov_posibles == [(7, 1)]
        assert rey.casposibles == [(7, 1)]

    @mock.patch('ajedrezoo.cocupadas')
    @mock.patch('ajedrezoo.torrenegra')
    @mock.patch('ajedrezoo.torreblanca')
    @mock.patch('ajedrezoo.metapieza.movlineal', return_value=[])
    @mock.patch('ajedrezoo.metapieza.movdiagonal', return_value=[])
    def test_torres_izq_movidas(self, mock_movlineal, mock_diagonal, mock_torreblanca,
                                mock_torrenegra, mock_cocupadas, setup_teardown_rey, setup_teardown_cocupadas):
        rey = setup_teardown_rey
        torres_blancas = [0, MagicMock(movida=1), MagicMock(movida=0)]
        torres_negras = [0, MagicMock(movida=1), MagicMock(movida=1)]
        mock_torrenegra.__getitem__.side_effect = torres_negras.__getitem__
        mock_torreblanca.__getitem__.side_effect = torres_blancas.__getitem__

        # Precondicion: Todas las casillas entre las torres y el rey estan libres
        matriz_cocupadas = setup_teardown_cocupadas
        mock_cocupadas.__getitem__.side_effect = matriz_cocupadas.__getitem__

        # Precondicion: Las torres en el lado izquierdo del tablero se movieron, las torres en el lado derecho y el
        # rey no se movieron
        assert mock_torrenegra[1].movida == 1
        assert mock_torrenegra[2].movida == 1
        assert mock_torreblanca[1].movida == 1
        assert mock_torreblanca[2].movida == 0
        assert rey.movida == 0

        mov_posibles = rey.movrey()

        # Postcondicion: Si se puede hacer enroque al lado derecho porque la torre no se movio y las casillas no estan ocupadas
        assert rey.movida == 0
        assert mov_posibles == [(7, 1)]
        assert rey.casposibles == [(7, 1)]

    @mock.patch('ajedrezoo.cocupadas')
    @mock.patch('ajedrezoo.torrenegra')
    @mock.patch('ajedrezoo.torreblanca')
    @mock.patch('ajedrezoo.metapieza.movlineal', return_value=[])
    @mock.patch('ajedrezoo.metapieza.movdiagonal', return_value=[])
    def test_ninguna_torre_movida_casilla_izq_ocupada(self, mock_movlineal, mock_diagonal, mock_torreblanca,
                                                      mock_torrenegra, mock_cocupadas, setup_teardown_rey,
                                                      setup_teardown_cocupadas):
        rey = setup_teardown_rey
        torres_blancas = [0, MagicMock(movida=0), MagicMock(movida=0)]
        torres_negras = [0, MagicMock(movida=1), MagicMock(movida=1)]
        mock_torrenegra.__getitem__.side_effect = torres_negras.__getitem__
        mock_torreblanca.__getitem__.side_effect = torres_blancas.__getitem__

        # Precondicion: La casilla en la posicion [casx-3] esta ocupada
        matriz_cocupadas = setup_teardown_cocupadas
        mock_cocupadas.__getitem__.side_effect = matriz_cocupadas.__getitem__
        mock_cocupadas[rey.casy][rey.casx - 3] = 1  # Marcamos como ocupada la casilla
        assert mock_cocupadas[rey.casy][rey.casx - 3] == 1

        # Precondicion: Ninguna de las torres blancas han sido movidas
        assert mock_torrenegra[1].movida == 1
        assert mock_torrenegra[2].movida == 1
        assert mock_torreblanca[1].movida == 0
        assert mock_torreblanca[2].movida == 0
        assert rey.movida == 0

        mov_posibles = rey.movrey()

        # Postcondicion: Solo se puede enrocar al lado derecho porque la casilla [casx-3] esta ocupada al lado izq
        assert rey.movida == 0
        assert mov_posibles == [(7, 1)]
        assert rey.casposibles == [(7, 1)]

    @mock.patch('ajedrezoo.cocupadas')
    @mock.patch('ajedrezoo.torrenegra')
    @mock.patch('ajedrezoo.torreblanca')
    @mock.patch('ajedrezoo.metapieza.movlineal', return_value=[])
    @mock.patch('ajedrezoo.metapieza.movdiagonal', return_value=[])
    def test_ninguna_torre_movida_casilla_2_izq_ocupada(self, mock_movlineal, mock_diagonal, mock_torreblanca,
                                                        mock_torrenegra, mock_cocupadas, setup_teardown_rey,
                                                        setup_teardown_cocupadas):
        rey = setup_teardown_rey
        torres_blancas = [0, MagicMock(movida=0), MagicMock(movida=0)]
        torres_negras = [0, MagicMock(movida=1), MagicMock(movida=1)]
        mock_torrenegra.__getitem__.side_effect = torres_negras.__getitem__
        mock_torreblanca.__getitem__.side_effect = torres_blancas.__getitem__

        # Precondicion: La casilla en la posicion [casx-2] esta ocupada
        matriz_cocupadas = setup_teardown_cocupadas
        mock_cocupadas.__getitem__.side_effect = matriz_cocupadas.__getitem__
        mock_cocupadas[rey.casy][rey.casx - 2] = 1  # Marcamos como ocupada la casilla
        assert mock_cocupadas[rey.casy][rey.casx - 2] == 1

        # Precondicion: Ninguna de las torres blancas han sido movidas
        assert mock_torrenegra[1].movida == 1
        assert mock_torrenegra[2].movida == 1
        assert mock_torreblanca[1].movida == 0
        assert mock_torreblanca[2].movida == 0
        assert rey.movida == 0

        mov_posibles = rey.movrey()

        # Postcondicion: Solo se puede enrocar al lado derecho porque la casilla [casx-2] esta ocupada al lado izq
        assert rey.movida == 0
        assert mov_posibles == [(7, 1)]
        assert rey.casposibles == [(7, 1)]

    @mock.patch('ajedrezoo.cocupadas')
    @mock.patch('ajedrezoo.torrenegra')
    @mock.patch('ajedrezoo.torreblanca')
    @mock.patch('ajedrezoo.metapieza.movlineal', return_value=[])
    @mock.patch('ajedrezoo.metapieza.movdiagonal', return_value=[])
    def test_ninguna_torre_movida_casilla_1_izq_ocupada(self, mock_movlineal, mock_diagonal, mock_torreblanca,
                                                        mock_torrenegra, mock_cocupadas, setup_teardown_rey,
                                                        setup_teardown_cocupadas):
        rey = setup_teardown_rey
        torres_blancas = [0, MagicMock(movida=0), MagicMock(movida=0)]
        torres_negras = [0, MagicMock(movida=1), MagicMock(movida=1)]
        mock_torrenegra.__getitem__.side_effect = torres_negras.__getitem__
        mock_torreblanca.__getitem__.side_effect = torres_blancas.__getitem__

        # Precondicion: La casilla en la posicion [casx-1] esta ocupada
        matriz_cocupadas = setup_teardown_cocupadas
        mock_cocupadas.__getitem__.side_effect = matriz_cocupadas.__getitem__
        mock_cocupadas[rey.casy][rey.casx - 1] = 1  # Marcamos como ocupada la casilla
        assert mock_cocupadas[rey.casy][rey.casx - 1] == 1

        # Precondicion: Ninguna de las torres blancas han sido movidas
        assert mock_torrenegra[1].movida == 1
        assert mock_torrenegra[2].movida == 1
        assert mock_torreblanca[1].movida == 0
        assert mock_torreblanca[2].movida == 0
        assert rey.movida == 0

        mov_posibles = rey.movrey()

        # Postcondicion: Solo se puede enrocar al lado derecho porque la casilla [casx-1] esta ocupada al lado izq
        assert rey.movida == 0
        assert mov_posibles == [(7, 1)]
        assert rey.casposibles == [(7, 1)]

    @mock.patch('ajedrezoo.cocupadas')
    @mock.patch('ajedrezoo.torrenegra')
    @mock.patch('ajedrezoo.torreblanca')
    @mock.patch('ajedrezoo.metapieza.movlineal', return_value=[])
    @mock.patch('ajedrezoo.metapieza.movdiagonal', return_value=[])
    def test_ninguna_torre_movida_ninguna_casilla_ocupada(self, mock_movlineal, mock_diagonal, mock_torreblanca,
                                                          mock_torrenegra, mock_cocupadas, setup_teardown_rey,
                                                          setup_teardown_cocupadas):
        rey = setup_teardown_rey
        torres_blancas = [0, MagicMock(movida=0), MagicMock(movida=0)]
        torres_negras = [0, MagicMock(movida=1), MagicMock(movida=1)]
        mock_torrenegra.__getitem__.side_effect = torres_negras.__getitem__
        mock_torreblanca.__getitem__.side_effect = torres_blancas.__getitem__

        # Precondicion: Ninguna casilla esta ocupada
        matriz_cocupadas = setup_teardown_cocupadas
        mock_cocupadas.__getitem__.side_effect = matriz_cocupadas.__getitem__

        # Precondicion: Ninguna de las torres blancas han sido movidas
        assert mock_torrenegra[1].movida == 1
        assert mock_torrenegra[2].movida == 1
        assert mock_torreblanca[1].movida == 0
        assert mock_torreblanca[2].movida == 0
        assert rey.movida == 0

        mov_posibles = rey.movrey()

        # Postcondicion: Es posible enrocar a ambos lados
        assert rey.movida == 0
        assert mov_posibles == [(7, 1), (3, 1)]
        assert rey.casposibles == [(7, 1), (3, 1)]
