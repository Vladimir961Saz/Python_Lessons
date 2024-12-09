# # 1
# from random import randint
# from random import randint as rd
# import random
# matrix = [[random.randint(-10, 10) for _ in range(3)] for _ in range(3)]
# print('Исходная матрица:', matrix)
# for i in range(3):
#     for j in range(3):
#         print(matrix[i][j], end=' ')
#     print()
# print('максимальное значение среди элементов третьего столбца ',
#       max([matrix[i][2] for i in range(3)]))
# print('минимальное значение среди элементов второго столбца ',
#       min([matrix[i][1] for i in range(3)]))

# # 2
# print('\n#2')

# arr = list()
# n = 3
# m = 3
# for i in range(n):
#     arr.append([randint(-9, 9) for x in range(m)])
# for i in range(n):
#     for j in range(m):
#         print(arr[i][j], end=' ')
#     print()
# for i in range(n):
#     for j in range(m):
#         if arr[i][j] < 0:
#             arr[i][j] = 0
#         else:
#             arr[i][j] = 1
# for i in range(n):
#     for j in range(m):
#         print(arr[i][j], end=' ')
#     print()


# # 3
# N = 3

# A = [
#     [2, 7, 6],
#     [9, 5, 1],
#     [4, 3, 8]]

# s = 0
# for i in range(N):
#     s += A[0][i]

# b = "YES"
# for i in range(N):
#     s1 = 0
#     s2 = 0
# for j in range(N):
#     s1 += A[i][j]
#     s2 += A[j][i]
# if s1 != s or s2 != s:
#     b = "NO"

# print(b)