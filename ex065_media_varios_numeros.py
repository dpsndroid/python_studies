#programa que leia vários números inteiros. No final mostre a média entre todos
#3 qual foi o maior e o menor. Programa deve perguntar se quer continuar ou não
#a digitação
tot = 0
counter = 0
continum = "S"
biggest = 0
smallest = 0
while continum in "Ss":
    num = int(input("type a number: "))
    tot += num
    counter += 1
    if counter == 1:
        biggest = smallest = num
    else:
        if num > biggest:
            biggest = num
        if num < smallest:
            smallest = num
    continum = str(input("Do you want to continue? 'S' to continue. Any key to stop. "))
average = tot / counter
print("You typed {} number(s), the total is {} and their average is {}".format(counter, tot, average))
print("The biggest number was {} and the smallest number was {}".format(biggest, smallest))
