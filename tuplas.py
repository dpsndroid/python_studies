#Variáveis compostas
#tuplas são imutáveis
lanche = ("hamburguer","suco","pizza","pudim","batata frita")
janta = ("arroz","feijão","suco","pizza","filé")
pessoa = ("Daniel",45,"M",1.83,85)
testeparadeletar = (1,2,3,4,5)
del(testeparadeletar) #deleta a variável tupla por completo
print("====" * 20)
print("{:^40}".format("TUPLAS"))
print("====" * 20)
print(lanche) #exibe os itens da tupla
print(janta) #exibe os itens da tupla
print(pessoa) #exibe os itens da tupla
print(lanche[1]) #exibe o segundo item da tupla
print(lanche[0]) #exibe o primeiro item da tupla
print(lanche[3]) #exibe o quarto item da tupla
print(lanche[2]) #exibe o terceiro item da tupla

print("====" * 20)

print(lanche[-2]) #exibe o segundo item de trás p frente da tupla
print(lanche[1:3]) #exibe o segundo e o terceiro item da tupla
print(lanche[2:]) #exibe do segundo item da tupla até o fim
print(lanche[:2]) #exibe do início até o segundo item da tupla
print(lanche[-3:]) #exibe os três últimos itens da tupla 
print(lanche[:-3]) #exibe a tupla menos os três últimos itens
print(len(lanche)) #exibe o comprimento da tupla, quantidade de posições ocupadas
print(sorted(lanche)) #ordena a tupla, em ordem crescente de números ou ordem alfabética de letras

print("====" * 20)

nova = lanche + janta
print(nova)

novab = janta + lanche
print(novab)

print(novab.count("pizza")) #exibe quantas vezes o item está presente na tupla
print(novab.index("pizza")) #exibe em que posição o item está presente na tupla

print("====" * 20)

for c in nova:
    print(c, end = "  ")
print(" ")

print("====" * 20)

for c in lanche:
    print(f"Eu vou comer {c}")
print("Tô cheio!!!")

print("====" * 20)

for counter in range(0, len(lanche)):
    print(lanche[counter])

print("====" * 20)

for counter in range(0, len(lanche)):
    print(f"Eu vou comer {lanche[counter]} na posição {counter}")

print("====" * 20)

for comida in lanche:
    print(f"Eu vou comer {comida}")

print("====" * 20)

for pos, comida in enumerate(lanche):
    print(f"Eu vou comer {comida} em posição {pos}")

print("====" * 20)

lanche[1] = "Refrigerante" #vai dar erro, não permite na tupla
