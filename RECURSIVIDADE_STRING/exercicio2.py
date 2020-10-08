def pesquisaCaracterString(texto, caracter):
    if len(texto) == 0:
        return False

    if texto[0] == caracter:
        return True
        
    return pesquisaCaracterString(texto[1:], caracter)

print(pesquisaCaracterString('prasgahfsgbnsx', 'b'))