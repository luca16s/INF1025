#16) Em um torneio internacional de natação participaram cinco atletas europeus, dois americanos e um
#brasileiro. De quantos modos distintos poderão ser distribuídas as medalhas de ouro, prata e bronze?
#A(8,3)=336

import math

resultado = math.factorial(8)/math.factorial(8-3)

print(int(resultado))