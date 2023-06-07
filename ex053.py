# Crie um programa que leia uma frase 
#qualquer e diga se ela é um palíndromo, desconsiderando os espaços.

frase = str(input('Digite uma frase qualquer ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = junto[::-1]

print("O inverso de {} é {}".format(junto,inverso))

if inverso == junto:
    print("É palíndromo")
else:               
    print("NÃO É PALÍNDROMO!")