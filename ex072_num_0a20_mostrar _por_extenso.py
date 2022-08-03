#program with a tuple filed of a sequence from 0 to 20
#the program must read a number and write it in full

num = ("zero","one","two","three","four","five","six","seven",
       "eight","nine","ten","eleven","twelve","thirteen","fourteen","fifteen",
       "sixteen","seventeen","eighteen","nineteen","twenty")

while True:
    while True:
        choice = int(input("Chose a number beetwen 0 and 20: "))
        if 0 <= choice <= 20:
            print(f"You typed the number {num[choice]}")
            print("====" * 20)
            break
        print("Not valid.", end = " ")
    continum = str(input("Continue: Any key to continue. 'n' to stop: ")).lower()
    if continum == "n":
        break
print("Thank you for your time")

