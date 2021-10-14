def SumNumberDivisible(m: int,  n: int):
    if 0 < m <= n:
        temp = 0
        for i in range(m, n+1):
            if i % 3 == 0 and i % 5 == 0:
                temp += i

    return temp


m = int(input("m: "))
n = int(input("n: "))

total = SumNumberDivisible(m, n)

print(total)
