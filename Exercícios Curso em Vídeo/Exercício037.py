# Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de
# conversão: 1 para binário, 2 para octal e 3 para hexadecimal.

numero = int(input('Digite um número inteiro: '))
print('''Escolha uma das bases para conversão:
[ 1 ] converter para BINÁRIO
[ 2 ] converter para OCTAL
[ 3 ] converter para HEXADECIMAL''')
op = int(input('Sua opção: '))
if op == 1:
    print('{} convertendo para BUNÁRIO é igual a {}'.format(numero, bin(numero)[2:]))
elif op == 2:
    print('{} convertendo para OCTAL é igual a {}'.format(numero, oct(numero)[2:]))
elif op == 3:
    print('{} convertendo para HEXADECIMAL é igual a {}'.format(numero, hex(numero)[2:]))
else:
    print('Opção INVÁLIDA!')
