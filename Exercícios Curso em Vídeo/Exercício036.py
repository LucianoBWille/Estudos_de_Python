# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, o
# salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salário ou
# então o empréstimo será negado.

casa = float(input('Valor da casa: R$ '))
salario = float(input('Salário do comprador: R$ '))
anos = int(input('Qunntos anos de financiamento? '))
meses = anos * 12
parcela = casa / meses
print('Para pagar o empréstimo de R${:.2f} em {} anos a prestação será de R${:.2f}'.format(casa, anos, parcela))
if parcela > salario * 0.3:
    print('Empréstimo NEGADO!')
else:
    print('Empréstimo pode ser CONCEDIDO!')
