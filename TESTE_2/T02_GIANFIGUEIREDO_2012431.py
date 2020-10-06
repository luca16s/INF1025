#Nome completo: GIAN LUCA DA SILVA FIGUEIREDO
#Matrícula PUC-Rio: 2012431
#Declaração de autoria: declaro que este documento foi produzido em sua totalidade por mim, sem consultas a outros alunos, professores ou qualquer outra pessoa.

def detFatorDesconto(s, valorTotalVenda):
    if s[1] == s[len(s)//2] or s[1] == s[-1]:
        return 0.27
    elif s[0:4] == s[4::1]:
        return 0.17
    elif valorTotalVenda > 900:
        return 0.1
    else:
        return 0.06

def CalculaDesconto(texto, horarioVenda, valorTotalVenda):
    UmTercoVenda = valorTotalVenda * (1/3)
    descontoAplicado = (detFatorDesconto(texto, valorTotalVenda) * valorTotalVenda) + (int(horarioVenda[:2:1])%15)
    if descontoAplicado < 0:
        return 0
    elif descontoAplicado > UmTercoVenda:
        return UmTercoVenda
    else:
        return descontoAplicado

nomeCliente = input('Insira o nome do Cliente: ')
horarioVenda = input('Insira o horário de venda: ')
valorTotalVenda = float(input('Insira o valor total venda: '))

descontoAplicado = CalculaDesconto(nomeCliente, horarioVenda, valorTotalVenda)
valorFinalVenda = valorTotalVenda-descontoAplicado

print('Nome: %s'%nomeCliente)
print('Valor do desconto: %.2f'%descontoAplicado)
print('Valor final da venda: %.2f'%valorFinalVenda)