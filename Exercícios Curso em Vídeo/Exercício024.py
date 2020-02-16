# Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome "SANTO".

cidade = input('Em que cidade você nasceu? ').strip()
'''
local = cidade.lower().find('santo')

if local == 0:
    encontrado = True
else:
    encontrado = False

print(encontrado)
'''
print(cidade[:5].lower() == 'santo')
