# Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o
# nome dos alunos e escrevendo na tela o nome do escolhido.

from random import choice
alunos = []
primeiro = input('Primeiro aluno: ')
segundo = input('Segundo aluno: ')
terceiro = input('Terceiro aluno: ')
quarto = input('Quarto aluno: ')

alunos = [primeiro, segundo, terceiro, quarto]

print('O aluno escolhido foi {}'.format(choice(alunos)))
