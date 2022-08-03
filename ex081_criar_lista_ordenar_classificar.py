#program that reads several numbers, put them in a list, show how many
#numbers were typed. Put it in decrescent order. Show if number 5 was
#typed or not
list = []
while True:
    num = int(input("Type a number: "))
    list.append(num)
    print("Added")
    continum = str(input("Contine? 'n' to stop. Any to continue: ")).lower()
    if continum == "n":
        break
           
print(f"You typed {len(list)} elements")
list.sort(reverse = True)
print(list)
if 5 in list:
    print(f"The number 5 is in the position {list.index(5)}")
else:
    print("The number 5 isn't in the list")
