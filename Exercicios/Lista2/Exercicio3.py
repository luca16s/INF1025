import math
from funcBase.funcBase import areaTriangulo
from funcBase.funcBase import areaCirculo, areaRetangulo
from funcBase.funcBase import escreveValor
from funcBase.funcBase import desLinha
from funcBase.funcBase import desCirculoPreenchido
from funcBase.funcBase import desRetangulo
from funcBase.funcBase import desTrianRet
from funcBase.funcBase import desTrianRetPreenchido
from funcBase.funcBase import desRetanguloPreenchido
from funcBase.funcBase import hipotenusa
import turtle

def movimentaTartaruga(tartaruga, eixoX, eixoY):
    tartaruga.up()
    tartaruga.goto(eixoX, eixoY)
    tartaruga.setheading(0)
    tartaruga.down()
    return

def ResetarTartaruga(tartaruga):
    tartaruga.up()
    tartaruga.goto(0, 0)
    tartaruga.clear()
    tartaruga.down()
    return

tortuga = turtle.Turtle()

desRetanguloPreenchido(tortuga, 30, 20, "yellow")
movimentaTartaruga(tortuga, 0, -30)
desRetanguloPreenchido(tortuga, 100, 30, "blue")
movimentaTartaruga(tortuga, 80, 0)
desRetanguloPreenchido(tortuga, 20, 60, "green")
areaTotal = areaRetangulo(30, 20) + areaRetangulo(100, 30) + areaRetangulo(20, 60)
escreveValor(tortuga, areaTotal, -150, 150)

ResetarTartaruga(tortuga)

tortuga.setheading(180)
movimentaTartaruga(tortuga, -30, 0)
desTrianRetPreenchido(tortuga, 30, "purple")
tortuga.setheading(0)
movimentaTartaruga(tortuga, -30, -40)
desRetanguloPreenchido(tortuga, 60, 40, "orange")
movimentaTartaruga(tortuga, 30, -40)
desRetanguloPreenchido(tortuga, 50, 20, "pink")
areaTotal = areaRetangulo(4, 6) + areaRetangulo(100, 30) + areaTriangulo(3, 3, hipotenusa(3, 3))
escreveValor(tortuga, areaTotal, -150, 150)

ResetarTartaruga(tortuga)

raio = 20
desCirculoPreenchido(tortuga, raio, 0, 0, "gray", 0)
movimentaTartaruga(tortuga, 0, 0)
tortuga.setheading(45)
desLinha(tortuga, raio, "black", 1)
movimentaTartaruga(tortuga, -20, -30)
desRetanguloPreenchido(tortuga, 40, 30, "white")
tortuga.setheading(35)
desLinha(tortuga, 50, "black", 1)
cateto = math.sqrt(5**2 - 3**2)
areaTotal = areaTriangulo(5, 3, cateto) + (areaCirculo(cateto/2)/2)
escreveValor(tortuga, areaTotal, -150, 150)
