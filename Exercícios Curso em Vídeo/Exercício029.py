# Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele
# foi multado. A multa vai custar R$7,00 por cada Km acima do limite.

velocidade = int(input('Qual é a velocidade atual do carro? '))
limite = 80

if velocidade > limite:
    multa = (velocidade - limite) * 7
    print('MULTADO! Você excedeu o limite permitido que é de {}Km/h'.format(limite))
    print('Você deve pagar uma multa de R${:.2f}!'.format(multa))
print('Tenha um bom dia! Dirija com segurança!')
