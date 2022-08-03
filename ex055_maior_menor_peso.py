#programa que leia peso de 5 pessoas. mostrar qual foi o maior e o menor
print("+---" * 20)
pesomaior = 0
pesomenor = 100
for c in range(1,6):
    novopeso = float(input("Qual o peso da {}ª pessoa: ".format(c)))
    if novopeso > pesomaior:
        pesomaior = novopeso
    if novopeso < pesomenor:
        pesomenor = novopeso
print("+---" * 20)
print("O maior peso foi de {} kg e o menor peso foi de {} kg".format(pesomaior, pesomenor))
print("+---" * 20)

print("""

OUTRA FORMA

""")

print("+---" * 20)
pesomaior = 0
pesomenor = 0
for c in range(1,6):
    novopeso = float(input("Qual o peso da {}ª pessoa: ".format(c)))
    if c == 1:
        pesomaior = novopeso
        pesomenor = novopeso
    else:
        if novopeso > pesomaior:
            pesomaior = novopeso
        if novopeso < pesomenor:
            pesomenor = novopeso
print("+---" * 20)
print("O maior peso foi de {} kg e o menor peso foi de {} kg".format(pesomaior, pesomenor))
print("+---" * 20)
    
