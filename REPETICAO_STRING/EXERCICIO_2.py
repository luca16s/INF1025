def contaConsoantes(nomeCompleto):
    contador = 0
    posicao = 0
    quantidadeLetras = len(nomeCompleto)
    while posicao < quantidadeLetras:
        if nomeCompleto[posicao].lower() in 'bcdfghjklmnpqrstvwxyz':
            contador +=1
        posicao += 1
    return contador

def definirSala(nomeCompleto, curso):    
    consoanteNomePar = contaConsoantes(nomeCompleto)%2
    if curso.lower() == 'agropecuária':
        if consoanteNomePar:
            return "Sala 24"
        else:
            return "Sala 32"
    elif curso.lower() == 'alimentos':
        if consoanteNomePar:
            return "Sala 43"
        else:
            return "Sala 24"
    elif curso.lower() == 'informática':
        if consoanteNomePar:
            return "Sala 32"
        else:
            return "Sala 43"


def retornarRubrica(nomeCompleto):
    posicao = 0
    tamanho = len(nomeCompleto)
    rubrica = nomeCompleto[posicao]
    while posicao < tamanho:
        if nomeCompleto[posicao] == ' ':
            rubrica += nomeCompleto[posicao+1]
        posicao += 1
    return rubrica

nomeCompleto = ''
qtdAlunoSala24 = 0
qtdAlunoSala32 = 0
qtdAlunoSala43 = 0

while nomeCompleto != 'FIM':
    nomeCompleto = input('Insira o nome do aluno: ')
    if nomeCompleto != 'FIM':
        nomeCurso = input('Insira o nome do curso: ')
        sala = definirSala(nomeCompleto, nomeCurso)
        print('%s, %s, %s, %s'%(nomeCompleto, nomeCurso, retornarRubrica(nomeCompleto), sala))
        if sala == "Sala 24":
            qtdAlunoSala24 +=1
        elif sala == "Sala 32":
            qtdAlunoSala32 +=1
        elif sala == "Sala 43":
            qtdAlunoSala43 +=1
    nomeCompleto = 'FIM'

print('A quantidade de alunos na sala 24 é: %s'%qtdAlunoSala24)
print('A quantidade de alunos na sala 32 é: %s'%qtdAlunoSala32)
print('A quantidade de alunos na sala 43 é: %s'%qtdAlunoSala43)
