#program that reads numbers and insert in a list in the correct order without
#using the command sort(). Show the order in the end

list = []
for c in range(0,5):
    num = int(input("type a number: "))
    if c == 0 or num > list[-1]:
        list.append(n)
        print("Added to the end of the list")
    else:
        pos = 0
        while pos < len(list):
            if num <= list[pos]:
                list.insert(pos, num)
                print(f"It was added in the position {pos}")
                break
            pos += 1
print(f"The typed values in order were {list}")

