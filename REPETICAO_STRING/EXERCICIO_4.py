def validaOrdemLexicografica(palavra):
    contador = 0
    tamanhoPalavra = len(palavra)
    palavraLexicografica = False
    while contador < tamanhoPalavra:
        proximaPosicao = contador+1
        if tamanhoPalavra > proximaPosicao:
            if  palavra[contador] < palavra[proximaPosicao]:
                palavraLexicografica = True
            else:
                palavraLexicografica = False
        contador += 1
    return palavraLexicografica

print(validaOrdemLexicografica('abc'))
print(validaOrdemLexicografica('bola'))