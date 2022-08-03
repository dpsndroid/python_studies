#programa que leia ano de nascimento e informe se ainda vai se alistar
#no serviço militar. se é a hora de se alistar. se já passou o tempo de alistamento
#também deve mostrar o tempo que falta ou o tempo que já passou
from datetime import date
anonasc = int(input("Qual o seu ano de nascimento: "))
hoje = date.today().year
idade = hoje - anonasc
if idade == 18:
    print("Você completou 18 anos. Está na hora de você se alistar no serviço militar")
elif idade > 18:
    print("Você completou 18 anos em {}".format(anonasc + 18))
    print("Se você ainda não se alistou, está atrasado {} anos".format(idade - 18))
    print("Você deveria ter se alistado em {}".format(anonasc + 18))
elif idade < 18:
    print("Você completa 18 anos em {}".format(anonasc + 18))
    print("Está próximo do seu alistamento. Falta(m) {} anos(s)".format(18 - idade))
    print("Seu alistamento será em {}".format(anonasc + 18))
