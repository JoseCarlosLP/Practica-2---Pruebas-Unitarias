from unittest import mock

import pytest

from ajedrezoo import mover_torres_enroque, Torrenegra, Torreblanca, Reyblanco, Reynegro


@pytest.fixture
def setup_teardown_torres_negras():
    print("\nSetup: Inicializando torres negras")
    torresnegras = [0, Torrenegra(1), Torrenegra(8)]
    yield torresnegras
    print("\nTeardown: Limpiando torres negras")


@pytest.fixture
def setup_teardown_torres_blancas():
    print("\nSetup: Inicializando torres blancas")
    torresblancas = [0, Torreblanca(1), Torreblanca(8)]
    yield torresblancas
    print("\nTeardown: Limpiando torres blancas")


@pytest.fixture
def setup_teardown_reyblanco():
    print("\nInicializando rey blanco...")
    reyblanco = Reyblanco()
    yield reyblanco
    print("\nLimpiando rey blanco...")


@pytest.fixture
def setup_teardown_reynegro():
    print("\nInicializando rey negro...")
    reynegro = Reynegro()
    yield reynegro
    print("\nLimpiando rey blanco negro...")


@mock.patch('ajedrezoo.torrenegra')
def test_torre_negra_derecha_enroque(mock_torrenegra, setup_teardown_torres_negras, setup_teardown_reynegro):
    torres_negras = setup_teardown_torres_negras
    mock_torrenegra.__getitem__.side_effect = torres_negras.__getitem__
    # Precondicion: Que las torres negras esten en su posicion inicial
    assert torres_negras[2].casx == 8
    assert torres_negras[2].casy == 1
    assert torres_negras[1].casx == 1
    assert torres_negras[1].casy == 1

    reynegro = setup_teardown_reynegro
    enroke = 1
    (nuevacasillax, nuevacasillay) = (7, 1)
    mover_torres_enroque(reynegro, enroke, nuevacasillax, nuevacasillay, reynegro)
    # Postcondicion: Que solo la torre negra de la derecha se haya movido
    assert torres_negras[2].casx == 6
    assert torres_negras[2].casy == 1
    assert torres_negras[1].casx == 1
    assert torres_negras[1].casy == 1


@mock.patch('ajedrezoo.torrenegra')
def test_torre_negra_derecha_sin_enroque(mock_torrenegra, setup_teardown_torres_negras, setup_teardown_reynegro):
    torres_negras = setup_teardown_torres_negras
    mock_torrenegra.__getitem__.side_effect = torres_negras.__getitem__
    # Precondicion: Que las torres negras esten en su posicion inicial
    assert torres_negras[2].casx == 8
    assert torres_negras[2].casy == 1
    assert torres_negras[1].casx == 1
    assert torres_negras[1].casy == 1

    reynegro = setup_teardown_reynegro
    enroke = 1
    (nuevacasillax, nuevacasillay) = (7, 2)
    mover_torres_enroque(reynegro, enroke, nuevacasillax, nuevacasillay, reynegro)
    # Postcondicion: Que ninguna torre se haya movido
    assert torres_negras[2].casx == 8
    assert torres_negras[2].casy == 1
    assert torres_negras[1].casx == 1
    assert torres_negras[1].casy == 1


@mock.patch('ajedrezoo.torrenegra')
def test_torre_negra_izquierda_enroque(mock_torrenegra, setup_teardown_torres_negras, setup_teardown_reynegro):
    torres_negras = setup_teardown_torres_negras
    mock_torrenegra.__getitem__.side_effect = torres_negras.__getitem__
    # Precondicion: Que las torres negras esten en su posicion inicial
    assert torres_negras[2].casx == 8
    assert torres_negras[2].casy == 1
    assert torres_negras[1].casx == 1
    assert torres_negras[1].casy == 1

    reynegro = setup_teardown_reynegro
    enroke = 2
    (nuevacasillax, nuevacasillay) = (3, 1)
    mover_torres_enroque(reynegro, enroke, nuevacasillax, nuevacasillay, reynegro)
    # Postcondicion: Que solo la torre negra de la izquierda se haya movido
    assert torres_negras[2].casx == 8
    assert torres_negras[2].casy == 1
    assert torres_negras[1].casx == 4
    assert torres_negras[1].casy == 1


