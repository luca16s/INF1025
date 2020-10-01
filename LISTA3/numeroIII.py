import math

def CalculaAreaCirculo(raio):
    return math.pi*raio**2

def CalculaAreaQuadrado(lado):
    return lado**2

def CalculaAreaTriangulo(base, altura):
    return (base * altura) / 2

def CalculaCatetoOposto(catetoAdjacente, hipotenusa):
    return catetoAdjacente**2 / hipotenusa ** 2

inputUsuario = int(input('Insira o valor de A: '))

catetoAdjacente = inputUsuario/2
catetoOposto = CalculaCatetoOposto(catetoAdjacente, inputUsuario)

areaCirculo = CalculaAreaCirculo(inputUsuario/2)
areaQuadrado = CalculaAreaQuadrado(inputUsuario)
areaTriangulo = CalculaAreaTriangulo(catetoAdjacente, catetoOposto)

print(str(areaTriangulo+(areaQuadrado-areaCirculo)))