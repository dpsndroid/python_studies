#Listas - parte 1
num = [2,5,9,1]
print(num)
local = num.index(9)
print(local)
num.sort() #coloca em ordem
print(num)
num.sort(reverse = True)
print(num)
num[2] = 0 #adciona 0 na posição 2
print(num)
num.append(7) #adiciona no final da lista
print(num)
num.sort(reverse=True) #organiza e coloca a ordem inversa
print(num)
print(len(num)) #comprimento da lista
num.insert(2,3) #insere 3 na posição 2
print(num)
num.pop() #retira o último item da lista
print(num)
num.pop(3) #retira o 4º item da lista
print(num)
num.insert(2,3)
print(num)
num.remove(3)
print(num)
if 8 in num:
    num.remove(8)
else:
    print("não achei")
print("====" * 20)
valores = []
valores.append(5)
valores.append(9)
valores.append(4)
print(valores)
for v in valores:
    print(v, end = " ")
print(" ")

for c in range(0,6):
    valores.append(int(input("digite valor: ")))
for c, v in enumerate(valores):
    print(f"posição {c} encontra valor {v}")
a = [2,3,4,7]
b = a # é como cópia, mas na verdade é uma ligação. um altera o outro
print(a)
print(b)
b = a[:] #copia apenas os elementos, então pode alterar sozinha
b[2] = 8
print(a)
print(b)
nova = [10,20,30,40,50,60,70]
del nova[2:]
print(nova)

