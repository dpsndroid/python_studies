#programa que leia o comprimento de 3 retas e dizer se pode ou não formar um triangulo
print("+---" * 20)
r1 = float(input("Insira a medida da primeira reta: "))
r2 = float(input("Insira a medida da segunda reta: "))
r3 = float(input("Insira a medida da terceira reta: "))
print("+---" * 20)
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print("É possível formar um triângulo com essas medidas")
else:
    print("Não é possível formar um triângulo com essas medidas")

