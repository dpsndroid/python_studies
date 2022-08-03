#programa que faça o computador "pensar" um número inteiro entre 0 e 5 e o
#usuário deve tentar descobrir. o programa escreve se o usuário errou ou acertou
from time import sleep
from random import randint
computador = randint(0,5)# a máquina escolhe número aleatório
jogador = int(input("Vou pensar em um número de 0 a 5. Tente advinhar: "))
print("Processando.....")
sleep(5)#fará uma pausa em segundos
if jogador == computador:
    print("Parabéns!Você venceu.")
else:
    print("Ganhei! Eu pensei no nº {} e você escolheu o nº {}".format(computador,jogador))

