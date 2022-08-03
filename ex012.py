valor = float(input("Qual o preço do produto? R$ "))
desconto = float(input("Qual o desconto oferecido? "))
novo = valor - (valor * desconto / 100)
print("Seu preço com desconto agora custa R${:.2f}".format(novo))

