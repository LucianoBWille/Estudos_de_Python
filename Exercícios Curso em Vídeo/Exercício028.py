# Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar
# descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.

from random import randint
#from time import sleep

valor = randint(0, 5)
print('Vou pensar em um número de 0 a 5. Tente adivinhar...')
palpite = int(input('Em que número eu pensei? '))

#print('PROCESSANDO...')
#sleep(1)

if palpite == valor:
    print('PARABÉNS! Você conseguiu vencer!')
else:
    print('GANHEI! Eu pensei no número {} e não no {}!'.format(valor, palpite))