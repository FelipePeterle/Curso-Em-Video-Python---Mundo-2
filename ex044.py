###Elabore um programa que calcule o valor a ser pago por um produto,
#considerando o seu preço normal e condição de pagamento:
# à vista dinheiro/cheque: 10% de desconto
#- à vista no cartão: 5% de desconto
#- em até 2x no cartão: preço formal
#- 3x ou mais no cartão: 20% de juros

print('\033[34m========LOJAS SHELBY COMPANY========')

Compras = float(input('Digite o preço das compras: R$'))
print('FORMAS DE PAGAMENTO: '
      '\n[ 1 ] Á VISTA DINHEIRO/CHEQUE'
      '\n[ 2 ] A VISTA NO CARTÃO'
      '\n[ 3 ] 2X NO CARTÃO\n'
      '[ 4 ] 3X OU MAIS NO CARTÃO\n')

opção = int(input('Qual é sua opção ? : '))

if opção == 1:
    desconto = Compras - (Compras * 10/100)
    print ('Sua compra de R${:.2f} vai custar R$ {:.2f} no final.'.format(Compras,desconto))
if opção == 2:
    desconto = Compras - (Compras * 5 / 100)
    print ('Sua compra de R${:.2f} vai custar R${:.2f} no final.' .format(Compras,desconto))
if opção == 3:
    desconto = (Compras/2)
    print('Sua compra de R${:.2f} vai custar R${:.2f} em um total de 2 parcelas.'.format(Compras, desconto))
if opção == 4:
    parcelas = int (input('Quantas parcelas ? :'))
    juros = Compras + (Compras * 20/100)
    divisão = juros/10
    print('Sua compra será parcelada em {}x de RS${} COM JUROS.'.format(parcelas,divisão))
    print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(Compras,juros))
if opção == 5:
    print('Opção invalida tente novamente !')
