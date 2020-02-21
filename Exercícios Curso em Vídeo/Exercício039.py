# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai se
# alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento. Seu programa
# também deverá mostrar o tempo que falta ou que passou do prazo.

from datetime import datetime

ano = int(input('Ano de nascimento: '))
atual = datetime.now().year

idade = atual - ano

diferença = 18 - idade

print('Quem nasceu em {} tem {} anos em {}.'.format(ano, idade, atual))

if diferença > 1:
    print('Ainda faltam {} anos para o alistamento.'.format(diferença))
    print('Seu alistamento será em {}.'.format(atual + diferença))
elif diferença == 1:
    print('Ainda falta {} ano para o alistamento.'.format(diferença))
    print('Seu alistamento será em {}.'.format(atual + diferença))
elif diferença == 0:
    print('Você deve se alistar IMEDIATAMENTE!')
elif diferença == -1:
    print('Você já deveria ter se alistado há {} ano.'.format(-diferença))
    print('Seu alistamento foi em {}.'.format(atual + diferença))
elif diferença < -1:
    print('Você já deveria ter se alistado há {} anos.'.format(-diferença))
    print('Seu alistamento foi em {}.'.format(atual + diferença))
