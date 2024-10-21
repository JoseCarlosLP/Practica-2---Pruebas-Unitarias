import pytest
import pygame
from ajedrezoo import inicializar_juego


def test_inicializar_juego():

    visor, tablero, puntoazul, gblancas, gnegras = inicializar_juego()

    # Postcondicion: Verificar que los datos devueltos son del tipo correcto
    assert isinstance(visor, pygame.Surface)
    assert isinstance(tablero, pygame.Surface)
    assert isinstance(puntoazul, pygame.Surface)
    assert isinstance(gblancas, pygame.Surface)
    assert isinstance(gnegras, pygame.Surface)
