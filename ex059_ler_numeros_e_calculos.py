#programa que leia 2 valores e mostre um menu na tela
#[1]somar [2]multiplicar [3]maior [4]novos números [5]sair do programa
#deve realizar a operação em cada caso
from time import sleep
option = 0
bigger = 0
reset = 0

v1 = int(input("Type a number: "))
v2 = int(input("type other number: "))
print("You typed the number {} and number {}".format(v1,v2))
print("+---" * 20)
while option !=5:
    print("[1]sum [2]multiply [3]bigger [4]new numbers [5]Quit")
    option = int(input("Choose an option in the menu above: "))
    print("+---" * 20)
    if option == 1:
        sum1 = v1 + v2
        print("{} + {} = {}".format(v1,v2,sum1))
        print("+---" * 20)
    elif option == 2:
        multiply = v1 * v2
        print("{} x {} = {}".format(v1,v2,multiply))
        print("+---" * 20)
    elif option == 3:
        if v1 > v2:
            bigger = v1
        else:
            bigger = v2
        print("The biggest number is {}".format(bigger))
        print("+---" * 20)
    elif option == 4:
        print("Choose new numbers")
        v1 = int(input("Type a number: "))
        v2 = int(input("type other number: "))
    elif option == 5:
        print("Finalizando....")
    else:
        print("Opção inválida")
sleep(3)
print("Thanks for try me")
print("+---" * 20)
        
    
