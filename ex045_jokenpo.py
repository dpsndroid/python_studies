#criar programa que jogue jokenpô.
import random
from time import sleep

print("{:=^50}".format(" VAMOS JOGAR JOKENPO? "))
print("+---" * 20)
print("[1] PEDRA    [2] PAPEL    [3] TESOURA")
print("+---" * 20)
print("Já escolhi um número aqui")
comp = random.randint(1,3)
pessoa = int(input("Sua vez! "))
print("JO")
sleep(1)
print("KEN")
sleep(1)
print("PO")
sleep(1)
if pessoa == 1 and comp == 3:
    print("Parabéns, você ganhou. Eu escolhi TESOURA")
elif pessoa == 1 and comp == 2:
    print("hahahah, eu ganhei. Eu escolhi PAPEL")
elif pessoa == 2 and comp == 1:
    print("Parabéns, você ganhou. Eu escolhi PEDRA")
elif pessoa == 2 and comp == 3:
    print("hahahah, eu ganhei. Eu escolhi TESOURA")
elif pessoa == 3 and comp == 2:
    print("Parabéns, você ganhou. Eu escolhi PAPEL")
elif pessoa == 3 and comp == 1:
    print("hahahah, eu ganhei. Eu escolhi PEDRA")
elif pessoa == comp:
    print("Deu empate!!!")
else:
    print("Digite um número válido")
print("+---" * 20)

print("OUTRA FORMA")

print("+---" * 20)
print("{:=^50}".format(" VAMOS JOGAR JOKENPO? "))
print("+---" * 20)
item = ("PEDRA","PAPEL","TESOURA")
sorteio = random.randint(0,2)
comp = item[sorteio]
pessoa = str(input("Escolha entre PEDRA, PAPEL OU TESOURA: ")).upper()
print(pessoa)
print("JO")
sleep(1)
print("KEN")
sleep(1)
print("PO")
sleep(1)

if pessoa == "PEDRA" and comp == "TESOURA":
    print("Parabéns, você ganhou. Eu escolhi TESOURA")
elif pessoa == "PEDRA" and comp == "PAPEL":
    print("hahahah, eu ganhei. Eu escolhi PAPEL")
elif pessoa == "PAPEL" and comp == "PEDRA":
    print("Parabéns, você ganhou. Eu escolhi PEDRA")
elif pessoa == "PAPEL" and comp == "TESOURA":
    print("hahahah, eu ganhei. Eu escolhi TESOURA")
elif pessoa == "TESOURA" and comp == "PAPEL":
    print("Parabéns, você ganhou. Eu escolhi PAPEL")
elif pessoa == "TESOURA" and comp == "PEDRA":
    print("hahahah, eu ganhei. Eu escolhi PEDRA")
elif pessoa == comp:
    print("Deu empate!!!")

print("+---" * 20)

    




