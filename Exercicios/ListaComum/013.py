#Considerando-se um capital inicial de R$10.000,00, aplicado a juros compostos, durante 1 ano, à taxa de 2,5% ao mês, qual
#será o capital final? Sabe-se que:
#capital final = P x (1 + i) n
#onde P = capital inicial, i = taxa de juros e n = número de períodos (no caso, meses)

import math

capitalInicial = 10000
quantidadeMeses = 12
taxaJuros = 2.5/100

capitalFinal = capitalInicial * (1 + taxaJuros)**quantidadeMeses

print('O capital final será de: ' + str(math.floor(capitalFinal)))