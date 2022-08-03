#program with a function named factorial(). It receives
#2 parameters. the first point the number to calculate
#the other named show(). A logic value to see if will be
#showed or not the process of calculate.
def fatorial(n, show = False):
    """
    -> Calculates the factorial of a number.
    """
    f = 1
    for c in range(n, 0, -1):
        if show:
            print(c, end = " ")
            if c > 1:
                print(f"x", end=" ")
            else:
                print(f"=", end = " ")
        f = f * c
    return f
print()
print(fatorial(5, show = True))
