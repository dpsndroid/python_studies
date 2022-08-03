#program that reads name, year of birth, and word card. register them by age.
#if ctps is different than 0, register also the year of hire and salary.
#calculate and add, how many to get retiring. As an example, use 35 year
#of contribution.
from datetime import datetime
total = []
while True:
    worker = {}
    print("ENTER THE WORKER DATA")
    print("====" * 20)
    worker["Name"] = str(input("Type name: "))
    birth = int(input(f"Type the age of birth from {worker['Name']}: "))
    worker["Age"] = datetime.now().year - birth
    ctps = int(input("Ctps number:[0 for no one]: "))
    if ctps == 0:
        print("There's no Ctps number")
    else:
        worker["Ctps"] = ctps
        worker["Year"] = int(input("Year of hire: "))
        worker["Salary"] = float(input("Salary: "))
        worker["Retirement"] = worker["Age"] + (worker["Year"] + 35) - datetime.now().year
    print("----" * 20)
    for k, v in worker.items():
        print(f"{k} = {v}", end = " ")
    print()
    print("----" * 20)
    total.append(worker)
    while True:
        continum = str(input("Continue? {Y/N]: ")).lower()[0]
        if continum in "yn":
            break
    if continum == "n":
            break
        
for c in total:
    print(c)
