# s = 'Peter the Great'
# print(s[:1])

# l = [i*i for i in range (10)]
# print(l)

# from random import randint
# l = [randint (10,80) for x in range (10)]
# print (l)


# def sum_d(n): #Определение функции с параметром
# sum = 0
# while n != 0:
# sum += n % 10
# n = n // 10
# return sum #Возврат значения функции

# Запуск программы
# print(sum_d(int(input())))

import pandas as pd

df = pd.DataFrame({'country': ['Kazahstan'],
                   'population': [150]})

print(df)


import numpy as np
import pandas as pd

data = [1, 2, 3, 4, 5]

df = pd.DataFrame(data, columns=['Numbers'])
print(df)

import pandas as pd
data = [{'a': i, 'b': 2 * i}
        for i in range(3)]
print('data:')
print(data)
print('')
result = pd.DataFrame(data)
print('result:')
print(result)

import pandas as pd

population_dict = {'Russia': 144,
             'Ukraine': 35,
             'Belarus': 9,
             'China': 1000,
             'USA': 300}
population = pd.Series(population_dict)
area_dict = {'Russia': 17.1,
                   'Ukraine': 0.6,
                   'Belarus': 0.2,
                   'China': 9.6,
                   'USA': 9.8}
area = pd.Series(area_dict)
df = pd.DataFrame({'population': population,
                   'area': area})