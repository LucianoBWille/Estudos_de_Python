# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

medida = float(input('Digite uma distancia em metros: '))

print('\n{} km'.format(medida/1000))
print('{} hm'.format(medida/100))
print('{} dam'.format(medida/10))
print('{} dm'.format(medida*10))
print('{} cm'.format(medida*100))
print('{} mm'.format(medida*1000))
