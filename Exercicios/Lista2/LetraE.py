#desCirculoPreenchido: : Esta função recebe uma tartaruga, as coordenadas do centro (x,y), o raio,
#a cor e a espessura da caneta e desenha um círculo preenchido
from LetraD import desCirculo

def desCirculoPreenchido(tartaruga, eixoX, eixoY, raio, corCaneta, espessuraCaneta):
    tartaruga.pencolor = corCaneta
    tartaruga.pensize = espessuraCaneta
    tartaruga.fillcolor = corCaneta
    tartaruga.begin_fill()
    desCirculo(tartaruga, raio, eixoX, eixoY, corCaneta, espessuraCaneta)
    tartaruga.end_fill()
    return