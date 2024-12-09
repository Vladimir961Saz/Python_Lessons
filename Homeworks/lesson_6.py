# 5
import random
matrix = [[random.randint(-10, 10) for _ in range(10)] for _ in range(10)]
s = []
for i in range(len(matrix)):
    s.append(sum(matrix[i]))
print('Строка с наибольшей суммой элементов:', matrix[s.index(max(s))])
print('Сумма элементов строки:', max(s))
print('Строка с наименьшей суммой элементов:', matrix[s.index(min(s))])
print('Сумма элементов строки:', min(s))

# 6
array_size = 8
random_array = [random.randint(1, 100) for _ in range(array_size)]
print(f"Массив случайных чисел: {random_array}")
