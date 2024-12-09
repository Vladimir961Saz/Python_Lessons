# 1
a = int(input('Введите верхний предел:'))
b = 0
s = 0
c = 0
if a > 100:
    print('Верхний предел должен быть меньше 100!')
else:
    while c < a:
        c += 1
        b += 1
        s += b**3
        print(int(s))
# 2
for i in range(1, 10):
    for j in range(1, 10):
        print(i*j, end='\t')
    print()
