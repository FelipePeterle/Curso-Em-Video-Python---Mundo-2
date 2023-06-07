#Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. 
#No final do programa, mostre: a média de idade do grupo, qual é o nome do homem 
#mais velho e quantas mulheres têm menos de 20 anos.

somasidades = 0
médiaidade = 0
velho = 0
nomemaisvelho = ''
mulher20 = 0

for c in range(1,5):
    pessoas = print("-----{}ª Pessoa-----".format(c))
    nome = str(input("Nome: ")).strip()
    Idade = int(input("Idade: "))
    genero = str(input("Sexo [M/F]: ")).strip()
    somasidades += Idade
    if c == 1 and genero in "Mm":
        velho = Idade
        nomemaisvelho = nome
    if genero in "Mm" and Idade>velho:
        velho = Idade
        nomemaisvelho = nome
    if genero in 'Ff' and Idade < 20: 
        mulher20 += 1


médiaidade = somasidades/4

print("A média de idade do grupo é de {}" .format(médiaidade))
print("O homem mais velho tem {} anos e se chama {}".format(velho,nomemaisvelho))
print("Ao todos são {} mulheres com menos de 20 anos".format(mulher20))

