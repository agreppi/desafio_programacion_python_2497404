def convertir_formato(cadena):

    if len(cadena) != 8:
        raise ValueError("La cadena debe tener 8 caracteres: '<hh>:<mm> NN'")

    horas = int(cadena[:2])
    minutos = cadena[3:5]
    ampm = cadena[6:]

    if not (0 < horas < 13):
        raise ValueError("Las horas deben estar entre 1 y 12")

    if int(minutos) > 60:
        raise ValueError("Los minutos deben estar entre 0 y 59")

    if ampm == "AM":
        if horas == 12:
            horas = 0
    elif ampm == "PM":
        if horas != 12:
            horas = horas + 12
    else:
        raise ValueError("Las últimas dos letras deben ser AM o PM")

    return f'{horas:02d}:{minutos}'

