# create a module called coin.py with the functions increase(), decrease(),
# double(), half(). Make a program that imports this module and uses the functions

import uteis.coin

n = float(input("type the price: R$ "))
t = int(input("What is the tax: "))
print(f"The half of R$ {n} is R$ {uteis.coin.half(n):.2f}")
print(f"the double of R$ {n} is R$ {uteis.coin.double(n):.2f}")
print(f"With 10% more, the new price is R$ {uteis.coin.increase(n, t):.2f}")
print(f"With 10% less, the new price is R$ {uteis.coin.decrease(n, t):.2f}")