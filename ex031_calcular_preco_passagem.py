#programa que pergunte a distancia em km da viagem.
#calcule preço de passagem sendo 0.50 centavos por kilometro viagens até 200km
#0.45 centavos por kilometro para viagens acima de 200km
dist = float(input("Qual a distância da viagem: "))
print("Sua viagem possui {}km".format(dist))
valor1 = dist * 0.45
valor2 = dist * 0.50
if dist > 200:
    print("Sua passagem custa R${:.2f}".format(valor1))
else:
    print("Sua passagem custa R${:.2f}".format(valor2))
desc = valor1 - 20 if dist > 200 else valor2 - 10
print("Você ganhou um desconto e vai pagar só R${:.2f}".format(desc))

