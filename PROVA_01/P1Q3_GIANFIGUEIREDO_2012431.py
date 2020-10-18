#Nome completo: GIAN LUCA DA SILVA FIGUEIREDO
#Matrícula PUC-Rio: 2012431
#Declaração de autoria: declaro que este documento foi produzido em sua totalidade por mim, sem consultas a outros alunos, professores ou qualquer outra pessoa.

def decifraPalavraOriginal(consoantes, vogais):
    if len(consoantes) == 0 or len(vogais) == 0:
        return consoantes + vogais

    consoanteAtual = consoantes[0]
    if consoanteAtual == '*':
        primeiraSequencia = vogais[-1]
        return primeiraSequencia + decifraPalavraOriginal(consoantes[1:], vogais[:-1])
    else:
        primeiraSequencia = consoanteAtual
    
    resto = decifraPalavraOriginal(consoantes[1:], vogais)

    return primeiraSequencia + resto

print(decifraPalavraOriginal ('CL*R*B','AIOAA'))
print(decifraPalavraOriginal ('TR**N','OIE'))
print(decifraPalavraOriginal ('TR*T*R','OA'))
print(decifraPalavraOriginal ('','AIA'))
print(decifraPalavraOriginal ('*T','UEA'))