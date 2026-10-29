m = int(input("Введите количество строк m: "))
n = int(input("Введите количество столбцов n: "))

matrix = []
print("Введите элементы матрицы построчно (через пробел):")
for i in range(m):
    row = list(map(float, input().split()))
    matrix.append(row)

print("Нулевые элементы найдены в позициях (строка, столбец):")
found = False
for i in range(m):
    for j in range(n):
        if matrix[i][j] == 0:
            print(f"[{i}][{j}]")
            found = True

if not found:
    print("Нулевых элементов в матрице нет")
