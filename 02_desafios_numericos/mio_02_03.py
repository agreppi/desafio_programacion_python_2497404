def nro_triangular_recursivo(numero):
    if not isinstance(numero,int):
        raise ValueError("El número tiene que ser entero")
    elif numero == 1:
        return 1
    elif numero < 1:
        raise ValueError("El número tiene que ser mayor a 0")
    else:
        return numero+nro_triangular_recursivo(numero-1)