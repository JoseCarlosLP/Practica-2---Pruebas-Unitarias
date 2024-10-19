from unittest import mock

import pygame

from ajedrezoo import Reynegro


class TestReynegro:
    def test_reynegro_init_(self):
        pieza = Reynegro()
        assert isinstance(pieza, Reynegro)
        assert pieza.casx == 5
        assert pieza.casy == 1
        assert pieza.color == 2
        assert isinstance(pieza.foto, pygame.Surface)

    @mock.patch('ajedrezoo.metarey.movrey', return_value=[(4, 1), (6, 1), (5, 2), (4, 2), (6, 2)])
    def test_puedemovera(self, mock_movdiagonal):
        pieza = Reynegro()
        # Precondicion: Que la instancia del Reynegro sea correcta
        assert isinstance(pieza, Reynegro)

        mov_posibles = pieza.puedemovera()

        # Postcondicion: Solo se puede mover a las casillas que el metodo metarey.movrey devuelve
        assert mov_posibles == [(4, 1), (6, 1), (5, 2), (4, 2), (6, 2)]
