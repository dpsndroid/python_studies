def read_money(text):
    while True:
        if text.isalpha() or text.strip() == "":
            text = str(input("Type a valid number: ")).lower()
        else:
            return float(text)

def read_taxmajor(text):
    while True:
        if text.isalpha() or text.strip() == "":
            text = str(input("Type a valid number: ")).lower()
        else:
            return float(text)

def read_taxminor(text):
    while True:
        if text.isalpha() or text.strip() == "":
            text = str(input("Type a valid number: ")).lower()
        else:
            return float(text)