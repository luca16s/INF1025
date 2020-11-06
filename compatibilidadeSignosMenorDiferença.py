# -*- coding: utf-8 -*-
"""
Created on Wed May 27 21:12:15 2020

@author: cf
"""
'''
1.	Construa um programa, utilizando a função contaLetra, que pergunte o signo 
de vários pares de pessoas (signo da 1ª pessoa, signo da 2ª pessoa) e, 
para cada par, informe a compatibilidade entre eles de acordo com a 
regra descrita abaixo:
•	se o total de letras não acentuadas do signo da 1ª pessoa  
   for igual ao total de letras não acentuadas do signo da 2ª pessoa, então o resultado será “Compatível”; 
•	 caso contrário, o resultado será “Não Compatível”. 
Exemplo1: “Áries” e “Gêmeos”  -> 4 e 5   Resultado: Não compatíveis
Exemplo1: “Gêmeos” e “Libra”  -> 5 e 5   Resultado: Compatíveis
Exemplo2: “Virgem” e “Peixes"  -> 6 e 6   Resultado:  Compatíveis
O término da entrada de dados ocorre quando for digitado como signo da 1ª pessoa
a palavra "FIM".
No final, seu programa deve exibir o percentual de pares compatíveis 
e a  menor diferença entre as palavras
---> Problema com o 1º: 
    como criar a variavel menor ANTES de começar a leitura dos dados?
    ( o valor fake tem que ser  maior que o tamanho da maior palavra
      que será digitada !!!)
    Solução
    Neste problema, como o signo da 1ª pessoa é lido antes do while, 
    é possível inicializar o menor com a qt de letras deste signo
    

'''

def ehLetra(c):
    return c>='A' and c<='Z' or c>='a' and c<='z'

def contaLetras(texto):
    pos=0
    tam=len(texto)
    qt=0
    while pos < tam:
        if ehLetra(texto[pos]):
            qt+=1
        pos+=1
    return qt	

ctaComp=0
ctaPares=0
sig1=input('Signo da 1ª pessoa: ')
primeira=True


while sig1.upper() != 'FIM':  # elimina o problema de digitações com mistura de maiúsculas e minúsculas
    ctaPares+=1
    sig2=input('Signo da 2ª pessoa: ')
    qt1=contaLetras(sig1)
    qt2=contaLetras(sig2)
    if qt1 == qt2:
        mens='compatíveis'
        ctaComp+=1
    else:
        mens='não compatíveis'
    print("%s - %s - %s"%(sig1,sig2,mens))
    dif=abs(qt1-qt2)
    if primeira==True:
        menor=dif
        primeira=False
    else:
        if dif<menor:
            menor=dif
        
    sig1=input('Signo da 1ª pessoa: ')
if ctaPares >0:
    print("Percentual de compatibilidade: %.1f%%"%(ctaComp/ctaPares*100))
    print("Menor diferença: %s"%menor)
    