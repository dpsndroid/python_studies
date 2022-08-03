# Create a small modularized system that allows
# to sign people from name and age
# The system will have only two options: sign people and list the signed people
import ex115mod

while True:
    ex115mod.menu(["Show registered people","Register new person","Shutdown"])
    op = str(input("Choose an option above: "))
    while True:
        if op in "123":
            break
        else:
            op = str(input("type a valid number: "))
    if op == "1":
        ex115mod.record_people()
    elif op == "2":
        ex115mod.signin()
    elif op == "3":
        break
ex115mod.header("Program ended successfuly")
        
        
            
    
    