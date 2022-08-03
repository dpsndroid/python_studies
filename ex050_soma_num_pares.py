#programa que leia 6 números inteiros e mostre soma apenas dos pares
#desconsiderar os impares
print("+---" * 20)
somap = 0
somai = 0
countp = 0
counti = 0 
for c in range(1,7):
    num = int(input("Digite o {}º valor: ".format(c)))
    if num % 2 == 0:
        somap = somap + num #já faz o somatório
        countp = countp + 1
    elif num % 2 != 0:
        somai = somai + num #já faz o somatório
        counti = counti + 1
print("+---" * 20)
print("A soma de todos os {} números pares é {}".format(countp,somap))
print("A soma de todos os {} números pares é {}".format(counti,somai))
