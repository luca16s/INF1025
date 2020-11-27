#Nome completo: GIAN LUCA DA SILVA FIGUEIREDO
#Matrícula PUC-Rio: 2012431
#Declaração de autoria: declaro que este documento foi produzido em sua totalidade por mim, sem consultas a outros alunos, professores ou qualquer outra pessoa.

def defineAdjacenteMaiorDiferencaAbsoluta():
    return


quantidadeConjuntos = 3
conjunto = 0
valorAnterior = 0
maiorDiferenca = 0
resposta = ''

while conjunto<quantidadeConjuntos:
    conjunto += 1
    print('Conjunto %d'%conjunto)
    for contador in range(0, 4):
        valorAtual = int(input('Digite um valor inteiro: '))
        diferencaAtual = valorAtual - valorAnterior
        if maiorDiferenca < diferencaAtual:
            maiorDiferenca < diferencaAtual
            resposta = '%d %d'%(valorAnterior, valorAtual)
        valorAnterior = valorAtual
    print('Valores adjacentes com maior diferença absoluta: %s'%resposta)