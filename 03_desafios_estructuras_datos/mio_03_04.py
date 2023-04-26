def triangulo_pascal(numero):
    tp = []
    tp.append([1])
    if not isinstance(numero, int):
        raise ValueError("El número tiene que ser entero")
    elif numero == 1:
        pass
    elif numero < 1:
        raise ValueError("El número tiene que ser mayor a 0")
    else:
        for fila in range(1, numero):
            tpaux = []
            tpaux.append(1)
            for col in range(1, fila):
                tpaux.append(tp[fila - 1][col-1] + tp[fila-1][col])
            tpaux.append(1)
            tp.append(tpaux)

    return tp
