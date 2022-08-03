print("+---" * 20)
print("ESTRUTURA DE REPETIÇÃO WHILE")
print("+---" * 20)
n = 1
while n < 101:
    print(n, end = " ")
    n += 1
print(" ")
print("+---" * 20)
continuar = "sim"
while continuar =="sim":
    valor = int(input("digite um valor: "))
    continuar = str(input("Quer continuar? "))
print("Obrigado pela sua colaboração")
print("+---" * 20)
n = 1
par = 0
impar = 0
while n != 0:
    n = int(input("digite um valor: "))
    if n != 0: #para não considerar o 0 na contagem
        if n % 2 ==0:
            par += 1
        else:
            impar += 1
print("Você digitou {} números pares e {} números ímpares".format(par, impar))
print("+---" * 20)
                
