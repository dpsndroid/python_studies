#program with a function named major(), it receives several integer parameters
#analise all the values e say wich one is the major value

def major(* num):
    count = 0
    major = 0
    print("----" * 10)
    for n in num:
        print(n, end = " ")
        if count == 0:
            major = n
        else:
            if n > major:
                major = n
        count += 1
    print()
    print(f"it was added {count} numbers")
    print(f"The major number is {major}")

major(1,2,3,4,5,6)
major(5,7,1,6,8)
major(9,2,3,7,1)
major(1,2,3)
major(8,5,2,4,7)
major()

