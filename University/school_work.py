# mas=[['b','c','a'],['l','r','k']]
# print (mas)
# print (mas[0][0])

# a=3
# mas = [0]*a
# for i in range (a):
    # mas[i]=[0]*a
# print (mas)

n = 3
arr = []
for i in range(n):
  arr.append([9]*n)
for i in range(n):
  for j in range(n):
    print(arr[i][j], end = ' ')
  print()
  for i in range (n):
    if arr[i][j]>0:
      arr[i][j]=1
    if [i][j]<0:
     arr [i][j]=0
    for i in range(n):
        for j in range(n):
            print(arr[i][j], end = ' ')
            print()

