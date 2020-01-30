# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.
#
# Considerando o dolar a R$3.27

preço_do_dolar = 3.27
valor_em_reais = float(input('Digite o quanto dinheiro tem: R$'))
valor_em_dolares = valor_em_reais / preço_do_dolar

print('Com R${:.2f} você pode comprar US${:.2f}'.format(valor_em_reais, valor_em_dolares))
