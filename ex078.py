#program that reads five values and put them inside a list
#in the end, show what is the major, the minor and their positions
list = []
major = 0
minor = 0
for c in range(0,5):
    list.append(int(input(f"Type a number for position {c}: ")))
    if c == 0:
        major = minor = list[c]
    else:
        if list[c] > major:
            major = list[c]
        elif list[c] < minor:
            minor = list[c]
print("----" * 20)        
print(f"You typed the numbers : {list}")
print(f"the MAJOR number(s) is(are): {major} in the position", end = " ")
for pos, v in enumerate(list):
    if v == major:
        print(pos, end = "... ")
print(" ")
print(f"the MINOR number(s) is(are): {minor} in the position", end = " ")       
for pos, v in enumerate(list):
    if v == minor:
        print(pos, end = "... ")
print(" ")
print("----" * 20)
print("Thank you for your time")
