# A. Faça um programa que pergunte ao usuário o valor atual da passagem de ônibus e o valor reajustado,
# calcule e mostre o percentual de reajuste.

precoOnibus = input('Digite o valor do ônibus: ')
valorReajuste = input('Digite o valor de reajuste: ')

percentualDeAjuste = ((float(valorReajuste) - float(precoOnibus))/float(precoOnibus))*100

print('O percentual de ajuste foi de: %d%%'%(percentualDeAjuste))