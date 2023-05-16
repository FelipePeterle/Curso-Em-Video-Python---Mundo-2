#Escreva um programa para aprovar o empréstimo bancário para a compra de
#uma casa.  O programa vai perguntar o valor da casa,
#o salário do comprador e em quantos anos ele vai pagar.
#Calcule o valor da prestação mensal,sabendo que ela não pode exceder 30% do
#salario ou então o empréstimo será negado.

from time import sleep

valorcasa = float(input('Digite o valor da casa que você deseja comprar:'))
financ = float(input('Em quantos anos você pretende financiar ?: '))
valorsalario = float(input('Digite seu salário: '))

Calcprest1 = (financ*12)
Calprest2 = valorcasa/Calcprest1
Porcentagem = valorsalario*0.30

print('\033[33m' 'Processando dados, por favor espere...')
sleep(2)

if Calprest2 <= Porcentagem:
    print('Empréstimo aceito  !')
else:
    print ('Empréstimo negado !')

print('Para pagar uma casa de \033[31m{} em \033[34m{} anos a prestação será de R$\033[36m{:.2f}'.format(valorcasa,financ,Calprest2))


