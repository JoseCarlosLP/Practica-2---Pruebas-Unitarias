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