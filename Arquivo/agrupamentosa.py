# -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 07:14:09 2020

@author: lcam
"""
'''
formato do Arquivo de saída:
    Nome do grupo  membros do grupo
    
[INF1025, [Kaka,Ceci,Teco]], --> INF1025  Kaka Ceci Teco
[FIS1020, [Keko]],
[FIS1212, [Tata]]
[CAL1010,[kiko]]
'''
def salvaTabGruposNoArq(tabGrupos):
    arqS=open('alunosPordisc.txt','w')
    for el in tabGrupos:  #  el:[INF1025, [Kaka,Ceci,Teco]]
        arqS.write("%s "%el[0])  # nome da disc
        for nome in el[1]: # lista de alunos da disc
            arqS.write("%s "%nome)
        arqS.write('\n')
    arqS.close()
    
def busca(l,valor):
    for (i,el) in enumerate(l):
        if el[0]==valor:
            return i  # local na lista do valor
    return None # valor não está na lista


arqE=open('alunos.txt','r')
tabGrupos=[]
for linha in arqE:
    linha=linha.strip()
    lVals=linha.split(',')
    nome=lVals[0]
    disc=lVals[1]
    faltas=int(lVals[2])
    med=float(lVals[3])
    pos =busca(tabGrupos,disc)
    if pos != None:
        tabGrupos[pos][1].append(nome)
    else:
        tabGrupos.append([disc,[nome]])
arqE.close()

salvaTabGruposNoArq(tabGrupos)
       