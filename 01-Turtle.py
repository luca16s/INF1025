import os
import turtle

tortuga = turtle.Turtle()
def ResetarTartaruga(tartaruga):
    tartaruga.up()
    tartaruga.goto(0, 0)
    tartaruga.clear()
    tartaruga.down()
    return

def DesenharTartaruga(tartaruga, passos, angulo):
    tartaruga.left(angulo/2)
    tartaruga.fd(passos)
    tartaruga.left(angulo)
    tartaruga.fd(passos)
    tartaruga.left(angulo)
    tartaruga.fd(passos)
    tartaruga.left(angulo)
    tartaruga.fd(passos)
    tartaruga.left(angulo/2)
    return

# 1
tortuga.circle(100)
tortuga.up()
tortuga.goto(0, 50)
tortuga.down()
tortuga.circle(50)
# 1
ResetarTartaruga(tortuga)
# 2
tortuga.circle(100)
tortuga.up()
tortuga.goto(200, 0)
tortuga.down()
tortuga.circle(100)
# 2
ResetarTartaruga(tortuga)
# 3
DesenharTartaruga(tortuga, 100, 90)
tortuga.up()
tortuga.fd(100)
tortuga.down()
DesenharTartaruga(tortuga, 100, 90)
# 3
ResetarTartaruga(tortuga)
# 4
tortuga.right(60)
tortuga.fd(100)
tortuga.right(120)
tortuga.fd(100)
tortuga.left(-120)
tortuga.fd(100)
# 4