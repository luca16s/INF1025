#Nome completo: GIAN LUCA DA SILVA FIGUEIREDO
#Matrícula PUC-Rio: 2012431
#Declaração de autoria: declaro que este documento foi produzido em sua totalidade por mim, sem consultas a outros alunos, professores ou qualquer outra pessoa.

def contabilizaEletroPorLoja(listaEletrodomestico):
    listaQuantidadePorLoja = []
    for eletrodomestico in listaEletrodomestico:
        for item in eletrodomestico:
            if type(item) == list:
                loja = item[0]
                
                if len(listaQuantidadePorLoja) == 0:
                    listaQuantidadePorLoja.append([loja, 1])
                else:
                    for (indice, valor) in enumerate(listaQuantidadePorLoja):
                        if loja in valor:
                            valor[1] += 1
                            break
                        elif indice + 1 == len(listaQuantidadePorLoja):
                            listaQuantidadePorLoja.append([loja, 0])                            

    return listaQuantidadePorLoja

listaEletrodomestico = [
    ['geladeira', ['KadeZAO', 1537.8], ['TaBarato', 1337.9], ['LojaMIM', 1436.1], ['MaisAqui', 1537.6], ['SuperEletro', 1438.9]],
    ['liquidificador', ['PrecoCerto', 229.1], ['SuperEletro', 213.5], ['KadeZAO', 238.9], ['MaisAqui', 226.2], ['LojaMIM', 243.2],['TaBarato', 258.7]],
    ['batedeira', ['SuperEletro', 183.2], ['KadeZAO', 193.1], ['MaisAqui', 193.6], ['LojaMIM', 207.8], ['CasaMania', 137.4],['PrecoCerto', 198.1]],
    ['lava roupas', ['PrecoCerto', 2038.2], ['SuperEletro', 2123.4], ['TemTudo', 2237.6], ['MaisAqui', 2138.8], ['KadeZAO', 2041.5],['TaBarato', 2039.8], ['CasaMania', 1939.6]],
    ['centrífuga', ['SuperEletro', 1037.1], ['LojaMIM', 1232.5],['MaisAqui', 1226.8], ['KadeZAO', 1117.9]],
    ['cafeteira', ['LojaMIM', 108.9], ['MaisAqui', 111.7], ['SuperEletro', 120.2], ['KadeZAO', 109.7], ['TaBarato', 105.9]]]

print(contabilizaEletroPorLoja(listaEletrodomestico))