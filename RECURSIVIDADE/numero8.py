def Funcao(numero):
    if numero == 1:
        return 1
    return Funcao(numero - 1) + numero


print(str(Funcao(4)))
