#program that generates five randomic numbers and insert them in a tuple
#next, print the list and indicate the major and the minor number
from random import randint
while True:
    tup = (randint(0,20),randint(0,20),randint(0,20),randint(0,20),randint(0,20))
    print("The chosen numbers were:", end = " ")
    for num in tup:
        print(num, end = " ")
    print(" ")
    print(f"The MAJOR number of the list is the number {max(tup)}") #max
    print(f"The MINOR number of the list is the number {min(tup)}") #min
    print("====" * 20)
    continum = str(input("Any key to continue, 'n' to stop: ")).lower()
    if continum == "n":
        break
print("====" * 20)
print("Thank you for your time")

