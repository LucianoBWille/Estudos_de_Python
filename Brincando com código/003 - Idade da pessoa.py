from datetime import date, datetime
print('=' * 28)
print('Calcular idade de uma pessoa'.upper())
print('=' * 28)
dia_nascimento = int(input('Dia: '))
mes_nascimento = int(input('Mês: '))
ano_nascimento = int(input('Ano: '))
'''
data_nascimento = ano_nascimento + '-' + mes_nascimento + '-' + dia_nascimento
data_nascimento = datetime.strptime(data_nascimento, '%Y-%m-%d')
dias = abs((datetime.today() - data_nascimento).days)
idade = dias // 365
'''
dia_atual = date.today().day
mes_atual = date.today().month
ano_atual = date.today().year

idade = ano_atual - ano_nascimento
if mes_atual < mes_nascimento:
    idade -= 1
elif dia_atual < dia_nascimento:
    idade -= 1

print('A pessoa tem {} ano(s) de idade'.format(idade))
