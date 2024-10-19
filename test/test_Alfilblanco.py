from unittest import mock

import pygame

from ajedrezoo import Alfilblanco


class TestAlfilblanco:

    def test_alfilblanco_init_(self):
        pieza = Alfilblanco(3)
        assert isinstance(pieza, Alfilblanco)
        assert pieza.casx == 3
        assert pieza.casy == 8
        assert pieza.color == 1
        assert isinstance(pieza.foto, pygame.Surface)

    @mock.patch('ajedrezoo.metapieza.movdiagonal', return_value=[(2, 7), (4, 7)])
    def test_puedemovera(self, mock_movdiagonal):
        pieza = Alfilblanco(3)
        # Precondicion: Que la instancia del Alfilblanco sea correcta
        assert isinstance(pieza, Alfilblanco)

        mov_posibles = pieza.puedemovera()

        # Postcondicion: Solo se puede mover a las casillas que el metodo metapieza.movdiagonal devuelve
        assert mov_posibles == [(2, 7), (4, 7)]