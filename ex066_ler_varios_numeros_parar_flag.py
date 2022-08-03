#program that reads several integer numbers. It will only stop when the number
#999 will be typed. In the end, show how many numbers were typed and what
#was the sum of them
num = 0
counter = 0
sum1 = 0
print("====" * 20)
while num != 999:
    num = int(input("Type a number: [999 to exit]: "))
    if num == 999:
        break
    sum1 += num
    counter +=1
print(f"The sum of the {counter} value(s) is {sum1}")
print("====" * 20)
