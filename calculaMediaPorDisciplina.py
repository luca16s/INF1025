def ehINF(cod):
    return cod[:3]=='INF'

def calcMedPond(n1,p1,n2,p2):
    return (n1*p1+n2*p2)/(p1+p2)

def calcMedDisc(cod, n1, n2):
    if ehINF(cod):
        media = calcMedPond(n1, 3, n2, 5)
    else:
        media = calcMedPond(n1, 2, n2, 8)
    return media

cod=input("Qual o código da disciplina?")
n1=float(input("Nota 1?"))
n2=float(input("Nota 2?"))
media=calcMedDisc(cod,n1,n2)
print("Sua media:%.2f"%media)
if media>8.5 and (n1>9 or n2>9):
   print("Você quer ser monitor?") 
