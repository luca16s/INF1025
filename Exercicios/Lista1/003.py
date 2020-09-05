#3) Guarde seu nome em uma variável. Exemplo: nome= 'Pedro José Silva Só'
#a) Exiba uma string formada por '*' com mesmo comprimento de seu nome
#(*******************)
#b) Replique o caractere do meio de seu nome, para que tenha o mesmo comprimento de seu
#primeiro nome ('ééééé')

nome = 'Gian Luca'

quantidadeCaracteresNome = len(nome)
caracterIntermediario = nome[quantidadeCaracteresNome//2]

print('*'*quantidadeCaracteresNome)

print(caracterIntermediario*quantidadeCaracteresNome)