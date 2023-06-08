#### Crie um programa que leia dois valores e mostre um menu na tela:
#[ 1 ] somar
#[ 2 ] multiplicar
#[ 3 ] maior
#[ 4 ] novos números
#[ 5 ] sair do programa
#Seu programa deverá realizar a operação solicitada em cada caso.

from time import sleep

primeiro = int(input('Digite o primeiro valor: '))
segundo = int(input("Digite o segundo valor: "))




while True:
    print('\033[34m================')
    print('ESCOLHA A OPÇÃO DESEJADA: '
        '\n[ 1 ] SOMAR '
        '\n[ 2 ] MULTIPLICAR '
        '\n[ 3 ] MAIOR \n'
        '[ 4 ] NOVOS NÚMEROS\n'
        '[ 5 ] sair do programa')
    print('\033[34m================')

    opção = int(input('Qual é sua opção ? : '))

    if opção == 1:
        soma = (primeiro+segundo)
        sleep(0.5)
       
        print('A soma entre {} e {} é: {}'.format(primeiro,segundo,soma))
        
    elif opção == 2:
        multiplicação = (primeiro * segundo)
        sleep(0.5)
        print('A multiplicação entre {} e {} é: {}'.format(primeiro,segundo,multiplicação))   
        
    elif opção == 3:
        maior = primeiro if primeiro > segundo else segundo
        sleep(0.5)
        print("Entre {} e {} o maior número digitado foi {} :".format(primeiro,segundo,maior))
        
    elif opção == 4:
        primeiro = int(input('Digite o primeiro valor:'))
        segundo = int(input('Digite o segundo valor: '))
    elif opção == 5:
        print('Programa encerrado.')
        break    
    else:
        print("Opção invalida digite novamente.")    
          