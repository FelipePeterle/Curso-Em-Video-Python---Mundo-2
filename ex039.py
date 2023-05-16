#Faça um programa que leia o ano de nascimento de um jovem e informe,
#de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar,
#se é a hora exata de se alistar ou se já passou do tempo do alistamento.
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

from datetime import date
ano = date.today().year
idade = int(input('Digite seu ano de nascimento para mais \ninformações sobre seu alistamento:'))
calcidade = (ano - idade)

print ('Quem nasceu em {} tem {} anos em 2023.'.format(idade,calcidade))

if calcidade == 18:
    print('Você tem que se alistar IMEDIATAMENTE!')
elif calcidade<18:
    saldo = 18 - calcidade
    print ('Ainda faltam {} anos para o alistamento.'.format(saldo))
    calcano = ano + saldo
    print ('Seu alistamento será em {}'.format(calcano))

elif calcidade>18:
    saldo = calcidade - 18
    print ('Você já deveria ter se alistado há {} anos.'.format(saldo))
    calcano2 = ano - saldo
    print ('Seu alistamento foi em {}'.format(calcano2))
