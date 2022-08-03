#improve the exercise 93 to work with several players, including a system
#to view the use of each player.
games = []
team = []
player = {}
while True:
    counter = 0
    games.clear()
    player.clear()
    player["NAME"] = str(input("Player's name: "))
    tot = int(input(f"How many games did {player['NAME']} play: "))
    for c in range(0, tot):
        counter += 1
        games.append(int(input(f"   How many goals in game {counter}? "))) #taka e look at this
    player["GOALS"] = games[:] #important
    player["TOTAL"]= sum(games)
    team.append(player.copy())
    
    while True:
        continum = str(input("(S)top or (C)ontinue: ")).lower()[0]
        if continum in "sc":
            break
    if continum == "s":
        break
print("----" * 20)
print(f"{'Cod.':<9}", end = "")
for i in player.keys():
    print(f"{i:<20}", end = "")
print()
print("----" * 20)
for k, v in enumerate(team):
    print(f"{k:<7} ", end = "")
    for d in v.values(): #it's new. I don't know what is it
        print(f"{str(d):<20}", end = "")
    print()
print("----" * 20)
while True:
    search = int(input("What player to show: "))
    if search == 999:
        break
    if search >= len(team):
        print("Number isn't valid")
    elif search < len(team):
        print("----" * 10)
        print(f"Data from player {team[search]['NAME']}")
        for i,g in enumerate(team[search]["GOALS"]):
            print(f"In game {i + 1} made {g} goals")
        print("----" * 10)
print("----" * 20)
print("Thank you for try me")

