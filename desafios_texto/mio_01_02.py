def primera_letra_repetida(texto):

    texto_sin_espacios = texto.replace(" ", "")

    for i in range(len(texto_sin_espacios)-1):
        for j in range(i+1, len(texto_sin_espacios)):
            if texto_sin_espacios[i] in texto_sin_espacios[j:]:
                return texto_sin_espacios[i]

    return None


print(primera_letra_repetida("saltar"))
print(primera_letra_repetida("me gusta"))
