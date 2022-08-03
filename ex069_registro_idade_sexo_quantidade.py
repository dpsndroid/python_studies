#program that reads age and sex from several people. For each registration ask
#if want to continue. At the end show: how many people more than 18
#how many men registrated. How many women less than 20
#continum = " "
man = 0
woman = 0
eighteen = 0
twenty = 0
sex = " "
while True:
    sex = " "
    age = 0
    print("====" * 20)
    while sex not in "MF":
        sex = str(input("type your sex: [M/F]: ")).upper()[0]
    age = int(input("type your age: "))
    if sex == "M":
        man += 1
        if age > 18:
            eighteen += 1
    elif sex == "F":
        woman += 1
        if age <20:
            twenty += 1
        elif age > 20:
            eighteen += 1
    continum = str(input("Do you want to continue? Any key to continue. 'N' to stop: ")).upper()
    if continum == "N":
        break
print("====" * 20)
print(f"There were {eighteen} people more than 18")
print(f"There were {man} man registered")
print(f"There were {twenty} women less than 20")
    
    
    
