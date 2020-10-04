def descobre_x(ano):
    if (ano >= 1900 or ano < 1999) or (ano >= 2000 or ano < 2099):
        return 24
    elif ano >= 2100 or ano < 2199:
        return 24
    elif ano >= 2200 or ano < 2299:
        return 25

def descobre_y(ano):
    if (ano >= 1900 or ano < 1999) or (ano >= 2000 or ano < 2099):
        return 5
    elif ano >= 2100 or ano < 2199:
        return 6
    elif ano >= 2200 or ano < 2299:
        return 7

def exibe_dia_mes(a, d, e):
    dia = 0
    mes = 0
    resultadoDE = (d+e)
    if resultadoDE > 9:
        dia = resultadoDE - 9
        mes = 4
    elif resultadoDE <= 9:
        dia = resultadoDE - 22
        mes = 3
    
    if mes == 4 and dia == 26:
        dia = dia - 7
    elif mes == 4 and dia == 25 and d == 28 and a > 10:
        dia = dia - 7
        
    return "%i/%i/%i"%(dia,mes,a)


dia = int(input("Insira o dia: "))
mes = int(input("Insira o mês: "))
ano = int(input("Insira o ano: "))

A = ano % 19
B = ano % 4
C = ano % 7
D = (19 * A + descobre_x(ano)) % 30
E = (2 * B + 4 * C + 6 * D + descobre_y(ano)) % 7

print(exibe_dia_mes(A, D, E))