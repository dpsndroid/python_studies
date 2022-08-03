#program to create a matrix with dimensions from 3x3 and fill
#it with inputs of numbers. In the end, show it with the correct form.
matrix = [[0,0,0], [0,0,0], [0,0,0]]
for line in range(0,3):
    for col in range(0,3):
        matrix[line][col] = int(input(f"Type a number for position ({line},{col}): "))
print("====" * 20)
for line in range(0,3):
    for col in range(0,3):
        print(f"[{matrix[line][col]:>5}]", end = " ")
    print()
print("====" * 20)
