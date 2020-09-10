#desRetangulo: Esta função recebe uma tartaruga, duas medidas de lado (comprimento e largura)
#e desenha um retângulo.

def desRetangulo(tartaruga, comprimento, largura):
    tartaruga.fd(comprimento)
    tartaruga.rt(90)
    tartaruga.fd(largura)
    tartaruga.rt(90)
    tartaruga.fd(comprimento)
    tartaruga.rt(90)
    tartaruga.fd(largura)
    return