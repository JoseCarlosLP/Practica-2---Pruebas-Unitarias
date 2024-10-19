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
