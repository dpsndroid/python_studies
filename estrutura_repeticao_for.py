#laços de repetição - parte 1
for c in range(0,6):
    print("oi")
print("fim")
print("+---" * 20)
for z in range(0,6):
    print(z)
print("fim")
print("+---" * 20)
for z in range(6,0,-1):
    print(z)
print("fim")
print("+---" * 20)
for z in range(0,9,2):
    print(z)
print("fim")
print("+---" * 20)
n = int(input("Digite um número: "))
for c in range(0,n):
    print(c)
print("fim")
print("+---" * 20)    
n = int(input("Digite um número: "))
for c in range(0,n+1):
    print(c)
print("fim")
print("+---" * 20)
inicio = int(input("inicio: "))
fim = int(input("fim: "))
passo = int(input("passo: "))
for c in range(inicio,fim+1,passo):
    print(c)
print("fim")
print("+---" * 20)
s = 0
for c in range(0,4):
    n = int(input("digite um valor: "))
    s = s + n
print("O somatório de todos os valores foi {}".format(s))
