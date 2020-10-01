def CalculaPotencia(numero, potencia):
    if potencia == 0:
        return 1
    if potencia % 2 == 0:
        return CalculaPotencia(numero, potencia/2)**2
    else:
        return numero * CalculaPotencia(numero, potencia-1)

print(CalculaPotencia(3, 4))
print(CalculaPotencia(2, 3))