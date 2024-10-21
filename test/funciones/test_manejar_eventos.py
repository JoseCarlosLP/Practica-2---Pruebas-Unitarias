import pytest
from unittest import mock
import pygame
import sys
from ajedrezoo import *
@pytest.fixture
def setup_teardown():
    print("\nSetup: Inicializando juego")
    inicializar_juego()
    yield  # Permitir que el test se ejecute

    print("\nTeardown: Reestableciendo juego")
    inicializar_juego()
    
class TestManejarEventos:
    
    @mock.patch('pygame.event.get')
    @mock.patch('pygame.mouse.get_pos', return_value=(100, 200))
    def test_evento_mousebuttondown(self, mock_get_pos, mock_event_get,setup_teardown):
        # Simular que se recibe un evento MOUSEBUTTONDOWN
        mock_event = mock.Mock(type=pygame.MOUSEBUTTONDOWN)
        mock_event_get.return_value = [mock_event]

        click = []
        result = manejar_eventos(click)

        # Verificar que la posición del mouse se añade a la lista click
        assert result == [(100, 200)]

    @mock.patch('pygame.event.get')
    def test_evento_desconocido(self, mock_event_get,setup_teardown):
        # Simular un evento que no es QUIT ni MOUSEBUTTONDOWN
        mock_event = mock.Mock(type=pygame.USEREVENT)  # Un evento no manejado
        mock_event_get.return_value = [mock_event]

        click = []
        result = manejar_eventos(click)
        assert result == click  
    @mock.patch('pygame.event.get')
    @mock.patch('pygame.quit')
    @mock.patch('sys.exit')
    @mock.patch('pygame.mouse.get_pos', return_value=(100, 200))
    def test_evento_quit(self, mock_get_pos, mock_exit, mock_quit, mock_event_get,setup_teardown):
        # Simular que se recibe un evento QUIT
        mock_event_get.return_value = [mock.Mock(type=pygame.QUIT)]

        click = []
        result = manejar_eventos(click)

        # Verificar que pygame.quit() y sys.exit() fueron llamados
        mock_quit.assert_called_once()
        mock_exit.assert_called_once()
        assert result == click
