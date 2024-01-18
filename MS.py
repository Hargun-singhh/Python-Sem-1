row= int(input("Enter the number of rows:"))
col = int(input("Enter the number of columns:"))

matrix = []

print("Enter values in matrix :")

for i in range(row):
    data = []
    for j in range(col):
        data.append(int(input()))
    matrix.append(data)
print("_____MATRIX______")
for i in range(row):
    for j in range(col):
        print(matrix[i][j], end=" ")
    print()
print("_______SUM_______")
for i in range(row):
    sum = 0
    for j in range(col):
        sum = sum + matrix[i][j]
    print('Sum of row', i + 1, ':', sum)