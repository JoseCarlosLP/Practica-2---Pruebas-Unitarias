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
