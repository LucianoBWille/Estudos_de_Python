# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo.
# Calcule e mostre o comprimento da hipotenusa.

from math import pow, sqrt, hypot

oposto = float(input('Comprimento do cateto oposto: '))
adjacente = float(input('Comprimento do cateto adjacente: '))

hipotenusa = (adjacente**2 + oposto**2)**0.5
print('A hipotenusa vai medir {:.2f}'.format(hipotenusa))

hipotenusa = sqrt(pow(adjacente, 2)+pow(oposto, 2))
print('A hipotenusa vai medir {:.2f}'.format(hipotenusa))

hipotenusa = hypot(oposto, adjacente)
print('A hipotenusa vai medir {:.2f}'.format(hipotenusa))
