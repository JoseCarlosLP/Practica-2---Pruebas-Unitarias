from unittest import mock
from unittest.mock import MagicMock

import pygame
import pytest
from ajedrezoo import Alfilnegro, metapieza


class TestAlfilnegro__init__:
    def test_alfilnegro_init_(self):
        pieza = Alfilnegro(3)
        assert isinstance(pieza, Alfilnegro)
        assert pieza.casx == 3
        assert pieza.casy == 1
        assert isinstance(pieza.foto, pygame.Surface)
