a = []
b = []


for i in range(0, 3):
    a.append([int(j) for j in input().split()])

print(a)
for i in range(3):
    temp = 0
    for j in range(3):
        temp += a[i][j]
    b.append(temp)
    print(b[i])

temp = 0
for i in range(3):
    if temp < b[i]:
        temp = b[i]


print(temp)
