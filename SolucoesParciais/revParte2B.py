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

def ler_criterios(lcrit, lpesos):
    #que  preenche duas listas,
    #uma com  o número de provas do critério(lcrit) e
    #outra com o peso de cada uma delas(lpesos).
    #Na primeira posição de lcrit armazena a quantidade de provas do critério 1
    #e na primeira posição de lpesos está uma sublista com o peso de cada uma,
    #e, assim, sucessivamente).
    arq = open("criteriosParte2B.txt","r")
    for linha in arq:
        linha=linha.strip()
        els=linha.split(' ')
        lcrit.append(int(els[0]))
        lp=[] # listinha de pesos do critério
        for el in els[1:]:
            lp.append(int(el))  #inclui os pesos de cada prova do critério na listinha
        lpesos.append(lp)   #inclui listinha de pesos do critério na lista de Critérios
    arq.close()
    return 

def busca(ldisc,disc):
    for (i,el) in enumerate(ldisc):
        if el[0] == disc:
            return i
    return None

def calculaMedia(ldiscAl,lPesos):
    for el in ldiscAl:
        disc=el[0]
        nProvas = el[2]
        nCriterio=el[1]
        pesos = lPesos[nCriterio]
        
        print("Digite suas notas na disciplina %s"%disc)
        somanotas=0
        totpeso=0
        for i in range(nProvas):
            nota=float(input("Sua nota na P%d"%(i+1)))
            somanotas+=nota*pesos[i]
            totpeso+=pesos[i]

        el.append(somanotas/totpeso) # inclui média do aluno nesta disciplina
    return

ldisc=ler_disciplinas()
lCrit=[]
lPesos=[]
ler_criterios (lCrit,lPesos)


aluno = input("Quem é vc?")
ldiscAl= [[aluno,[]]]
disc=input("Qual sua disciplina? ou enter para finalizar")
while disc:
    pos = busca(ldisc,disc)
    if pos != None:
        nCriterio=ldisc[pos][1]
        nProvas=lCrit[nCriterio]
        ldiscAl[0][1].append([disc,nCriterio, nProvas]) 
    else:
        print("Disciplina inexistente")
    disc=input("Qual sua disciplina? ou enter para finalizar: ")

for aluno in ldiscAl:
    calculaMedia(aluno[1],lPesos)
print(ldiscAl)
    

