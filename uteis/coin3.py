# Obs: Também pode simplificar fazendo apenas monetary(res) para
# enviar o resultado formatado

def increase(price = 0, tax = 0, formate = False):
    res = price + (price / 100 * tax)
    return res if formate is False else monetary(res)


def decrease(price = 0, tax = 0, formate = False):
    res = price - (price / 100 * tax)
    return res if formate is False else monetary(res)


def double(price = 0, formate = False):
    res = price * 2
    return res if formate is False else monetary(res)

    
def half(price = 0, formate = False):
    res = price / 2
    return res if formate is False else monetary(res)

def monetary(price = 0, cent = "R$ "):
    return f"{cent}{price:.2f}".replace('.',',') #substitui o uma coisa por outra onde estiver
