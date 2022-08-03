# change the functions created on ex 107 to accept one more parameter
# tell if the value is going to be or not formated by the function coin()
# created on exercise 108

import uteis.coin3

n = float(input("type the price: R$ "))
t = int(input("What is the tax: "))
print(f"The half of R$ {uteis.coin3.monetary(n)} is {uteis.coin3.half(n, True)}")
print(f"the double of R$ {uteis.coin3.monetary(n)} is {uteis.coin3.double(n, True)}")
print(f"With 10% more, the new price is {uteis.coin3.increase(n, t, True)}")
print(f"With 10% less, the new price is {uteis.coin3.decrease(n, t, True)}")