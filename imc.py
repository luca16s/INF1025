def CalculaImc(altura, peso):
    return peso / (altura * altura)

altura = float(input("Insira sua altura atual: "))
peso = float(input("Insira seu peso atual: "))

valorImcCalculado = CalculaImc(altura, peso)

if valorImcCalculado < 18.5:
    print("Abaixo do peso ideal.")
elif valorImcCalculado > 18.5 and valorImcCalculado < 24.9:
    print("Peso ideal")
elif valorImcCalculado > 25 and valorImcCalculado < 29.9:
    print("Sobre peso")
elif valorImcCalculado > 30 and valorImcCalculado < 34.9:
    print("Obesidade grau 1")
elif valorImcCalculado > 35 and valorImcCalculado < 39.9:
    print("Obesidade grau 2")
else:
    print("Obesidade grau 3")
