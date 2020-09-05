#14) Em uma urna de sorteio de prêmios existem dez bolas enumeradas de 0 a 9. Determine o número de
#possibilidades existentes num sorteio cujo prêmio é formado por uma sequência de 6 algarismos.
#(151200)

import math

resultado = math.factorial(10)/math.factorial(10-6)

print(int(resultado))