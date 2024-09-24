arr = []
for i in range(0, 101):
    ar = []
    for j in range(0, 101):
        ar.append(0)
    arr.append(ar)

while ((str := input()) != ""):
    a, b = map(int, str.split(', '))
    arr[a][b] = arr[a][b] + 1


for i in range(1, 101):
    for j in range (1, 101):
        for k in range(0, arr[i][j]):
            print(f'{i}, {j}')

