lista = [32,18,1,3,8,10,2,15,22,31,27,16,17,44,45,38,29,51,52,74,33,48]
lista.sort()
teste = []
nova = []
cont = 0

for i in lista:
    inicio = lista[cont-1]
    num = lista[cont]
    dist = (num - 1) == inicio
    if dist == True:
        if inicio not in teste:
            teste.append(inicio)
        if num not in teste:
            teste.append(num)
    elif dist == False:
        teste = []
        nova.append(teste)
    
    cont += 1

retirar = []  

try:
    while True:
        nova.remove(retirar)
except ValueError:
    pass

print(nova)
  
print("----------------------------------------------------")

# EXEMPLO DO SERGIO
import random
game  = [1, 3, 7, 10, 11, 12, 20 ,21, 28, 30, 31, 40, 45, 50, 51, 52, 53, 54, 58, 60]


def func_findseq(game):                                 # Encontra as sequencias - Melhorar essa função, não está ok ainda.
    game.sort()
    n = 0
    seq =set()
    game.append(0)
    i = 0
    while game[i] != 0:
        if game[i] != game[i+1]-1:                      
            pass
        else:
            seq.add(game[i])                          # Aqui eu uso conjunto (set) para retirar os repetidos.
            seq.add(game[i+1])        

        i +=1

    seq = list(seq)
    seq.sort()
    game.remove(game[-1])

    seq.append(0)                                   # Aqui eu conto as sequencias 
    for i in range(len(seq)-1):
        if  seq[i] != seq[i+1]-1:
            n +=1
    seq.remove(seq[-1])

    print(f'Número de sequencias é: {n}')
    return seq



seq = func_findseq(game)
print(seq)