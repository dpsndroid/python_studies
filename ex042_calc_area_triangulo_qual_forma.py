#refazer desafio 35 dos triangulos e mostrar que tipo de triangulo
#é formado. equilátero todos os lados iguais. isósceles dois lados iguais
#escaleno todos os lados diferentes
r1 = float(input("primeira medida: "))
r2 = float(input("segunda medida: "))
r3 = float(input("terceira medida: "))
noway = False
print("+---" * 20)
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print("É possível formar um triângulo com essas medidas")
else:
    print("Não é possível formar um triângulo com essas medidas")
    noway = True
print("+---" * 20)
if r1 == r2 and r1 == r3:
    print("Você pode formar um triângulo equilátero")
elif r1 == r2 and r1 < r3 or r1 == r3 and r1 < r2 or r3 == r2 and r3 < r1:
    print("Você pode formar um triângulo isósceles")
elif r1 != r2 and r1 != r3 and r3 != r2:
    if noway == True:
        print("Medidas inválidas, tente novamente")
    else:
        print("Você pode formar um triângulo escaleno")
print("+---" * 20)