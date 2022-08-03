#program gets seven numbers typed. it has to maintain the even values
#separeted from odd values in only one list. In the end, show the evens and the odds
#in crescent order
listnum = [[], []]
for c in range(0,7):
    num = int(input("Type a number: "))
    if num % 2 == 0:
        listnum[0].append(num)
    elif num % 2 != 0:
        listnum[1].append(num)
            
listnum[0].sort()
listnum[1].sort()
print(f"The full list is: {listnum}")
print(f"The even list is {listnum[0]}")
print(f"The odd list is {listnum[1]}")

        
