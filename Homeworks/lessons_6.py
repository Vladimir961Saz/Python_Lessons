import random
matrix = [[random.randint(-10, 10) for _ in range(3)] for _ in range(3)]
print('Исходная матрица:',matrix)
s=[]
for i in range(len(matrix)):
    s.append(sum(matrix[i]))
print("Строка с наибольшей суммой:",matrix[s.index(max(s))],"Сумма элементов:",max(s),"Строка с наименьшей суммой:",matrix[s.index(min(s))],"Сумма элементов:",min(s))

from random import randint as rd 
m, n = map(int,input().split())
arr = [[rd(1, 10) for i in range(m)] for j in range(n)]
for i in arr :
    print(*i)
print()
for row in arr :
    rmin = min(row)
    row = [(1 if rmin % 2 else 0) if j == rmin else j for j in row]
    print(*row)