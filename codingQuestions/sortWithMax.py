def sortt():
    l = []
    n = int(input("Enter n"))
    for i in range(n):
        l.append(int(input()))
    l.sort()
    return l


def findMaxElement():
    l = [11, 13, 2, 4, 15, 17, 67, 44, 112, 100, 23]
    # n = int(input("Enter n"))
    # for i in range(n):
    #     l.append(int(input()))
    print(max(l))


l = sortt()
print(l)
