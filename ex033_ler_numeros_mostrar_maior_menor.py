#programa que leia 3 números e mostre qual é o maior e o menor.
a = int(input("digite o primeiro número: "))
b = int(input("digite o segundo número: "))
c = int(input("digite o terceiro número: "))
#testando o menor valor
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c

print("O menor número digitado foi {}".format(menor))

maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c

print("O maior número digitado foi {}".format(maior))