@mock.patch('ajedrezoo.torrenegra')
def test_torre_negra_izquierda_sin_enroque(mock_torrenegra, setup_teardown_torres_negras, setup_teardown_reynegro):
    torres_negras = setup_teardown_torres_negras
    mock_torrenegra.__getitem__.side_effect = torres_negras.__getitem__
    # Precondicion: Que las torres negras esten en su posicion inicial
    assert torres_negras[2].casx == 8
    assert torres_negras[2].casy == 1
    assert torres_negras[1].casx == 1
    assert torres_negras[1].casy == 1

    reynegro = setup_teardown_reynegro
    enroke = 2
    (nuevacasillax, nuevacasillay) = (3, 2)
    mover_torres_enroque(reynegro, enroke, nuevacasillax, nuevacasillay, reynegro)
    # Postcondicion: Que ninguna torre se haya movido
    assert torres_negras[2].casx == 8
    assert torres_negras[2].casy == 1
    assert torres_negras[1].casx == 1
    assert torres_negras[1].casy == 1


@mock.patch('ajedrezoo.torrenegra')
def test_torres_negras_sin_enroque(mock_torrenegra, setup_teardown_torres_negras, setup_teardown_reynegro):
    torres_negras = setup_teardown_torres_negras
    mock_torrenegra.__getitem__.side_effect = torres_negras.__getitem__
    # Precondicion: Que las torres negras esten en su posicion inicial
    assert torres_negras[2].casx == 8
    assert torres_negras[2].casy == 1
    assert torres_negras[1].casx == 1
    assert torres_negras[1].casy == 1

    reynegro = setup_teardown_reynegro
    enroke = 0
    (nuevacasillax, nuevacasillay) = (7, 1)
    mover_torres_enroque(reynegro, enroke, nuevacasillax, nuevacasillay, reynegro)
    # Postcondicion: Que ninguna torre se haya movido
    assert torres_negras[2].casx == 8
    assert torres_negras[2].casy == 1
    assert torres_negras[1].casx == 1
    assert torres_negras[1].casy == 1


@mock.patch('ajedrezoo.torreblanca')
def test_torre_blanca_derecha_enroque(mock_torreblanca, setup_teardown_torres_blancas, setup_teardown_reynegro, setup_teardown_reyblanco):
    torres_blancas = setup_teardown_torres_blancas
    mock_torreblanca.__getitem__.side_effect = torres_blancas.__getitem__
    # Precondicion: Que las torres blancas esten en su posicion inicial
    assert torres_blancas[2].casx == 8
    assert torres_blancas[2].casy == 8
    assert torres_blancas[1].casx == 1
    assert torres_blancas[1].casy == 8

    reyblanco = setup_teardown_reyblanco
    enroke = 1
    (nuevacasillax, nuevacasillay) = (7, 8)
    mover_torres_enroque(reyblanco, enroke, nuevacasillax, nuevacasillay, setup_teardown_reynegro)
    # Postcondicion: Que solo la torre blanca de la derecha se haya movido
    assert torres_blancas[2].casx == 6
    assert torres_blancas[2].casy == 8
    assert torres_blancas[1].casx == 1
    assert torres_blancas[1].casy == 8


