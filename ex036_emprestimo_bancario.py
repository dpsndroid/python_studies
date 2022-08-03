#programa para aprovar empréstimo bancário. pergunta o valor da casa
#o salário e em quantos anos vai pagar
#calcular valor da prestação mensal, não exceder 30% do salário ou será negado
casa = float(input("Qual o valor da casa: R$ "))
salario = float(input("Qual o seu salário: R$ "))
percent = salario / 100 * 30
anos = int(input("Em quantos anos pretende pagar: "))
prestacao = casa / (anos * 12)
print("+---" * 20)
print("O imóvel pretendido custa {:.2f}".format(casa))
print("O salário informado é de R$ {:.2f}".format(salario))
if percent < prestacao:
    print("Para pagamento em {} anos nestas condições, empréstimo negado".format(anos))
else:
    print("Para pagamento em \033[1m{}\033[m anos nestas condições, as parcelas serão de R$ \033[1m{:.2f}\033[m fixas".format(anos,prestacao))
print("+---" * 20)