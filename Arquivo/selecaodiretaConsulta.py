# -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 07:14:09 2020

@author: lcam
"""
def busca(l,valor):
    for (i,el) in enumerate(l):
        if el[0]==valor:
            return i  # local na lista do valor
    return None # valor não está na lista

def montaTabelaDisciplinas():
    tab=[]
    arqD=open('disciplinas.txt','r')
    for linha in arqD:
        lVals=linha.strip().split(',')
        lVals[1]=int(lVals[1])
        tab.append(lVals)
    arqD.close()
    return tab    
tabDisc=montaTabelaDisciplinas()
arqE=open('alunos.txt','r')
arqS=open("aprovados.txt",'w')
for linha in arqE:
    linha=linha.strip()
    lVals=linha.split(',')
    nome=lVals[0]
    disc=lVals[1]
    faltas=int(lVals[2])
    med=float(lVals[3])
    if med >= 6:
        # Se o número de faltas < que o da disciplina
        pos =busca(tabDisc,disc)
        if pos != None and faltas < tabDisc[pos][1]:
            arqS.write("%s %d\n"%(nome,faltas))
arqE.close()
arqS.close()        