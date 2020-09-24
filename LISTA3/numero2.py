# Uma escola deseja monitorar quanto tempo seus alunos ficam na escola. Faça um programa que leia o horário
# de entrada (uma string hh:mm) e o horário de saída (uma string hh:mm) de um aluno exibindo o tempo (em
# horas:minutos) que o aluno ficou na escola.
# a) Faça uma função que receba um horário(string hh:mm) e retorne-o convertido em minutos
# (converteHorario)
# b) Faça uma função que receba uma quantidade de minutos e exiba-a no formato nnh:nnm (horario)

def ConverteHorario(horarioEntrada, horarioSaida):
    hora =  int(horarioSaida[0:2]) - int(horarioEntrada[0:2])
    minutos = int(horarioSaida[:2:-1]) - int(horarioEntrada[:2:-1])
    return (hora * 60 + minutos)

def FormatarMinutos(minutos):
    return '$i:%i'%(minutos//60, minutos%60)

entradaAluno = input('Insira o horário de entrada do aluno: ')
saidaAluno = input('Insira a saída do aluno: ')

tempoTotal = ConverteHorario(entradaAluno, saidaAluno)

print(FormatarMinutos(tempoTotal))