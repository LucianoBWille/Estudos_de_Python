# Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
# - EQUILÁTERO: todos os lados iguais
# - ISÓSCELES: dois lados iguais, um diferente
# - ESCALENO: todos os lados diferentes

print('=' + '-=' * 12)
print('Analizador de Triângulos')
print('=' + '-=' * 12)

a = float(input('Primeiro segmento: '))
b = float(input('Segundo segmento: '))
c = float(input('Terceiro segmento: '))

if abs(b - c) < a < (b + c) and abs(a - c) < b < (a + c) and abs(a - b) < c < (a + b):
    print('Os segmentos PODEM FORMAR um triângulo ', end='')
    if a == b == c:
        print('EQUILÁTERO')
    elif a == b or a == c or b == c:
        print('ISÓSCELES')
    else:
        print('ESCALENO')
else:
    print('Os segmentos NÃO PODEM FORMAR um triângulo!')
