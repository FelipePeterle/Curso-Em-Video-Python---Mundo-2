#Refaça o DESAFIO 035 dos triângulos, acrescentando o
#recurso de mostrar que tipo de triângulo será formado:

#EQUILÁTERO: todos os lados iguais

#ISÓSCELES: dois lados iguais, um diferente

#ESCALENO: todos os lados diferentes


print ('-=-=-='*8)
print ('Analisador de Triãngulos')
print ('-=-=-='*8)

lado1 =(float(input('Digite o primeiro lado do triângulo: ')))
lado2 = (float(input('Digite o segundo lado do triângulo: ')))
base = (float(input('Digite o base lado do triângulo: ')))

if lado1 == lado2 and lado1 == base and lado2 == base:
    print ('Os segmentos acima \033[32mPODEM formar um triângulo \033[33mEQUILÁTERO.')
elif lado1 == lado2 or lado2 == lado1 or lado1 == base or lado2 == base:
    print('Os segmentos acima \033[32mPODEM formar um triângulo \033[33mISÓSCELES.')
elif lado1!=lado2 and lado2!=lado1 and lado1!=base and lado2!=base:
    print('Os segmentos acima \033[32mPODEM formar um triângulo \033[33mESCALENO.')

