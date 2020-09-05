#10) Uma rampa plana, de 36 m de comprimento, faz ângulo de 30° com o plano horizontal. Uma pessoa que
#sobe a rampa inteira eleva-se verticalmente quantos m?
import math

rampa = 36
angulo = 30

elevacao = math.sin(math.radians(angulo)) * rampa

print(elevacao)