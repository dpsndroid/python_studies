#program that reads several numbers and regist in a list. If the number already
#exists, it will not be added. Show the numbers in crescent order.
num = list()
while True:
    n = int(input("Type a number: "))
    if n not in num:
        num.append(n)
        print("Value added")
    else:
        print("The number already exists.")
    continum = str(input("Continue? 'n' to stop. Any key to continue: ")).lower()
    if continum == "n":
        break
print("----" * 20)
num.sort()
print(num)
num.sort(reverse=True)
print(num)
print("----" * 20)
print("Thank you for your time")
