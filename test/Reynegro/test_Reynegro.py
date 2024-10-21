from unittest import mock

import pygame
import pytest

from ajedrezoo import Reynegro, ocupadas, cocupadas


class TestReynegro:
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

    def test_reynegro_init_(self, setup_teardown_metapieza):
        pieza = Reynegro()
        assert isinstance(pieza, Reynegro)
        assert pieza.casx == 5
        assert pieza.casy == 1
        assert pieza.color == 2
        assert isinstance(pieza.foto, pygame.Surface)
        assert ocupadas[pieza.casy][pieza.casx] == pieza
        assert cocupadas[pieza.casy][pieza.casx] == 2

    @mock.patch('ajedrezoo.metarey.movrey', return_value=[(4, 1), (6, 1), (5, 2), (4, 2), (6, 2)])
    def test_puedemovera(self, mock_movdiagonal, setup_teardown_metapieza):
        pieza = Reynegro()
        # Precondicion: Que la instancia del Reynegro sea correcta
        assert isinstance(pieza, Reynegro)

        mov_posibles = pieza.puedemovera()

        # Postcondicion: Solo se puede mover a las casillas que el metodo metarey.movrey devuelve
        assert mov_posibles == [(4, 1), (6, 1), (5, 2), (4, 2), (6, 2)]
