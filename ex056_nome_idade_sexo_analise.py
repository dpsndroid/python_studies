#programa que leia nome, idade e sexo de 4 pessoas e mostre.
#média de idade do grupo, nome do homem mais velho e quantas mulheres com
#menos de 20 anos
print("+---" * 20)
idade = 0
idade2 = 0
media = 0
nome = ""
totmulher = 0
for c in range(1,5):
    nome1 = str(input("Digite o nome da {}ª pessoa: ".format(c)))
    idade1 = int(input("Digite a idade da {}ª pessoa: ".format(c)))
    sexo = str(input("Digite o sexo da {}ª pessoa(m ou f): ".format(c)))
    print("+---" * 10)
    idade = idade + idade1
    if idade1 > idade2 and sexo in "Mm":  #observe o in "Mn", considera tudo dentro
        nome = nome1
        idade2 = idade1
    if sexo in "Ff" and idade1 < 20:
        totmulher += 1
media = idade / 4        
print("A média de idade do grupo é {} anos".format(int(media)))
print("O nome do homem mais velho é {}".format(nome))
print("Neste grupo existe(m) {} mulher(es) com menos de 20 anos".format(totmulher))
print("+---" * 20)
