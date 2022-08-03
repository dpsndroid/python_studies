#program where 4 playes throw a dice and get randomic results. In the end
#put this dictionary in order. The winner got the highest score.
from random import randint
from time import sleep
from operator import itemgetter  #to get informations about the items
counter = ""
while True:
    print("====" * 20)
    for c in range(1,4):
        if counter == "":
            print("READY >>> ", end = "")
            sleep(1)
            counter = "READY"
        elif counter == "READY":
            print("SET >>> ", end = "")
            sleep(1)
            counter = "SET"
        elif counter == "SET":
            print("GO!!!")
            sleep(1)
            counter = ""
            break
    print("----" * 20)    
    game = {"Player 1": randint(1,6),
            "Player 2": randint(1,6),
            "Player 3": randint(1,6),
            "Player 4": randint(1,6),}
    for k,v in game.items():
        print(f"{k} got {v} in the dice")
        sleep(1)
    ranking = [] #created a list instead of a dictionary
    ranking = sorted(game.items(), key=itemgetter(1), reverse = True) #get information from item and shows the results in reverse
    print("----" * 20)
    print("PLAYER'S RANKING", end = " ")
    for c in range(1,6):
        print(".", end = "")
        sleep(1)
    print()
    print("----" * 20)
    print(f"The winner was {ranking[0][0]} with number {ranking[0][1]}")
    print("----" * 20)
    for i, v in enumerate(ranking):
        print(f"{i +1}th place: {v[0]} with number {v[1]}")
    print("----" * 20)
    continum = str(input("Wanna play again? :")).lower()
    if continum in "sn":
        if continum == "s":
            continue
        elif continum == "n":
            break
print("----" * 20)
print("Have a nice day")
