#Escreva uma função para calcular e retornar a hipotenusa de um triângulo retângulo. Esta função
#deverá receber os valores dos catetos e retornar o valor da hipotenusa.
import math

def CalculaHipotenusa(catetoOposto, catetoAdjacente):
    return math.sqrt(catetoAdjacente**2 + catetoOposto**2)