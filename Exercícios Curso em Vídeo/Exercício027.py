# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.

nome = input('Digite seu nome completo: ').strip().split()

print('Muito prazer em te conhecer!')
print('Seu primeiro nome é {}'.format(nome[0].capitalize()))
print('Seu último nome é {}'.format(nome[-1].capitalize()))
