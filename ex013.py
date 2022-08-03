salario = float(input("Qual o salário do funcionário? R$ "))
percentual = float(input("Percentual de aumento: "))
novo = salario + (salario * percentual / 100)
print("Seu novo salário é de R$ {:.2f}".format(novo))
