import mio_01_02
import pytest


@pytest.mark.parametrize("texto, resultado",
                         [("hola mundo", "o"),
                          ("hola", None),
                             ("6*9", None),
                             ("khadskfh", "k"),
                          ])
def test_repetida(texto, resultado):
    assert mio_01_02.primera_letra_repetida(texto) == resultado
