def increase(price, tax):
    res = price + (price / 100 * tax)
    return res


def decrease(price, tax):
    res = price - (price / 100 * tax)
    return res


def double(price):
    res = price * 2
    return res

    
def half(price):
    res = price / 2
    return res
