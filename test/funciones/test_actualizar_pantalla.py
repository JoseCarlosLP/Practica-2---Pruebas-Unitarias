import pytest
from unittest import mock
from ajedrezoo import *
@pytest.fixture
def setup_teardown():
    print("\nSetup: Inicializando juego")
    inicializar_juego()
    yield  # Permitir que el test se ejecute

    print("\nTeardown: Reestableciendo juego")
    inicializar_juego()
    

class TestActualizarPantalla:
    @mock.patch('pygame.display.update')
    def test_actualizar_pantalla_rey_blanco_fuera_de_rango(self, mock_update,setup_teardown):
        # Precondiciones:
        
        reynegro = mock.Mock()
        reynegro.casx = 5  

        reyblanco = mock.Mock()
        reyblanco.casx = 9 
        assert reyblanco.casx>=9

        visor = mock.Mock()
        gblancas = mock.Mock()
        gnegras = mock.Mock()

        actualizar_pantalla(visor, None, gblancas, gnegras, reynegro, reyblanco)

        visor.blit.assert_called_once_with(gnegras, (0, 0))
        mock_update.assert_called_once()

    @mock.patch('pygame.display.update')
    def test_actualizar_pantalla_reyes_dentro_de_rango(self, mock_update,setup_teardown):
        reynegro = mock.Mock()
        reynegro.casx = 5 
        assert reynegro.casx<9
        reyblanco = mock.Mock()
        reyblanco.casx = 5
        assert reyblanco.casx<9
        visor = mock.Mock()
        gblancas = mock.Mock()
        gnegras = mock.Mock()

        # Llamar a la función
        actualizar_pantalla(visor, None, gblancas, gnegras, reynegro, reyblanco)

        visor.blit.assert_not_called()
        mock_update.assert_called_once() 
    @mock.patch('pygame.display.update')
    def test_actualizar_pantalla_rey_negro_fuera_de_rango(self, mock_update,setup_teardown):
        # Precondiciones:
        # Mockear las instancias de los reyes
        reynegro = mock.Mock()
        reynegro.casx = 9  
        assert reynegro.casx>=9
        reyblanco = mock.Mock()
        reyblanco.casx = 5 
        # Mockear el visor y las imágenes
        visor = mock.Mock()
        gblancas = mock.Mock()
        gnegras = mock.Mock()

        actualizar_pantalla(visor, None, gblancas, gnegras, reynegro, reyblanco)

        visor.blit.assert_called_once_with(gblancas, (0, 0))
        mock_update.assert_called_once()
