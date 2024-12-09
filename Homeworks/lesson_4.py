# 1
s = input('Введите строку: \n')
s = s.replace('н', '!')
print(s)

# 2
a = input('Введите строку и скобки: \n')
print(a[a.find('(') + 1:a.find(')')])
b = input('Введите строку: \n')
print(b.replace(' ', '')[b.find('a')+1:b.find('я')])

# 3
input(str) = "аллея абстракция"
for w in str.split():
    if (w.startswith("а") or w.endswith("я")):
        print(w)
