def temVogal(texto):
    if len(texto) == 0:
        return False

    if texto[0] in 'aeiouAEIOU':
        return True
        
    return temVogal(texto[1:])

print(temVogal('bcde'))