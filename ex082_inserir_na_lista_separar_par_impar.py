#program that reads several numbers and put them in a list
#create 2 more lists that will contain the odd values and even values
#in the end, show the content of both the 3 lists
list = []
even = []
odd = []
while True:
    list.append(int(input("type a number: ")))
    continum = str(input("Continue? ['N'/ Any key]: ")).upper()
    if continum == "N":
        break
for index, value in enumerate(list):
    if value % 2 == 0:
        even.append(value)
    else:
        odd.append(value)
list.sort()
even.sort()
odd.sort()
print(f"The full list is {list}")
print(f"The even list is {even}")
print(f"The odd list is  {odd}")

