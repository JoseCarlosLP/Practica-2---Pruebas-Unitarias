from unittest import mock

import pygame

from ajedrezoo import Reyblanco


class TestReyblanco:
    def test_reyblanco_init_(self):
        pieza = Reyblanco()
        assert isinstance(pieza, Reyblanco)
        assert pieza.casx == 5
        assert pieza.casy == 8
        assert pieza.color == 1
        assert isinstance(pieza.foto, pygame.Surface)

    @mock.patch('ajedrezoo.metarey.movrey', return_value=[(4, 8), (6, 8), (5, 7), (4, 7), (6, 7)])
    def test_puedemovera(self, mock_movdiagonal):
        pieza = Reyblanco()
        # Precondicion: Que la instancia del Reyblanco sea correcta
        assert isinstance(pieza, Reyblanco)

        mov_posibles = pieza.puedemovera()

        # Postcondicion: Solo se puede mover a las casillas que el metodo metarey.movrey devuelve
        assert mov_posibles == [(4, 8), (6, 8), (5, 7), (4, 7), (6, 7)]
