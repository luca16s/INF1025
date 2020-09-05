#8) Crie a string alfabeto
#alfabeto = "abcdefghijklmnopqrstuvwxyz"
#e, a partir da string alfabeto:
#a) crie uma string com o primeiro caractere, o caractere do meio e o último caractere
#b) Importe o módulo random
#c) Veja o help da função choice : help(random.choice)
#d) Veja o help da função randint : help(random.randint)
#e) Mostre o caractere do alfabeto escolhido pelas duas funções (choice e o randint)

alfabeto = "abcdefghijklmnopqrstuvwxyz"
quantidadeCaracteres = len(alfabeto)

print(alfabeto[0] + alfabeto[quantidadeCaracteres//2] + alfabeto[-1])

import random

help(random.choice)
help(random.randint)

print(random.choice(alfabeto))
print(alfabeto[random.randint(0, quantidadeCaracteres)])