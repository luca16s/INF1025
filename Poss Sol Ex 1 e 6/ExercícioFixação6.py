
def calcMontanteFinal(valor,juros,qtdm):
    mes = 1
    while mes <= qtdm:
        if mes%3 == 0:
            juros = juros + 0.002
        if mes%2 == 0:
            juros = juros + 0.02
        
        print("Mês %i) "%mes,end=' ')
        print("Taxa de juros utilizada: %.3f%%"%(juros), end=' - ')
        if valor%13 == 0:
            valor = valor + 1000
            print("Houve a incorporação de um prêmio de R$1000,00.", end= ' - ')
        valor = valor + valor*juros
        print("Montante reajustado: R$%.2f"%(valor))
        mes = mes + 1

valor = float(input("Qual o valor inicial a ser aplicado? "))
jurosI = float(input("Qual o percentual da taxa de juros inicial? "))
juros = jurosI/100
qtdm = int(input("Quantos meses a aplicar? "))
calcMontanteFinal(valor,juros,qtdm)
