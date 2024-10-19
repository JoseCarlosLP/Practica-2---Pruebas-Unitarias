from unittest import mock

import pygame

from ajedrezoo import Reinablanca


class TestReinanegra:
    def test_reinanegra_init_(self):
        pieza = Reinablanca()
        assert isinstance(pieza, Reinablanca)
        assert pieza.casx == 4
        assert pieza.casy == 8
        assert pieza.color == 1
        assert isinstance(pieza.foto, pygame.Surface)

    @mock.patch('ajedrezoo.metapieza.movlineal', return_value=[(4, 7)])
    @mock.patch('ajedrezoo.metapieza.movdiagonal', return_value=[(3, 7)])
    def test_puedemovera(self, mock_movdiagonal, mock_movlineal):
        pieza = Reinablanca()
        # Precondicion: Que la instancia del Reinablanca sea correcta
        assert isinstance(pieza, Reinablanca)

        mov_posibles = pieza.puedemovera()

        # Postcondicion: Solo se puede mover a las casillas que los metodos movlineal y movdiagonal devuelve
        assert mov_posibles == [(4, 7), (3, 7)]
