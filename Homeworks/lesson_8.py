# 1
import re
lst = input()
print('Список номеров частных автомобилей:', re.findall(
    r'\b[АВЕКМНОРСТУХ]\d{3}[АВЕКМНОРСТУХ]{2}\d{2,3}\b', lst))
print('Список номеров такси:', re.findall(
    r'\b[АВЕКМНОРСТУХ]{2}\d{5,6}\b', lst))

# 2
text = str(input())
re.findall(r"\w[\w-]*\w*", text)
print(len((re.findall)(r"\w[\w-]*\w*", text)))

# 3
newStr = 'Уважаемые! Если вы к 09:00 не вернете чемодан.\n\
То уже в 09:00:01 я за себя не отвечаю!\n\.'
print(newStr)
s = re.findall(r'(?:[01]\d|2[0123]):(?:[012345]\d):(?:[012345]\d)', newStr)
pat = r'((?:[01]\d|2[0-3])\:(?:[0-5]\d)(?:\:[0-5]\d)?)'
res = re.sub(pat, "(TBD)", newStr)
print(res)

# 4


def find_abbreviations(text):
    pattern = r'\b[A-ZА-Я]{2,}(?:\s+[A-ZА-Я]{2,})*\b'
    abbreviations = re.findall(pattern, text)
    return abbreviations


text = str(input())
abbreviations = find_abbreviations(text)
print(abbreviations)
