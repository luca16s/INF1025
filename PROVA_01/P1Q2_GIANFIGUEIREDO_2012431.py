#Nome completo: GIAN LUCA DA SILVA FIGUEIREDO
#Matrícula PUC-Rio: 2012431
#Declaração de autoria: declaro que este documento foi produzido em sua totalidade por mim, sem consultas a outros alunos, professores ou qualquer outra pessoa.

def calcularVolumeCaixa(comprimento, largura, altura):
    return comprimento * largura * altura

def validarEspecificacoesCaixa(comprimento, largura, altura, peso):
    volumeCaixa = calcularVolumeCaixa(comprimento, largura, altura)

    if volumeCaixa <= 8000:
        return 30.00
    elif volumeCaixa > 8000 and volumeCaixa <= 64000:
        if peso <= 20:
            return 65.00
        elif peso > 20:
            return 80.00
    elif volumeCaixa > 64000 and volumeCaixa <= 216000 and peso > 30 and peso < 50:
        return 100.00
    else:
        return 0

def mostrarMensagem(valor):
    if valor > 0:
        print("  Valor: %.2f"%valor)
    else:
        print("Caixa fora das especificações")

comprimento = float(input("Comprimento: "))
largura = float(input("Largura: "))
altura = float(input("Altura: "))
peso = float(input("Peso: "))
mostrarMensagem(validarEspecificacoesCaixa(comprimento, largura, altura, peso))