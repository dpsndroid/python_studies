#programa que leia comprimento do cateto oposto e adjacente do triangulo retangulo
#calcule e mostre a hipotenusa
import math
catop = float(input("Qual é o comprimento do cateto oposto: "))
catad = float(input("Qual é o comprimento do cateto adjacente: "))
#cálculo manual
hipo = (catop ** 2 + catad **2) ** (1/2)
print("Calculo manual: A hipotenusa mede: {:.4f}".format(hipo))
#cálculo automático do python
hipo2 = math.hypot(catop, catad)
print("Cálculo python: A hipotenusa mede: {:.4f}".format(hipo2))

