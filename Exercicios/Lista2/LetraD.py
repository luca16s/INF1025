#desCirculo: Esta função recebe uma tartaruga, o raio, as coordenadas do centro (x,y), a cor e a
#espessura da caneta e desenha um circulo
def desCirculo(tartaruga, raio, eixoX, eixoY, corCaneta, espessuraCaneta):
    tartaruga.pencolor(corCaneta)
    tartaruga.pensize(espessuraCaneta)
    tartaruga.up()
    tartaruga.goto(eixoX, eixoY)
    tartaruga.down()
    tartaruga.circle(raio)
    return