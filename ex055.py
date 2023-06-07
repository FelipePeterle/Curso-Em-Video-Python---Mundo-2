#Faça um programa que leia o peso de cinco pessoas. 
#No final, mostre qual foi o maior e o menor peso lidos.

maior_peso = 0
menor_peso = 0

for c in range(1,6):
    pessoa = float(input("\033[36mDigite o peso da {}º pessoa: ".format(c)))
    if c == 1:
        maior_peso = pessoa
        menor_peso = pessoa
    else:
        if pessoa > maior_peso:   
            maior_peso = pessoa
        if pessoa < menor_peso:
            menor_peso = pessoa


print("O maior peso lido foi: {}".format(maior_peso))
print("O menor peso lido foi: {}".format(menor_peso))