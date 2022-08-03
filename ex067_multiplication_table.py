#program that shows a multiplication table from several numbers. One at a time.
#the program will stop when the number is negative.
num = 0
print("====" * 20)
print("MULTIPLICATION TABLE")
print("====" * 20)
while True:
    num = int(input("type a number to calculate: "))
    if num < 0:
        break
    for counter in range(1,11):
        print(f"{num} x {counter:2} = {num*counter:4}")
        counter += 1
    print("====" * 20)
print("Thank you for your time")
print("====" * 20)
