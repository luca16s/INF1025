#2)Escreva um programa para calcular a redução do tempo de vida de um fumante. Calcule
#randomicamente a quantidade de cigarros fumados por dia e quantos anos ele já fumou. Considere
#que um fumante perde 10 minutos de vida a cada cigarro, calcule quantos dias de vida um fumante
#perderá.
#a) Exiba o total em dias.
#b) Exiba o total em semanas
#c) Exiba o total em meses, dias considere todos os meses com 30 dias)
#d) Exiba o total em anos, meses, dias (considere todos os anos com 365 dias e os meses com 30
#dias)
import random

quantidadeMinutosDia = 24*60
quantidadeMinutosSemana = 7*(24*60)
quantidadeMinutosMes = 30*(24*60)
quantidadeMinutosAno = 365*(24*60)

quantidadeCigarrosPorDia = random.randint(1, 10000000)
quantidadeCigarrosAnteriormenteFumados = random.randint(1, 100)

tempoVidaPerdido = (quantidadeCigarrosAnteriormenteFumados * 10) + (quantidadeCigarrosPorDia * 10)

dias = tempoVidaPerdido // quantidadeMinutosDia
semanas = tempoVidaPerdido // quantidadeMinutosSemana
meses = tempoVidaPerdido // quantidadeMinutosMes
anos = tempoVidaPerdido // quantidadeMinutosAno

print('Total perdido em dias: ' + str(dias))
print('Total perdido em semanas: ' + str(semanas))
print('Total perdido em mesas: ' + str(meses))
print('Total perdido em Anos, Meses, dias: ' + str(anos) + ' ' + str(meses) + ' ' + str(dias))
