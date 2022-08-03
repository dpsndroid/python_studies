#programa que leia ano de nascimento do atleta e mostre sua categoria
#até 9 mirim, até 14 infantil, até 19 junior, até 20 senior, acima master
from datetime import date
anonasc = int(input("Qual o seu ano de nascimento: "))
hoje = date.today().year
idade = hoje - anonasc
print("+---" * 20)
if idade <= 9:
    print("Você tem {} anos e sua categoria é \033[1mMirim\033[m".format(idade))
elif idade > 9 and idade <= 14:
    print("Você tem {} anos e sua categoria é \033[1mInfantil\033[m".format(idade))
elif idade > 15 and idade <= 19:
    print("Você tem {} anos e sua categoria é \033[1mJunior\033[m".format(idade))
elif idade == 20:
    print("Você tem {} anos e sua categoria é \033[1mMaster\033[m".format(idade))
elif idade > 20:
    print("Você tem {} anos e sua categoria é \033[1mSenior\033[m".format(idade))
print("+---" * 20)