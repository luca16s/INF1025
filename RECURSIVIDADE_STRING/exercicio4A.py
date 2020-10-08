def mesclaTexto(texto1, texto2):
    if len(texto1) == 0 or len(texto2) == 0:
        return ''
    
    primeiraSequencia = texto1[0] + texto2[0]
    demaisSequencias = mesclaTexto(texto1[1:], texto2[1:])
    return primeiraSequencia + demaisSequencias

print(mesclaTexto('AB', 'CD'))