def validaSenhaUsuario(lista, login, senha):
    posicaoUsuario = None
    for (index, elemento) in enumerate(lista):
        if type(elemento) != list:
            if elemento == login or elemento == senha:
                return index
        else:
            posicaoUsuario = validaSenhaUsuario(elemento, login, senha)
    return posicaoUsuario

def alterarSenhaUsuario(lista):
    for elemento in lista:
        if type(elemento) == list:
            infoValidadas = alterarSenhaUsuario(elemento)
        else:
            if elemento == login:
                infoValidadas = True
            else:
                infoValidadas = False


ListaUser = [['huguinho', '12345'], ['luisinho', '2345'], ['zezinho', '1111'], ['lala', '12345'], ['lele', '2345'], ['lili', 'oi']]

login = 'luisinho'#input('Insira seu login: ')
senha = '2345'#input('Insira sua senha: ')

if validaSenhaUsuario(ListaUser, login, senha) == True:
    novaSenha = input('Insira a nova senha: ')
    if novaSenha == input('Por favor confirme a nova senha: '):
        a