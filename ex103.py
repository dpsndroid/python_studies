#program with function sheet(). it receives 2 optional
#parameters. Name of the player and how many goals
#did he score
#the program must be able to show the player's sheet
#even if a data is missing

def file(player = "unknown", goals = 0):
    print(f"The player {player} made {goals} goal(s)")

p = str(input("Name of the player: "))
g = str(input("Number of goals: "))
if g.isnumeric():
    g = int(g)
else:
    g = 0

if p.strip() == "":
    file(goals = g)
else:
    file(p, g)