@mock.patch('ajedrezoo.torreblanca')
def test_torre_blanca_derecha_sin_enroque(mock_torreblanca, setup_teardown_torres_blancas, setup_teardown_reynegro, setup_teardown_reyblanco):
    torres_blancas = setup_teardown_torres_blancas
    mock_torreblanca.__getitem__.side_effect = torres_blancas.__getitem__
    # Precondicion: Que las torres blancas esten en su posicion inicial
    assert torres_blancas[2].casx == 8
    assert torres_blancas[2].casy == 8
    assert torres_blancas[1].casx == 1
    assert torres_blancas[1].casy == 8

    reyblanco = setup_teardown_reyblanco
    enroke = 1
    (nuevacasillax, nuevacasillay) = (7, 7)
    mover_torres_enroque(reyblanco, enroke, nuevacasillax, nuevacasillay, setup_teardown_reynegro)
    # Postcondicion: Que ninguna torre blanca se haya movido
    assert torres_blancas[2].casx == 8
    assert torres_blancas[2].casy == 8
    assert torres_blancas[1].casx == 1
    assert torres_blancas[1].casy == 8


@mock.patch('ajedrezoo.torreblanca')
def test_torre_blanca_izquierda_enroque(mock_torreblanca, setup_teardown_torres_blancas, setup_teardown_reynegro, setup_teardown_reyblanco):
    torres_blancas = setup_teardown_torres_blancas
    mock_torreblanca.__getitem__.side_effect = torres_blancas.__getitem__
    # Precondicion: Que las torres blancas esten en su posicion inicial
    assert torres_blancas[2].casx == 8
    assert torres_blancas[2].casy == 8
    assert torres_blancas[1].casx == 1
    assert torres_blancas[1].casy == 8

    reyblanco = setup_teardown_reyblanco
    enroke = 2
    (nuevacasillax, nuevacasillay) = (3, 8)
    mover_torres_enroque(reyblanco, enroke, nuevacasillax, nuevacasillay, setup_teardown_reynegro)
    # Postcondicion: Que solo la torre blanca de la izquierda se haya movido
    assert torres_blancas[2].casx == 8
    assert torres_blancas[2].casy == 8
    assert torres_blancas[1].casx == 4
    assert torres_blancas[1].casy == 8


@mock.patch('ajedrezoo.torreblanca')
def test_torre_blanca_izquierda_sin_enroque(mock_torreblanca, setup_teardown_torres_blancas, setup_teardown_reynegro, setup_teardown_reyblanco):
    torres_blancas = setup_teardown_torres_blancas
    mock_torreblanca.__getitem__.side_effect = torres_blancas.__getitem__
    # Precondicion: Que las torres blancas esten en su posicion inicial
    assert torres_blancas[2].casx == 8
    assert torres_blancas[2].casy == 8
    assert torres_blancas[1].casx == 1
    assert torres_blancas[1].casy == 8

    reyblanco = setup_teardown_reyblanco
    enroke = 2
    (nuevacasillax, nuevacasillay) = (3, 7)
    mover_torres_enroque(reyblanco, enroke, nuevacasillax, nuevacasillay, setup_teardown_reynegro)
    # Postcondicion: Que ninguna torre se haya movido
    assert torres_blancas[2].casx == 8
    assert torres_blancas[2].casy == 8
    assert torres_blancas[1].casx == 1
    assert torres_blancas[1].casy == 8


@mock.patch('ajedrezoo.torreblanca')
def test_torres_blancas_sin_enroque(mock_torreblanca, setup_teardown_torres_blancas, setup_teardown_reynegro, setup_teardown_reyblanco):
    torres_blancas = setup_teardown_torres_blancas
    mock_torreblanca.__getitem__.side_effect = torres_blancas.__getitem__
    # Precondicion: Que las torres blancas esten en su posicion inicial
    assert torres_blancas[2].casx == 8
    assert torres_blancas[2].casy == 8
    assert torres_blancas[1].casx == 1
    assert torres_blancas[1].casy == 8

    reyblanco = setup_teardown_reyblanco
    enroke = 0
    (nuevacasillax, nuevacasillay) = (7, 8)
    mover_torres_enroque(reyblanco, enroke, nuevacasillax, nuevacasillay, setup_teardown_reynegro)
    # Postcondicion: Que ninguna torre se haya movido
    assert torres_blancas[2].casx == 8
    assert torres_blancas[2].casy == 8
    assert torres_blancas[1].casx == 1
    assert torres_blancas[1].casy == 8
