#programa que leia o nome e diga se ela tem silva no nome
nome = str(input("Digite seu nome completo: ")).strip()
print("Seu nome tem Silva? {}".format("silva" in nome.lower()))
