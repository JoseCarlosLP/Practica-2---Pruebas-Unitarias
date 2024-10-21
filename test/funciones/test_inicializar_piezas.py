from unittest.mock import patch, MagicMock
from ajedrezoo import inicializar_piezas

def test_inicializar_piezas():
    patch_reynegro = patch('ajedrezoo.Reynegro', return_value=MagicMock(name='Reynegro'))
    patch_reyblanco = patch('ajedrezoo.Reyblanco', return_value=MagicMock(name='Reyblanco'))
    patch_reinanegra = patch('ajedrezoo.Reinanegra', return_value=MagicMock(name='Reinanegra'))
    patch_reinablanca = patch('ajedrezoo.Reinablanca', return_value=MagicMock(name='Reinablanca'))

    with patch_reynegro as mock_reynegro, patch_reyblanco as mock_reyblanco, patch_reinanegra as mock_reinanegra, patch_reinablanca as mock_reinablanca:
        
        # Precondición
        piezas = inicializar_piezas()

        # Desempaquetar
        reynegro, reyblanco, reinanegra, reinablanca, peonegro, peonblanco, caballonegro, caballoblanco, alfilnegro, alfilblanco = piezas

        # Postcondición
        assert isinstance(reynegro, MagicMock)
        assert isinstance(reyblanco, MagicMock)
        assert isinstance(reinanegra, MagicMock)
        assert isinstance(reinablanca, MagicMock)
        assert isinstance(peonegro, list) and peonegro == [0]
        assert isinstance(peonblanco, list) and peonblanco == [0]
        assert isinstance(caballonegro, list) and caballonegro == [0]
        assert isinstance(caballoblanco, list) and caballoblanco == [0]
        assert isinstance(alfilnegro, list) and alfilnegro == [0]
        assert isinstance(alfilblanco, list) and alfilblanco == [0]