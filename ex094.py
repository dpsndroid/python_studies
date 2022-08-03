#program that reads name, sex and age from several people. Put them in
#a dictionary and put these in a list. In the end, shows how many persons
#registered. the age average of the group. A list with all the women.
#A list with people above the average age 

people = []
person = {}
totage = 0
while True:
    person["name"] = str(input("type name: ")).lower().title()
    person["age"] = int(input(f"type age of {person['name']}: "))
    totage += person["age"]
    while True:
        person["sex"] = str(input(f"type the sex of {person['name']} [M/F]: ")).lower()[0]
        if person["sex"] in "mf":
            break
        print(f"type only 'M' or 'F'")
  
    people.append(person.copy())
    while True:
        continum = str(input("(S)top or (C)ontinue: ")).lower()[0]
        if continum in "sc":
            break
    if continum == "s":
        break
average = totage / len(people)            
print(f"The total of registered people are {len(people)}")
print(f"The average age of the group is {average:.0f}")
print("The total of women in the list are:", end = " ")
for p in people:
    if p["sex"] == "f":
        print(f"({p['name']})", end= " ")
print()
print("The total of people above the average are:", end = " ")
for p in people:
    if p["age"] > average:
        print(f"({p['name']})", end= " ")
        print()
        for k,v in p.items():
            print(f"{k} = {v}", end = "  ")
