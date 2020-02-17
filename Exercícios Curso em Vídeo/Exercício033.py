# Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
'''
numero = int(input('Primeiro valor:\t'))

menor = maior = numero

numero = int(input('Segundo valor:\t'))

if numero > maior:
    maior = numero
elif numero < menor:
    menor = numero

numero = int(input('Terceiro valor:\t'))

if numero > maior:
    maior = numero
elif numero < menor:
    menor = numero
'''
numeros = [int(input('Primeiro valor:\t')), int(input('Segundo valor:\t')), int(input('Terceiro valor:\t'))]
maior = max(numeros)
menor = min(numeros)

print('O menor valor digitado foi {}'.format(menor))
print('O maior valor digitado foi {}'.format(maior))
