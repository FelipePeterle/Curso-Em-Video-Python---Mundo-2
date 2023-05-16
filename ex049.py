# Refaça o DESAFIO 009, mostrando a tabuada de um número que o
# usuário escolher, só que agora utilizando um laço for.

num = int(input('Digite um número para ver a tabuada: '))
for m in range (1,11):
    print('\033[31m{} \033[34mx \033[32m{} \033[36m= \033[33m{}'.format(num,m,num*m))

