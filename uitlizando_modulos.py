import random
from math import sqrt, ceil, floor
num = int(input("digite um número: "))
raiz = sqrt(num)
print("A raiz de {} é {:.2f}".format(num,raiz))
print("raiz arredondada para cima: {}".format(ceil(raiz)))
print("raiz arredondada para baixo: {}".format(floor(raiz)))
          
numero = random.random()
numero1 = random.randint(1,10)
print(numero)
print(numero1)
