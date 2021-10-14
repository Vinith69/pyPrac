n = int(input("Enter number\n"))

d = {}
for i in range(n):
    num = int(input())
    d[num] = d.get(num, 0)+1

count = 0
print(d)
for k, v in d.items():
    count += v//2

print(count)

# def sockMerchant(n, ar):
#     pairs = 0
#     set_ar = set(ar)
#     print(set_ar)
#     for i in set_ar:
#         count = ar.count(i)
#         print(count)
#         pairs += count//2
#     return pairs


# n = int(input())
# ar = list(map(int, input().split()))
# print(sockMerchant(n, ar))
