# adapt the code from exercise 107 with a function that shows the values
# with a monetary value format

import uteis.coin2

n = float(input("type the price: R$ "))
t = int(input("What is the tax: "))
print(f"The half of R$ {uteis.coin2.monetary(n)} is {uteis.coin2.monetary(uteis.coin2.half(n))}")
print(f"the double of R$ {uteis.coin2.monetary(n)} is {uteis.coin2.monetary(uteis.coin2.double(n))}")
print(f"With 10% more, the new price is {uteis.coin2.monetary(uteis.coin2.increase(n, t))}")
print(f"With 10% less, the new price is {uteis.coin2.monetary(uteis.coin2.decrease(n, t))}")