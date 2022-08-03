#program with function readint(). Works similar to the function
#input(), but making the validation to accept only
#one numeric value
def readInt(msg):
    while True:
        number = str(input(msg))
        if number.isnumeric():
            value = int(number)
            return value
        else:
            print("\033[0;31mtype a valid number.\033[m")

number = readInt("Type a number: ")
print(f"You just typed the number {number}")
