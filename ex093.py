#program that manages a soccer player's use. How many games did he play.
#How many goals in each game. Put it in a dictionary including his total
#scored goals during the championship
games = []
player = {}
counter = 0
player["NAME"] = str(input("Player's name: "))
tot = int(input(f"How many games did {player['NAME']} play: "))
for c in range(0, tot):
    counter += 1
    games.append(int(input(f"How many goals in game {counter}? "))) #taka e look at this
player["GOALS"] = games[:] #important
player["TOTAL"]= sum(games)
print("----" * 20)
print(player)
print("----" * 20)
for k,v in player.items():
    print(f"{k} = {v}")
print("----" * 20)
print(f"The player {player['NAME']} played {counter} games")
print(f"The player {player['NAME']} played {tot} games")
print(f"The player {player['NAME']} played {len(player['GOALS'])} games")
for i, v in enumerate(player['GOALS']):
    print(f"In game {i + 1} made {v} goals")
print(f"it was a total of {player['TOTAL']} goals")
print("----" * 20)
print(games)
