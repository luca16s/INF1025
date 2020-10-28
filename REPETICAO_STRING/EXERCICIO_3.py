idade = 0
motivoEscolha = 0
escolhaAptidao = 0
totalAlunos = int(input('Total de Alunos: '))
contador = 0

while contador < totalAlunos:
    idade += int(input('Insira a idade: '))
    if int(input('Motivo da escolha: (1) Remuneração (2) Aptidão (3) Não sei (4) outros ')) == 2:
        escolhaAptidao += 1
    contador +=1

print('%.0f escolheram o curso por aptidão'%((escolhaAptidao/totalAlunos)*100))
print('A média de idade dos alunos é de: %.0f'%(idade/totalAlunos))