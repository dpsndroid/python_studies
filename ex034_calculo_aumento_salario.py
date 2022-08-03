#programa que pergunte o salário e calcule o valor do aumento
#salários acima de R$1250,00 - 10% de aumento
#salário iguais ou inferiores - 15% de aumento
salario = float(input("Qual é o seu salário: "))
if salario > 1250:
    novo = salario + (salario /100 *10)
else:
    novo = salario + (salario /100 *15)

print("Você recebe R${:.2f} e seu novo salário é de R${:.2f}".format(salario,novo))
