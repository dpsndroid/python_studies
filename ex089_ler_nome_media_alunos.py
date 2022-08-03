#program that reads name and 2 grades from several students and put it in a
#composed list. In the end show a list containing the average and allow the user
#to show each student's grade separated.
students = []
temp = []
while True:
    name = str(input("Type the name: "))
    first = float(input("Type de 1th grade: "))
    second = float(input("type de 2th grade: "))
    average = (first + second) / 2
    students.append([name, [first, second], average])
    continum = str(input("Continue? [S/N]: ")).lower()
    if continum in "sn":
        if continum == "s":
            continue
        elif continum == "n":
            break
print("----" * 10)
print(f"{'NUMBER':<10}      {'STUDENTS':<20}          {'AVERAGE':<10}")
print("----" * 10)
for i,v in enumerate(students):
    print(f"{i:<13}   {v[0]:<22}   -    {v[2]:<10}")
print("----" * 10)
while True:
    choice = int(input("Chose a number to see the grades: [999 to stop]: "))
    if choice == 999:
        break
    if choice <= len(students) - 1:
        print(f"The grades from {students[choice][0]} are {students[choice][1]}")
    print("----" * 10)
print("Have a good day!!!")
   
    
