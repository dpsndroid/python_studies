#programa que leia número inteiro e diga se é número primo
print("+---" * 20)
print("Números Primos")
print("+---" * 20)
tot = 0 
num = int(input("Digite um número para saber se é primo: "))
for c in range(1, num + 1):
    if num % c == 0:
        print("{:2} <<<".format( c ))
        tot = tot + 1
    else:
        print("{:2}".format( c ))   
print("+---" * 20)
print("O número {} foi divisível {} vezes.".format( num , tot ))
if tot == 2:
    print("Por isso ele é primo.")
else:
    print("Por isso ele não é primo.")
print("+---" * 20)
