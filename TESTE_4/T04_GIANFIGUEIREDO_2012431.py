#Nome completo: GIAN LUCA DA SILVA FIGUEIREDO
#Matrícula PUC-Rio: 2012431
#Declaração de autoria: declaro que este documento foi produzido em sua totalidade por mim, sem consultas a outros alunos, professores ou qualquer outra pessoa.

totalAlunos = 257
contadorAlunos = 0
idadeAlunoMaisVelho = 0
quantidadeAlunosIntervaloZeroDezessete = 0
quantidadeAlunosIntervaloDezoitoVinteNove = 0
quantidadeAlunosAcimaVinteNove = 0

while contadorAlunos < totalAlunos:
    contadorAlunos +=1
    idadeAluno = int(input('Qual a idade do %io. aluno?'%contadorAlunos))

    if idadeAlunoMaisVelho < idadeAluno:
        idadeAlunoMaisVelho = idadeAluno
    
    if idadeAluno <= 17:
        quantidadeAlunosIntervaloZeroDezessete += 1
    elif idadeAluno >= 18 and idadeAluno <= 29:
        quantidadeAlunosIntervaloDezoitoVinteNove += 1
    else:
        quantidadeAlunosAcimaVinteNove += 1

print('')
print('Idade do aluno mais velho: %i'%idadeAlunoMaisVelho)
print('Qtd. de alunos no intervalo [0, 17]: %i'%quantidadeAlunosIntervaloZeroDezessete)
print('Qtd. de alunos no intervalo [18, 29]: %i'%quantidadeAlunosIntervaloDezoitoVinteNove)
print('Qtd. de alunos com mais de 29 anos: %i'%quantidadeAlunosAcimaVinteNove)