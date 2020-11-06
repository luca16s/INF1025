def concatenaLista(lista):
    listaConcatenada = ''

    for item in lista:
        if type(item) != list:
            listaConcatenada += item
        else:
            listaConcatenada += concatenaLista(item)

    return listaConcatenada

def descobrePalavraMaiorCaracter(lista):
    tamanhoMaiorPalavra = ''
    for item in lista:
        if type(item) != list:
            if item.count(' ') > 0:
                listaString = item.split(' ')
                item = descobrePalavraMaiorCaracter(listaString)
        else:
            if len(item) > len(tamanhoMaiorPalavra):
                item = descobrePalavraMaiorCaracter(item)
        
        if len(item) > len(tamanhoMaiorPalavra):
                tamanhoMaiorPalavra = item
    return tamanhoMaiorPalavra

def contaQuantidadePalavras(lista):
    quantidadePalavras = 0
    for item in lista:
        if type(item) != list:
            quantidadePalavras += 1
        else:
            quantidadePalavras += contaQuantidadePalavras(item)
    return quantidadePalavras

def transformaMaiusculo(lista):
    for (indice, elemento) in enumerate(lista):
        if type(elemento) != list:
            lista[indice] = elemento.upper()
            print(lista[indice])
        else:
            lista[indice] = transformaMaiusculo(elemento)

Lstrings=['Oi',['estamos','aprendendo',' a trabalhar'], 'com', 'listas', ['de',' strings']]

print(concatenaLista(Lstrings))
print(descobrePalavraMaiorCaracter(Lstrings))
print(contaQuantidadePalavras(Lstrings))
transformaMaiusculo(Lstrings)