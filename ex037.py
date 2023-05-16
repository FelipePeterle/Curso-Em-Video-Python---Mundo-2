#Escreva um programa que leia um número inteiro qualquer e peça
#para o usuário escolher qual será a base de conversão:
#1 para binário
#2 para octal
#3 para hexadecimal

num = int(input('Digite o número a ser convertido : '))

print('Escolha a base de conversão:'
      '\n[ 1 ] para Binário\n'
      '[ 2 ] para Octal\n'
      '[ 3 ] para hexadecimal\n''')
opção = int(input('Escolha sua opção: '))

if opção == 1:
    print('Seu número \033[33m{} convertido na base binária é: \033[31m{}'.format(num,(bin(num))))
elif opção == 2:
    print('Seu número \033[33m{} convertido na base Octal é: \033[31m{}'.format(num,(oct(num))))
elif opção == 3:
    print('Seu número \033[33m{} convertido na base Hexadecimal é \033[31m{}:'.format(num,(hex(num))))
else:
    print('Opção invalida, Por favor tente novamente.')
