#programa que calcule a soma entre todos os números ímpares multiplos de 3
#no intervalo de 1 até 500
print("programa que calcula todos os números ímpares múltiplos de 3 (até 500)")
print("+---" * 20)
inicio = input("aperte qualquer tecla para iniciar:" )
print("+---" * 20)
soma = 0
cont = 0
for counter in range(1,501,2):
    if counter % 3 == 0:
        print(counter, end=" ")
        cont = cont + 1
        soma = soma + counter
print(" ")
print("+---" * 20)
print("A soma de todos os {} valores é {}".format(cont,soma))
print(" ")
