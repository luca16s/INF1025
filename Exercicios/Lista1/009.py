#9) Um operador de crossover pode ser aplicado a duas strings s1 e s2 e consiste em sortear aleatoriamente
#um ponto de s1 e s2. Escolhido este ponto, então, é realizada a troca de informações de s1 e s2 tal como
#mostrado no esquema da Figura abaixo:
#a) crie duas strings s1 e s2
#b) considere um ponto de quebra sorteado via randint
import random

s1 = 'ATGCCGTA'
s2 = 'TAGAAGAT'

pontoQuebra = random.randint(0, len(s1))

crossover = s1[:pontoQuebra] + s2[pontoQuebra:]
s2 = s1[pontoQuebra:] + s2[:pontoQuebra]
s1 = crossover
print(s1)
print(s2)