def geraTermos(numero):
    if numero == 1:
        return numero
    if numero%2 == 0:
        print(str(numero))
        return geraTermos(numero/2)
    else:
        print(str(numero))
        return geraTermos(numero*3+1)

def geraTermosEComprCiclo(numero, count=0):
    if numero == 1:
        print(str(numero))
        count +=1
        return count
    if numero%2 == 0:
        print(str(numero))
        count +=1
        return geraTermosEComprCiclo(numero/2, count)
    else:
        print(str(numero))
        count +=1
        return geraTermosEComprCiclo(numero*3+1, count)

#print(str(geraTermos(22)))
print('A quantidade de iterações foi de: %s'%str(geraTermosEComprCiclo(22)))