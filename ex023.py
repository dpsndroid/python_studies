#faça um programa que leia um número de 0 a 9999 e mostre cada
#digito separado. Ex 1834  unidade 4 dezena 3 centena 8 milhar 1
num = int(input("Digite um número de 0 a 9999: "))
u = num //1 % 10
d = num //10 % 10
c = num //100 % 10
m = num //1000 % 10
print("O número escolhido foi {}".format(num))
print("A unidade deste número é {}".format(u))
print("A dezena deste número é {}".format(d))
print("A centena deste número é {}".format(c))
print("O milhar deste número é {}".format(m))
#de outra forma
print("De outra forma ......")
print("A unidade deste número é {}".format(num //1 % 10))
print("A dezena deste número é {}".format(num //10 % 10))
print("A centena deste número é {}".format(num //100 % 10))
print("O milhar deste número é {}".format(num //1000 % 10))

