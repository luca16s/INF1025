def validarCompatibilidadeSigno(quantidadeLetrasSignoA, quantidadeLetrasSignoB):
    return quantidadeLetrasSignoA == quantidadeLetrasSignoB

def contaLetra(signo):
    contador = 0
    posicao = 0
    quantidadeLetras = len(signo)
    while posicao < quantidadeLetras:
        if signo[posicao].lower() in 'abcdefghijklmnopqrstuvwxyz':
            contador +=1
        posicao += 1
    return contador

signoA = ''
signoB = ''

compativeis = 0
incompativeis = 0
menorPalavra = ''

while signoA != 'FIM':
    signoA = input('Insira o signo da primeira Pessoa: ')

    if signoA != 'FIM':
        signoB = input('Insira o signo da segunda Pessoa: ')
        tamanhoSignoA = contaLetra(signoA)
        tamanhoSignoB = contaLetra(signoB)

        if (tamanhoSignoA < tamanhoSignoB and tamanhoSignoA < contaLetra(menorPalavra)) or menorPalavra == '':
            menorPalavra = signoA
        elif tamanhoSignoB < contaLetra(menorPalavra) or menorPalavra == '':
            menorPalavra = signoB

        if validarCompatibilidadeSigno(tamanhoSignoA, tamanhoSignoB):
            compativeis += 1
            print('Compatíveis')
        else:
            incompativeis += 1
            print('Não compatíveis')

if incompativeis == 0 and compativeis == 0:
    porcentagemCompativeis = ((compativeis/(compativeis+incompativeis))*100)
    print("Percentual de pares compatíveis: %.2f"%porcentagemCompativeis)
    print("Menor palavra: %s"%menorPalavra)