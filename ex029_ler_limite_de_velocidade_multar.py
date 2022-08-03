#programa que leia a velocidade de um carro. se passar de 80, mensagem de multado
#a multa custa 7 reais para cada km acima do limite
veloc = float(input("Velocidade do carro: "))
excesso = veloc - 80
multa = excesso * 7.00
if veloc > 80:
    print("MULTADO! EXCESSO DE VELOCIDADE: Você excedeu em {}km".format(excesso))
    print("Você deve pagar R$ {:.2f} de multa".format(multa))
else:
    print("Parabéns! A sua velocidade de {}km está dentro do limite permitido".format(veloc))
print("Tenha um bom dia!!!")
