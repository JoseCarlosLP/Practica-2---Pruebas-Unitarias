from unittest import mock

import pygame
import pytest

from ajedrezoo import Reinablanca, ocupadas, cocupadas


class TestReinanegra:
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

    def test_reinanegra_init_(self, setup_teardown_metapieza):
        pieza = Reinablanca()
        assert isinstance(pieza, Reinablanca)
        assert pieza.casx == 4
        assert pieza.casy == 8
        assert pieza.color == 1
        assert isinstance(pieza.foto, pygame.Surface)
        assert ocupadas[pieza.casy][pieza.casx] == pieza
        assert cocupadas[pieza.casy][pieza.casx] == 1

    @mock.patch('ajedrezoo.metapieza.movlineal', return_value=[(4, 7)])
    @mock.patch('ajedrezoo.metapieza.movdiagonal', return_value=[(3, 7)])
    def test_puedemovera(self, mock_movdiagonal, mock_movlineal, setup_teardown_metapieza):
        pieza = Reinablanca()
        # Precondicion: Que la instancia del Reinablanca sea correcta
        assert isinstance(pieza, Reinablanca)

        mov_posibles = pieza.puedemovera()

        # Postcondicion: Solo se puede mover a las casillas que los metodos movlineal y movdiagonal devuelve
        assert mov_posibles == [(4, 7), (3, 7)]
