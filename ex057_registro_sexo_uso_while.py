#programa que leia sexo, só aceita M ou F. caso esteja errado, peça
#a digitação novamente
print("+---" * 20)
sexo = str(input("Digite o sexo: [M/F] ")).strip().upper()[0]
while sexo not in "MF":
    sexo = str(input("Digite um valor válido: ")).strip().upper()[0]
print("+---" * 20)
print("sexo {} registrado com sucesso".format(sexo))
print("Programa finalizado")
