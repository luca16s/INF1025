salario = 0
totalSalario = 0
totalPessoas = 0
quantidadeFilhos = 0
mediaSalarial = 0
maiorSalario = 0
quantidadePessoasMaiorSalario = 0
quantidadePessoasSalarioAteCem = 0

while salario >= 0:
    salario = float(input('Insira o seu salário: '))
    if salario >= 0:
        totalSalario += salario
        quantidadeFilhos += int(input('Insira a sua quantidade de filhos: '))
        if maiorSalario < salario:
            maiorSalario = salario
    
        if maiorSalario == salario:
            quantidadePessoasMaiorSalario += 1
    
        if salario <= 100.00:
            quantidadePessoasSalarioAteCem += 1
        totalPessoas+=1

if totalPessoas > 0:
    print('Média salarial da população: %.2f'%(totalSalario/totalPessoas))
    print('Média de número de filhos: %.2f'%(quantidadeFilhos/totalPessoas))
    print('Maior salário recebido: %.2f por %d pessoas'%(maiorSalario, quantidadePessoasMaiorSalario))
    print('Percentual de pessoas que recebem até $100: %d'%((quantidadePessoasSalarioAteCem/totalPessoas)*100))