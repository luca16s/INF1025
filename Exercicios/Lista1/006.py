#6) Guarde o nome de seu pai em uma variável. Guarde o nome de sua mãe em uma variável. Mostre as
#possibilidades de nomes para você, considerando combinações das metades dos nomes de seus pais.
#Por ex 1ª metade mãe com 1ª metade do pai.
import math

nomePai = 'Carlos Antonio'
nomeMae = 'Elisangela'

quantidadeLetrasPai = len(nomePai) // 2
quantidadeLetrasMae = len(nomeMae) // 2

print(math.factorial(quantidadeLetrasMae + quantidadeLetrasPai))