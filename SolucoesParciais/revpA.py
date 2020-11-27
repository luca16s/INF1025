def ler_disciplinas():
    #que preenche a lista de disciplinas onde cada elemento é uma sublista
    #com o código e critério utilizado nas disciplinas a partir dos dados
    #do arquivo Disciplinas.txt (vide exemplo)
    ldisc=[]
    arq = open("disciplinas.txt","r")
    for linha in arq:
        linha=linha.strip()
        els=linha.split('\t')
        els[1]=int(els[1])
        ldisc.append(els)
    
    arq.close()
    return ldisc

def ler_criterios():
    #que  preenche uma lista  com o número de provas de cada um dos 5 critérios
    #por ordem de critério (na primeira posição armazena a quantidade de provas do critério 1,
    #na segunda posição armazena  a quantidade de provas do  critério 2 e, assim, sucessivamente).
    #O  arquivo Criterios.txt armazena, em cada linha, o número de provas de cada critério (vide exemplo)
    #Como o arquivo de critério só contem um número em cada linha, pode ser lido "de uma vez só"
    
    arq = open("criterios.txt","r")
    tudo=arq.read() # lê todas as linha do arquivo em 1 string
    tudo=tudo.strip()
    lcrit= tudo.split('\n')
    for (i,el) in enumerate(lcrit):
        lcrit[i]=int(el)
    
    arq.close()
    return lcrit

def busca(ldisc,disc):
    for i,el in enumerate(ldisc):
        if el[0] == disc:
            return i
    return None
    


ldisc=ler_disciplinas()
print(ldisc)  

lcrit = ler_criterios ()
print(lcrit)

aluno = input("Quem é vc?")
ldiscAl= [aluno,[]]
disc=input("Qual sua disciplina? ou enter para finalizar")
while disc:
    pos = busca(ldisc,disc)
    if pos != None:
        ncriterio=ldisc[pos][1]
        print("A disciplina %s tem %d provas"%(disc,lcrit[ncriterio]))

    else:
        print("Disciplina inexistente")
    disc=input("Qual sua disciplina? ou enter para finalizar")
print(ldiscAl)
