#Escreva um programa que leia dois números inteiros e compare-os.
#Mostrando na tela uma mensagem:
#- O primeiro valor é maior
#- O segundo valor é maior
#- Não existe valor maior, os dois são iguais

print('\033[33mOlá,este é um comparador de dois números inteiros.')
print('Por favor digite os números a serem comparados:\n')

n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))

if n1>n2:
    print('O primeiro valor é maior.')
elif n2>n1:
    print('O segundo valor é maior.')
elif n1 == n2:
    print('Não existe um valor maior ou menor, ambos são iguais.')
elif n2 == n1:
    print('Não existe um valor maior ou menor, ambos são iguais.')


