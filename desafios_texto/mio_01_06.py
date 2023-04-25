def esta_balanceado(cadena):
    if cadena[0] == ')' or len(cadena) % 2 == 1:
        return False
    else:
        while len(cadena) > 1:
            cadena = cadena.replace("()","")
    
    if len(cadena) > 1:
        return False
    else:
        return True
                

