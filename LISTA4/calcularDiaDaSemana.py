def NumeroDiadaSemana(ano, mes, dia):
    a = (14-mes) //12
    y = mes - a
    m = mes +12*a-2
    q = dia + (31*m//2) + y + y//4 - 4//100 + y//400
    return q % 7

def DiaDaSemana(ano, mes, dia):
    numeroDiaSemana = NumeroDiadaSemana(ano, mes, dia)
    diaDaSemana = ''
    if numeroDiaSemana == 0:
        diaDaSemana = 'domingo'
    elif  numeroDiaSemana == 1:
        diaDaSemana = 'segunda-feira'
    elif  numeroDiaSemana == 2:
        diaDaSemana = 'terça-feira'
    elif  numeroDiaSemana == 3:
        diaDaSemana = 'quarta-feira'
    elif  numeroDiaSemana == 4:
        diaDaSemana = 'quinta-feira'
    elif  numeroDiaSemana == 5:
        diaDaSemana = 'sexta-feira'
    elif  numeroDiaSemana == 6:
        diaDaSemana = 'sábado'
    return