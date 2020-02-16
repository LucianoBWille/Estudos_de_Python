# Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.

numero = input('Informe um número: ')
print('Analisando o número {}'.format(numero))
'''
numero = list(numero)
numero.insert(0, 0)
numero.insert(0, 0)
numero.insert(0, 0)
numero.insert(0, 0)
unidade = numero[-1]
print('Unidade: {}'.format(unidade))
dezena = numero[-2]
print('Dezena: {}'.format(dezena))
centena = numero[-3]
print('Centena: {}'.format(centena))
milhar = numero[-4]
print('Milhar: {}'.format(milhar))
'''
numero = int(numero)
unidade = numero // 1 % 10
print('Unidade: {}'.format(unidade))
dezena = numero // 10 % 10
print('Dezena: {}'.format(dezena))
centena = numero // 100 % 10
print('Centena: {}'.format(centena))
milhar = numero // 1000 % 10
print('Milhar: {}'.format(milhar))
