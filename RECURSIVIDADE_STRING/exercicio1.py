
def repeteCaracteres(texto):
    if len(texto) == 0:
        return texto
    duplicaPrimeiro = texto[1:]*2
    duplicaResto = repeteCaracteres(texto[1:])
    return duplicaPrimeiro + duplicaResto


print(repeteCaracteres('pr'))