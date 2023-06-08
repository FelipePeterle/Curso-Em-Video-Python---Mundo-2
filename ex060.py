#Faça um programa que leia um número qualquer e mostre o seu fatorial.

import math

numero = int(input("Digite um número para calcular seu fatorial: "))

fatorial = (math.factorial(numero))

print('O fatorial do número digitado {} é: {}'.format(numero,fatorial))