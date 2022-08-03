#program that has a function named vote(). it receives
#the year of birth as parameter. Returning if the person
#has his vote denied, optional or mandatory in the elections

def vote(born):
    from datetime import date
    today = date.today().year
    age = today - born
    if age < 16:
        return f"You are {age} years old, and your vote is denied."
    elif 16 <= age < 18 or age > 60:
        return f"You are {age} years old, and your vote is optional."
    elif 18 <= age < 60:
        return f"You are {age} years old, and your vote is mandatory."
    
birth = int(input("Type your birth: "))
print(vote(birth))
