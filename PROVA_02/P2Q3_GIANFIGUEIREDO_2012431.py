#Nome completo: GIAN LUCA DA SILVA FIGUEIREDO
#Matrícula PUC-Rio: 2012431
#Declaração de autoria: declaro que este documento foi produzido em sua totalidade por mim, sem consultas a outros alunos, professores ou qualquer outra pessoa.

def lerDados(arquivo):
    listaDadosCaixa = []
    arquivo = open(arquivo, "r")
    for linha in arquivo:
        linha = linha.strip()
        informacoesCaixa = linha.split(';')
        informacoes = [ informacoesCaixa[0], int(informacoesCaixa[1]), int(informacoesCaixa[2]), int(informacoesCaixa[3]) ]
        listaDadosCaixa.append(informacoes)    
    arquivo.close()
    return listaDadosCaixa

def retornaCaixaCompativel(listaCaixas, largura, altura, profundidade):
    caixaCompativel = ''
    for caixa in listaCaixas:
        if type(caixa) != list:
            if altura <= listaCaixas[1] and largura <= listaCaixas[2] and profundidade <= listaCaixas[3]:
                return caixa
            else:
                break
        else:
            if caixaCompativel == '':
                caixaCompativel = retornaCaixaCompativel(caixa, largura, altura, profundidade)
            else:
                return caixaCompativel
    return caixaCompativel

altura = int(input('Digite a altura do objeto: '))
largura = int(input('Digite a largura: '))
profundididade = int(input('Digite a profundidade: '))

listaInformacoesCaixa = lerDados('PROVA_02\\dados.txt')
retorno = retornaCaixaCompativel(listaInformacoesCaixa, largura, altura, profundididade)
if retorno == '':
    print('Modelo da caixa:  FORA DOS PADRÕES')
else:
    print('Modelo da caixa: %s'%retorno)