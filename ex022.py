#criar programa que leia nome completo e mostre nome com todas as maiusculas
#todas as minusculas, quantas letras tem ao todo sem espaços
#quantas letras o primeiro nome
nome = str(input("Digite seu nome completo: "))
print("Seu nome em maiúsculas é {}".format(nome.upper()))
print("Seu nome em minúsculas é {}".format(nome.lower()))
print("Esse nome tem ao todo {} letras".format(len(nome) - nome.count(" ")))
print("Seu primeiro nome tem {} letras".format(nome.find(" ")))
separa = nome.split()
print(separa)
print(separa[1])
print("Seu segundo nome é {} e ele tem {} letras".format(separa[1],len(separa[1])))
