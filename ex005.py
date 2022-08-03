nome = input("Qual é o seu nome? ")
print("Prazer em te conhecer {}".format(nome))
print("Prazer em te conhecer {:20}".format(nome))
print("Prazer em te conhecer {:<20}".format(nome))
print("Prazer em te conhecer {:>20}".format(nome))
print("Prazer em te conhecer {:^20}".format(nome))
print("Prazer em te conhecer {:=^20}".format(nome))
n1 = 2
n2 = 3
print("A soma vale {:3f}".format(n1+n2), end="\n>>>>> ")

num = int(input("digite um número: "))
print("O número é: {}".format(num))
print("Seu antecessor é: {}".format(num-1))
print("Seu sucessor é: {}".format(num+1))
