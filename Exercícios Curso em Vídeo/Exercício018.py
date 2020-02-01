# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

from math import sin, cos, tan, pi, radians

angulo = float(input('Digite o ângulo que você deseja: '))
#angulo = angulo * pi / 180
anguloRad = radians(angulo)
seno = sin(anguloRad)
print('O ângulo de {} tem o SENO de {:.2f}'.format(angulo, seno))
cosseno = cos(anguloRad)
print('O ângulo de {} tem o COSSENO de {:.2f}'.format(angulo, cosseno))
tangente = tan(anguloRad)
print('O ângulo de {} tem o TANGENTE de {:.2f}'.format(angulo, tangente))
