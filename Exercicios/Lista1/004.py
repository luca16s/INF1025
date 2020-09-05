#4) Guarde sua data de nascimento em uma variável no formato 'dd/mm/aaaa'.
#Exemplo dt = '01/01/1984'
#a) Exiba apenas o ano ('1984')
#b) Exiba o ano invertido ('4891')
#c) Exiba toda a data invertido ('4891/10/10')
#d) Exiba a data no formato 'dd-mm-aaaa'

dataNascimento = '16/04/1995'

print('Ano de Nascimento: ' + dataNascimento[-4:])
print('Ano de Nascimento Invertido: ' + dataNascimento[:-5:-1])
print('Nascimento Invertido: ' + dataNascimento[::-1])
print('Data no Formato dd-mm-aaaa: ' + dataNascimento[0:2] + '-' + dataNascimento[3:5] + '-' + dataNascimento[6:])