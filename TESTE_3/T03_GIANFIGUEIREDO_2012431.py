#Nome completo: GIAN LUCA DA SILVA FIGUEIREDO
#Matrícula PUC-Rio: 2012431
#Declaração de autoria: declaro que este documento foi produzido em sua totalidade por mim, sem consultas a outros alunos, professores ou qualquer outra pessoa.

# se a = 0 e b = 0 retorno falso
# se a = b retorno falso
# se a < b retorno falso
# se a = b*2 retorno verdadeiro
def verificaDobro(primeiroNumero, segundoNumero):
    if primeiroNumero == 0 and segundoNumero == 0:
        return False
    else:
        primeiroNumeroAtual = primeiroNumero%10
        segundoNumeroAtual = segundoNumero%10

        if primeiroNumeroAtual == segundoNumeroAtual:
            return False
        elif primeiroNumeroAtual < segundoNumeroAtual:
            return False
        else:
            if primeiroNumero < 10 and segundoNumero < 10:
                if (segundoNumeroAtual*2) == primeiroNumeroAtual:
                    return True
                else:
                    return False
            else:
                prefixoPrimeiroNumero = primeiroNumero//10
                prefixoSegundoNumero = segundoNumero//10
                if verificaDobro(prefixoPrimeiroNumero, prefixoSegundoNumero) == True:
                    return True
                else:
                    return False

def testaRestricao(primeiroNumero, segundoNumero):
    mensagem1 = 'Todos os algarismos do 1o. número são o dobro dos de mesma posição do 2o. número'
    mensagem2 = 'Nem todos os algarismos do 1o. número são o dobro dos de mesma posição do 2o. número'
    if primeiroNumero == 0 and segundoNumero == 0:
        return mensagem2
    else:
        if verificaDobro(primeiroNumero, segundoNumero):
            return mensagem1
        
        return mensagem2

print('TESTE 1 - valores %d e %d\n\t%s\n' %(4646, 2323, testaRestricao(4646, 2323)))
print('TESTE 2 - valores %d e %d\n\t%s\n' %(8648, 2224, testaRestricao(8648, 2224)))
print('TESTE 3 - valores %d e %d\n\t%s\n' %(682, 341, testaRestricao(682, 341)))
print('TESTE 4 - valores %d e %d\n\t%s\n' %(4361, 8431, testaRestricao(4361, 8431)))
