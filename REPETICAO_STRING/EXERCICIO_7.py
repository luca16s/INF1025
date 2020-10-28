excursoes = 5
contador = 0

while contador < excursoes:
    identificacaoPessoa = 1

    lider = 0
    idadeLider = 0
    maiorIdade = 0
    identificacaoLider = 0
    quantidadePessoas = 0

    while identificacaoPessoa != 0:
        identificacaoPessoa = int(input('Insira o id da pessoa: '))

        if identificacaoPessoa != 0:
            idadePessoa = int(input('Insira a idade da pessoa: '))
            if idadePessoa < 11:
                print('Excursão não aprovada')
                continue
            
            if idadePessoa >= 18:
                maiorIdade += 1
            
            if idadeLider < idadePessoa:
                lider = identificacaoPessoa
                idadeLider = idadePessoa
        quantidadePessoas += 1    

    if quantidadePessoas/2 == 0:
        print('Excursão não aprovada')
        quantidadePessoas += 1
        continue

    if quantidadePessoas < 5:
        print('Excursão não aprovada')
        quantidadePessoas += 1
        continue
    print('Líder aprovado: %d'%lider)
contador += 1