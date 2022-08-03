#programa que leia ano de nascimento de 7 pessoas. mostre quantas são de menor
#quantas são maiores. maioridade 21 anos
import datetime
atual = datetime.date.today().year
totmaior = 0
totmenor = 0
print("+---" * 20)
for c in range(1,8):
    nasc = int(input("Em que ano a {}ª pessoa nasceu? ".format(c)))
    idade = atual - nasc
    if idade < 21:
        print("Essa pessoa é menor de idade. Tem {} anos".format(idade))
        totmenor = totmenor + 1
    elif idade >= 21:
        print("Essa pessoa é maior de idade Tem {} anos".format(idade))
        totmaior = totmaior + 1
print("+---" * 20)
print("Ao todo tivemos {} pessoas maiores de idade e {} pessoas menores de idade".format(totmaior, totmenor))

