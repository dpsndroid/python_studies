#program that reads name and weight and put them in a list. In the end
#show how many people are registered. list with the heaviest people
#list with the lightiest people
listm = []
temp = []
major = 0
minor = 0
while True:
    temp = []
    temp.append(str(input("Type a name: ")))
    temp.append(float(input("Type a weight: ")))
    listm.append(temp[:])
    #temp.clear() I can use this or what I did. Name the variable as empty
    if major == minor == 0:
        major = minor = temp[1]
    else:
        if temp[1] > major:
            major = temp[1]
        elif temp[1] < minor:
            minor = temp[1]
        
    continum = str(input("Continue [S/N): ")).lower()
    if continum in "sn":
        if continum == "s":
            continue
        elif continum == "n":
            break
print(listm)
print(f"There are(is) {len(listm)} person(s) registered.")

for c in listm:
    if c[1] == major:
        print(f"The heaviest person is {c[0]} with {c[1]}kg")
    if c[1] == minor:
        print(f"The lightest person is {c[0]} with {c[1]}kg")


