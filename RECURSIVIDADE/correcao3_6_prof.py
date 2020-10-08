# -*- coding: utf-8 -*-
"""
Created on Tue Oct  6 08:40:01 2020

@author: lcam
"""
'''
3)	Crie uma função recursiva para contar quantos algarismos 2 
   o número possui

'''
def conta2(num):
    if num<10: # num com 1 algarismo
        # num é o 2-->1 ou  num não ser o 2 -->0
        if num ==2:
            return 1
        else:
            return 0
    else:  # num tem + que 1 algarismo
        unidade=num%10
        prefixo=num//10
        qtos2Noprefixo=conta2(prefixo)
        if unidade == 2:
           qt= qtos2Noprefixo + 1
        else:
            qt=qtos2Noprefixo
        return qt
        
'''
6)	Crie uma função que que verifique se um número possui 
todos os algarismos em ordem crescente. 
Esta função retorna True se os algarismos estão em ordem crescente, 
False  caso contrário
Exemplo:  
    2 True   
12 False  21 True    
642 True	 345 False    
9103 False 4321  True  
'''
def emOrdem(num):
    if num <10:
        return True
    unidade= num%10
    dezena= num%100//10
    if unidade > dezena:
        return False
    else:
        prefixo=num//10
        resp=emOrdem(prefixo)
        return resp
    
      
        
        
        
        
        