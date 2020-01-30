# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos
# quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

dias = int(input('Quantos dias alugados? '))
km_rodados = int(input('Quantos Km rodados? '))

custo_dia = 60
custo_km = 0.15

valor_a_pagar = custo_dia * dias + custo_km * km_rodados

print('O total a pagar é de R${:.2f}'.format(valor_a_pagar))
