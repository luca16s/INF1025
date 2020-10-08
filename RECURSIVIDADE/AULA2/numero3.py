def contaQuantidadeAlgarismosDois(numero):
    if numero < 10:
        if numero == 2:
            return 1
        else:
            return 0
    else:
        unidade=numero%10
        prefixo=numero//10
        count = contaQuantidadeAlgarismosDois(prefixo)
        if unidade == 2:
            count += 1
        return count

resultado = contaQuantidadeAlgarismosDois(248542)
print(resultado)