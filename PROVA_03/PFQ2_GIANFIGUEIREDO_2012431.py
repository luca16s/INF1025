#Nome completo: GIAN LUCA DA SILVA FIGUEIREDO
#Matrícula PUC-Rio: 2012431
#Declaração de autoria: declaro que este documento foi produzido em sua totalidade por mim, sem consultas a outros alunos, professores ou qualquer outra pessoa.

def montaXY(x, y):
    return (x % (y + 3))

def montaNum(numero):
    numeroMultiploOnze = numero % 11 == 0
    numeroMultiploDois = numero % 2 == 0

    unidade = numero%10
    dezena = (numero//10)%10

    if numeroMultiploOnze == True and numeroMultiploDois == False:
        return numero * 100 + montaXY(dezena, unidade) - montaXY(unidade, dezena)
    else:
        return numero * 100 + montaXY(unidade, dezena) - montaXY(dezena, unidade)


print('Valor original: %d     Valor gerado: %d'%(110, montaNum(110)))
print('Valor original: %d     Valor gerado: %d'%(99, montaNum(99)))
print('Valor original: %d     Valor gerado: %d'%(33, montaNum(33)))
print('Valor original: %d     Valor gerado: %d'%(44, montaNum(44)))
print('Valor original: %d     Valor gerado: %d'%(80, montaNum(80)))
print('Valor original: %d     Valor gerado: %d'%(20, montaNum(20)))
