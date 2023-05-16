#Crie um programa que leia duas notas de um aluno e calcule sua média,
# mostrando uma mensagem no final, de acordo com a média atingida:
# Média abaixo de 5.0: REPROVADO
# Média entre 5.0 e 6.9: RECUPERAÇÃO
# Média 7 ou superior: APROVADO

nota1 = float(input('Digite a primeira nota:'))
nota2 = float(input('Digite a segunda nota: '))

aritmetica = (nota1+nota2)/2

print ('Tirando {} e {} a média do aluno é: {}'.format(nota1,nota2,aritmetica))

if aritmetica >=7:
    print('O aluno está \033[32mAPROVADO! !')
elif aritmetica < 5:
    print('O aluno está \033[31mREPROVADO! !')
elif aritmetica >=5.0 and aritmetica <=6.9:
    print ('O aluno está de \033[36mRECUPERAÇÃO!')
