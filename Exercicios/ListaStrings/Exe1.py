'''1. Crie as funções abaixo e teste-as no interpretador. Lembre-se que uma função pode chamar
outra função.
a. Construa a função calcDigVerificador que recebe um número e retorna o dígito
verificador deste número, calculado do seguinte modo:
(dezena-unidade)%9
b. Faça a função incDigVerificador que recebe um número e retorna uma string com os
algarismos do número, seguidos de ‘-‘ e do dígito verificador. Utilize a função
calcDigVerificador.
Exemplo: 12385  '12385-3'
Exemplo: 12345 '12345-8'
c. Faça uma função que receba o número da agência e o número da conta bancária de
uma pessoa, inclua o dígito verificador na agência e na conta e os exiba. Esta função
não possui valor de retorno.'''
#---------------------------------------------------------------------------------
def CalcDigVerificador(numeroInserido):
    dezena = numeroInserido//10
    unidade = numeroInserido%10
    return (dezena-unidade)%9
#---------------------------------------------------------------------------------
def IncDigVerificador(numeroInserido):
    digitoVerificador = CalcDigVerificador(numeroInserido)
    return str(numeroInserido) + '-' + str(digitoVerificador)
#---------------------------------------------------------------------------------
def IncluirDigitoVerificador(numeroAgencia, numeroContaBancaria):
    numeroAgencia = IncDigVerificador(numeroAgencia)
    numeroContaBancaria = IncDigVerificador(numeroContaBancaria)
    print(numeroAgencia)
    print(numeroContaBancaria)
    return
#---------------------------------------------------------------------------------
numeroEscolhido = 12385
print(CalcDigVerificador(numeroEscolhido))
print(IncDigVerificador(numeroEscolhido))
IncluirDigitoVerificador(123456, 12348)