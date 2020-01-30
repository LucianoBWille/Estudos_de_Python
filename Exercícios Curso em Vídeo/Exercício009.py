# Faça um programa que leia um número Inteiro qualquer e mostre na tela a sua tabuada.

valor = int(input('Digite um número para ver sua tabuada: '))

print('-' * 18)
for i in range(1,11):
    print('| {} x {:2}  = {:3} |'.format(valor,i,valor*i))
print('-' * 18)
