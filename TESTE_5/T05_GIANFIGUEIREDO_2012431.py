#Nome completo: GIAN LUCA DA SILVA FIGUEIREDO
#Matrícula PUC-Rio: 2012431
#Declaração de autoria: declaro que este documento foi produzido em sua totalidade por mim, sem consultas a outros alunos, professores ou qualquer outra pessoa.

def contaQuantidadeStringsLista(item):
    qtdString = 0
    if type(item) == str:
        qtdString += 1
    return qtdString

def contaQuantidadeNumericosLista(item):
    qtdNumericos = 0
    if type(item) == int or type(item) == float:
        qtdNumericos += 1
    return qtdNumericos

def validaSeQuantidadeNumericosMenorStrings(lista):
    menosNumericosStrings = False
    qtdNumericos = 0
    qtdStrings = 0

    for item in lista:
        if type(item) != list:
            qtdNumericos += contaQuantidadeNumericosLista(item)
            qtdStrings += contaQuantidadeStringsLista(item)

            if qtdNumericos == 0 and qtdStrings > 0:
                menosNumericosStrings = False
            elif qtdStrings == 0 and qtdNumericos > 0:
                menosNumericosStrings = True
            else:
                menosNumericosStrings = qtdNumericos < qtdStrings

    return menosNumericosStrings

listaExemplo1 = [2, 5, ['paz', 7.8, [['maré', 3.0, 'alegria'], 'ação', 0], 'amigos'], [1, 2, 3], 'professor']
listaExemplo2 = [2, 5, ['paz', 7.8, [['maré', 3.0, 'alegria'], 'ação', 0, 'informática', 'Python'], 'amigos'], ['ser', 1, 'programação'], 'professor', 'meninas', 'meninos']
listaExemplo3 = [1, 2, [3, 4, 5]]
listaExemplo4 = ['1', '2', '3']
listaExemplo5 = ['1', 2, ['3', 4]]

listaGeral = [ listaExemplo1, listaExemplo2, listaExemplo3, listaExemplo4,  listaExemplo5]

for listaExemplo in listaGeral:
    valido = validaSeQuantidadeNumericosMenorStrings(listaExemplo)
    if valido == True:
        print('Há menos valores numéricos que strings em cada uma das listas.')
        print()
    elif valido == False:
        print('Não há menos valores numéricos que strings em cada uma das listas.')
        print()
    else:
        print('Há valores iguais em cada uma das listas.')
        print()