#program that reads name and average from a student. keeping also the situation
#show the content of the structure in the end.
student = {}
condition = ""
student["NAME"] = str(input("Type your name: "))
student["AVERAGE"] = float(input(f"Type de average of {student['NAME']}: "))
if student["AVERAGE"] >= 7:
    student["CONDITION"] = "aproved"
elif student["AVERAGE"] >= 5 < 7:
    student["CONDITION"] = "recovery"
elif student["AVERAGE"] < 5:
    student["CONDITION"] = "reproved"
print("----" * 20)
for k, v in student.items():
    print(f"{k} = {v}")
print("----" * 20)
print("Have a nice day!")
