# -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 07:14:09 2020

@author: lcam
"""

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
        arqS.write("%s %d\n"%(nome,faltas))
arqE.close()
arqS.close()        