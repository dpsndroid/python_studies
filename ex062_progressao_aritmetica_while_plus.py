#melhore o desafio 61, perguntando para o usuário se ele quer mostrar mais
#alguns termos. O programa encerra quando disser que quer mostrar 0 termos
print("let's see the 10 first terms from a arithmetic progression")
continum = "s"
term = int(input("Type the first term: "))
reason = int(input("What is the reason: "))
numterm = 10
totnumterm = 0
print("+---" *20)
while continum == "s":
    tenth = term + (11 - 1) * reason
    counter = 1
    while counter <= numterm:
        if counter == numterm:
            print("{}".format(term), end =" ")
        else:
            print("{} ->".format(term), end =" ")
        term += reason
        counter += 1
    print("")
    continum = str(input("Do you want to add more terms? 's' to continue. Any key to exit: "))
    if continum == "s":
        numterm = int(input("How many terms now?: "))
    totnumterm
    += numterm
print("It was showed {} terms.".format(totnumterm))
print("It's over! Thank you for your time.")
print("+---" *20)
