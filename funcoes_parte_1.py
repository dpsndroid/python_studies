#Funções - parte 1

def sline():
    print("----" * 20) #função sem parâmetro
sline()
print("Hello")
sline()
print("what the hell!!")
sline()


def message(msg):
    print("----------") #função com parâmetro
    print(msg)
    print("Do you want some cake?")
    print("----------")
message("who I am")
message("Abracadabra")
message("Pacatatucotianão")
message("I think i am going to start to understand")

sline()

def continha(a,b,c,d):
    res = (a + b + c) * d
    print(res)

continha(1, 2, 3, 4)
continha(4, 3, 2, 1)
continha(a=10, b=20, c=15, d=7)

sline()

def nome(m1,m2):
    print(f"pensei que {m1} fosse primo de {m2}")
nome("andre","joca")

sline()

def contador(*num):  #asterisco desempacota e cria uma tupla
    for valor in num:  #pode fazer tudo que faria com a tupla
        print(valor, end = " ")
    print()
contador(1,2,3)
contador(4,5,6)
contador(7,8,9)


def dobra(lst):    
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos +=1


valores = [7,6,5,8,2,1]
dobra(valores)
print(valores)

sline()


def soma2(* valores):
    s = 0
    for c in valores:
        s += c
    print(f"A soma dos valores é {s}")

soma2(2,3)
soma2(7,8,9,4)
soma2(1,1,1,1)


