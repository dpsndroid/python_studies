#program with function grades(). it receives several grades
#from the students and return a dictionary containing
#amount of grades, the major grade, the minor grade, average
#and the situation (optional)

def grades(*n, sit = False):
    r = dict()  # The other way to create a dictionary
    r["total"] = len(n)
    r["major"] = max(n)
    r["minor"] = min(n)
    r["average"] = sum(n)/len(n)
    if sit:
        if r["average"] >= 7:
            r["situation"] = "good"
        elif r["average"] >= 5:
            r["situation"] = "reasonable"
        else:
            r["situation"] = "bad"
    return r

# Main Program
resp = grades(5.5, 8.1, 7.7, sit = True)
print(resp)
