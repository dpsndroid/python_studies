#programa que leia vários números inteiros. Só vai para quando digitar
#o valor 999, condição de parada. No final mostre quantos números
#foram digitados e qual foi a soma deles
num = 0
counter = 0
tot = 0
print("+---" * 20)
while num != 999:
    num = int(input("Type a number [999 to stop]: "))
    counter += 1
    tot = tot + num
    if num == 999:
        counter -= 1
        tot = tot - 999
print("+---" * 20)
print("You typed {} number(s) and their sum is {}".format(counter,tot))
print("Thank you for your time")
print("""

OTHER WAY - BEST OPTION

""")
num = 0
counter = 0
tot = 0
print("+---" * 20)
num = int(input("Type a number [999 to stop]: ")) #best option
while num != 999:
    counter += 1
    tot = tot + num
    num = int(input("Type a number [999 to stop]: "))
print("+---" * 20)
print("You typed {} number(s) and their sum is {}".format(counter,tot))
print("Thank you for your time")
print("""

OTHER WAY

""")
num = 0
counter = 0
tot = 0
print("+---" * 20)
while num != 999:
    num = int(input("Type a number [999 to stop]: "))
    counter += 1
    tot = tot + num
print("+---" * 20)
print("You typed {} number(s) and their sum is {}".format(counter - 1,tot - 999))
print("Thank you for your time")
