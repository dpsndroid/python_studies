from ex115mod import header


def fileexists(name):
    try:
        a = open(name, "rt") # rt means read text
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True

def createfile(name):
    try:
        a = open(name, "wt+") # wt+ means write a text, and + means to create a new file
        a.close()
    except:
        print("There was an error creating the file")
    else:
        print(f"File '{name}' created successfully")


def readfile(name):
    try:
        a = open(name, "rt")
    except:
        print("There was an error reading the file")
    else:
        header("REGISTERED PEOPLE")
        print(a.read()) # read the file