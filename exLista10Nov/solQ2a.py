# -*- coding: utf-8 -*-
"""
Created on Tue Nov 10 07:41:00 2020

@author: lcam
"""
'''
2.	a) Faça uma função para permitir que um usuário altere sua senha. 
Esta função recebe uma lista de listas, onde cada lista interna armazena 
o login e a senha de um usuário,  e realiza a alteração da senha se 
possível. 
Para alterar sua senha, o usuário deverá digitar seu login, 
caso esteja correto, o usuário deverá, digitar a senha  atual.  
Se ela estiver correta, o usuário  poderá alterar sua senha, 
digitando duas vezes a nova senha. 
Esta nova senha será aceita como atual. 
Uma mensagem adequada deve ser exibida nas situações inválidas.
Para testar sua função considere a seguinte lista de usuários:
'''
def busca( login,lUser):
    # caso login pertença a lUser --> posição
    # caso o login não pertença a lUser --> None
    for (i,el) in enumerate(lUser):
        loginUser=el[0]
        if  login == loginUser:
            return i
    #Aqui , só quando não acha
    return None

def alteraSenha(lUser):
    login= input("Login? ")
    senhaAtual= input("Senha? ")
    # Achar o login na lUser como não é de valores, in/index não funcionam
    posUser=busca(login,lUser)
    if posUser == None:
        print("User inex")
    elif senhaAtual != lUser[posUser][1]:
        print("senha incorreta")
    else:  # atualizar a senha
        novaSenha=input("Nova Senha? ")
        confNovaSenha=input("Confirma Nova Senha: ")
        if novaSenha == confNovaSenha:
            # atualiza
            lUser[posUser][1]=novaSenha
        else:
            print("senhas não conferem")
   
    return

lUser=[ ['huguinho', '12345'],
		['luisinho', '2345'],
		['zezinho', '1111'],
		['lala',  '12345'],
		['lele',  '2345'],
		['lili',  'oi']
	  ]