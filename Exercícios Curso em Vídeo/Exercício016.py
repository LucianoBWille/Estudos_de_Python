# Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.

num = float(input('Digite um valor: '))

from math import trunc
print('O valor digitado foi {} e sua parte inteira é {}'.format(num, trunc(num)))

print('O valor digitado foi {} e sua parte inteira é {}'.format(num, int(num)))
