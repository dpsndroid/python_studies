#refaça o desafio 51. ler o primeiro termo e a razao de uma PA
#mostrando os 10 primeiros termos, usando while
print("let's see the 10 first terms from a arithmetic progression")
term = int(input("Type the first term: "))
reason = int(input("What is the reason: "))
print("+---" *20)
tenth = term + (11 - 1) * reason
counter = 1
while counter <= 10:
    if counter == 10:
        print("{}".format(term), end =" ")
    else:
        print("{} ->".format(term), end =" ")
    term += reason
    counter += 1
print("")
print("It's over! Thank you for your time.")
print("+---" *20)
    
