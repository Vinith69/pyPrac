n = int(input("Enter size of array"))

arr = []

print("Enter the elements of an array")
for i in range(n):
    arr.append(int(input()))

d = {}
for i in arr:
    d[i] = d.get(i, 0)+1

newArr = []
for k, v in d.items():
    if v < 2:
        newArr.append(k)

newArr.sort()
print(newArr)
