#13) Uma família é composta por seis pessoas (pai, mãe e quatro filhos) que nasceram em meses diferentes
#do ano. Calcule as sequências dos possíveis meses de nascimento dos membros dessa família.
#(arranjo)(resposta = 665.280)

import math

quantidadePessoas = 6

resultado = math.factorial(12)/math.factorial(12-quantidadePessoas)

print(int(resultado))