import mio_01_04
import pytest


@pytest.mark.parametrize("texto1, texto2, resultado",
                         [("coral", "calor", True ),
                          ("amore", "amor", False),
                          ])
def test_anagrama(texto1, texto2, resultado):
    assert mio_01_04.es_anagrama(texto1, texto2) == resultado