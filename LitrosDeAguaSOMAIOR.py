'''
Um professor,  sabendo que a dose diária de água é individual,
resolveu calcular a quantidade mínima de litros de água que deve ser ingerida
por cada um dos  alunos de uma turma. O término da entrada de dados ocorre
quando o professor digitar como valor do peso do aluno um número negativo
Esta medida é calculada por:
 	litros de água/dia  =  35ml de água  * peso corporal/1000
Faça um programa que inicialmente  obtenha a quantidade  de alunos da turma (n).
A seguir, para cada um dos alunos, obtenha o  peso  e
mostre a quantidade mínima de litros que o aluno deve consumir.
Seu programa deve responder:
    V1- Quantos alunos desta turma ingerem menos de 2 L de água?
         contagem dos que ingerem menos de 2 L de água
    v2 - Qual o percentual de alunos desta turma que ingerem menos de 2L?
         conta2L*100/número de alunos (n)
    V3  Qual o total de litros de água consumidos pela turma?
         soma dos litros de cada aluno (lAgua)
    V4 - Qual a quantidade média de litros de água por aluno nesta turma?
         soma dos litros de cada aluno (totLitros)/n
    v5 - Qual o peso médio dos alunos desta turma que consomem mais que 3l?
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



maior=-1
peso = float(input("Peso do 1º aluno ou um valor negativo para finalizar "))
while  peso >=0 : # professor quiser--> professor digitar algo 
    lAgua = AguaIndiv(peso)
    if lAgua > maior:
        maior=lAgua
    print('Aluno-Peso:%6.2f-Litros de água:%6.2f' %(peso,lAgua))
    peso = float(input("Peso do próximo aluno ou um valor negativo para finalizar "))
print(maior)

