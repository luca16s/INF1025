#desRetanguloPreenchido: Esta função recebe uma tartaruga, duas medidas de lado (comprimento
#e largura) e a cor de preenchimento e desenha um retângulo preenchido com a cor
from LetraF import desRetangulo
import turtle

def desRetanguloPreenchido(tartaruga, comprimento, largura, corPreenchimento):
    tartaruga.begin_fill()
    tartaruga.fillcolor(corPreenchimento)
    desRetangulo(tartaruga, comprimento, largura)
    tartaruga.end_fill()
    return

desRetanguloPreenchido(turtle.Turtle(), 50, 40, 'cyan')
