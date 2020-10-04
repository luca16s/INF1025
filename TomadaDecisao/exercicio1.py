def CalcularImc(peso, altura):
    return peso/(altura)**2

def CalcularImcAtleta(genero, medidaPescoco):
    if genero == 'feminino':
        return RetornarImcAtletaFeminino(medidaPescoco)
    elif genero == 'masculino':
        return RetornarImcAtletaMasculino(medidaPescoco)

def CalcularImcIdoso(genero, medidaCircunferenciaBraco):
    if genero == 'feminino':
        return medidaCircunferenciaBraco * 100 / 29.9
    elif genero == 'masculino':
        return medidaCircunferenciaBraco * 100 / 30.7

def RetornarImc(valorImc):
    if valorImc < 18.5:
        return 'Abaixo'
    elif valorImc == 18.5 or valorImc <= 24.9:
        return 'Normal'
    elif valorImc == 25 or valorImc <= 29.9:
        return 'Sobrepeso'
    elif valorImc > 29.9:
        return 'Obesidade'

def RetornarImcIdoso(medidaCircunferenciaBraco):
    if medidaCircunferenciaBraco < 90:
        return 'Abaixo'
    elif medidaCircunferenciaBraco == 90 or medidaCircunferenciaBraco < 110:
        return 'Normal'
    elif medidaCircunferenciaBraco == 110.1 or medidaCircunferenciaBraco <= 120:
        return 'Sobrepeso'
    elif medidaCircunferenciaBraco > 120:
        return 'Obesidade'

def RetornarImcAtletaFeminino(medidaPescoco):
    if medidaPescoco < 18:
        return 'Abaixo'
    elif medidaPescoco == 18 or medidaPescoco < 34:
        return 'Normal'
    elif medidaPescoco == 34.1 or medidaPescoco <= 36.4:
        return 'Sobrepeso'
    elif medidaPescoco > 36.4:
        return 'Obesidade'

def RetornarImcAtletaMasculino(medidaPescoco):
    if medidaPescoco < 21:
        return 'Abaixo'
    elif medidaPescoco == 21 or medidaPescoco < 37:
        return 'Normal'
    elif medidaPescoco == 37.1 or medidaPescoco <= 39.4:
        return 'Sobrepeso'
    elif medidaPescoco > 39.4:
        return 'Obesidade'

def identificaEstadoNutricional(peso, altura, idoso, atleta, genero):
    if idoso == True:
        braco = float(input("Insira o tamanho do braço: "))
        return RetornarImcIdoso(CalcularImcIdoso(genero, braco))
    elif atleta == True:
        pescoco = float(input("Insira o tamanho do pescoço: "))
        return CalcularImcAtleta(genero, pescoco)
    else:
        return RetornarImc(CalcularImc(peso, altura))

peso = float(input("Insira seu peso: "))
altura = float(input("Insira sua altura: "))
genero = input("Insira seu gênero: ").lower()

isAtleta = False
resposta = input("Você é atleta? 0 - Não, 1 - Sim ")
if resposta == '0':
    isAtleta = False
elif resposta == '1':
    isAtleta = True

isIdoso = False
resposta = input("Você é idoso? 0 - Não, 1 - Sim ")
if resposta == '0':
    isIdoso = False
elif resposta == '1':
    isIdoso = True

print(identificaEstadoNutricional(peso, altura, isAtleta, isIdoso, genero))