# Create a package calle utilidadescev with two internal modules called coin and data
# Transfer all the functions from ex 107, 108, 109 for the first package

from uteis.utilitiescev import coin

n = float(input("type the price: R$ "))
ti = int(input("type the tax up: "))
td = int(input("type the tax down: "))
coin.summary(n, ti, td)