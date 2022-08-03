#program with a tuple with several words.
#Next, show in each word what are the vogals.

list = [str(input("Type a text: ")),
        str(input("Type a text: ")),
        str(input("Type a text: ")),
        str(input("Type a text: ")),
        str(input("Type a text: ")),
        ]
print("----" *20)
for c in list:
    print(f"You typed the word {c.upper():8} and it has the vogals:", end = " ")
    for letter in c:
        if letter.lower() in "aeiou":
            print(letter, end = " ")
    print(" ")
