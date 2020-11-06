# -*- coding: utf-8 -*-
"""
Created on Wed May 27 21:12:15 2020

@author: cf
"""
'''
1.	Construa um programa, utilizando a função contaLetra, que pergunte o 
signo de 5 pares de pessoas (signo da 1ª pessoa, signo da 2ª pessoa) e, 
para cada par, informe a compatibilidade entre eles de acordo com a 
regra descrita abaixo:
•	se o total de letras não acentuadas do signo da 1ª pessoa  
   for igual ao total de letras não acentuadas do signo da 2ª pessoa, então o resultado será “Compatível”; 
•	 caso contrário, o resultado será “Não Compatível”. 
Exemplo1: “Áries” e “Gêmeos”  -> 4 e 5   Resultado: Não compatíveis
Exemplo1: “Gêmeos” e “Libra”  -> 5 e 5   Resultado: Compatíveis
Exemplo2: “Virgem” e “Peixes"  -> 6 e 6   Resultado:  Compatíveis

No final, seu programa deve exibir o percentual de pares compatíveis 
e a  palavra com o menor número de letras
---> Problema com o 1º: 
    como criar a variavel menor ANTES de começar a leitura dos dados?
    ( o valor fake tem que ser  maior que o tamanho da maior palavra
      que será digitada !!!)
    Possíveis estratégias:
       a) colocar um valor escolhido ( por ex. negativo, '#', etc) na variável menor
          e testar  se o valor do menor é o escolhido, significa que é a 1ª
          comparação, coloca o valor na variável menor 
       b) criar uma variável para marcar  o número da repetição ( por contagem ou variável booleana)
          se esta variável indica que é a primeira repetição, 
          cria a variável menor e altera a a variável indicadora da 1ª vez
            

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

'''
# CONTROLANDO VIA Nº do ciclo
ctaComp=0
ctaPares=0

while ctaPares < 5:    
    ctaPares+=1  #contagem dos ciclos
    sig1=input('Signo da 1ª pessoa: ')
    sig2=input('Signo da 2ª pessoa: ')
    qt1=contaLetras(sig1)
    qt2=contaLetras(sig2)
    if qt1 == qt2:
        mens='compatíveis'
        ctaComp+=1
    else:
        mens='não compatíveis'
    print("\n%s - %s - %s"%(sig1,sig2,mens))
    if ctaPares==1:  # primeiro ciclo da repetição
        if qt1<qt2:
            menor=qt1
            menorSig=sig1
        else:
            menor=qt2
            menorSig=sig2
    else:
        if qt1<menor:
            menor=qt1
            menorSig=sig1
        if qt2<menor:
            menor=qt2
            menorSig=sig2
        
    
print("\nPercentual de compatibilidade: %.1f%%"%(ctaComp/ctaPares*100))
print("Signo com menor número de letras: %s"%menorSig)
'''   

# CONTROLANDO VIA VARIÁVEL BOOLEANA

ctaComp=0
ctaPares=0
primeira = True
while ctaPares < 5:    
    ctaPares+=1  #contagem dos ciclos
    sig1=input('Signo da 1ª pessoa: ')
    sig2=input('Signo da 2ª pessoa: ')
    qt1=contaLetras(sig1)
    qt2=contaLetras(sig2)
    if qt1 == qt2:
        mens='compatíveis'
        ctaComp+=1
    else:
        mens='não compatíveis'
    print("\n%s - %s - %s"%(sig1,sig2,mens))
    if primeira:  # primeiro ciclo da repetição
        primeira=False
        if qt1<qt2:
            menor=qt1
            menorSig=sig1
        else:
            menor=qt2
            menorSig=sig2
    else:
        if qt1<menor:
            menor=qt1
            menorSig=sig1
        if qt2<menor:
            menor=qt2
            menorSig=sig2
        
    
print("\nPercentual de compatibilidade: %.1f%%"%(ctaComp/ctaPares*100))
print("Signo com menor número de letras: %s"%menorSig)
