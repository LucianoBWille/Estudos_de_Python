# Faça um programa que leia um ano qualquer e mostre se ele é bissexto.

from datetime import datetime

ano = int(input('Que ano quer analisar? Coleque 0 para analisar o ano atual: '))

if ano == 0:
    ano = datetime.now().year

if (ano % 4 == 0 and ano % 100 != 0) or ano % 400 == 0:
    print('O ano {} é \033[1;33mBISSEXTO\033[m'.format(ano))  # BISSEXTO em negrito e em amarelo
else:
    print('O ano {} \033[1;31mNÃO\033[m é \033[1;33mBISSEXTO\033[m'.format(ano))  # NÃO em negrito e em vermelho
