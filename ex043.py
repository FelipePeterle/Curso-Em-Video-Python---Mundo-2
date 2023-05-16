#Desenvolva uma lógica que leia o peso e a altura de uma pessoa,
#calcule seu Índice de Massa Corporal (IMC) e mostre seu status,
#de acordo com a tabela abaixo:
#- IMC abaixo de 18,5: Abaixo do Peso
#- Entre 18,5 e 25: Peso Ideal
#- 25 até 30: Sobrepeso
#- 30 até 40: Obesidade
#- Acima de 40: Obesidade Mórbida

peso = float(input('Qual é seu peso ? (KG): '))
altura = float(input('Qual é sua altura ? (m) : '))

imc = (peso/altura**2)


print (' o IMC dessa pessoa é de: {:.1f}'.format(imc))

if imc <18.5:
    print ('Tome cuidado, você está abaixo do seu peso ideal.')
elif imc == 18.5 or imc <= 25:
    print ('Parabéns você está no seu peso ideal !')
elif imc == 25 or imc <= 30:
    print('Se cuide, você está sobrepeso.')
elif imc == 30 or imc <= 40:
    print ('Procure um médico você sofre de obesidade.')
elif imc>40:
    print ('Você está com obesidade mórbida.')

