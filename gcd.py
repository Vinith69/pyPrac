def gcd(num1, num2):
    if(num1 == 0):
        return num2
    else:
        return gcd(num2 % num1, num1)


num1 = int(input("Enter num 1\n"))
num2 = int(input("Enter num 2\n"))
num3 = int(input("Enter num 3\n"))

print(gcd(gcd(num1, num2), num3))
