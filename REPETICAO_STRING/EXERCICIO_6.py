def converteHorasEmMinutos(horas):
    return (int(horas[0:2])*60) + int(horas[:2:-1])

def processarVoos(horarioPrevistoChegada, horarioChegada):
    chegada = converteHorasEmMinutos(horarioChegada)
    chegadaPrevista = converteHorasEmMinutos(horarioPrevistoChegada)
    if chegada < chegadaPrevista:
        print('O voo chegou adiantado')
    elif chegadaPrevista == chegada:
        print('O voo chegou no horário')
    else:
        print('O voo chegou atrasado')
    return chegada - chegadaPrevista

quantidadeVoos = int(input('Quantidade de voos: '))
contador = 0
tempoTotalAtrasos = 0
quantidadeVooHorario = 0
quantidadeVoosComAtraso = 0
maiorAtraso = 0
quantidadeVoosComMaiorAtraso = 0

while contador < quantidadeVoos:
    tempoVoo = processarVoos(input('Insira o horário previsto para chegada: '), input('Insira o horário de chegada: '))

    if maiorAtraso < tempoVoo:
            maiorAtraso = tempoVoo            
    
    if tempoVoo == maiorAtraso:
        quantidadeVoosComMaiorAtraso += 1

    if tempoVoo == 0:
        quantidadeVooHorario += 1
    elif tempoVoo > 0:
        tempoTotalAtrasos += tempoVoo
        quantidadeVoosComAtraso += 1

    contador += 1

print('Percentual de voos atrasados: %d'%((quantidadeVoosComAtraso/quantidadeVoos)*100))
print('Maior atraso: %d quantidade de voos com maior atraso: %d'%(maiorAtraso, quantidadeVoosComMaiorAtraso))
print('Tempo total de atrasados: %d'%tempoTotalAtrasos)
print('Quantidade de voos no horário: %d'%quantidadeVooHorario)