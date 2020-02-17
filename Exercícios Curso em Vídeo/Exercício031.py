# Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50
# por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.

distancia = float(input('Qual é a distância da sua viagem? '))

if distancia <= 200:
    valor = distancia * 0.5
else:
    valor = distancia * 0.45

print('você está prestes a começar uma viajem de {}Km.'.format(distancia))
print('E o preço da sua passagem será R${:.2f}'.format(valor))
