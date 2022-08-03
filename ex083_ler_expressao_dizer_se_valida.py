#program where the user type any expression. Program must analize if the expression
#has parentheses opened and closed in the correct order.
expression = input("type an expression: ")
list = []
for item in expression:
    if item == "(":
        list.append("(")
    elif item == ")":
        list.pop()
if len(list) == 0:
    print("The expression is VALID") 
else:
    print("The expression is INVALID")
print("----" * 20)
print("OTHER WAY")
print("----" * 20)


if list.count('(') == list.count(')'):
    print("The expression is VALID") 
else:
    print("The expression is INVALID")


    
        
    
