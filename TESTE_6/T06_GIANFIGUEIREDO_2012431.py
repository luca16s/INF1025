#Nome completo: GIAN LUCA DA SILVA FIGUEIREDO
#Matrícula PUC-Rio: 2012431
#Declaração de autoria: declaro que este documento foi produzido em sua totalidade por mim, sem consultas a outros alunos, professores ou qualquer outra pessoa.

def realizaLeituraArquivo(listaArquivoEleicoes):
    listaHorario = []
    for linha in listaArquivoEleicoes:
        linha=linha.strip()
        listaInformacoesEleicao=linha.split(';')
        idade = int(listaInformacoesEleicao[3])
        hora = int(listaInformacoesEleicao[4][0:2])
        zonaEleitoral = listaInformacoesEleicao[1]
        if idade < 60 and hora >= 7 and hora < 10:
            listaHorario.append(zonaEleitoral)
    listaHorario.sort()
    return listaHorario

def contaQuantidadePalavras(lista, palavra):
    quantidadePalavras = 0
    for item in lista:
        if len(item) > 1 and item == palavra:
               quantidadePalavras +=1
    return quantidadePalavras

arquivoEleicoes = open('TESTE_6\MOVELEICOES.txt','r')
arquivoHorario = open("TESTE_6\HORARIO.txt",'w')

listaHorarioAEscrever = realizaLeituraArquivo(arquivoEleicoes)

for (indice, zonaEleitoral) in enumerate(listaHorarioAEscrever):
    if indice+1 != len(listaHorarioAEscrever):
        if zonaEleitoral == listaHorarioAEscrever[indice+1]:
            continue
    arquivoHorario.write("%s:%d\n"%(zonaEleitoral, contaQuantidadePalavras(listaHorarioAEscrever, zonaEleitoral)))

arquivoEleicoes.close()
arquivoHorario.close()