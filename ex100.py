#program with a list named numbers. 2 functions. Sort them and sum the even numbers
#Sort 5 numbers e put them inside a list
#show the sum of all even numbers

from random import randint
from time import sleep


def func1(list1):
    for c in range(0,5):
        num = randint(0,50)
        while num in numbers:
            num = randint(0,50)
        else:
            list1.append(num)
        print(f"{num}", end = " ", flush = True)
        sleep(0.3)
    print()
    print(f"the sorted numbers are: {numbers}")


def func2(list1):
    soma = 0
    for c in list1:
        if c % 2 == 0:
            soma += c
    print(f"The sum of the even numbers is: {soma}")

numbers = list()
func1(numbers)
func2(numbers)
        


