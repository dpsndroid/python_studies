def increase(price = 0, taxi = 0, formate = False):
    res = price + (price / 100 * taxi)
    return res if formate is False else monetary(res)


def decrease(price = 0, taxd = 0, formate = False):
    res = price - (price / 100 * taxd)
    return res if formate is False else monetary(res)


def double(price = 0, formate = False):
    res = price * 2
    return res if formate is False else monetary(res)

    
def half(price = 0, formate = False):
    res = price / 2
    return res if formate is False else monetary(res)

def monetary(price = 0, cent = "R$ "):
    return f"{cent}{price:.2f}".replace('.',',') #substitui o uma coisa por outra onde estiver

def summary(price = 0, taxup = 10, taxdown = 5):
    print("-----" * 5)
    print("VALUE'S SUMMARY")
    print("-----" * 5)
    print(f"The price obtained is: \t\t{monetary(price)}")
    print(f"The double of the price is: \t{double(price, True)}")
    print(f"The half of the price is: \t{half(price, True)}")
    print(f"Increasing {taxup} %: \t\t{increase(price, taxup, True)}")
    print(f"Decreasing {taxdown} %: \t\t{decrease(price, taxdown, True)}")
    print("-----" * 5)

