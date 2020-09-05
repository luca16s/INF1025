#7) Calcule o número PI usando as funções arco-seno/inversa do seno, conforme o roteiro a seguir:
#a) Escolha um número qualquer entre -1 e 1 e armazene-o em x
#b) Use o número em x na fórmula abaixo e o resultado vai ser algo próximo de pi.
#pi = 2 * (arcsen (sqrt(1 – x**2)) + abs (arcsen(x))).
# "Arcsen" indica o seno inverso, em radianos.
# “sqrt" é a raiz quadrada.
# “abs" é o valor absoluto.
#Observação:Escolha randomicamente 3 valores para x.

import math, random

x = random.randint(-1, 1)
pi = 2 * (math.acos(math.sqrt(1-x**2))+abs(math.acos(x)))
print(pi)