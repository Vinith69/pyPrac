n = int(input("Size: "))
start = int(input("Start: "))
end = int(input("End: "))

arr = []
for i in range(n):
    arr.append(int(input("Enter")))

for i, employee in enumerate(arr):
    if(start <= employee <= end):
        print(i)
