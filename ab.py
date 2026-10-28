matrix = []

for row_number in range(3):
    values = input().split()
    row = [int(values[0]), int(values[1]), int(values[2])]
    matrix.append(row)

for row in matrix:
    print(row)