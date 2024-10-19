from unittest import mock
from unittest.mock import MagicMock

import pygame
import pytest
from ajedrezoo import Alfilnegro, metapieza


class TestAlfilnegro:
    def test_alfilnegro_init_(self):
        pieza = Alfilnegro(3)
        assert isinstance(pieza, Alfilnegro)
        assert pieza.casx == 3
        assert pieza.casy == 1
        assert isinstance(pieza.foto, pygame.Surface)

    @mock.patch('ajedrezoo.metapieza.movdiagonal', return_value=[(2, 2), (4, 2)])
    def test_puedemovera(self, mock_movdiagonal):
        pieza = Alfilnegro(3)
        # Precondicion: Que la instancia del Alfilnegro sea correcta
        assert isinstance(pieza, Alfilnegro)

        mov_posibles = pieza.puedemovera()

        #Postcondicion: Solo se puede mover a las casillas que el metodo metapieza.movdiagonal devuelve
        assert mov_posibles == [(2, 2), (4, 2)]
