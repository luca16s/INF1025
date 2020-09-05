#11) Um pequeno, porém horrível, alienígena está no topo da Torre Eiffel (que tem 324 metros de altura) e
#ameaça destruir a cidade de Paris! Um agente da MIB está no nível do chão, a 54 metros da Torre Eiffel,
#mirando sua arma a laser no alienígena. Em que ângulo, em graus, o agente deve disparar o laser?

import math

altura = 324
comprimento = 54
angulo = math.atan2(altura, comprimento)

print(math.degrees(angulo))