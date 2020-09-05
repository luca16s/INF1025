#15) Possuo 4 bolas amarelas, 3 bolas vermelhas, 2 bolas azuis e 1 bola verde. Pretendo colocá-las em um
#tubo acrílico translúcido e incolor, onde elas ficarão umas sobre as outras na vertical. De quantas
#maneiras distintas eu poderei formar esta coluna de bolas? permutação P10(4,3,2) ( 12600)
import math

resultado = math.factorial(10)/math.factorial(10-4)

print(int(resultado))