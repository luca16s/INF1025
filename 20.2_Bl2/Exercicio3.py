def calculaNumeroAcertos(gabarito, respostas):
    quantidadeAcertos = 0
    for (indice, valor) in enumerate(gabarito):
        if type(valor) != list:
            if valor == respostas[indice]:
                quantidadeAcertos +=1
        else:
            quantidadeAcertos += calculaNumeroAcertos(valor, respostas[indice])

    return quantidadeAcertos

gabarito = [[1, 2, 3], [[4, [5, 6], 7]], 8, 9, 10]
resposta = [[1, 5, 3], [[4, [5, 2], 7]], 8, 9, 1]

print(calculaNumeroAcertos(gabarito, resposta))