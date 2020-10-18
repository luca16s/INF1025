#Nome completo: GIAN LUCA DA SILVA FIGUEIREDO
#Matrícula PUC-Rio: 2012431
#Declaração de autoria: declaro que este documento foi produzido em sua totalidade por mim, sem consultas a outros alunos, professores ou qualquer outra pessoa.

def juntaDigitos(x, y):
    return x % (y + 1)

def montaNovoNum(numero):
    numeroPar = numero%2
    unidade= numero%10
    dezena= (numero//10)%10
    numeroMultiploNove = (unidade + dezena) % 9 == 0

    if numeroMultiploNove and numeroPar == 0:
        return numero * 100 + juntaDigitos(unidade, dezena) - juntaDigitos(dezena, unidade)
    else:
        return numero * 100 - juntaDigitos(unidade, dezena) - juntaDigitos(dezena, unidade)

numero1 = int(input("Insira um número: "))
numero2 = int(input("Insira um número: "))

print('Valor original: %d     Valor gerado: %d'%(numero1, montaNovoNum(numero1)))
print('Valor original: %d     Valor gerado: %d'%(numero2, montaNovoNum(numero2)))