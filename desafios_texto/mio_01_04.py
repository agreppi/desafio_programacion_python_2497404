def es_anagrama(texto1, texto2):

    texto1_minuscula = sorted(texto1.lower())
    texto2_minuscula = sorted(texto2.lower())



    return texto1_minuscula == texto2_minuscula