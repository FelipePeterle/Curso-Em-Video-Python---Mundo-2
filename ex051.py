#Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
#No final, mostre os 10 primeiros termos dessa progressão.

print('\033[34m='*20)
print('\033[31m10 TERMOS DE UMA PA')
print('\033[34m='*20)

Termo = int(input('Digite o primeiro termo da PA: '))
Razao = int(input('Digite a razão da PA: '))
decimo = Termo + (10-1) * Razao
for c in range (Termo,decimo+Razao,Razao):
    print ('{}'.format(c),end=' ')
print('Acabou')


