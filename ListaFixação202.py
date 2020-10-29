#----------------------------------------------
#----------------------------------------------
lTextoDasQuestoes=['3+5=....', '9*3=....','2+3*4=....','7-5+9=....','4*6/3+2=....']
lGabarito=[8,27,14,11,10]
'''
Exibir o texto das questões
'''
print("=========================")
for q in lTextoDasQuestoes:
    print(q)

'''
Exibir nº e texto das questões
'''

print("=========================")
for (i,q) in enumerate(lTextoDasQuestoes):
    print("Q%i) %s"%(i+1,q))

'''
Exibir o número da questão e o gabarito da questão
'''
print("=========================")
for (ind,gab) in enumerate(lGabarito):
    print("Q%d) %d"%(ind+1,gab))

'''    
Exibir cada questão seguida do gabarito

print(lTextoDasQuestoes[0],'-',lGabarito[0])
print(lTextoDasQuestoes[1],'-',lGabarito[1])
print(lTextoDasQuestoes[2],'-',lGabarito[2])
'''
print("=========================")
for ind in range(0,len(lGabarito)):
    print("Q%d) %-12s - Gabarito: %d" % (ind+1,lTextoDasQuestoes[ind],lGabarito[ind]))

#----------------------------------------------
#----------------------------------------------
    
l1= [3,7,12,90,20]
l2= [4,3,2,9,2,16,4]
l3=[3,[98,2,1],10]
#----------------------------------------------
#----------------------------------------------
'''
Faça uma função que retorne a soma de todos os valores de uma lista
Ex  	soma (l1) = 132	
	soma(l2) = 40
'''
def soma(l):
    tot=0
    for val in l:
        tot+=val
    return  tot
print("=========================")
print('\nLista: ',[3,7,12,90,20], '\nTotal dos valores: ',soma([3,7,12,90,20]))
print("=========================")
print('\nLista: ',l2,'\nTotal dos valores: ',soma(l2))    
#----------------------------------------------
#----------------------------------------------

l1= [3,7,12,90,20]
l2= [4,3,2,9,2,16,4]
l3=[3,[98,2,1],10]
'''
I) Faça as funções abaixo e teste-as para l1:
    1) retorne  o produto dos números de uma lista
    2) retorne a média dos números de uma lista
    3) retorne o maior valor da lista
    4) substitua todos os múltiplos de 4 pelo número 0 na lista recebida
           altera(l1)
           print(l1)
    5) receba também  um número informado pelo usuário e retorne True, se o número está na lista e False, caso contrário
    6) exiba a posição dos valores acima da média
    7) exiba os valores que são múltiplos de sua posição 
        Cuidado: o primeiro elemento está na posição 0
    8)	exiba os valores iguais em posições simétricas ( 1º e último, 2º e penúltimo,...)
    9)	exiba os valores das posições pares
    10) return True se os elementos da lista estão em ordem crescente ou False, caso contrário
'''   
def calcularProduto(lista):
    produto = 1
    for numero in lista:
        produto *= numero
    return produto

def calcularMedia(lista):
    soma = 0
    for numero in lista:
        soma += numero
    soma/len(lista)

def retornaMaiorLista(lista):
    maiorNumero = 0
    for numero in lista:
        if numero > maiorNumero:
            maiorNumero = numero
    return maiorNumero

def substituirMultiplos(lista, multiplo, numeroSubstituto):
    for (indice, numero) in enumerate(lista):
        if numero%multiplo == 0:
            lista[indice] = numeroSubstituto

def checarExistenciaNumero(lista, numeroInserido):
    if numeroInserido in lista:
        return True
    else:
        return False

def exibirPosicaoAcimaMedia(lista):
    mediaLista = sum(lista)/len(lista)
    for (indice, numero) in enumerate(lista):
        if numero > mediaLista:
            return indice
        
def exibeMultiplosPosicao(lista):
    

#----------------------------------------------
#----------------------------------------------
'''
II) Faça as funções abaixo que recbem l1 e l2:
    1)	mostre os números que estão na mesma posição e são iguais
    2)  mostre a interseção
    3)  mostre a união

'''
#----------------------------------------------------
#----------------------------------------------


