#escreva um programa que leia um número inteiro e mostre os
#elementos de uma sequência de fibonacci

term = int(input("type an integer number: "))
n1 = 0
n2 = 1
c = 3
print("{} - {}".format(n1,n2), end = " ")
while c <= term:
    n3 = n1 + n2
    print(" - {}".format(n3), end = " ")
    n1 = n2
    n2 = n3
    c += 1
print("")
print("it's done")
