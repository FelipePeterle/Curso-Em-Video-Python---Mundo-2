#Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10. 
#Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites 
#foram necessários para vencer.

import random

print("===== Jogo da Adivinhação =====")
print("Adivinhe o número que estou pensando entre 0 e 10!")

numero_pensado = random.randint(0, 10)
tentativas = 0

while True:
    palpite = int(input("Digite seu palpite: "))
    tentativas += 1

    if palpite == numero_pensado:
        print("Parabéns! Você acertou!")
        break
    elif palpite < numero_pensado:
        print("O número pensado é maior. Tente novamente!")
    else:
        print("O número pensado é menor. Tente novamente!")

print('Você acertou em {}'.format(tentativas))

