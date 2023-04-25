import mio_02_03
import pytest


@pytest.mark.parametrize("numero, resultado",
                         [(1, 1),
                          (2, 3),
                          (3, 6),
                          (4, 10),
                          (5, 15),
                          ])
def test_positivo(numero, resultado):
    assert mio_02_03.nro_triangular_recursivo(numero) == resultado


@pytest.mark.parametrize("numero",
                         [(3.4),
                          (-558.36),
                          ])
def test_nro_no_entero(numero):
    with pytest.raises(ValueError, match="El número tiene que ser entero"):
        mio_02_03.nro_triangular_recursivo(numero)

@pytest.mark.parametrize("numero",
                         [(-3),
                          (0),
                          ])
def test_nro_negativo(numero):
    with pytest.raises(ValueError, match="El número tiene que ser mayor a 0"):
        mio_02_03.nro_triangular_recursivo(numero)
