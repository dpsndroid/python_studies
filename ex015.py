km = float(input("Quantos quilômetros percorridos: "))
dias = int(input("Quantos dias de aluguel: "))
diaria = 60
kmr = 0.15
valor = (dias * diaria) + (km * kmr)
print("Você percorreu {}Km, por {} dias.".format(km,dias))
print("O total a pagar pelo aluguel é de R$ {:.2f}".format(valor))
