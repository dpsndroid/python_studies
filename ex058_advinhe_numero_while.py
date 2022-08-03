#Improve the challenge from game 28. Computer thinks a number beetwen 1 and 10
#and the player will try to find, showing the attempts after

from random import randint
from time import sleep
computer = randint(1,10)
counter = 0
bullseye = False
print("I thought a number beetwen 1 and 10. Guess what is it:")
print("+---" *20)
while bullseye == False: #he used while not bullseye. I didn't understand
    player = int(input("Try it: "))
    counter += 1
    if player == computer:
        bullseye = True
    else:
        if player < computer:
            print("Almost! Try a bigger one: ")
        if player > computer:
            print("Almost! Try a smaller one: ")
print("+---" *20)            
print("Congratulations, You won. The number was {}".format(player))
print("And you had {} attempt(s) to find".format(counter))
print("+---" *20)

