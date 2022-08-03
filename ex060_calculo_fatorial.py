#program that reads any number and shows its factorial
#ex 5: 5x4x3x2x1=120
import math
continum = "y"
while continum == "y":
    num = int(input("Type a number: "))
    print("The factorial of number {} is {}.".format(num,math.factorial(num)))
    continum = str(input("Do you want to continue? 'Y' to continue. Any key to leave: "))
print("Thank you for your time.")
print("+---" * 20)
print("""

OTHER WAY

""")
num = int(input("Type a number: "))
counter = num
fac = 1
print("Calculating {}! = ".format(num), end = " ")
while counter > 0 :
    print("{}".format(counter), end= " ")
    print("x" if counter > 1 else"=", end = " ")
    fac *= counter
    counter -=1
print("{}".format(fac))
print("Thank you for your time")
print("+---" * 20)
print("""

OTHER WAY

""")
num = int(input("Type a number: "))
fac = 1
print("Calculating {}! = ".format(num), end = " ")
for counter in range(num, 0, -1):
    print("{}".format(counter), end= " ")
    print("x" if counter > 1 else"=", end = " ")
    fac *= counter
    counter -=1
print("{}".format(fac))
print("Thank you for your time")
print("+---" * 20)
    
        
    
