import mio_03_04
import pytest


@pytest.mark.parametrize("numero, lista",
                         [(12, [1, 11, 55, 165, 330, 462, 462, 330, 165, 55, 11, 1]),
                          (1, [1]),
                          (2, [1, 1]),
                          (4, [1, 3, 3, 1]),
                          ])
def test_positivo(numero, lista):
    assert mio_03_04.triangulo_pascal(numero)[numero-1] == lista


@pytest.mark.parametrize("numero",
                         [(3.4),
                          (-558.36),
                          ])
def test_nro_no_entero(numero):
    with pytest.raises(ValueError, match="El número tiene que ser entero"):
        mio_03_04.triangulo_pascal(numero)


@pytest.mark.parametrize("numero",
                         [(-3),
                          (0),
                          ])
def test_nro_negativo(numero):
    with pytest.raises(ValueError, match="El número tiene que ser mayor a 0"):
        mio_03_04.triangulo_pascal(numero)
