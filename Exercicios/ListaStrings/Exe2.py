'''2. a) Escreva uma função que receba duas strings e retorne a concatenação da primeira, sem a sua
primeira metade com a segunda, sem os (no máximo) n primeiros caracteres, onde n é igual ao
tamanho da metade da primeira string.
Faça um programa que pergunte o nome da mãe e o nome do pai de um bebê, mostrando as
combinações possíveis dos nomes da mãe e pai de acordo com a regra acima.
Exemplo: mãe: Margarida pai: Donald
combina(‘Margarida’,’Donald’) Margld
combina(’Donald’ ,‘Margarida’) Dongarida'''
#---------------------------------------------------------------------------------
def ConcatenarTexto(texto1, texto2):
    metadeTexto1 = len(texto1)//2
    return texto1[0:metadeTexto1]+texto2[metadeTexto1:]
#---------------------------------------------------------------------------------
def CombinarNomes(nome1, nome2):
    return ConcatenarTexto(nome1, nome2)
#---------------------------------------------------------------------------------
print(ConcatenarTexto('ABCD', 'DEFG'))
#---------------------------------------------------------------------------------
nomeMae = input('Insira o nome da mãe: ')
nomePai = input('Insira o nome do pai: ')

print(ConcatenarTexto(nomeMae, nomePai))