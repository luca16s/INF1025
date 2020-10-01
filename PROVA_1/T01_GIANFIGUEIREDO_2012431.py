#Nome completo: GIAN LUCA DA SILVA FIGUEIREDO
#Matrícula PUC-Rio: 2012431
#Declaração de autoria: declaro que este documento foi produzido em sua totalidade por mim, sem consultas a outros alunos, professores ou qualquer outra pessoa.
import math
import turtle

def ladoQuadrado(perimetro):
    return perimetro/4

def diagonalQuadrado(comprimentoLado):
    return comprimentoLado * math.sqrt(2)

def CalculaHipotenusa(catetoOposto, catetoAdjacente):
    return math.sqrt(catetoAdjacente**2 + catetoOposto**2)

def desQuadrado(turtle, lado):
    turtle.fd(lado)
    turtle.rt(90)
    turtle.fd(lado)
    turtle.rt(90)
    turtle.fd(lado)
    turtle.rt(90)
    turtle.fd(lado)
    return

def desCirculo(turtle, raio, eixoX, eixoY, corCaneta, espessuraCaneta):
    turtle.pencolor(corCaneta)
    turtle.pensize(espessuraCaneta)
    turtle.up()
    turtle.goto(eixoX, eixoY)
    turtle.down()
    turtle.circle(raio)
    return

def desenhaTrianguloRetangulo(turtle, catetoAdjacente, catetoOposto, hipotenusa, corCaneta, espessuraCaneta):
    turtle.pencolor(corCaneta)
    turtle.pensize(espessuraCaneta)
    tartaruga.fd(catetoOposto)
    tartaruga.lt(135)
    tartaruga.fd(hipotenusa)
    tartaruga.lt(135)
    tartaruga.fd(catetoAdjacente)
    return

def movimentaTartaruga(turtle, eixoX, eixoY):
    turtle.up()
    turtle.goto(eixoX, eixoY)
    turtle.setheading(0)
    turtle.down()
    return

tartaruga = turtle.Turtle()
ladoQuadrado = ladoQuadrado(800)

movimentaTartaruga(tartaruga, 0, 0)
desCirculo(tartaruga, ladoQuadrado/2, 0, 0, 'black', 1)
movimentaTartaruga(tartaruga, -100, 200)
desQuadrado(tartaruga, ladoQuadrado)
movimentaTartaruga(tartaruga, 0, 0)
desenhaTrianguloRetangulo(tartaruga, ladoQuadrado/2, ladoQuadrado/2, CalculaHipotenusa(ladoQuadrado/2, ladoQuadrado/2), 'black', 1)