#Nome completo: GIAN LUCA DA SILVA FIGUEIREDO
#Matrícula PUC-Rio: 2012431
#Declaração de autoria: declaro que este documento foi produzido em sua totalidade por mim, sem consultas a outros alunos, professores ou qualquer outra pessoa.

def contabilizaAlunosPorAno(listaAlunos):
    listaDisciplinasAno = []
    quantidadePalavras = 0 # Apagar
    for item in listaAlunos:
        if type(item) != list:
            if item >= 2015 and item <= 2020:
                print()
            else:
                continue
        else:
            quantidadePalavras += contabilizaAlunosPorAno(item)
    return quantidadePalavras

listaAlunos = [
    [111, ['FIS155', '2018_1'], ['MAT232', '2018_1'], ['INF100', '2019_1'], ['REL445', '2020_1']],
    [333, ['INF100', '2017_1'], ['FIS155', '2017_2'], ['ECO929', '2020_1']],
    [777, ['REL445', '2019_1'], ['FIS155', '2019_2'], ['ECO929', '2019_2'], ['INF100', '2020_1']],
    [444, ['REL445', '2015_1'], ['INF100', '2015_1'], ['FIS155', '2016_1']],
    [888, ['FIS155', '2017_1'], ['MAT232', '2017_2'], ['ECO929', '2019_1'], ['INF100', '2020_1']],
    [222, ['FIS155', '2016_1'], ['MAT232', '2016_2'], ['ECO929', '2017_1'], ['REL445', '2017_2']]
    ]

print(contabilizaAlunosPorAno(listaAlunos))
