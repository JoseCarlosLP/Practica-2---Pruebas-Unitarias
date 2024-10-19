from unittest import mock

import pygame

from ajedrezoo import Reinanegra


class TestReinanegra:
    def test_reinanegra_init_(self):
        pieza = Reinanegra()
        assert isinstance(pieza, Reinanegra)
        assert pieza.casx == 4
        assert pieza.casy == 1
        assert pieza.color == 2
        assert isinstance(pieza.foto, pygame.Surface)

    @mock.patch('ajedrezoo.metapieza.movlineal', return_value=[(4, 2)])
    @mock.patch('ajedrezoo.metapieza.movdiagonal', return_value=[(3, 2)])
    def test_puedemovera(self, mock_movdiagonal, mock_movlineal):
        pieza = Reinanegra()
        # Precondicion: Que la instancia del Reinanegra sea correcta
        assert isinstance(pieza, Reinanegra)

        mov_posibles = pieza.puedemovera()

        # Postcondicion: Solo se puede mover a las casillas que los metodos movlineal y movdiagonal devuelve
        assert mov_posibles == [(4, 2), (3, 2)]
