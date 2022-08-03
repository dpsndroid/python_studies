#programa que leia o primeiro termo e a razão de uma progressão aritmética
#no final mostre os 10 primeiros termos da progressão
print("+---" * 20)
print("{:^40}".format("10 TERMOS DE UMA PROGRESSÃO ARITMÉTICA"))
print("+---" * 20)
termo = int(input("Primeiro termo: "))
razao = int(input("Razão: "))
decimo = termo + (11 - 1) * razao # para calcular até o décimo termo. está 11 pois elimina o último
print("+---" * 20)
for c in range(termo, decimo , razao):
    print("{}".format(c), end = " -> ")
print(" ")
print("+---" * 20)
print("ACABOU!")
