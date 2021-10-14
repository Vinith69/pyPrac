n = list(input("Enter n\n").split())

price = list(input("Enter price\n").split())

distance = list(input("Enter distance\n").split())
sku = list(input("Enter sku\n").split())

total = []
for i, item in enumerate(sku):
    print(i, item, sku[i])
    if (int(sku[i]) > 0):
        total.append(int(price[i]) * int(distance[i]))

print(total)
