# Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.

numero = int(input('Me diga um número qualquer: '))
if numero % 2 == 0:
    print('O número {} é \033[1;34mPAR\033[m'.format(numero))       # \033[m é o codigo para estilizar o texto
else:                                                               # o numero 1 se refere a negrito
    print('O número {} é \033[1;34mÍMPAR\033[m'.format(numero))     # o número 34 é a cor azul para letra
