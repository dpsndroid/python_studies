def increase(price = 0, tax = 0):
    res = price + (price / 100 * tax)
    return res


def decrease(price = 0, tax = 0):
    res = price - (price / 100 * tax)
    return res


def double(price = 0):
    res = price * 2
    return res

    
def half(price = 0):
    res = price / 2
    return res

def monetary(price = 0, cent = "R$ "):
    return f"{cent}{price:.2f}".replace('.',',') #substitui o uma coisa por outra onde estiver
