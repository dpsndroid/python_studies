#improve the exercise 86 showing the sum of all even values.
#the sum of the third collumm. The major value from the second row
matrix = [[0,0,0], [0,0,0], [0,0,0]]
even = 0
odd = 0
scol = 0
bigger = 0
for line in range(0,3):
    for col in range(0,3):
        matrix[line][col] = int(input(f"Type a number for position ({line},{col}): "))
        if matrix[line][col] % 2 ==0:
            even += matrix[line][col]
        elif matrix[line][col] % 2 !=0:
            odd += matrix[line][col]
            
print("====" * 20)
for line in range(0,3):
    for col in range(0,3):
        print(f"[{matrix[line][col]:>5}]", end = " ")
    print()
print("====" * 20)
print(f"The sum of the even numbers are: {even}")
print(f"The sum of the odd numbers are: {odd}")
for c in matrix[1]:
    if bigger == 0:
        bigger = c
    else:
        if c > bigger:
            bigger = c
print(f"The major number of the second row is: {c}")
for line in range(0,3):
    scol += matrix[line][2]
print(f"The sum of the third collumm is: {scol}")

