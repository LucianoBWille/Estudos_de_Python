# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

valor_original = float(input('Qual é o valor do produto? R$'))

percentual_de_desconto = 5

valor_com_desconto: float = valor_original * (1 - percentual_de_desconto/100)

print('O produto que custava R${:.2f}, na promoção com desconto de {}% vai custar R${:.2f}'.format(valor_original, percentual_de_desconto, valor_com_desconto))
