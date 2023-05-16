#Crie um programa que faça o computador jogar Jokenpô com você.

from time import sleep
from random import randint
itens = ('Pedra','Papel','Tesoura')
computador = randint(0, 2)
opção = print('Suas opções: '
         '\033[32m\n[ 0 ] PEDRA'
         '\033[33m\n[ 1 ] PAPEL'
         '\033[34m\n[ 2 ] TESOURA')

jogador = int(input('\033[35mQual é sua jogada ? :'))

print('Jo')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!!')
sleep(1)


print('=='*12)
print ('Computador jogou {}'.format(itens[computador]))
print('Jogador jogou {}'.format(itens[jogador]))
print('=='*12)

if computador == 0:
    if jogador == 0:
        print ('EMPATE!')
    elif jogador == 1:
        print('JOGADOR VENCE!')
    elif jogador ==2:
        print('COMPUTADOR VENCEU!')
    else:
        print('\033[35mJOGADA INVALIDA!')
elif computador == 1:
        if jogador == 0:
            print('COMPUTADOR VENCE!')
        elif jogador == 1:
            print('EMPATE!')
        elif jogador == 2:
            print('JOGADOR VENCEU!!')
        else:
            print('\033[35mJOGADA INVALIDA!')
elif computador == 2:
        if jogador == 0:
            print('O JOGADOR VENCE!')
        elif jogador ==  1:
            print('O COMPUTADOR VENCE!')
        elif jogador == 2:
            print('EMPATE!')
        else:
            print('\033[35mJOGADA INVALIDA!')
