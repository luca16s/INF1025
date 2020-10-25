# -*- coding: utf-8 -*-
'''
Um professor,  sabendo que a dose diária de água é individual,
resolveu calcular a quantidade mínima de litros de água que deve ser ingerida
por cada um dos seus n (lido) alunos de uma turma.
Esta medida é calculada por:
 	litros de água/dia  =  35ml de água  * peso corporal/1000
Faça um programa que inicialmente  obtenha a quantidade  de alunos da turma (n).
A seguir, para cada um dos alunos, obtenha o  peso  e
mostre a quantidade mínima de litros que o aluno deve consumir.
Seu programa deve responder:
    V1- Quantos alunos desta turma ingerem menos
    de 2 L de água?
         contagem dos que ingerem menos de 2 L de água
    v2 - Qual o percentual de alunos desta 
    turma que ingerem menos de 2L?
         conta2L*100/número de alunos (n)
    V3  Qual o total de litros de água 
    consumidos pela turma?
         soma dos litros de cada aluno (lAgua)
    V4 - Qual a quantidade média de litros de 
    água por aluno nesta turma?
         soma dos litros de cada aluno (totLitros)/n
    v5 - Qual o peso médio dos alunos  peso2+peso3+peso4/3  somatório/qtdade
    turma que consomem mais que 3l? 
         soma dos pesos que consomem mais que 3l/qt de alunos que consomem mais que 3l
    V6 - Considere 3 turmas de alunos deste professor
         repetir 3 x o processamento de uma turma
    V7 - Qual o total de litros ingeridos pelas turmas deste professor? 
         --> totLitros da Turma 1 + totLitros da Turma 2 + totLitros da Turma 3
         Qual o número deste aluno?
        
    V8 - DESAFIO: Qual a maior quantidade individual ingerida?
'''
def AguaIndiv(peso):
    return peso*35/1000

def processaUmaTurma(n):
    jaFiz=0  # CONTAGEM DE EXEXC guardar a quantidade de vezes que já rodou o código 
    conta2L=0
    totLitros=0
    somaPeso3L=0
    qtAl3L=0
    while jaFiz < n:
        peso = float(input("Peso do aluno %d "%(jaFiz+1)))
        lAgua = AguaIndiv(peso)
        
        if lAgua <2:
            conta2L+=1  #    conta2L=conta2L+1 
        elif lAgua > 3:
           somaPeso3L+=peso
           qtAl3L+=1
            
        totLitros+=lAgua
        print('Aluno %d-Peso:%6.2f-Litros de água:%6.2f' %(jaFiz+1,peso,lAgua))
        jaFiz+=1
    print("\nEstatísticas da turma")
    print(" V1-  Qt de alunos que ingerem menos de 2 L de água: %.1f"%(conta2L))
    print(" V2-  Percentual de alunos que ingerem menos de 2 L de água: %.1f%%"%(conta2L*100/n))
    print(" V3- Total de litros de água consumidos pela turma: %.1f"%(totLitros))
    print(" V4- Quantidade média de litros de água por aluno nesta turma: %.1f"%(totLitros/n))
    if qtAl3L>0:
        print(" V5-  Peso médio  dos alunos que ingerem mais d 3L: %.1f"%(somaPeso3L/qtAl3L))
    return totLitros
# Informar o total de litros consumidos pelas 3 turmas: totLit T1 + totLit T2 + totLIt T3
contaTurma=0
totLitGeral=0
while contaTurma < 3:
    contaTurma+=1
    n=int(input("Quantos alunos na Turma %i? "%contaTurma))
    totLitrosTurma=processaUmaTurma(n)
    totLitGeral += totLitrosTurma
print(" Total Geral: %.2f"%totLitGeral)   