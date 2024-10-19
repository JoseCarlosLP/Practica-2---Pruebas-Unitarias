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
