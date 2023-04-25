import mio_01_03
import pytest
import re


@pytest.mark.parametrize("cadena, resultado",
                         [("01:23 AM", "01:23"),
                          ("01:05 PM", "13:05"),
                          ("12:00 AM", "00:00"),
                          ("12:00 PM", "12:00"),
                          ("04:25 PM", "16:25"),
                          ])
def test_convertir(cadena, resultado):
    assert mio_01_03.convertir_formato(cadena) == resultado


@pytest.mark.parametrize("cadena",
                         [("01:23 6M"),
                          ("01:05 PK"),
                          ])
def test_no_AM_o_PM(cadena):
    with pytest.raises(ValueError, match="Las últimas dos letras deben ser AM o PM"):
        mio_01_03.convertir_formato(cadena)


@pytest.mark.parametrize("cadena",
                         [(" 01:23 6M"),
                          ("01:05dfa PK"),
                          ])
def test_longitud_cadena(cadena):
    with pytest.raises(ValueError, match="La cadena debe tener 8 caracteres: '<hh>:<mm> NN'"):
        mio_01_03.convertir_formato(cadena)


@pytest.mark.parametrize("cadena",
                         [("00:23 PM"),
                          ("32:05 AM"),
                          ])
def test_valor_horas_incorrectas(cadena):
    with pytest.raises(ValueError, match="Las horas deben estar entre 1 y 12"):
        mio_01_03.convertir_formato(cadena)


@pytest.mark.parametrize("cadena",
                         [("12:98 PM"),
                          ("02:65 AM"),
                          ])
def test_valor_minutos_incorrectos(cadena):
    with pytest.raises(ValueError, match="Los minutos deben estar entre 0 y 59"):
        mio_01_03.convertir_formato(cadena)


def test_horas_no_numericas(cadena="AA:02 PM"):
    with pytest.raises(ValueError, match=re.escape("invalid literal for int() with base 10: '") + cadena[:2] + "'"):
        mio_01_03.convertir_formato(cadena)

def test_minutos_no_numericos(cadena="10:KJ PM"):
    with pytest.raises(ValueError, match=re.escape("invalid literal for int() with base 10: '") + cadena[3:5] + "'"):
        mio_01_03.convertir_formato(cadena)