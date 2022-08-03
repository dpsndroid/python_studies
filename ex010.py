real = float(input("Quantos reais você possui? R$ "))
dolar = real / 3.27
print("Você possui R${:.2f} reais".format(real))
print("Então pode comprar US${:.2f} dólares".format(dolar))
