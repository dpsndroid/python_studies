# Add to module coin.py, a function called summary(), that shows informations
# of the functions already created

import uteis.coin4

n = float(input("type the price: R$ "))
ti = int(input("type the tax up: "))
td = int(input("type the tax down: "))
uteis.coin4.summary(n, ti, td)
