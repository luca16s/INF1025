def validaOrdemCrescenteAlgarismos(numero):
    if numero < 10:
        return True
    else:
        numeroAtual = numero%10
        prefixo = numero//10
        numeroPosterior = (prefixo)%10
        if numeroAtual < numeroPosterior:
            return validaOrdemCrescenteAlgarismos(prefixo)
        else:
            return False

print(validaOrdemCrescenteAlgarismos(654321))