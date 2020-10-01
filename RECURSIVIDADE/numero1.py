# mdc(x, y)
# y, se x % y = 0
# mdc(y, (x % y)), se x % y não for zero

def Mdc(numero1, numero2):
    resto = numero1 % numero2
    if resto == 0:
        return numero2
    else:
        div = Mdc(numero2, resto)
        return div