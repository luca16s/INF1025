#5) Associe a variáveis, seu primeiro nome, a sua data de nascimento, a data de nascimento de sua mãe e a
#data de nascimento de seu pai, como strings no formato ‘dd/mm/aaaa’.
#a) Crie uma senha composta por: 2 letras sorteadas randomicamente de seu nome, seguidas da
#soma dos dias das datas de nascimento, seguidas do primeiro dígito do mês de nascimento de
#seu pai, seguido do segundo dígito do mês de nascimento de sua mãe e do ano de seu nascimento
#invertido.
#b) Calcule a soma dos anos de nascimentos invertidos
#c) Construa uma string no formato s1$s2@s3 onde s1 é uma string com o dia do seu nascimento
#replicado 3 vezes, s2 é o mês de nascimento de sua mãe invertido replicado 2 vezes e s3 é a
#unidade do dia de nascimento de seu pai seguido da dezena e milhar do ano de nascimento do
#seu pai
import random

primeiroNome = 'Gian Luca'
dataNascimento = '16/04/1995'
NascimentoMae = '20/06/1975'
NascimentoPai = '02/11/1970'

senha = random.choice(primeiroNome) + random.choice(primeiroNome) + str(int(dataNascimento[0:2]) + int(NascimentoMae[0:2]) + int(NascimentoPai[0:2])) + NascimentoPai[3:5] + NascimentoMae[4:5] + dataNascimento[:-5:-1]
print(senha)

print(str(int(dataNascimento[:-5:-1]) + int(NascimentoMae[:-5:-1]) + int(NascimentoPai[:-5:-1])))

print((dataNascimento[-4:]*3) + '$' + (NascimentoMae[4:2:-1]*2) + '@' + (NascimentoPai[0:1] + NascimentoPai[6:7] + NascimentoPai[8:9]))