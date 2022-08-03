#program with a counter function. Get three parameters. Begining, end and pass
#make the count:  a) 1 to 10 from 1 and 1.  b) 10 to 0  from 2 and 2
# c) a personalized counter


def counter(b,e,s):
    for c in range(1,11,1):
        print(f"{c}", end=" ")
    print("end")
    for d in range(10,-1,-2):
        print(f"{d}", end=" ")
    print("end")
    for z in range(b, e, s):
        print(f"{z}", end=" ")
    print("end")

begin = int(input("To start: "))
end = int(input("To stop: "))
steps = int(input("How many steps: "))
if begin > end and steps > 0:
    double = steps * 2
    steps = steps - double
    end -= 1
else:
    end += 1
if steps == 0:
    steps = 1

counter(begin, end, steps)





