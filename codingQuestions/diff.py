num = (input("Enter number: "))

even = []
odd = []
for i, number in enumerate(num):
    if(int(number) % 2 == 0):
        even.append(int(number))
    else:
        odd.append(int(number))


total = sum(odd) - sum(even)

print(total)
