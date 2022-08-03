#listas parte 2
data = list()
data.append("peter")
data.append("josh")
data.append("handerson")
print(data)
print(data[0])
people = list()
people.append(data[:])
print(people)
datab = [["simone", 53], ["daniel", 45], ["luiza", 12]]
print(datab)
print(datab[2])
print(datab[2][1])
print(f"{datab[2][0]} is {datab[2][1]}")
for p in datab:
    print(f"{p[0]} is {p[1]} years old")
crowd = list()
datac = list()
for c in range(0,2):
    datac.append(str(input("Name: ")))
    datac.append(int(input("Age: ")))
    crowd.append(datac[:]) #cria uma cópia dos dados
print(datac)    
datac.clear()
    
