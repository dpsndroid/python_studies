#program that reads four values and put it in a tuple. show how many times
#the number 9 appeared. In what position was typed the first value 3.
#What were the even numbers
while True:
    v1 = int(input("Type a number: "))
    v2 = int(input("Type a number: "))
    v3 = int(input("Type a number: "))
    v4 = int(input("Type a number: "))
    tup = (v1,v2,v3,v4)
    print("You chose the respective numbers:", end = " ")
    for c in tup:
        print(c, end = " ")
    print(f"\nThe last element of the tuple is: {tup[3]}")
    print(f"The number 9 appeared {tup.count(9)} times")
    if 3 in tup:
        print(f"The number 3 appeared in the {tup.index(3) + 1}th position")
    else:
        print("The number 3 wasn't inserted in the tuple")
    print("The even number(s) are(is):", end = " ")
    for n in tup:
        if n % 2 == 0:
            print(n, end = " ")
        else:
            print("No one")
            break
    continum = str(input("\nContinue: 'n' stop / Any key continue: "))
    if continum == "n":
        break
print("Thank you for your time")
