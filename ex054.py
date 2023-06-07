#Crie um programa que leia o ano de nascimento de sete pessoas. 
#No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.

import datetime

data_atual = datetime.datetime.now().year
pessoas_menores = 0
pessoas_maiores = 0

for c in range(1, 8):
    pessoa = int(input("Em que ano a {}ª pessoa nasceu? ".format(c)))
    idadecheck = data_atual - pessoa

    if idadecheck >= 18:
        pessoas_maiores += 1
    else:
        pessoas_menores += 1

print("\nQuantidade de pessoas menores de idade: {} ".format(pessoas_menores))
print("Quantidade de pessoas maiores de idade: {} ".format(pessoas_maiores))

    