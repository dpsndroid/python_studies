#a tuple with products and their prices in sequence
#In the end, show the products and the prices in tabular form
tup = ("Pencil",1.75,"Rubber",2.00,"Notepad",15.90,"Case",25.00,
       "Transfer",4.00,"Compass",9.99,"Backpack",120.32,"Pens",
       22.30,"Book",34.90)

print("====" * 20)
print(f"{'LISTAGEM DE PREÇOS':^35}")
print("====" * 20)
for pos in range(0, len(tup)):
    if pos % 2 ==0:             #it will complete untill fill 30 indexes
        print(f"{tup[pos]:.<30}", end = " ")
    else:
        print(f"R${tup[pos]:>7.2f}")

print("====" * 20)
