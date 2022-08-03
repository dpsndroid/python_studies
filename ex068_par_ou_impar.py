#program that plays even or odd. It will interrupt when the player lost
#showing the total of consecutive victories of the player.
from random import randint
playernum = 11
playeropt = " "
victory = 0
opt = " "
print("====" * 20)
print("ODDS OR EVENS")
print("====" * 20)
while True:
    while playernum < 0 or playernum > 10:
        playernum = int(input("choose a number from 0 to 10: "))
    while playeropt not in "EO":
        playeropt = str(input("choose even or odd: [E/O]: ")).upper()
    compnum = randint(0,10)
    tot = compnum + playernum
    if tot % 2 == 0:
        opt = "Even"
    else:
        opt = "Odd"
    print(f"You chose number {playernum} and computer chose number {compnum}")
    print(f"The number {tot} is {opt}")
    if playeropt == "E":
        if tot % 2 == 0:
            print("you won")
            victory +=1
            playernum = int(input("choose a number from 0 to 10: "))
            playeropt = str(input("choose even or odd: [E/O]: ")).upper()
        else:
            print("you loose")
            break
    elif playeropt == "O":
        if tot % 2 != 0:
            print("you won")
            victory +=1
            playernum = int(input("choose a number from 0 to 10: "))
            playeropt = str(input("choose even or odd: [E/O]: ")).upper()
        else:
            print("you loose")
            break
        
print(f"It's over! You won {victory} times")
print("====" * 20)
    
