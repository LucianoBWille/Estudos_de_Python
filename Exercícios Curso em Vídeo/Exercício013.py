# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

percentual_de_aumento = 15

salario_atual = float(input('Qual o salário do funcionário? R$'))
salario_com_aumento = salario_atual * (1 + percentual_de_aumento / 100)

print('Um funcionário que ganhava R${:.2f}, com {}% de aumento, passa a receber R${:.2f}'.format(salario_atual, percentual_de_aumento, salario_com_aumento))
