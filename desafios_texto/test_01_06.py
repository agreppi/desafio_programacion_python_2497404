import mio_01_06
import pytest


@pytest.mark.parametrize("cadena, resultado",
                         [("()((()))", True),
                          ("((()()(()))", False),
                          ])
def test_balanceado(cadena, resultado):
    assert mio_01_06.esta_balanceado(cadena) == resultado
