# 1
import matplotlib.pyplot as plt
from matplotlib import pyplot as plt
import pandas as pd
import numpy as np
df = pd.DataFrame(np.random.rand(3, 2),
                  columns=['foo', 'bar'],
                  index=['a', 'b', 'c'])
print(df)

# 2

s1 = pd.Series([1, 2, 3, 4, 5])
s2 = pd.Series([4, 5, 6, 7, 8])
s1_unique = s1[~s1.isin(s2)]
s2_unique = s2[~s2.isin(s1)]

print("Элементы, которые есть в s1, но нет в s2:", s1_unique)
print("Элементы, которые есть в s2, но нет в s1:", s2_unique)

# 3

sr = pd.Series(["bla", "bla", "bla", "", "bla", "hi", "how",
               "are", "how", "are", "how", "are", "are", "are", "are"])
print(sr)

plt.bar(sr.value_counts().index, sr.value_counts().values)
plt.grid(axis='y', linestyle='--', alpha=0.6)
plt.show()

# 4
df1 = pd.DataFrame({
    'A': [1, 2, 3],
    'B': [4, 5, 6]
})

df2 = pd.DataFrame({
    'A': [7, 8, 9],
    'B': [10, 11, 12]
})

result = pd.concat([df1, df2], axis=0, ignore_index=True)
print(result)
# 5


data = {
    'X': [1, 2, 3, 4, 5],
    'Y1': [2, 3, 5, 7, 11],
    'Y2': [1, 2, 4, 8, 16],
    'Y3': [3, 4, 6, 8, 10]
}

df = pd.DataFrame(data)

plt.figure(figsize=(8, 6))

for column in df.columns[1:]:
    plt.plot(df['X'], df[column], label=column)

plt.title('Зависимость столбцов от X')
plt.xlabel('X')
plt.ylabel('Значения')
plt.legend(title='Столбцы')

plt.grid(True)
plt.show()
