import math

def desTrianRet (tartaruga, cateto):
    tartaruga.fd(cateto)
    tartaruga.lt(135)
    tartaruga.fd((2*(cateto**2))**0.5)
    tartaruga.lt(135)
    tartaruga.fd(cateto)
    return

def desTrianRetPreenchido (tartaruga, cateto, corPreenchimento):
    tartaruga.fillcolor(corPreenchimento)
    tartaruga.begin_fill()
    desTrianRet(tartaruga,cateto)
    tartaruga.end_fill()
    return

def desLinha(tartaruga, largura, corPreenchimento, espessura):
    tartaruga.color(corPreenchimento)
    tartaruga.width(espessura)
    tartaruga.fd(largura)
    return

def desCirculo(tartaruga, raio, eixoX, eixoY, corPreenchimento, espessura):
    tartaruga.up()
    tartaruga.goto(eixoX, eixoY-raio)
    tartaruga.setheading(0)
    tartaruga.down()
    tartaruga.color(corPreenchimento)
    tartaruga.width(espessura)
    tartaruga.circle(raio)
    return

def desCirculoPreenchido(tartaruga, raio, eixoX, eixoY, corPreenchimento, espessura):   
    tartaruga.begin_fill()    
    desCirculo(tartaruga, raio, eixoX, eixoY, corPreenchimento, espessura)
    tartaruga.fillcolor(corPreenchimento)
    tartaruga.end_fill()
    return

def desRetangulo(tartaruga, comprimento, largura):
    tartaruga.fd(comprimento)
    tartaruga.lt(90)
    tartaruga.fd(largura)
    tartaruga.lt(90)
    tartaruga.fd(comprimento)
    tartaruga.lt(90)
    tartaruga.fd(largura)
    tartaruga.lt(90)
    return

def desRetanguloPreenchido(tartaruga, comprimento, largura, corPreenchimento):
    tartaruga.begin_fill()
    tartaruga.fillcolor(corPreenchimento)
    desRetangulo(tartaruga, comprimento, largura)
    tartaruga.end_fill()
    return

def desTrianEquilatero(tartaruga, comprimento):
    tartaruga.setheading(60)
    tartaruga.fd(comprimento)
    tartaruga.setheading(-60)
    tartaruga.fd(comprimento)
    tartaruga.setheading(180)
    tartaruga.fd(comprimento)
    return

def desTrianEquilateroPreenchido(tartaruga, lado, corPreenchimento):
    tartaruga.begin_fill()
    tartaruga.fillcolor(corPreenchimento)
    desTrianEquilatero(tartaruga, lado)
    tartaruga.end_fill()
    return

def areaRetangulo(base, altura):
    return (base*altura)

def perCirculo(raio):
    return 2*math.pi*raio

def areaCirculo(raio):
    return (math.pi)*(raio**2)

def hipotenusa(catetoadjacente, catetoOposto):
    return (catetoadjacente**2 + catetoOposto**2)**0.5
    
def perimetroTri(lado1, lado2, lado3):
    return lado1 + lado2 + lado3
    
def areaTriangulo(lado1, lado2, lado3):
    perimetro = perimetroTri(lado1, lado2, lado3)/2
    return perimetro * (perimetro-lado1)*(perimetro-lado2)*(perimetro-lado3)

def distEuclidiana(x1, y1, x2, y2):
    return ((x1- x2)**2 + (y1-y2)**2)**0.5

def escreveValor(tartaruga, valor, eixoX, eixoY):
    tartaruga.up()
    tartaruga.goto(eixoX, eixoY)
    tartaruga.down()
    tartaruga.write(valor)
    return    