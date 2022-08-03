#tuple with first 20 placed in the Brazilian Soccer Championship
#Show the first 5 placed, show the last 4 placed. Show a list of the teams in
#alphabetical order, In what position is Chapecoense team.

teams = ("Palmeiras","Corinthians","Sao Paulo","Internacional",
         "Athletico","Santos","Atletico MG","Coritiba","Fluminense",
         "America MG","Avai","Bragantino","Ceara","Goias","Atletico GO",
         "Flamengo","Botafogo","Cuiaba","Juventude","Fortaleza")

print("====" * 20)
print("BRAZILIAN CHAMPIONSHIP")
print("====" * 20)

print("THE FIVE FIRST TEAMS IN THE CHAMPIONSHIP ARE:")
for c in teams[0:5]:
    print(c)
print("====" * 20)

print(f"THE FOUR LAST TEAMS IN THE CHAMPIONSHIP ARE:")
for c in teams[-4:]:
    print(c)
print("====" * 20)

print("TEAMS IN ALFABETHICAL ORDER:")
for c in sorted(teams):
    print(c)
print("====" * 20)

print(f"Flamengo is in the {teams.index('Flamengo') + 1}th position")
