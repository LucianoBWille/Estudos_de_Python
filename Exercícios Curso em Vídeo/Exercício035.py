# Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.

print('=' + '-=' * 12)
print('Analizador de Triângulos')
print('=' + '-=' * 12)

a = float(input('Primeiro segmento: '))
b = float(input('Segundo segmento: '))
c = float(input('Terceiro segmento: '))

if abs(b - c) < a < (b + c) and abs(a - c) < b < (a + c) and abs(a - b) < c < (a + b):
    print('Os segmentos PODEM FORMAR um triângulo!')
else:
    print('Os segmentos NÃO PODEM FORMAR um triângulo!')
