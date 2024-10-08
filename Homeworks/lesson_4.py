s = input ('Введите строку: \n')
s = s.replace ('н', '!')
print (s)


a = input('Введите строку и скобки: \n')
print(a[a.find('(') + 1:a.find(')')])


b = input ('Введите строку: \n')
print (b.replace(' ','')[b.find('a')+1:b.find('я')])