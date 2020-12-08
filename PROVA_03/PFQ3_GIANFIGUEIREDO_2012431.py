#Nome completo: GIAN LUCA DA SILVA FIGUEIREDO
#Matrícula PUC-Rio: 2012431
#Declaração de autoria: declaro que este documento foi produzido em sua totalidade por mim, sem consultas a outros alunos, professores ou qualquer outra pessoa.

def lerDados(arquivo):
    listaDadosPessoais = []
    arquivo = open(arquivo, "r")
    for linha in arquivo:
        linha = linha.strip()
        informacaoPessoal = linha.split(';')
        informacao = [ int(informacaoPessoal[0]), informacaoPessoal[1], informacaoPessoal[2], informacaoPessoal[3], informacaoPessoal[4] ]
        listaDadosPessoais.append(informacao)
    arquivo.close()
    return listaDadosPessoais

def contaQuantidadeAnimaisEstado(listaInformacoes):
    listaEstadoAnimal = []
    for informacoes in listaInformacoes:
        animal = informacoes[4]
        estado = informacoes[1]

        if animal != 'GATO' and animal != 'CACHORRO':
            if len(listaEstadoAnimal) == 0:
                listaEstadoAnimal.append([estado, 1])
            else:
                for (indice, valor) in enumerate(listaEstadoAnimal):
                    if estado in valor:
                        listaEstadoAnimal[indice][1] += 1
                        break
                    elif indice + 1 == len(listaEstadoAnimal):
                        listaEstadoAnimal.append([estado, 0])
    return listaEstadoAnimal

listaInformacoesPessoais = lerDados('PROVA_03\\preferencias.txt')
listaDadosTradados = contaQuantidadeAnimaisEstado(listaInformacoesPessoais)

for dado in listaDadosTradados:
    print('Estado: %s    Quantidade: %d'%(dado[0], dado[1]))