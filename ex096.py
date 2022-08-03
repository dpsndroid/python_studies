#program with a function named area(). receives dimensions of a retangular land
#height and lenght, and show the area of the land.

def area1(height, length):
    area = height * length
    print(f"The area of the land from {height} x {length} is {area}m²")

h = float(input("height: "))
l = float(input("lenght: "))

area1(h, l)


