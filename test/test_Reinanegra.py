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