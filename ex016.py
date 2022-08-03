#programa que leia um número real e mostre a parte inteira
import math
num = float(input("digite um número real: "))
print("O número digitado foi {}, e sua porção inteira é {}".format(num,math.trunc(num)))
print("O número digitado foi {}, e sua porção inteira é {}".format(num,int(num)))               
