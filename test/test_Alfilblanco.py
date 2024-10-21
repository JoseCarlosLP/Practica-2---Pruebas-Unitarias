from unittest import mock

import pygame
import pytest

from ajedrezoo import Alfilblanco, ocupadas, cocupadas


class TestAlfilblanco:
    @pytest.fixture
    def setup_teardown_metapieza(self):
        global ocupadas, cocupadas

        print("\nSetup: Inicializando tablero")
        assert all(len(fila) == 9 for fila in ocupadas), "Error: ocupadas debe tener 9 columnas"
        assert all(len(fila) == 9 for fila in cocupadas), "Error: cocupadas debe tener 9 columnas"

        yield

        print("\nTeardown: Limpiando ocupadas y cocupadas")
        ocupadas = [[0] * 9 for _ in range(9)]
        cocupadas = [[0] * 9 for _ in range(9)]

        assert all(
            all(casilla == 0 for casilla in fila) for fila in ocupadas), "Error: ocupadas no fue limpiada correctamente"
        assert all(
            all(casilla == 0 for casilla in fila) for fila in
            cocupadas), "Error: cocupadas no fue limpiada correctamente"

    def test_alfilblanco_init_(self, setup_teardown_metapieza):
        pieza = Alfilblanco(3)
        assert isinstance(pieza, Alfilblanco)
        assert pieza.casx == 3
        assert pieza.casy == 8
        assert pieza.color == 1
        assert isinstance(pieza.foto, pygame.Surface)
        assert ocupadas[pieza.casy][pieza.casx] == pieza
        assert cocupadas[pieza.casy][pieza.casx] == 1

    @mock.patch('ajedrezoo.metapieza.movdiagonal', return_value=[(2, 7), (4, 7)])
    def test_puedemovera(self, mock_movdiagonal, setup_teardown_metapieza):
        pieza = Alfilblanco(3)
        # Precondicion: Que la instancia del Alfilblanco sea correcta
        assert isinstance(pieza, Alfilblanco)

        mov_posibles = pieza.puedemovera()

        # Postcondicion: Solo se puede mover a las casillas que el metodo metapieza.movdiagonal devuelve
        assert mov_posibles == [(2, 7), (4, 7)]
