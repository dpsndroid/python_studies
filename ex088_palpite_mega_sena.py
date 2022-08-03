#program to create hints for the megasena. program asks how many games
#will be generated and sort 6 numbers beetwen 1 and 60 for each game
#registering everything in a list.
from random import randint
from time import sleep
listmega = []
temp = []
count = 1
print("----" * 10)
print("MEGA SENA GUESSES")
print("----" * 10)
amount = int(input("HOW MANY GAMES DO YOU WANT: "))
print("====" * 10)
for c in range(0, amount):
    print(f"{count:<3}th GAME: ", end = " ")
    sleep(2)
    for game in range(1,7):
        game = randint(1,60)
        while game in temp:
            game = randint(1,60)
        else:
            temp.append(game)
    listmega.append(temp[:])
    print(temp)
    temp.clear()
    print("----" * 10)
    count += 1
print("TRY ONE, TWO, ..., OR ALL OF THEM AND GOOD LUCK!!!")
print()
print(listmega)
