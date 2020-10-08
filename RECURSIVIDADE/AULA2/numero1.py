def contarAlgarimos(numero):
    if numero < 10:
        return 1
    else:
        prefixo=numero//10
        count = contarAlgarimos(prefixo)
        count += 1
        return count
    

print(contarAlgarimos(367780))